#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0703-Kth-Largest-Element-in-a-Stream.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-08
=================================================================="""

import sys
import time
from typing import List
import heapq
# import functools

"""
LeetCode - 0703 - (Easy) - Kth Largest Element in a Stream
https://leetcode.com/problems/kth-largest-element-in-a-stream/

Description & Requirement:
    Design a class to find the kth largest element in a stream. 
    Note that it is the kth largest element in the sorted order, not the kth distinct element.

    Implement KthLargest class:
        KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
        int add(int val) Appends the integer val to the stream and 
            returns the element representing the kth largest element in the stream.

Example 1:
    Input
        ["KthLargest", "add", "add", "add", "add", "add"]
        [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
    Output
        [null, 4, 5, 5, 8, 8]
    Explanation
        KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
        kthLargest.add(3);   // return 4
        kthLargest.add(5);   // return 5
        kthLargest.add(10);  // return 5
        kthLargest.add(9);   // return 8
        kthLargest.add(4);   // return 8

Constraints:
    1 <= k <= 10^4
    0 <= nums.length <= 10^4
    -10^4 <= nums[i] <= 10^4
    -10^4 <= val <= 10^4
    At most 10^4 calls will be made to add.
    It is guaranteed that there will be at least k elements in the array when you search for the kth element.
"""


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []  # heap, max length == k
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]  # return the smallest one of k largest numbers


def main():
    # Example 1: Output: [null, 4, 5, 5, 8, 8]
    command_list = ["KthLargest", "add", "add", "add", "add", "add"]
    param_list = [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]

    # init instance
    # solution = Solution()
    k = param_list[0][0]
    nums = param_list[0][1]
    obj = KthLargest(k, nums)
    ans = ["null"]

    # run & time
    start = time.process_time()
    assert len(command_list) == len(param_list)
    for idx in range(len(command_list)):
        command = command_list[idx]
        param = param_list[idx]
        if command == "add":
            if isinstance(param, list) and len(param) == 1:
                ans.append(obj.add(param[0]))
            else:
                ans.append("null")
        else:
            ans.append("null")
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
