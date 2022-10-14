#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0940-Distinct-Subsequences-II.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-10-14
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 0940 - (Hard) - Distinct Subsequences II
https://leetcode.com/problems/distinct-subsequences-ii/

Description & Requirement:
    Given a string s, return the number of distinct non-empty subsequences of s. 
    Since the answer may be very large, return it modulo 10^9 + 7.

    A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) 
    of the characters without disturbing the relative positions of the remaining characters. 
    (i.e., "ace" is a subsequence of "abcde" while "aec" is not.

Example 1:
    Input: s = "abc"
    Output: 7
    Explanation: The 7 distinct subsequences are "a", "b", "c", "ab", "ac", "bc", and "abc".
Example 2:
    Input: s = "aba"
    Output: 6
    Explanation: The 6 distinct subsequences are "a", "b", "ab", "aa", "ba", and "aba".
Example 3:
    Input: s = "aaa"
    Output: 3
    Explanation: The 3 distinct subsequences are "a", "aa" and "aaa".

Constraints:
    1 <= s.length <= 2000
    s consists of lowercase English letters.
"""


class Solution:
    def distinctSubseqII(self, s: str) -> int:
        # exception case
        assert isinstance(s, str) and len(s) >= 1 and s.islower()
        # main method: (dynamic programming)
        return self._distinctSubseqII(s)

    def _distinctSubseqII(self, s: str) -> int:
        assert isinstance(s, str) and len(s) >= 1 and s.islower()

        MOD = int(1e9+7)
        NUM_LETTER = 26
        last = [-1 for _ in range(NUM_LETTER)]  # last[i] is the index of the last appeared char: chr(i + ord("a"))

        n = len(s)
        dp = [1 for _ in range(n)]
        ord_a = ord("a")

        for i, ch in enumerate(s):
            for j in range(NUM_LETTER):
                if last[j] != -1:
                    dp[i] = (dp[i] + dp[last[j]]) % MOD
            last[ord(s[i]) - ord_a] = i

        res = 0
        for i in range(NUM_LETTER):
            if last[i] != -1:
                res = (res + dp[last[i]]) % MOD

        return res


def main():
    # Example 1: Output: 7
    # s = "abc"

    # Example 2: Output: 6
    s = "aba"

    # Example 3: Output: 3
    # s = "aaa"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.distinctSubseqII(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
