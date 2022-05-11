#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1641-Count-Sorted-Vowel-Strings.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-05-11
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 1641 - (Medium) - Count Sorted Vowel Strings
https://leetcode.com/problems/count-sorted-vowel-strings/

Description & Requirement:
    Given an integer n, return the number of strings of length n that 
    consist only of vowels (a, e, i, o, u) and are lexicographically sorted.

    A string s is lexicographically sorted if for all valid i, 
    s[i] is the same as or comes before s[i+1] in the alphabet.

Example 1:
    Input: n = 1
    Output: 5
    Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].
Example 2:
    Input: n = 2
    Output: 15
    Explanation: The 15 sorted strings that consist of vowels only are
        ["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
        Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.
Example 3:
    Input: n = 33
    Output: 66045

Constraints:
    1 <= n <= 50
"""


class Solution:
    def countVowelStrings(self, n: int) -> int:
        # exception case
        assert isinstance(n, int) and n >= 1
        # main method: (dynamic programming)
        return self._countVowelStrings(n)

    def _countVowelStrings(self, n: int) -> int:
        assert isinstance(n, int) and n >= 1

        # dp = [[0, 0, 0, 0, 0] for _ in range(n + 1)]
        # dp[1] = [1, 1, 1, 1, 1]  # if len(string) == 1 & start with "a"/"e"/"i"/"o"/"u", there is 1/1/1/1/1 valid str
        # for i in range(2, n + 1):
        #     for j in range(5):
        #         dp[i][j] = sum(dp[i - 1][j:])
        # return sum(dp[-1])

        # compress state
        dp_last = [1, 1, 1, 1, 1]
        for _ in range(2, n + 1):
            dp_cur = [0, 0, 0, 0, 0]
            for j in range(5):
                dp_cur[j] = sum(dp_last[j:])
            dp_last = dp_cur
        return sum(dp_last)


def main():
    # Example 1: Output: 5
    # n = 1

    # Example 2: Output: 15
    # n = 2

    # Example 3: Output: 66045
    n = 33

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.countVowelStrings(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
