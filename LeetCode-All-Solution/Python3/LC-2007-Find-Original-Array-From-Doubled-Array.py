#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2007-Find-Original-Array-From-Doubled-Array.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-09-15
=================================================================="""

import sys
import time
from typing import List
import heapq
# import collections
# import functools

"""
LeetCode - 2007 - (Medium) - Find Original Array From Doubled Array
https://leetcode.com/problems/find-original-array-from-doubled-array/

Description & Requirement:
    An integer array original is transformed into a doubled array changed by 
    appending twice the value of every element in original, and then randomly shuffling the resulting array.

    Given an array changed, return original if changed is a doubled array. 
    If changed is not a doubled array, return an empty array. 
    The elements in original may be returned in any order.

Example 1:
    Input: changed = [1,3,4,2,6,8]
    Output: [1,3,4]
    Explanation: One possible original array could be [1,3,4]:
        - Twice the value of 1 is 1 * 2 = 2.
        - Twice the value of 3 is 3 * 2 = 6.
        - Twice the value of 4 is 4 * 2 = 8.
        Other original arrays could be [4,3,1] or [3,1,4].
Example 2:
    Input: changed = [6,3,0,1]
    Output: []
    Explanation: changed is not a doubled array.
Example 3:
    Input: changed = [1]
    Output: []
    Explanation: changed is not a doubled array.

Constraints:
    1 <= changed.length <= 10^5
    0 <= changed[i] <= 10^5
"""


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        # exception case
        assert isinstance(changed, list) and len(changed) >= 1
        for num in changed:
            assert isinstance(num, int) and num >= 0
        # main method: (sort and use heap, match the lowest pair first)
        return self._findOriginalArray(changed)

    def _findOriginalArray(self, changed: List[int]) -> List[int]:
        """
        Runtime: 4069 ms, faster than 5.13% of Python3 submissions for Find Original Array From Doubled Array.
        Memory Usage: 29.1 MB, less than 95.61% of Python3 submissions for Find Original Array From Doubled Array.
        """
        assert isinstance(changed, list) and len(changed) >= 1
        n = len(changed)
        if n & 0x01 == 1:
            return []

        changed.sort()
        heap = []
        res = []

        for idx in range(n):
            cur_num = changed[idx]
            if len(heap) > 0 and (heap[0] << 1) == cur_num:
                res.append(heapq.heappop(heap))  # matched
            else:
                heapq.heappush(heap, cur_num)

        return res if len(heap) == 0 else []


def main():
    # Example 1: Output: [1,3,4]
    changed = [1, 3, 4, 2, 6, 8]

    # Example 2: Output: []
    # changed = [6, 3, 0, 1]

    # Example 3: Output: []
    # changed = [1]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.findOriginalArray(changed)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
