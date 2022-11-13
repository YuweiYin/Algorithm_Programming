#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0791-Custom-Sort-String.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-11-13
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 0791 - (Medium) - Custom Sort String
https://leetcode.com/problems/custom-sort-string/

Description & Requirement:
    You are given two strings order and s. 
    All the characters of order are unique and were sorted in some custom order previously.

    Permute the characters of s so that they match the order that order was sorted. 
    More specifically, if a character x occurs before a character y in order, 
    then x should occur before y in the permuted string.

    Return any permutation of s that satisfies this property.

Example 1:
    Input: order = "cba", s = "abcd"
    Output: "cbad"
    Explanation: 
        "a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a". 
        Since "d" does not appear in order, it can be at any position in the returned string. 
        "dcba", "cdba", "cbda" are also valid outputs.
Example 2:
    Input: order = "cbafg", s = "abcd"
    Output: "cbad"

Constraints:
    1 <= order.length <= 26
    1 <= s.length <= 200
    order and s consist of lowercase English letters.
    All the characters of order are unique.
"""


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # exception case
        assert isinstance(order, str) and len(order) >= 1
        assert isinstance(s, str) and len(s) >= 1
        # main method: (hash dict counter)
        return self._customSortString(order, s)

    def _customSortString(self, order: str, s: str) -> str:
        """
        Runtime: 23 ms, faster than 99.42% of Python3 online submissions for Custom Sort String.
        Memory Usage: 13.9 MB, less than 69.98% of Python3 online submissions for Custom Sort String.
        """
        assert isinstance(order, str) and len(order) >= 1
        assert isinstance(s, str) and len(s) >= 1

        s_cnt = dict({})
        for ch in s:
            if ch not in s_cnt:
                s_cnt[ch] = 1
            else:
                s_cnt[ch] += 1

        res = ""
        for ch in order:
            if ch in s_cnt and s_cnt[ch] > 0:
                res += ch * s_cnt[ch]
                s_cnt[ch] = 0

        for k, v in s_cnt.items():
            if v > 0:
                res += k * v

        return res


def main():
    # Example 1: Output: "cbad"
    order = "cba"
    s = "abcd"

    # Example 2: Output: "cbad"
    # order = "cbafg"
    # s = "abcd"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.customSortString(order, s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
