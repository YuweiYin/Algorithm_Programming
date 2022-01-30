#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0583-Delete-Operation-for-Two-Strings.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-30
=================================================================="""

import sys
import time
# from typing import List
# import collections

"""
LeetCode - 0583 - (Medium) - Delete Operation for Two Strings
https://leetcode.com/problems/delete-operation-for-two-strings/

Description & Requirement:
    Given two strings word1 and word2, 
    return the minimum number of steps required to make word1 and word2 the same.

    In one step, you can delete exactly one character in either string.

Example 1:
    Input: word1 = "sea", word2 = "eat"
    Output: 2
    Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
Example 2:
    Input: word1 = "leetcode", word2 = "etco"
    Output: 4

Constraints:
    1 <= word1.length, word2.length <= 500
    word1 and word2 consist of only lowercase English letters.
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # exception case
        if not isinstance(word1, str) or len(word1) <= 0:
            return len(word2)  # Error word1 input type
        if not isinstance(word2, str) or len(word2) <= 0:
            return len(word1)  # Error word2 input type
        # main method: (Dynamic Programming. up DP method get LCS of word1 and word2)
        #     number of delete char is ((len(word1) - len(LCS)) + (len(word2) - len(lCS)))
        #     related problem: LC-1143-Longest-Common-Subsequence
        return self._minDistance(word1, word2)

    def _minDistance(self, word1: str, word2: str) -> int:
        len_word1 = len(word1)
        len_word2 = len(word2)
        assert len_word1 >= 1 and len_word2 >= 1

        len_lcs = self._longestCommonSubsequence(word1, word2)

        return len_word1 + len_word2 - (len_lcs << 1)

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
    # Example 1: Output: 2
    word1 = "sea"
    word2 = "eat"

    # Example 2: Output: 4
    # word1 = "leetcode"
    # word2 = "etco"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minDistance(word1, word2)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
