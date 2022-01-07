#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0131-Palindrome-Partitioning.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-05
=================================================================="""
import functools
import sys
import time
from typing import List

"""
LeetCode - 0131 - (Medium) - Palindrome Partitioning
https://leetcode.com/problems/palindrome-partitioning/

Description & Requirement:
    Given a string s, partition s such that every substring of the partition is a palindrome. 
    Return all possible palindrome partitioning of s.

    A palindrome string is a string that reads the same backward as forward.

Example 1:
    Input: s = "aab"
    Output: [["a","a","b"],["aa","b"]]
Example 2:
    Input: s = "a"
    Output: [["a"]]

Constraints:
    1 <= s.length <= 16
    s contains only lowercase English letters.
"""


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # exception case
        if not isinstance(s, str) or len(s) <= 0:
            return []
        # border case
        if len(s) == 1:
            return [[s[0]]]
        if len(s) == 2:
            return [[s[0], s[1]]] if s[0] != s[1] else [[s[0], s[1]], [s]]
        # main method: (Memorized DFS or Dynamic Programming)
        return self._partition_mem_dfs(s)
        # return self._partition_dp(s)

    def _partition_mem_dfs(self, s: str) -> List[List[str]]:
        res_list = []
        palindrome_list = []
        len_s = len(s)  # must >= 3
        # res_list.append([s[i] for i in range(len_s)])  # default answer: split every char as a single substring

        @functools.lru_cache(maxsize=None)
        def __is_palindrome(left_index: int, right_index: int) -> bool:
            """
            memorized search to find out if a string is palindrome or not
            """
            if left_index >= right_index:
                return True  # one single char is a palindrome
            # when the leftmost char matches the rightmost char, then judge if the inner part is a palindrome
            return __is_palindrome(left_index + 1, right_index - 1) if s[left_index] == s[right_index] else False

        def __dfs(left_index: int):
            if left_index == len_s:  # dfs end condition: no char left in the current interval
                # now, all chars are grouped as several palindromes, so the palindrome_list is a possible partition
                res_list.append(palindrome_list[:])  # note that NOT to append palindrome_list but p_list[:]
                return

            # consider all possible partition
            for split_index in range(left_index, len_s):
                # if the left part is a palindrome, then it's possible for each part to be valid
                if __is_palindrome(left_index, split_index):
                    # current substring is a palindrome, record it
                    palindrome_list.append(s[left_index: split_index + 1])
                    # go deeper and check if the right part can be divided as palindromes
                    __dfs(split_index + 1)
                    # backtrack and git rid of the palindrome: s[left_index: split_index + 1]
                    palindrome_list.pop()

        __dfs(0)  # dfs from the leftmost index (Top-Down search: from the biggest interval to the smallest interval)
        __is_palindrome.cache_clear()  # clear cache of the memorized search function
        return res_list

    def _partition_dp(self, s: str) -> List[List[str]]:
        res_list = []
        palindrome_list = []
        len_s = len(s)  # must >= 3
        # dp value: dp[i][j] is True: s[i: j+1] is a palindrome; dp[i][j] is False: s[i: j+1] is not a palindrome
        # default value is True, because one single char is a palindrome, i.e., dp[i][i] must be True
        dp = [[True for _ in range(len_s)] for _ in range(len_s)]  # len_s * len_s

        # get dp table (Bottom-Up search: from the smallest interval to the biggest interval)
        for left_index in range(len_s - 1, -1, -1):
            for right_index in range(left_index + 1, len_s):
                # when left_index == right_index, the dp value must be True, because one single char is a palindrome
                dp[left_index][right_index] = (s[left_index] == s[right_index]) and dp[left_index + 1][right_index - 1]

        def __dfs(l_index: int):
            if l_index == len_s:  # dfs end condition: no char left in the current interval
                # now, all chars are grouped as several palindromes, so the palindrome_list is a possible partition
                res_list.append(palindrome_list[:])  # note that NOT to append palindrome_list but p_list[:]
                return

            for r_index in range(l_index, len_s):
                if dp[l_index][r_index]:  # the same function to `__is_palindrome`: judge if an interval is a palindrome
                    palindrome_list.append(s[l_index: r_index + 1])  # current substring is a palindrome, record it
                    __dfs(r_index + 1)  # go deeper and check if the right part can be divided as palindromes
                    palindrome_list.pop()  # backtrack and git rid of the palindrome: s[l_index: r_index + 1]

        __dfs(0)  # dfs from the leftmost index (Top-Down search: from the biggest interval to the smallest interval)
        return res_list


def main():
    # Example 1: Output: [["a","a","b"],["aa","b"]]
    s = "aab"

    # Example 2: Output: [["a"]]
    # s = "a"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.partition(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
