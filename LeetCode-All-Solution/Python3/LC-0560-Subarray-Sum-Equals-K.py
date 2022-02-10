#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0560-Subarray-Sum-Equals-K.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-10
=================================================================="""

import sys
import time
from typing import List

"""
LeetCode - 0560 - (Medium) - Subarray Sum Equals K
https://leetcode.com/problems/subarray-sum-equals-k/

Description & Requirement:
    Given an array of integers nums and an integer k, 
    return the total number of continuous subarrays whose sum equals to k.

Example 1:
    Input: nums = [1,1,1], k = 2
    Output: 2
Example 2:
    Input: nums = [1,2,3], k = 3
    Output: 2

Constraints:
    1 <= nums.length <= 2 * 10^4
    -1000 <= nums[i] <= 1000
    -10^7 <= k <= 10^7

Related Problem:
    LC-0713-Subarray-Product-Less-Than-K
"""


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # exception case
        if not isinstance(nums, list) or len(nums) <= 0:
            return 0  # Error input type
        if len(nums) == 1:
            return 1 if nums[0] == k else 0
        # main method: (prefix sum & hash dict)
        return self._subarraySum(nums, k)

    def _subarraySum(self, nums: List[int], k: int) -> int:
        """
        Runtime: 264 ms, faster than 72.47% of Python3 online submissions for Subarray Sum Equals K.
        Memory Usage: 16.6 MB, less than 93.61% of Python3 online submissions for Subarray Sum Equals K.
        """
        len_nums = len(nums)
        assert len_nums >= 2

        res = 0
        prefix_sum = 0
        hash_dict = dict({})  # key: prefix_sum; value: counter of this prefix_sum
        hash_dict[0] = 1  # from start, sum is 0, occurrence is 1

        for idx, num in enumerate(nums):
            prefix_sum += num

            # core: to count how many valid subarrays with end index = idx,
            # just look at how many former_prefix == (prefix_sum - k)
            # because we can remove the left part (which a former_prefix represents) of the current prefix_sum to get k
            # e.g., nums = [1, 2, 3], k = 5.  when idx == 2, num == 3, cur hash_dict == {0: 1, 1: 1, 3: 1}
            # cur prefix_sum == 6, clearly, [1, 2, 3] can't fulfill sum == k,
            # so consider if there is former prefix that equals to (prefix_sum - k) == 6 - 5 == 1
            # yes, there is. so remove former_prefix [1] from the current_prefix [1, 2, 3] to get [2, 3], bingo!
            if (prefix_sum - k) in hash_dict:
                res += hash_dict[prefix_sum - k]

            # update hash_dict, count the occurrence of this prefix_sum
            if prefix_sum not in hash_dict:
                hash_dict[prefix_sum] = 1
            else:
                hash_dict[prefix_sum] += 1

        return res


def main():
    # Example 1: Output: 2
    # nums = [1, 1, 1]
    # k = 2

    # Example 2: Output: 2
    # nums = [1, 2, 3]
    # k = 3

    # Example 3: Output: 6
    nums = [1, 1, 1, -1, -1, 3, 1]
    k = 2

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.subarraySum(nums, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
