#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0072-Edit-Distance.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-31
=================================================================="""

import sys
import time
# from typing import List
# import collections

"""
LeetCode - 0072 - (Hard) - Edit Distance
https://leetcode.com/problems/edit-distance/

Description & Requirement:
    Given two strings word1 and word2, 
    return the minimum number of operations required to convert word1 to word2.

    You have the following three operations permitted on a word:
        Insert a character
        Delete a character
        Replace a character

Example 1:
    Input: word1 = "horse", word2 = "ros"
    Output: 3
    Explanation: 
        horse -> rorse (replace 'h' with 'r')
        rorse -> rose (remove 'r')
        rose -> ros (remove 'e')
Example 2:
    Input: word1 = "intention", word2 = "execution"
    Output: 5
    Explanation: 
        intention -> inention (remove 't')
        inention -> enention (replace 'i' with 'e')
        enention -> exention (replace 'n' with 'x')
        exention -> exection (replace 'n' with 'c')
        exection -> execution (insert 'u')

Constraints:
    0 <= word1.length, word2.length <= 500
    word1 and word2 consist of lowercase English letters.
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # exception case
        if not isinstance(word1, str) or len(word1) <= 0:
            return len(word2)  # Error word1 input type
        if not isinstance(word2, str) or len(word2) <= 0:
            return len(word1)  # Error word2 input type
        # main method: (Dynamic Programming)
        #     first, simplify the operations: (without simplification, there are 6 operation options at each step)
        #         1. insert char into A is equivalent to delete char in B
        #         2. delete char in A is equivalent to insert char into B
        #         3. replace char in A is equivalent to replace char in B (coz we always want A and B are closer)
        #     therefore, only consider 3 operation options at each step: 1. insert A; 2. delete A; 3. replace A.
        #     dp[i][j] is the minimum edit distance between word1[0: i+1] and word2[0: j+1]
        #     dp equation: dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1])   if word1[i] == word2[j]
        #                      explanation: if word1[i] == word2[j], dp[i-1][j-1] to dp[i][j] needn't any operation
        #                                   dp[i-1][j] to dp[i][j] need insert one char into A (same as delete in B)
        #                                   dp[i][j-1] to dp[i][j] need delete one char in A (same as insert into B)
        #                  dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])   if word1[i] != word2[j]
        #                      explanation: if word1[i] != word2[j], get to dp[i][j] always need one operation step
        #                                   dp[i-1][j] to dp[i][j] need insert one char into A (same as delete in B)
        #                                   dp[i][j-1] to dp[i][j] need delete one char in A (same as insert into B)
        #                                   dp[i-1][j-1] to dp[i][j] need replace one char in A (same as replace in B)
        #     dp init: dp[i][0] == i, dp[0][j] == j, because from a "" to a non-null string s, edit dist == len(s)
        #     dp aim: get dp[-1][-1]
        return self._minDistance(word1, word2)

    def _minDistance(self, word1: str, word2: str) -> int:
        len_word1 = len(word1)
        len_word2 = len(word2)
        assert len_word1 >= 1 and len_word2 >= 1

        # dp[i][j] is the minimum edit distance between word1[0: i+1] and word2[0: j+1]
        dp = [[0 for _ in range(len_word2 + 1)] for _ in range(len_word1 + 1)]

        # dp init: dp[i][0] == i, dp[0][j] == j, because from a "" to a non-null string s, edit dist == len(s)
        for i_index in range(len_word1 + 1):
            dp[i_index][0] = i_index
        for j_index in range(len_word2 + 1):
            dp[0][j_index] = j_index

        for i in range(1, len_word1 + 1):
            for j in range(1, len_word2 + 1):
                if word1[i - 1] == word2[j - 1]:  # note that the index of word is not the same as index in dp matrix
                    # dp equation: dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1])  if word1[i] == word2[j]
                    dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1])
                else:
                    # dp equation: dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])  if word1[i] != word2[j]
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

        return dp[-1][-1]


def main():
    # Example 1: Output: 3
    #     Explanation:
    #         horse -> rorse (replace 'h' with 'r')
    #         rorse -> rose (remove 'r')
    #         rose -> ros (remove 'e')
    # word1 = "horse"
    # word2 = "ros"

    # Example 2: Output: 5
    #     Explanation:
    #         intention -> inention (remove 't')
    #         inention -> enention (replace 'i' with 'e')
    #         enention -> exention (replace 'n' with 'x')
    #         exention -> exection (replace 'n' with 'c')
    #         exection -> execution (insert 'u')
    word1 = "intention"
    word2 = "execution"

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
