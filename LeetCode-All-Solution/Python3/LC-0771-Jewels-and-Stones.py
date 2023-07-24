#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0771-Jewels-and-Stones.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-07-24
=================================================================="""

import sys
import time
# from typing import List
# import functools
# import itertools

"""
LeetCode - 0771 - (Easy) - Jewels and Stones
https://leetcode.com/problems/jewels-and-stones/

Description & Requirement:
    You're given strings jewels representing the types of stones that are jewels, 
    and stones representing the stones you have. Each character in stones is a type of stone you have. 
    You want to know how many of the stones you have are also jewels.

    Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:
    Input: jewels = "aA", stones = "aAAbbbb"
    Output: 3
Example 2:
    Input: jewels = "z", stones = "ZZ"
    Output: 0

Constraints:
    1 <= jewels.length, stones.length <= 50
    jewels and stones consist of only English letters.
    All the characters of jewels are unique.
"""


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # exception case
        assert isinstance(jewels, str) and len(jewels) >= 1
        assert isinstance(stones, str) and len(stones) >= 1
        # main method: (hash set)
        return self._numJewelsInStones(jewels, stones)

    def _numJewelsInStones(self, jewels: str, stones: str) -> int:
        assert isinstance(jewels, str) and len(jewels) >= 1
        assert isinstance(stones, str) and len(stones) >= 1

        j_set = set(jewels)
        return sum(s in j_set for s in stones)


def main():
    # Example 1: Output: 3
    jewels = "aA"
    stones = "aAAbbbb"

    # Example 2: Output: 0
    # jewels = "z"
    # stones = "ZZ"

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.numJewelsInStones(jewels, stones)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
