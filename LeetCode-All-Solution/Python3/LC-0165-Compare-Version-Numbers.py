#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0165-Compare-Version-Numbers.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-25
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 0165 - (Medium) - Compare Version Numbers
https://leetcode.com/problems/compare-version-numbers/

Description & Requirement:
    Given two version numbers, version1 and version2, compare them.

    Version numbers consist of one or more revisions joined by a dot '.'. 
    Each revision consists of digits and may contain leading zeros. 
    Every revision contains at least one character. Revisions are 0-indexed from left to right, 
    with the leftmost revision being revision 0, the next revision being revision 1, and so on. 
    For example 2.5.33 and 0.1 are valid version numbers.

    To compare version numbers, compare their revisions in left-to-right order. 
    Revisions are compared using their integer value ignoring any leading zeros. 
    This means that revisions 1 and 001 are considered equal. 
    If a version number does not specify a revision at an index, then treat the revision as 0. 
    For example, version 1.0 is less than version 1.1 because their revision 0s are the same, 
    but their revision 1s are 0 and 1 respectively, and 0 < 1.

    Return the following:
        If version1 < version2, return -1.
        If version1 > version2, return 1.
        Otherwise, return 0.

Example 1:
    Input: version1 = "1.01", version2 = "1.001"
    Output: 0
    Explanation: Ignoring leading zeroes, both "01" and "001" represent the same integer "1".
Example 2:
    Input: version1 = "1.0", version2 = "1.0.0"
    Output: 0
    Explanation: version1 does not specify revision 2, which means it is treated as "0".
Example 3:
    Input: version1 = "0.1", version2 = "1.1"
    Output: -1
    Explanation: version1's revision 0 is "0", while version2's revision 0 is "1". 0 < 1, so version1 < version2.

Constraints:
    1 <= version1.length, version2.length <= 500
    version1 and version2 only contain digits and '.'.
    version1 and version2 are valid version numbers.
    All the given revisions in version1 and version2 can be stored in a 32-bit integer.
"""


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # exception case
        assert isinstance(version1, str) and len(version1) > 0
        assert isinstance(version2, str) and len(version2) > 0
        # main method: (split version string by dot ".", remove leading 0, and compare two versions from left to right)
        return self._compareVersion(version1, version2)

    def _compareVersion(self, version1: str, version2: str) -> int:
        ver_list_1 = version1.split(".")
        len_ver_1 = len(ver_list_1)
        ver_list_2 = version2.split(".")
        len_ver_2 = len(ver_list_2)

        def __clear_version_string(_s: str) -> int:
            # clear zero and convert to integer
            non_zero_idx = 0
            len_s = len(_s)
            while non_zero_idx < len_s and _s[non_zero_idx] == "0":
                non_zero_idx += 1
            if non_zero_idx == len_s:
                return 0
            else:
                return int(_s[non_zero_idx:])

        min_len = min(len_ver_1, len_ver_2)
        cur_idx = 0
        while cur_idx < min_len:
            cur_sub_ver_1 = __clear_version_string(ver_list_1[cur_idx])
            cur_sub_ver_2 = __clear_version_string(ver_list_2[cur_idx])
            if cur_sub_ver_1 < cur_sub_ver_2:
                return -1
            elif cur_sub_ver_1 > cur_sub_ver_2:
                return 1
            else:  # keep comparing next sub version
                cur_idx += 1

        # now, for the min_len part, version1 == version2, so consider the rest part
        if len_ver_1 < len_ver_2:  # version2 is longer, check the rest part
            while cur_idx < len_ver_2:
                if __clear_version_string(ver_list_2[cur_idx]) > 0:
                    return -1  # version2 is larger
                cur_idx += 1
        elif len_ver_1 > len_ver_2:  # version1 is longer, check the rest part
            while cur_idx < len_ver_1:
                if __clear_version_string(ver_list_1[cur_idx]) > 0:
                    return 1  # version1 is larger
                cur_idx += 1
        else:  # equal length
            return 0

        return 0


def main():
    # Example 1: Output: 0
    # version1 = "1.01"
    # version2 = "1.001"

    # Example 2: Output: 1
    # version1 = "1.0"
    # version2 = "1.0.1"

    # Example 3: Output: -1
    # version1 = "0.1"
    # version2 = "1.1"

    # Example 4: Output: 1
    version1 = "1.0.1"
    version2 = "1"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.compareVersion(version1, version2)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
