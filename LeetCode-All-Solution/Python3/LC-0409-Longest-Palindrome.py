#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0409-Longest-Palindrome.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-16
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 0409 - (Easy) - Longest Palindrome
https://leetcode.com/problems/longest-palindrome/

Description & Requirement:
    Given a string s which consists of lowercase or uppercase letters, 
    return the length of the longest palindrome that can be built with those letters.

    Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

Example 1:
    Input: s = "abccccdd"
    Output: 7
    Explanation:
    One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:
    Input: s = "a"
    Output: 1
Example 3:
    Input: s = "bb"
    Output: 2

Constraints:
    1 <= s.length <= 2000
    s consists of lowercase and/or uppercase English letters only.

Related Problem:
    LC-0516-Longest-Palindromic-Subsequence
"""


class Solution:
    def longestPalindrome(self, s: str) -> int:
        # exception case
        assert isinstance(s, str) and len(s) > 0
        # main method: (count the occurrence)
        return self._longestPalindrome(s)

    def _longestPalindrome(self, s: str) -> int:
        counter = dict({})
        for ch in s:
            if ch not in counter:
                counter[ch] = 1
            else:
                counter[ch] += 1

        res = 0
        has_residual = False
        for ch, count in counter.items():
            if count >= 2:
                if count & 0x01 == 1:  # count is an odd number
                    res += count - 1
                    has_residual = True
                else:  # count is an even number
                    res += count
            else:  # count == 1
                has_residual = True

        return (res + 1) if has_residual else res

    def _longestPalindromeSubsequence(self, s: str) -> int:
        """
        dp[i][j] is the max len of palin subseq using chars s[i: j+1]
        dp equation: dp[i][j] = dp[i+1][j-1] + 2  if s[i] == s[j]
                     dp[i][j] = max(dp[i+1][j], dp[i][j-1])  if s[i] != s[j]
        dp init: dp[i][i] = 1, dp[i][i+1] == 2 if s[i] == s[i+1] else 1
        dp aim: get dp[0][-1]
        note that DP start from small intervals, otherwise it's the same as `_longestPalindromeSubseqDfs`
        """
        if not isinstance(s, str) or len(s) <= 0:
            return 0  # Error input type
        len_s = len(s)
        if len_s == 1:
            return 1  # s itself is a palindrome
        if len_s == 2:
            return 2 if s[0] == s[1] else 1
        assert len_s >= 3

        # dp[i][j] is the max len of palin subseq using chars s[i: j+1]
        dp = [[0 for _ in range(len_s)] for _ in range(len_s)]

        # dp init: dp[i][i] = 1, dp[i][i+1] == 2 if s[i] == s[i+1] else 1
        for idx in range(len_s):
            dp[idx][idx] = 1
        for idx in range(len_s - 1):
            if s[idx] == s[idx + 1]:
                dp[idx][idx + 1] = 2
            else:
                dp[idx][idx + 1] = 1

        # dp equation: dp[i][j] = dp[i+1][j-1] + 2  if s[i] == s[j]
        #              dp[i][j] = max(dp[i+1][j], dp[i][j-1])  if s[i] != s[j]
        # first interval s[-1][-1], then s[-2][-2] and s[-2][-1], and so on
        #     when start_idx == 0, all the needed sub intervals have been calculated and stored in dp[1][j]
        for start_idx in reversed(range(len_s)):
            for end_idx in range(start_idx + 2, len_s):
                if s[start_idx] == s[end_idx]:
                    dp[start_idx][end_idx] = dp[start_idx + 1][end_idx - 1] + 2
                else:
                    dp[start_idx][end_idx] = max(dp[start_idx + 1][end_idx], dp[start_idx][end_idx - 1])

        return dp[0][-1]


def main():
    # Example 1: Output: 7
    s = "abccccdd"

    # Example 2: Output: 1
    # s = "a"

    # Example 3: Output: 2
    # s = "bb"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.longestPalindrome(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
