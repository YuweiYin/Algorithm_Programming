#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1354-Construct-Target-Array-With-Multiple-Sums.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-06-24
=================================================================="""

import sys
import time
from typing import List
import heapq
# import functools

"""
LeetCode - 1354 - (Hard) - Construct Target Array With Multiple Sums
https://leetcode.com/problems/construct-target-array-with-multiple-sums/

Description & Requirement:
    You are given an array target of n integers. 
    From a starting array arr consisting of n 1's, you may perform the following procedure :

        let x be the sum of all elements currently in your array.
        choose index i, such that 0 <= i < n and set the value of arr at index i to x.
        You may repeat this procedure as many times as needed.

    Return true if it is possible to construct the target array from arr, otherwise, return false.

Example 1:
    Input: target = [9,3,5]
    Output: true
    Explanation: Start with arr = [1, 1, 1] 
        [1, 1, 1], sum = 3 choose index 1
        [1, 3, 1], sum = 5 choose index 2
        [1, 3, 5], sum = 9 choose index 0
        [9, 3, 5] Done
Example 2:
    Input: target = [1,1,1,2]
    Output: false
    Explanation: Impossible to create target array from [1,1,1,1].
Example 3:
    Input: target = [8,5]
    Output: true

Constraints:
    n == target.length
    1 <= n <= 5 * 10^4
    1 <= target[i] <= 10^9
"""


class Solution:
    def isPossible(self, target: List[int]) -> bool:
        # exception case
        assert isinstance(target, list) and len(target) >= 1
        for num in target:
            assert isinstance(num, int) and num >= 1
        # main method: (heap: from target list, try to construct [1, 1, ..., 1])
        return self._isPossible(target)

    def _isPossible(self, target: List[int]) -> bool:
        assert isinstance(target, list) and len(target) >= 1

        cumulus = 0
        heap = []

        if len(target) == 1:
            return target[0] == 1

        for num in target:
            heapq.heappush(heap, - num)
            cumulus += num

        while heap[0] != -1:
            cur_num = - heapq.heappop(heap)

            other_num = cumulus - cur_num
            if other_num < len(target) - 1:
                return False

            diff = cur_num - other_num
            if diff < 1:
                return False
            if other_num == 0:
                return False
            diff %= other_num
            if diff == 0:
                diff = other_num

            heapq.heappush(heap, - diff)
            cumulus -= cur_num - diff

        return True


def main():
    # Example 1: Output: true
    # target = [9, 3, 5]

    # Example 2: Output: false
    # target = [1, 1, 1, 2]

    # Example 3: Output: true
    target = [8, 5]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.isPossible(target)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
