#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0229-Majority-Element-II.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-10-05
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools
# import itertools

"""
LeetCode - 0229 - (Medium) Majority Element II
https://leetcode.com/problems/majority-element-ii/

Description & Requirement:
    Given an integer array of size n, 
    find all elements that appear more than ⌊ n/3 ⌋ times.

Example 1:
    Input: nums = [3,2,3]
    Output: [3]
Example 2:
    Input: nums = [1]
    Output: [1]
Example 3:
    Input: nums = [1,2]
    Output: [1,2]

Constraints:
    1 <= nums.length <= 5 * 10^4
    -10^9 <= nums[i] <= 10^9

Follow up:
    Could you solve the problem in linear time and in O(1) space?
"""


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        # main method: (Moore Voting)
        # A Fast Majority Vote Algorithm - J Strother Moore
        # https://www.cs.utexas.edu/users/boyer/ftp/ics-reports/cmp32.pdf
        return self._majorityElement(nums)

    def _majorityElement(self, nums: List[int]) -> List[int]:
        assert isinstance(nums, list) and len(nums) >= 1

        res = []
        item1, item2 = 0, 0
        vote1, vote2 = 0, 0

        for num in nums:
            # if it is the first item, the counter pluses one
            if vote1 > 0 and num == item1:
                vote1 += 1
            # if it is the first item, the counter also pluses one
            elif vote2 > 0 and num == item2:
                vote2 += 1
            # choose the first item
            elif vote1 == 0:
                item1 = num
                vote1 += 1
            # choose the second item
            elif vote2 == 0:
                item2 = num
                vote2 += 1
            # if the three items defer from each other, offset once
            else:
                vote1 -= 1
                vote2 -= 1

        cnt1, cnt2 = 0, 0
        # check if the number of occurrence fulfill the requirements
        for num in nums:
            if vote1 > 0 and num == item1:
                cnt1 += 1
            if vote2 > 0 and num == item2:
                cnt2 += 1

        if vote1 > 0 and cnt1 > len(nums) / 3:
            res.append(item1)
        if vote2 > 0 and cnt2 > len(nums) / 3:
            res.append(item2)

        return res


def main():
    # Example 1: Output: [3]
    nums = [3, 2, 3]

    # Example 2: Output: [1]
    # nums = [1]

    # Example 3: Output: [1,2]
    # nums = [1, 2]

    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.majorityElement(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
