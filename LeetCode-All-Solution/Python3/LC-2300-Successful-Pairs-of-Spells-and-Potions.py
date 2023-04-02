#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2300-Successful-Pairs-of-Spells-and-Potions.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-04-02
=================================================================="""

import sys
import time
from typing import List
import bisect
# import collections
# import functools

"""
LeetCode - 2300 - (Medium) - Successful Pairs of Spells and Potions
https://leetcode.com/problems/successful-pairs-of-spells-and-potions/

Description & Requirement:
    You are given two positive integer arrays spells and potions, of length n and m respectively, 
    where spells[i] represents the strength of the i-th spell and 
    potions[j] represents the strength of the j-th potion.

    You are also given an integer success. A spell and potion pair is considered successful 
    if the product of their strengths is at least success.

    Return an integer array pairs of length n where pairs[i] is the number of potions that 
    will form a successful pair with the ith spell.

Example 1:
    Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
    Output: [4,0,3]
    Explanation:
        - 0th spell: 5 * [1,2,3,4,5] = [5,10,15,20,25]. 4 pairs are successful.
        - 1st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
        - 2nd spell: 3 * [1,2,3,4,5] = [3,6,9,12,15]. 3 pairs are successful.
        Thus, [4,0,3] is returned.
Example 2:
    Input: spells = [3,1,2], potions = [8,5,8], success = 16
    Output: [2,0,2]
    Explanation:
        - 0th spell: 3 * [8,5,8] = [24,15,24]. 2 pairs are successful.
        - 1st spell: 1 * [8,5,8] = [8,5,8]. 0 pairs are successful. 
        - 2nd spell: 2 * [8,5,8] = [16,10,16]. 2 pairs are successful. 
        Thus, [2,0,2] is returned.

Constraints:
    n == spells.length
    m == potions.length
    1 <= n, m <= 10^5
    1 <= spells[i], potions[i] <= 10^5
    1 <= success <= 10^10
"""


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # exception case
        assert isinstance(spells, list) and len(spells) >= 1
        assert isinstance(potions, list) and len(potions) >= 1
        assert isinstance(success, int) and success >= 1
        # main method: (sort and binary search)
        return self._successfulPairs(spells, potions, success)

    def _successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        assert isinstance(spells, list) and len(spells) >= 1
        assert isinstance(potions, list) and len(potions) >= 1
        assert isinstance(success, int) and success >= 1

        potions.sort()
        return [len(potions) - bisect.bisect_right(potions, (success - 1) // x) for x in spells]


def main():
    # Example 1: Output: [4,0,3]
    spells = [5, 1, 3]
    potions = [1, 2, 3, 4, 5]
    success = 7

    # Example 2: Output: [2,0,2]
    # spells = [3, 1, 2]
    # potions = [8, 5, 8]
    # success = 16

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.successfulPairs(spells, potions, success)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
