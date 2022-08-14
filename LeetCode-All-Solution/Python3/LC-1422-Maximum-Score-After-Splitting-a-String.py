#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1422-Maximum-Score-After-Splitting-a-String.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-08-14
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 1422 - (Easy) - Maximum Score After Splitting a String
https://leetcode.com/problems/maximum-score-after-splitting-a-string/

Description & Requirement:
    Given a string s of zeros and ones, return the maximum score after splitting the string into 
    two non-empty substrings (i.e. left substring and right substring).

    The score after splitting a string is the number of zeros in the left substring 
    plus the number of ones in the right substring.

Example 1:
    Input: s = "011101"
    Output: 5 
    Explanation: 
        All possible ways of splitting s into two non-empty substrings are:
        left = "0" and right = "11101", score = 1 + 4 = 5 
        left = "01" and right = "1101", score = 1 + 3 = 4 
        left = "011" and right = "101", score = 1 + 2 = 3 
        left = "0111" and right = "01", score = 1 + 1 = 2 
        left = "01110" and right = "1", score = 2 + 1 = 3
Example 2:
    Input: s = "00111"
    Output: 5
    Explanation: When left = "00" and right = "111", we get the maximum score = 2 + 3 = 5
Example 3:
    Input: s = "1111"
    Output: 3

Constraints:
    2 <= s.length <= 500
    The string s consists of characters '0' and '1' only.
"""


class Solution:
    def maxScore(self, s: str) -> int:
        # exception case
        assert isinstance(s, str) and len(s) >= 2
        # main method: (try all splitting positions)
        return self._maxScore(s)

    def _maxScore(self, s: str) -> int:
        """
        Runtime: 36 ms, faster than 93.56% of Python3 online submissions for Maximum Score After Splitting a String
        Memory Usage: 13.8 MB, less than 61.81% of Python3 online submissions for Maximum Score After Splitting a String
        """
        assert isinstance(s, str) and len(s) >= 2

        cur_score = 0
        for ch in s[:1]:
            if ch == "0":
                cur_score += 1
        for ch in s[1:]:
            if ch == "1":
                cur_score += 1

        res = cur_score
        for ch in s[1:-1]:
            if ch == "0":
                cur_score += 1  # move a "0" from right split to the right split, score += 1
            elif ch == "1":
                cur_score -= 1  # move a "1" from right split to the right split, score -= 1

            res = max(res, cur_score)

        return res


def main():
    # Example 1: Output: 5
    # s = "011101"

    # Example 2: Output: 5
    # s = "00111"

    # Example 3: Output: 3
    s = "1111"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maxScore(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
