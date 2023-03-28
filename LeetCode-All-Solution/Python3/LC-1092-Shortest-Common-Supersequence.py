#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1092-Shortest-Common-Supersequence.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-03-28
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 1092 - (Hard) - Shortest Common Supersequence
https://leetcode.com/problems/shortest-common-supersequence/

Description & Requirement:
    Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. 
    If there are multiple valid strings, return any of them.

    A string s is a subsequence of string t if 
    deleting some number of characters from t (possibly 0) results in the string s.

Example 1:
    Input: str1 = "abac", str2 = "cab"
    Output: "cabac"
    Explanation: 
        str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
        str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
        The answer provided is the shortest such string that satisfies these properties.
Example 2:
    Input: str1 = "aaaaaaaa", str2 = "aaaaaaaa"
    Output: "aaaaaaaa"

Constraints:
    1 <= str1.length, str2.length <= 1000
    str1 and str2 consist of lowercase English letters.
"""


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # exception case
        assert isinstance(str1, str) and len(str1) >= 1
        assert isinstance(str2, str) and len(str2) >= 1
        # main method: (LCS & DP)
        return self._shortestCommonSupersequence(str1, str2)

    def _shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        assert isinstance(str1, str) and len(str1) >= 1
        assert isinstance(str2, str) and len(str2) >= 1

        m, n = len(str1), len(str2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        ans = []
        i, j = m, n

        while i or j:
            if i == 0:
                j -= 1
                ans.append(str2[j])
            elif j == 0:
                i -= 1
                ans.append(str1[i])
            else:
                if dp[i][j] == dp[i - 1][j]:
                    i -= 1
                    ans.append(str1[i])
                elif dp[i][j] == dp[i][j - 1]:
                    j -= 1
                    ans.append(str2[j])
                else:
                    i, j = i - 1, j - 1
                    ans.append(str1[i])

        return "".join(ans[::-1])


def main():
    # Example 1: Output: "cabac"
    str1 = "abac"
    str2 = "cab"

    # Example 2: Output: "aaaaaaaa"
    # str1 = "aaaaaaaa"
    # str2 = "aaaaaaaa"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.shortestCommonSupersequence(str1, str2)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
