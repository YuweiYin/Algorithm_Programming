#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-INTERVIEW-0105-One-Away-LCCI.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-05-13
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - INTERVIEW-0105 - (Medium) - One Away LCCI
https://leetcode.cn/problems/one-away-lcci/

Description & Requirement:
    There are three types of edits that can be performed on strings: 
    insert a character, remove a character, or replace a character.

    Given two strings, write a function to check if they are one edit (or zero edits) away.

Example 1:
    Input: 
        first = "pale"
        second = "ple"
    Output: True
Example 2:
    Input: 
        first = "pales"
        second = "pal"
    Output: False
"""


class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        # exception case
        assert isinstance(first, str) and isinstance(second, str)
        # main method: (try to modify the unmatched char)
        return self._oneEditAway(first, second)

    def _oneEditAway(self, first: str, second: str) -> bool:
        assert isinstance(first, str) and isinstance(second, str)
        if first == second:
            return True

        len_f, len_s = len(first), len(second)
        if len_f == 0:
            return len_s == 1 or len_s == 0
        if len_s == 0:
            return len_f == 1 or len_f == 0
        if abs(len_f - len_s) >= 2:
            return False
        if len_f == len_s:  # need to modify one char from first or second
            can_modify = True  # can modify at most once
            for idx, ch_f in enumerate(first):
                ch_s = second[idx]
                if ch_f != ch_s:
                    if can_modify:
                        can_modify = False
                    else:
                        return False
            return True
        else:  # need to delete one char from first or second
            if len_f < len_s:  # set first as the longer string
                first, second = second, first
                len_f, len_s = len(first), len(second)
            can_delete = True
            idx_f = 0
            idx_s = 0
            while idx_f < len_f and idx_s < len_s:
                ch_f = first[idx_f]
                ch_s = second[idx_s]
                if ch_f == ch_s:
                    idx_f += 1
                    idx_s += 1
                else:
                    if can_delete:
                        can_delete = False
                        idx_f += 1  # delete this char in the first string
                    else:
                        return False
            if idx_s != len_s:
                return False
            if idx_f == len_f:
                return True
            elif idx_f == len_f - 1:  # delete the last one char
                return can_delete
            else:
                return False


def main():
    # Example 1: Output: True
    # first = "pale"
    # second = "ple"

    # Example 2: Output: False
    # first = "pales"
    # second = "pal"

    # Example 3: Output: True
    first = "a"
    second = "ab"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.oneEditAway(first, second)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
