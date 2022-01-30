#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1143-Longest-Common-Subsequence.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-30
=================================================================="""

import sys
import time
# from typing import List
# import collections

"""
LeetCode - 1143 - (Medium) - Longest Common Subsequence
https://leetcode.com/problems/longest-common-subsequence/

Description & Requirement:
    Given two strings text1 and text2, return the length of their longest common subsequence. 
    If there is no common subsequence, return 0.

    A subsequence of a string is a new string generated from the original string 
    with some characters (can be none) deleted without changing the relative order of the remaining characters.
        For example, "ace" is a subsequence of "abcde".
    A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:
    Input: text1 = "abcde", text2 = "ace" 
    Output: 3
    Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:
    Input: text1 = "abc", text2 = "abc"
    Output: 3
    Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:
    Input: text1 = "abc", text2 = "def"
    Output: 0
    Explanation: There is no such common subsequence, so the result is 0.

Constraints:
    1 <= text1.length, text2.length <= 1000
    text1 and text2 consist of only lowercase English characters.
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # exception case
        if not isinstance(text1, str) or len(text1) <= 0:
            return 0  # Error input type
        if not isinstance(text2, str) or len(text2) <= 0:
            return 0  # Error input type
        # main method: (Dynamic Programming: dp[i][j] means the len of max LCS using text1[0: i+1] and text2[0: j+1])
        #     dp equation: dp[i][j] = dp[i-1][j-1] + 1   if  text1[i-1] == text2[j-1]
        #                  dp[i][j] = max(dp[i-1][j], dp[i][j-1])   if text1[i-1] != text2[j-1]
        #     dp init: dp[0] == 0, which means len("") is 0.
        #     dp aim: get dp[-1][-1]
        return self._longestCommonSubsequence(text1, text2)

    def _longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len_text1 = len(text1)
        len_text2 = len(text2)
        assert len_text1 >= 1 and len_text2 >= 1

        # dp[i][j] means the len of max LCS using text1[0: i+1] and text2[0: j+1]
        dp = [[0 for _ in range(len_text2 + 1)] for _ in range(len_text1 + 1)]

        for i in range(1, len_text1 + 1):
            for j in range(1, len_text2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    # dp equation: dp[i][j] = dp[i-1][j-1] + 1   if  text1[i-1] == text2[j-1]
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # dp equation: dp[i][j] = max(dp[i-1][j], dp[i][j-1])   if text1[i-1] != text2[j-1]
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]


def main():
    # Example 1: Output: 3
    text1 = "abcde"
    text2 = "ace"

    # Example 2: Output: 3
    # text1 = "abc"
    # text2 = "abc"

    # Example 3: Output: 0
    # text1 = "abc"
    # text2 = "def"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.longestCommonSubsequence(text1, text2)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
