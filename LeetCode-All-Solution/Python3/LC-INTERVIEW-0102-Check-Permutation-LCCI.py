#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-INTERVIEW-0102-Check-Permutation-LCCI.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-09-27
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - INTERVIEW-0102 - (Easy) - Check Permutation
https://leetcode.cn/problems/check-permutation-lcci/

Description & Requirement:
    Given two strings,write a method to decide if one is a permutation of the other.

Example 1:
    Input: s1 = "abc", s2 = "bca"
    Output: true
Example 2:
    Input: s1 = "abc", s2 = "bad"
    Output: false

Note:
    0 <= len(s1) <= 100
    0 <= len(s2) <= 100
"""


class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        # exception case
        assert isinstance(s1, str) and isinstance(s2, str)
        # main method: (hash dict)
        return self._CheckPermutation(s1, s2)

    def _CheckPermutation(self, s1: str, s2: str) -> bool:
        assert isinstance(s1, str) and isinstance(s2, str)

        if len(s1) != len(s2):
            return False

        hash_dict = dict({})
        for ch in s1:
            if ch not in hash_dict:
                hash_dict[ch] = 1
            else:
                hash_dict[ch] += 1

        for ch in s2:
            if ch not in hash_dict or hash_dict[ch] <= 0:
                return False
            else:
                hash_dict[ch] -= 1

        return True


def main():
    # Example 1: Output: true
    # s1 = "abc"
    # s2 = "bca"

    # Example 2: Output: false
    s1 = "abc"
    s2 = "bad"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.CheckPermutation(s1, s2)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
