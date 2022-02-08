#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0918-Maximum-Sum-Circular-Subarray.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-08
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0918 - (Medium) - Maximum Sum Circular Subarray
https://leetcode.com/problems/maximum-sum-circular-subarray/

Description & Requirement:
    Given a circular integer array nums of length n, 
    return the maximum possible sum of a non-empty subarray of nums.

    A circular array means the end of the array connects to the beginning of the array. 
    Formally, the next element of nums[i] is nums[(i + 1) % n] and 
    the previous element of nums[i] is nums[(i - 1 + n) % n].

    A subarray may only include each element of the fixed buffer nums at most once. 
    Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], 
    there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

Example 1:
    Input: nums = [1,-2,3,-2]
    Output: 3
    Explanation: Subarray [3] has maximum sum 3.
Example 2:
    Input: nums = [5,-3,5]
    Output: 10
    Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.
Example 3:
    Input: nums = [-3,-2,-3]
    Output: -2
    Explanation: Subarray [-2] has maximum sum -2.

Constraints:
    n == nums.length
    1 <= n <= 3 * 10^4
    -3 * 10^4 <= nums[i] <= 3 * 10^4

Related Problem:
    LC-0053-Maximum-Subarray
"""


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # exception case
        if not isinstance(nums, list) or len(nums) <= 0:
            return 0  # Error input type
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1], nums[0] + nums[1])
        # main method: (note: all the intervals in following description are inclusive close interval.)
        #     two main case: 1. the max array is [idx1, idx2], where idx1 <= idx2;
        #     2. the max array is [0, idx1] and [idx2, len(nums)-1], where 0 <= idx1, idx2 < len(nums), idx1 + 2 <= idx2
        # for case 1, just apply Kadane's algorithm to nums[:]
        # for case 2, think reversely: the max subarray of [0, idx1] + max subarray of [idx2, len(nums)-1] is just
        #     equal to the sum(nums) - the min subarray of [idx1 + 1, idx2 - 1];
        #     to get a min subarray of [idx1 + 1, idx2 - 1], just apply Kadane's algorithm to the neg_nums,
        #         where neg_nums = [-num for num in nums],
        #         however, applying K's alg to the whole neg_nums means [0, idx1] and [idx2, len(nums)-1]
        #         are both empty, this is not correct, so apply K's alg to neg_nums[1:] and neg_nums[:-1] separately
        #     the final res is max(K(nums), sum(nums) + K(neg_nums[1:]), sum(nums) + K(neg_nums[:-1]))
        return self._maxSubarraySumCircular(nums)

    def _maxSubarraySumCircular(self, nums: List[int]) -> int:

        def __kadane_max_subarray(numbers: List[int]) -> int:
            # len_numbers = len(numbers)
            # if len_numbers == 1:
            #     return numbers[0]
            # if len_numbers == 2:
            #     return max(numbers[0], numbers[1], numbers[0] + numbers[1])

            kadane_res = numbers[0]
            accumulate_sum = 0  # from some num, the accumulated sum

            for cur_num in numbers:
                # accumulate_sum is either the current num or the former accumulate_sum + current num
                # idea: if accumulate_sum is positive, it is always helpful. Once it's negative, change it to cur_num
                accumulate_sum = max(cur_num, accumulate_sum + cur_num)
                # update res
                kadane_res = max(kadane_res, accumulate_sum)

            return kadane_res

        res_1 = __kadane_max_subarray(nums)

        neg_nums = [-num for num in nums]
        sum_nums = sum(nums)
        res_2 = sum_nums + __kadane_max_subarray(neg_nums[1:])
        res_3 = sum_nums + __kadane_max_subarray(neg_nums[:-1])

        return max(res_1, res_2, res_3)


def main():
    # Example 1: Output: 3
    # nums = [1, -2, 3, -2]

    # Example 2: Output: 10
    nums = [5, -3, 5]

    # Example 3: Output: -2
    # nums = [-3, -2, -3]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maxSubarraySumCircular(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
