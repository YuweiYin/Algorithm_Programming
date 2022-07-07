#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0097-Interleaving-String.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-07-07
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 0097 - (Medium) - Interleaving String
https://leetcode.com/problems/interleaving-string/

Description & Requirement:
    Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

    An interleaving of two strings s and t is a configuration where 
    they are divided into non-empty substrings such that:
        s = s1 + s2 + ... + sn
        t = t1 + t2 + ... + tm
        |n - m| <= 1
    The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...

    Note: a + b is the concatenation of strings a and b.

Example 1:
    Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
    Output: true
Example 2:
    Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
    Output: false
Example 3:
    Input: s1 = "", s2 = "", s3 = ""
    Output: true

Constraints:
    0 <= s1.length, s2.length <= 100
    0 <= s3.length <= 200
    s1, s2, and s3 consist of lowercase English letters.

Follow up:
    Could you solve it using only O(s2.length) additional memory space?
"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # exception case
        assert isinstance(s1, str) and isinstance(s2, str) and isinstance(s3, str)
        # main method: (dynamic programming)
        return self._isInterleave(s1, s2, s3)

    def _isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        assert isinstance(s1, str) and isinstance(s2, str) and isinstance(s3, str)
        len_s1, len_s2, len_s3 = len(s1), len(s2), len(s3)
        if len_s1 + len_s2 != len_s3:
            return False
        if len_s3 == 0:
            return len_s1 == 0 and len_s2 == 0

        # dp[i][j] is True means s1[:i+1] and s2[:j+1] can construct s3[:i+j+1]
        dp = [[False for _ in range(len_s2 + 1)] for _ in range(len_s1 + 1)]
        dp[0][0] = True

        for i in range(len_s1 + 1):
            for j in range(len_s2 + 1):
                k = i + j - 1
                if i > 0:  # test if dp[i - 1][j] can transition to dp[i][j]
                    dp[i][j] |= dp[i - 1][j] and s1[i - 1] == s3[k]
                if j > 0:  # test if dp[i][j - 1] can transition to dp[i][j]
                    dp[i][j] |= dp[i][j - 1] and s2[j - 1] == s3[k]

        return dp[-1][-1]


def main():
    # Example 1: Output: true
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"

    # Example 2: Output: false
    # s1 = "aabcc"
    # s2 = "dbbca"
    # s3 = "aadbbbaccc"

    # Example 3: Output: true
    # s1 = ""
    # s2 = ""
    # s3 = ""

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.isInterleave(s1, s2, s3)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
