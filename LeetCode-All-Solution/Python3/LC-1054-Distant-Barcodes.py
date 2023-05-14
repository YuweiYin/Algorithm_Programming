#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1054-Distant-Barcodes.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-05-14
=================================================================="""

import sys
import time
from typing import List
import collections
import heapq
# import functools

"""
LeetCode - 1054 - (Medium) - Distant Barcodes
https://leetcode.com/problems/distant-barcodes/

Description & Requirement:
    In a warehouse, there is a row of barcodes, where the ith barcode is barcodes[i].

    Rearrange the barcodes so that no two adjacent barcodes are equal. 
    You may return any answer, and it is guaranteed an answer exists.

Example 1:
    Input: barcodes = [1,1,1,2,2,2]
    Output: [2,1,2,1,2,1]
Example 2:
    Input: barcodes = [1,1,1,1,2,2,3,3]
    Output: [1,3,1,3,1,2,1,2]

Constraints:
    1 <= barcodes.length <= 10000
    1 <= barcodes[i] <= 10000
"""


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        # exception case
        assert isinstance(barcodes, list) and len(barcodes) >= 1
        # main method: (heap)
        return self._rearrangeBarcodes(barcodes)

    def _rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        assert isinstance(barcodes, list) and len(barcodes) >= 1

        count = collections.Counter(barcodes)
        queue = []

        for x, cx in count.items():
            heapq.heappush(queue, (-cx, x))

        res = []
        while len(queue) > 0:
            cx, x = heapq.heappop(queue)
            if len(res) == 0 or res[-1] != x:
                res.append(x)
                if cx < -1:
                    heapq.heappush(queue, (cx + 1, x))
            else:
                cy, y = heapq.heappop(queue)
                res.append(y)
                if cy < -1:
                    heapq.heappush(queue, (cy + 1, y))
                heapq.heappush(queue, (cx, x))

        return res


def main():
    # Example 1: Output: [2,1,2,1,2,1]
    # barcodes = [1, 1, 1, 2, 2, 2]

    # Example 2: Output: [1,3,1,3,1,2,1,2]
    barcodes = [1, 1, 1, 1, 2, 2, 3, 3]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.rearrangeBarcodes(barcodes)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
