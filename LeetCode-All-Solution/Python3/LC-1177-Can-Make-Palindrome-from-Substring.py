#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1177-Can-Make-Palindrome-from-Substring.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-06-15
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1177 - (Medium) - Can Make Palindrome from Substring
https://leetcode.com/problems/can-make-palindrome-from-substring/

Description & Requirement:
    You are given a string s and array queries where queries[i] = [left_i, right_i, k_i]. 
    We may rearrange the substring s[left_i...right_i] for each query and then 
    choose up to k_i of them to replace with any lowercase English letter.

    If the substring is possible to be a palindrome string after the operations above, 
    the result of the query is true. Otherwise, the result is false.

    Return a boolean array answer where answer[i] is the result of the ith query queries[i].

    Note that each letter is counted individually for replacement, so if, 
    for example s[left_i...right_i] = "aaa", and k_i = 2, we can only replace two of the letters. 
    Also, note that no query modifies the initial string s.

Example 1:
    Input: s = "abcda", queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]
    Output: [true,false,false,true,true]
    Explanation:
        queries[0]: substring = "d", is palidrome.
        queries[1]: substring = "bc", is not palidrome.
        queries[2]: substring = "abcd", is not palidrome after replacing only 1 character.
        queries[3]: substring = "abcd", could be changed to "abba" which is palidrome. 
            Also this can be changed to "baab" first rearrange it "bacd" then replace "cd" with "ab".
        queries[4]: substring = "abcda", could be changed to "abcba" which is palidrome.
Example 2:
    Input: s = "lyb", queries = [[0,1,0],[2,2,1]]
    Output: [false,true]

Constraints:
    1 <= s.length, queries.length <= 10^5
    0 <= left_i <= right_i < s.length
    0 <= k_i <= s.length
    s consists of lowercase English letters.
"""


class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        # exception case
        assert isinstance(s, str) and len(s) >= 1
        assert isinstance(queries, list) and len(queries) >= 1
        # main method: (prefix sum and bit manipulation)
        return self._canMakePaliQueries(s, queries)

    def _canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        assert isinstance(s, str) and len(s) >= 1
        assert isinstance(queries, list) and len(queries) >= 1

        n = len(s)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] ^ (1 << (ord(s[i]) - ord('a')))

        res = []
        for left, right, k in queries:
            bits = (prefix[right + 1] ^ prefix[left]).bit_count()
            res.append(bits <= k * 2 + 1)

        return res


def main():
    # Example 1: Output: [true,false,false,true,true]
    s = "abcda"
    queries = [[3, 3, 0], [1, 2, 0], [0, 3, 1], [0, 3, 2], [0, 4, 1]]

    # Example 2: Output: [false,true]
    # s = "lyb"
    # queries = [[0, 1, 0], [2, 2, 1]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.canMakePaliQueries(s, queries)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
