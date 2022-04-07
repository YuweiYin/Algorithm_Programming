#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0014-Longest-Common-Prefix.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-07
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0014 - (Easy) - Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/

Description & Requirement:
    Write a function to find the longest common prefix string amongst an array of strings.

    If there is no common prefix, return an empty string "".

Example 1:
    Input: strs = ["flower","flow","flight"]
    Output: "fl"
Example 2:
    Input: strs = ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.

Constraints:
    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lower-case English letters.
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # exception case
        assert isinstance(strs, list) and len(strs) >= 1
        # main method: (check chars one by one)
        return self._longestCommonPrefix(strs)

    def _longestCommonPrefix(self, strs: List[str]) -> str:
        len_strs = len(strs)
        assert len_strs >= 1 and isinstance(strs[0], str)

        prefix = ""
        max_idx = min([len(_str) for _str in strs])
        for idx in range(max_idx):
            cur_char = strs[0][idx]
            if all([_str[idx] == cur_char for _str in strs]):
                prefix += cur_char
            else:
                break

        return prefix


def main():
    # Example 1: Output: "fl"
    strs = ["flower", "flow", "flight"]

    # Example 2: Output: ""
    # strs = ["dog","racecar","car"]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.longestCommonPrefix(strs)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
