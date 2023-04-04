#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2405-Optimal-Partition-of-String.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-04-04
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 2405 - (Medium) - Optimal Partition of String
https://leetcode.com/problems/optimal-partition-of-string/

Description & Requirement:
    Given a string s, partition the string into one or more substrings such that 
    the characters in each substring are unique. 
    That is, no letter appears in a single substring more than once.

    Return the minimum number of substrings in such a partition.

    Note that each character should belong to exactly one substring in a partition.

Example 1:
    Input: s = "abacaba"
    Output: 4
    Explanation:
    Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").
    It can be shown that 4 is the minimum number of substrings needed.
Example 2:
    Input: s = "ssssss"
    Output: 6
    Explanation:
        The only valid partition is ("s","s","s","s","s","s").

Constraints:
    1 <= s.length <= 10^5
    s consists of only English lowercase letters.
"""


class Solution:
    def partitionString(self, s: str) -> int:
        # exception case
        assert isinstance(s, str) and len(s) >= 1 and s.islower()
        # main method: (bit manipulation)
        return self._partitionString(s)

    def _partitionString(self, s: str) -> int:
        assert isinstance(s, str) and len(s) >= 1 and s.islower()

        res = 0
        bit_map = 0
        ord_a = ord("a")

        for ch in s:
            ch_id = ord(ch) - ord_a
            if (bit_map >> ch_id) & 0x01:
                bit_map = 0
                res += 1
            bit_map |= (1 << ch_id)

        res += 1
        return res


def main():
    # Example 1: Output: 4
    s = "abacaba"

    # Example 2: Output: 6
    # s = "ssssss"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.partitionString(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
