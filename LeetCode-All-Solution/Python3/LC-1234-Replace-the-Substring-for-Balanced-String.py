#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1234-Replace-the-Substring-for-Balanced-String.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-02-13
=================================================================="""

import sys
import time
import collections
# from typing import List
# import functools

"""
LeetCode - 1234 - (Medium) - Replace the Substring for Balanced String
https://leetcode.com/problems/replace-the-substring-for-balanced-string/

Description & Requirement:
    You are given a string s of length n containing only four kinds of characters: 'Q', 'W', 'E', and 'R'.

    A string is said to be balanced if each of its characters appears n / 4 times where n is the length of the string.

    Return the minimum length of the substring that can be replaced with any other string of the same length 
    to make s balanced. If s is already balanced, return 0.

Example 1:
    Input: s = "QWER"
    Output: 0
    Explanation: s is already balanced.
Example 2:
    Input: s = "QQWE"
    Output: 1
    Explanation: We need to replace a 'Q' to 'R', so that "RQWE" (or "QRWE") is balanced.
Example 3:
    Input: s = "QQQW"
    Output: 2
    Explanation: We can replace the first "QQ" to "ER".

Constraints:
    n == s.length
    4 <= n <= 10^5
    n is a multiple of 4.
    s contains only 'Q', 'W', 'E', and 'R'.
"""


class Solution:
    def balancedString(self, s: str) -> int:
        # exception case
        assert isinstance(s, str) and len(s) >= 4
        # main method: (sliding window)
        return self._balancedString(s)

    def _balancedString(self, s: str) -> int:
        assert isinstance(s, str) and len(s) >= 4

        cnt = collections.Counter(s)
        partial = len(s) // 4

        def check():
            if cnt['Q'] > partial or cnt['W'] > partial or \
                    cnt['E'] > partial or cnt['R'] > partial:
                return False
            return True

        if check():
            return 0

        res = len(s)
        right = 0
        for left, ch in enumerate(s):
            while right < len(s) and not check():
                cnt[s[right]] -= 1
                right += 1
            if not check():
                break
            res = min(res, right - left)
            cnt[ch] += 1

        return res


def main():
    # Example 1: Output: 0
    s = "QWER"

    # Example 2: Output: 1
    # s = "QQWE"

    # Example 3: Output: 2
    # s = "QQQW"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.balancedString(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
