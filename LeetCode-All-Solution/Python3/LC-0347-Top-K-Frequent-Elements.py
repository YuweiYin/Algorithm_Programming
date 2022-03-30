#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0347-Top-K-Frequent-Elements.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-30
=================================================================="""

import sys
import time
from typing import List, Tuple
import random
# import functools

"""
LeetCode - 0347 - (Medium) - Top K Frequent Elements
https://leetcode.com/problems/top-k-frequent-elements/

Description & Requirement:
    Given an integer array nums and an integer k, return the k most frequent elements. 
    You may return the answer in any order.

Example 1:
    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]
Example 2:
    Input: nums = [1], k = 1
    Output: [1]

Constraints:
    1 <= nums.length <= 10^5
    k is in the range [1, the number of unique elements in the array].
    It is guaranteed that the answer is unique.

Follow up:
    Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        assert isinstance(k, int) and k >= 1
        # main method: (use hash dict to record the counter of each number)
        #     and then find the k-th top frequent ones, based on LC-0215-Kth-Largest-Element-in-an-Array
        return self._topKFrequent(nums, k)

    def _topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Runtime: 108 ms, faster than 85.90% of Python3 online submissions for Top K Frequent Elements.
        Memory Usage: 18.9 MB, less than 23.62% of Python3 online submissions for Top K Frequent Elements.
        """
        hash_dict = dict({})
        for num in nums:
            if num not in hash_dict:
                hash_dict[num] = 1
            else:
                hash_dict[num] += 1

        num_counter = list(hash_dict.items())
        top_k_num_counter = self._findKthLargest(num_counter, k)

        return [num_c[0] for num_c in top_k_num_counter]

    def _findKthLargest(self, nums: List[Tuple[int]], k: int) -> List[Tuple[int]]:
        assert isinstance(k, int) and k >= 1
        assert isinstance(nums, list) and len(nums) >= k

        def __quick_select(left: int, right: int, target_order: int):
            cur_order = __partition(left, right)  # now, cur_order numbers are less than or equal to nums[cur_order]
            if cur_order == target_order:
                # return nums[cur_order]
                return nums[cur_order:]  # top k
            elif cur_order < target_order:
                return __quick_select(cur_order + 1, right, target_order)
            else:
                return __quick_select(left, cur_order - 1, target_order)

        def __partition(left: int, right: int) -> int:
            pivot_idx = random.randint(left, right)
            nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]  # swap pivot and right number
            # partition
            # pivot_num = nums[right]
            pivot_num_freq = nums[right][1]
            slow_ptr = left - 1
            for fast_ptr in range(left, right):  # fast_ptr always moves on, but slow_ptr doesn't
                if nums[fast_ptr][1] <= pivot_num_freq:  # any number that <= pivot_num should be put in left part
                    slow_ptr += 1
                    nums[fast_ptr], nums[slow_ptr] = nums[slow_ptr], nums[fast_ptr]
            # now, put pivot_num to the correct position
            slow_ptr += 1
            nums[right], nums[slow_ptr] = nums[slow_ptr], nums[right]
            return slow_ptr

        return __quick_select(0, len(nums) - 1, len(nums) - k)


def main():
    # Example 1: Output: [1,2]
    # nums = [1, 1, 1, 2, 2, 3]
    # k = 2

    # Example 2: Output: [1]
    nums = [1]
    k = 1

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.topKFrequent(nums, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
