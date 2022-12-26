#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1759-Count-Number-of-Homogenous-Substrings.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-12-26
=================================================================="""

import sys
import time
from itertools import groupby
# from typing import List
# import collections
# import functools

"""
LeetCode - 1759 - (Medium) - Count Number of Homogenous Substrings
https://leetcode.com/problems/count-number-of-homogenous-substrings/

Description & Requirement:
    Given a string s, return the number of homogenous substrings of s. 
    Since the answer may be too large, return it modulo 10^9 + 7.

    A string is homogenous if all the characters of the string are the same.

    A substring is a contiguous sequence of characters within a string.

Example 1:
    Input: s = "abbcccaa"
    Output: 13
    Explanation: The homogenous substrings are listed as below:
        "a"   appears 3 times.
        "aa"  appears 1 time.
        "b"   appears 2 times.
        "bb"  appears 1 time.
        "c"   appears 3 times.
        "cc"  appears 2 times.
        "ccc" appears 1 time.
        3 + 1 + 2 + 1 + 3 + 2 + 1 = 13.
Example 2:
    Input: s = "xy"
    Output: 2
    Explanation: The homogenous substrings are "x" and "y".
Example 3:
    Input: s = "zzzzz"
    Output: 15

Constraints:
    1 <= s.length <= 10^5
    s consists of lowercase letters.
"""


class Solution:
    def countHomogenous(self, s: str) -> int:
        # exception case
        assert isinstance(s, str) and len(s) >= 1 and s.islower()
        # main method: (mathematics)
        return self._countHomogenous(s)

    def _countHomogenous(self, s: str) -> int:
        """
        Time: beats 95.95%; Space: beats 6.88%
        """
        assert isinstance(s, str) and len(s) >= 1 and s.islower()

        res = 0
        MOD = int(1e9+7)

        for ch, group in groupby(s):
            g_len = len(list(group))
            res += ((g_len + 1) * g_len) >> 1
            res %= MOD

        return res % MOD


def main():
    # Example 1: Output: 13
    s = "abbcccaa"

    # Example 2: Output: 2
    # s = "xy"

    # Example 3: Output: 15
    # s = "zzzzz"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.countHomogenous(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
