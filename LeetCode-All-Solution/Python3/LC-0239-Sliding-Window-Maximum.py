#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0239-Sliding-Window-Maximum.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-08-16
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools
# import itertools

"""
LeetCode - 0239 - (Hard) Sliding Window Maximum
https://leetcode.com/problems/sliding-window-maximum/

Description & Requirement:
    You are given an array of integers nums, there is a sliding window of size k which 
    is moving from the very left of the array to the very right. 
    You can only see the k numbers in the window. 
    Each time the sliding window moves right by one position.

    Return the max sliding window.

Example 1:
    Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
    Output: [3,3,5,5,6,7]
    Explanation: 
        Window position                Max
        ---------------               -----
        [1  3  -1] -3  5  3  6  7       3
         1 [3  -1  -3] 5  3  6  7       3
         1  3 [-1  -3  5] 3  6  7       5
         1  3  -1 [-3  5  3] 6  7       5
         1  3  -1  -3 [5  3  6] 7       6
         1  3  -1  -3  5 [3  6  7]      7
Example 2:
    Input: nums = [1], k = 1
    Output: [1]

Constraints:
    1 <= nums.length <= 10^5
    -10^4 <= nums[i] <= 10^4
    1 <= k <= nums.length
"""


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        assert isinstance(k, int) and k >= 1
        # main method: (queue)
        return self._maxSlidingWindow(nums, k)

    def _maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        assert isinstance(nums, list) and len(nums) >= 1
        assert isinstance(k, int) and k >= 1

        n = len(nums)
        q = collections.deque()
        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)

        res = [nums[q[0]]]
        for i in range(k, n):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            while q[0] <= i - k:
                q.popleft()
            res.append(nums[q[0]])

        return res


def main():
    # Example 1: Output: [3,3,5,5,6,7]
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    # Example 2: Output: [1]
    # nums = [1]
    # k = 1

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.maxSlidingWindow(nums, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
