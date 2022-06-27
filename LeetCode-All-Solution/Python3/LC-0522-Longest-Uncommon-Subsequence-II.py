#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0522-Longest-Uncommon-Subsequence-II.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-06-27
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0522 - (Medium) - Longest Uncommon Subsequence II
https://leetcode.com/problems/longest-uncommon-subsequence-ii/

Description & Requirement:
    Given an array of strings strs, return the length of the longest uncommon subsequence between them. 
    If the longest uncommon subsequence does not exist, return -1.

    An uncommon subsequence between an array of strings is a string 
    that is a subsequence of one string but not the others.

    A subsequence of a string s is a string that can be obtained after deleting any number of characters from s.

    For example, "abc" is a subsequence of "aebdc" because you can delete the underlined characters in "aebdc" 
    to get "abc". Other subsequences of "aebdc" include "aebdc", "aeb", and "" (empty string).

Example 1:
    Input: strs = ["aba","cdc","eae"]
    Output: 3
Example 2:
    Input: strs = ["aaa","aaa","aa"]
    Output: -1

Constraints:
    2 <= strs.length <= 50
    1 <= strs[i].length <= 10
    strs[i] consists of lowercase English letters.
"""


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        # exception case
        assert isinstance(strs, list) and len(strs) >= 2
        for s in strs:
            assert isinstance(s, str) and len(s) >= 1
        # main method: (check if each string is a subsequence of other strings, O(n^2))
        return self._findLUSlength(strs)

    def _findLUSlength(self, strs: List[str]) -> int:
        assert isinstance(strs, list) and len(strs) >= 2

        def __is_sub(_s: str, _t: str) -> bool:
            s_idx, t_idx = 0, 0
            while s_idx < len(_s) and t_idx < len(_t):
                if _s[s_idx] == _t[t_idx]:
                    s_idx += 1
                t_idx += 1
            return s_idx == len(_s)

        # strs.sort(key=lambda x: len(x), reverse=True)

        res = -1
        for cur_idx, cur_str in enumerate(strs):
            not_sub = True
            for other_idx, other_str in enumerate(strs):
                if cur_idx != other_idx and __is_sub(cur_str, other_str):
                    not_sub = False
                    break
            if not_sub:
                res = max(res, len(cur_str))

        return res


def main():
    # Example 1: Output: 3
    strs = ["aba", "cdc", "eae"]

    # Example 2: Output: -1
    # strs = ["aaa", "aaa", "aa"]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.findLUSlength(strs)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
