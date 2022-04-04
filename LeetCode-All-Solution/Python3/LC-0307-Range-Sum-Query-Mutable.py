#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0307-Range-Sum-Query-Mutable.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-04
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0307 - (Medium) - Range Sum Query - Mutable
https://leetcode.com/problems/range-sum-query-mutable/

Description & Requirement:
    Given an integer array nums, handle multiple queries of the following types:
        Update the value of an element in nums.
        Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.

    Implement the NumArray class:
        NumArray(int[] nums) Initializes the object with the integer array nums.
        void update(int index, int val) Updates the value of nums[index] to be val.
        int sumRange(int left, int right) Returns the sum of the elements of nums 
            between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

Example 1:
    Input
        ["NumArray", "sumRange", "update", "sumRange"]
        [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
    Output
        [null, 9, null, 8]
    Explanation
        NumArray numArray = new NumArray([1, 3, 5]);
        numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
        numArray.update(1, 2);   // nums = [1, 2, 5]
        numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8

Constraints:
    1 <= nums.length <= 3 * 10^4
    -100 <= nums[i] <= 100
    0 <= index < nums.length
    -100 <= val <= 100
    0 <= left <= right < nums.length
    At most 3 * 10^4 calls will be made to update and sumRange.
"""


class NumArray:

    def __init__(self, nums: List[int]):
        # Segment Tree
        # self.nums = nums
        self.num_nodes = len(nums)
        self.segment_tree = [0 for _ in range(len(nums) << 2)]  # at most 4 * len(nums) nodes, value is interval sum
        self._build_tree(nums, 0, 0, len(nums) - 1)  # recursively build segment tree

    def _build_tree(self, nums: List[int], cur_root: int, seg_start: int, seg_end: int) -> None:
        if seg_start == seg_end:  # leaf node, interval length is 1
            self.segment_tree[cur_root] = nums[seg_start]
            return
        seg_mid = (seg_start + seg_end) >> 1
        self._build_tree(nums, (cur_root << 1) + 1, seg_start, seg_mid)  # left subtree root is (cur_root << 1) + 1
        self._build_tree(nums, (cur_root << 1) + 2, seg_mid + 1, seg_end)  # right subtree root is (cur_root << 1) + 2

        # maintain the interval sum
        self.segment_tree[cur_root] = self.segment_tree[(cur_root << 1) + 1] + self.segment_tree[(cur_root << 1) + 2]

    def update(self, index: int, val: int) -> None:
        self._update(index, val, 0, 0, self.num_nodes - 1)

    def _update(self, index: int, val: int, cur_root: int, seg_start: int, seg_end: int) -> None:
        if seg_start == seg_end:  # leaf node, interval length is 1
            self.segment_tree[cur_root] = val
            return
        seg_mid = (seg_start + seg_end) >> 1
        if index <= seg_mid:
            self._update(index, val, (cur_root << 1) + 1, seg_start, seg_mid)  # left subtree
        else:
            self._update(index, val, (cur_root << 1) + 2, seg_mid + 1, seg_end)  # right subtree

        # maintain the interval sum
        self.segment_tree[cur_root] = self.segment_tree[(cur_root << 1) + 1] + self.segment_tree[(cur_root << 1) + 2]

    def sumRange(self, left: int, right: int) -> int:
        return self._sumRange(left, right, 0, 0, self.num_nodes - 1)

    def _sumRange(self, left: int, right: int, cur_root: int, seg_start: int, seg_end: int) -> int:
        if left == seg_start and right == seg_end:  # match interval
            return self.segment_tree[cur_root]
        seg_mid = (seg_start + seg_end) >> 1
        if right <= seg_mid:  # the whole target interval is on the left side
            return self._sumRange(left, right, (cur_root << 1) + 1, seg_start, seg_mid)  # left subtree
        if left > seg_mid:  # the whole target interval is on the right side
            return self._sumRange(left, right, (cur_root << 1) + 2, seg_mid + 1, seg_end)  # right subtree

        # the target interval is on both sides
        left_sum = self._sumRange(left, seg_mid, (cur_root << 1) + 1, seg_start, seg_mid)
        right_sum = self._sumRange(seg_mid + 1, right, (cur_root << 1) + 2, seg_mid + 1, seg_end)
        return left_sum + right_sum


def main():
    # Example 1: Output: [null, 9, null, 8]
    command_list = ["NumArray", "sumRange", "update", "sumRange"]
    param_list = [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]

    # init instance
    # solution = Solution()
    nums = param_list[0][0]
    obj = NumArray(nums)

    # run & time
    start = time.process_time()
    ans = ["null"]
    assert len(command_list) == len(param_list)
    for idx in range(1, len(command_list)):
        command = command_list[idx]
        param = param_list[idx]
        if command == "update":
            if isinstance(param, list) and len(param) == 2:
                obj.update(param[0], param[1])
            ans.append("null")
        elif command == "sumRange":
            if isinstance(param, list) and len(param) == 2:
                ans.append(obj.sumRange(param[0], param[1]))
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
