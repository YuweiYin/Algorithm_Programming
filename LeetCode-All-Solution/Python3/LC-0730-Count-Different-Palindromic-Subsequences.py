#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0730-Count-Different-Palindromic-Subsequences.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-06-10
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 0730 - (Hard) - Count Different Palindromic Subsequences
https://leetcode.com/problems/count-different-palindromic-subsequences/

Description & Requirement:
    Given a string s, return the number of different non-empty palindromic subsequences in s. 
    Since the answer may be very large, return it modulo 10^9 + 7.

    A subsequence of a string is obtained by deleting zero or more characters from the string.

    A sequence is palindromic if it is equal to the sequence reversed.

    Two sequences a1, a2, ... and b1, b2, ... are different if there is some i for which ai != bi.

Example 1:
    Input: s = "bccb"
    Output: 6
    Explanation: The 6 different non-empty palindromic subsequences are 'b', 'c', 'bb', 'cc', 'bcb', 'bccb'.
        Note that 'bcb' is counted only once, even though it occurs twice.
Example 2:
    Input: s = "abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba"
    Output: 104860361
    Explanation: There are 3104860382 different non-empty palindromic subsequences, 
        which is 104860361 modulo 10^9 + 7.

Constraints:
    1 <= s.length <= 1000
    s[i] is either 'a', 'b', 'c', or 'd'.
"""


class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        # exception case
        assert isinstance(s, str) and len(s) >= 1
        # main method: (dynamic programming)
        return self._countPalindromicSubsequences(s)

    def _countPalindromicSubsequences(self, s: str) -> int:
        assert isinstance(s, str) and len(s) >= 1
        len_s = len(s)

        MOD = int(1e9+7)
        # dp[c][i][j] denotes the number of palindromic subsequences in s[i: j] that starts and ends with char c
        # 4 cases: 1. s[i] == s[j] == c; 2. s[i] == c, s[j] != c; 3. s[i] != c, s[j] == c; 4. s[i] != c, s[j] != c.
        dp = [[[0 for _ in range(len_s)] for _ in range(len_s)] for _ in range(4)]

        ord_a = ord("a")
        for idx, ch in enumerate(s):
            dp[ord(ch) - ord_a][idx][idx] = 1

        for length in range(2, len_s + 1):
            for j in range(length - 1, len_s):
                i = j - length + 1
                # s[i] is either 'a', 'b', 'c', or 'd'.
                for idx, ch in enumerate("abcd"):
                    # 4 cases
                    if s[i] == ch and s[j] == ch:
                        dp[idx][i][j] = (2 + sum(_dp[i + 1][j - 1] for _dp in dp)) % MOD
                    elif s[i] == ch:
                        dp[idx][i][j] = dp[idx][i][j - 1]
                    elif s[j] == ch:
                        dp[idx][i][j] = dp[idx][i + 1][j]
                    else:
                        dp[idx][i][j] = dp[idx][i + 1][j - 1]

        return sum(_dp[0][len_s - 1] for _dp in dp) % MOD


def main():
    # Example 1: Output: 6
    # s = "bccb"

    # Example 2: Output: 104860361
    s = "abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.countPalindromicSubsequences(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
