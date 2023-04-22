#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1312-Minimum-Insertion-Steps-to-Make-a-String-Palindrome.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-04-22
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 1312 - (Hard) - Minimum Insertion Steps to Make a String Palindrome
https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/

Description & Requirement:
    Given a string s. In one step you can insert any character at any index of the string.

    Return the minimum number of steps to make s palindrome.

    A Palindrome String is one that reads the same backward as well as forward.

Example 1:
    Input: s = "zzazz"
    Output: 0
    Explanation: The string "zzazz" is already palindrome we do not need any insertions.
Example 2:
    Input: s = "mbadm"
    Output: 2
    Explanation: String can be "mbdadbm" or "mdbabdm".
Example 3:
    Input: s = "leetcode"
    Output: 5
    Explanation: Inserting 5 characters the string becomes "leetcodocteel".

Constraints:
    1 <= s.length <= 500
    s consists of lowercase English letters.
"""


class Solution:
    def minInsertions(self, s: str) -> int:
        # exception case
        assert isinstance(s, str) and len(s) >= 1
        # main method: (dynamic programming)
        return self._minInsertions(s)

    def _minInsertions(self, s: str) -> int:
        assert isinstance(s, str) and len(s) >= 1

        n = len(s)
        t = s[::-1]
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)

        return n - dp[-1][-1]


def main():
    # Example 1: Output: 0
    s = "zzazz"

    # Example 2: Output: 2
    # s = "mbadm"

    # Example 3: Output: 5
    # s = "leetcode"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minInsertions(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
