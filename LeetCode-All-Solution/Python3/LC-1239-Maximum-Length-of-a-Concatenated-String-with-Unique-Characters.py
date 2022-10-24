#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1239-Maximum-Length-of-a-Concatenated-String-with-Unique-Characters.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-10-24
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1239 - (Medium) - Maximum Length of a Concatenated String with Unique Characters
https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

Description & Requirement:
    You are given an array of strings arr. 
    A string s is formed by the concatenation of a subsequence of arr that has unique characters.

    Return the maximum possible length of s.

    A subsequence is an array that can be derived from another array by deleting some or no elements 
    without changing the order of the remaining elements.

Example 1:
    Input: arr = ["un","iq","ue"]
    Output: 4
    Explanation: All the valid concatenations are:
        - ""
        - "un"
        - "iq"
        - "ue"
        - "uniq" ("un" + "iq")
        - "ique" ("iq" + "ue")
        Maximum length is 4.
Example 2:
    Input: arr = ["cha","r","act","ers"]
    Output: 6
    Explanation: Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").
Example 3:
    Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
    Output: 26
    Explanation: The only string in arr has all 26 characters.

Constraints:
    1 <= arr.length <= 16
    1 <= arr[i].length <= 26
    arr[i] contains only lowercase English letters.
"""


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # exception case
        assert isinstance(arr, list) and len(arr) >= 1
        for string in arr:
            assert isinstance(string, str) and 26 >= len(string) >= 1
        # main method: (bit manipulation, DFS & backtrack)
        return self._maxLength(arr)

    def _maxLength(self, arr: List[str]) -> int:
        """
        Runtime: 173 ms, faster than 70.87% for Maximum Length of a Concatenated String with Unique Characters.
        Memory Usage: 14.1 MB, less than 38.57% for Maximum Length of a Concatenated String with Unique Characters.
        """
        assert isinstance(arr, list) and len(arr) >= 1

        masks = []
        for s in arr:
            mask = 0
            for ch in s:
                idx = ord(ch) - ord("a")
                if (mask >> idx) & 1:
                    mask = 0
                    break
                mask |= 1 << idx
            if mask > 0:
                masks.append(mask)

        res = [0]

        def __dfs(pos: int, _mask: int) -> None:
            if pos == len(masks):
                res[0] = max(res[0], bin(_mask).count("1"))
                return

            if (_mask & masks[pos]) == 0:
                __dfs(pos + 1, _mask | masks[pos])
            __dfs(pos + 1, _mask)

        __dfs(0, 0)

        return res[0]


def main():
    # Example 1: Output: 4
    # arr = ["un", "iq", "ue"]

    # Example 2: Output: 6
    arr = ["cha", "r", "act", "ers"]

    # Example 3: Output: 26
    # arr = ["abcdefghijklmnopqrstuvwxyz"]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maxLength(arr)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
