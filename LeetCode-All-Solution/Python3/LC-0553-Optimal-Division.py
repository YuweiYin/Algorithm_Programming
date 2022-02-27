#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0553-Optimal-Division.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-27
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0553 - (Medium) - Optimal Division
https://leetcode.com/problems/optimal-division/

Description & Requirement:
    You are given an integer array nums. The adjacent integers in nums will perform the float division.

    For example, for nums = [2,3,4], we will evaluate the expression "2/3/4".

    However, you can add any number of parenthesis at any position to change the priority of operations. 
    You want to add these parentheses such the value of the expression after the evaluation is maximum.

    Return the corresponding expression that has the maximum value in string format.

    Note: your expression should not contain redundant parenthesis.

Example 1:
    Input: nums = [1000,100,10,2]
    Output: "1000/(100/10/2)"
    Explanation:
        1000/(100/10/2) = 1000/((100/10)/2) = 200
        However, the bold parenthesis in "1000/((100/10)/2)" are redundant, 
            since they don't influence the operation priority. So you should return "1000/(100/10/2)".
        Other cases:
        1000/(100/10)/2 = 50
        1000/(100/(10/2)) = 50
        1000/100/10/2 = 0.5
        1000/100/(10/2) = 2
Example 2:
    Input: nums = [2,3,4]
    Output: "2/(3/4)"
Example 3:
    Input: nums = [2]
    Output: "2"

Constraints:
    1 <= nums.length <= 10
    2 <= nums[i] <= 1000
    There is only one optimal division for the given input.
"""


class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        # exception case
        assert isinstance(nums, list) and len(nums) > 0
        # main method: (since nums[i] >= 2, the A in A/B/C/... must be (A), and try to minimize (B/C/...))
        #     to minimize (B/C/...), just keep this form and don't add any parentheses because nums[i] >= 2
        return self._optimalDivision(nums)

    def _optimalDivision(self, nums: List[int]) -> str:
        len_nums = len(nums)
        assert len_nums > 0
        if len_nums == 1:
            return str(nums[0])
        if len_nums == 2:
            return str(nums[0]) + "/" + str(nums[1])

        # now len_nums >= 3, construct result: "A/(B/C/D/...)"
        res = str(nums[0]) + "/" + "("
        for num in nums[1: -1]:
            res += str(num) + "/"
        res += str(nums[-1]) + ")"
        return res


def main():
    # Example 1: Output: "1000/(100/10/2)"
    #     Explanation:
    #         1000/(100/10/2) = 1000/((100/10)/2) = 200
    #         However, the bold parenthesis in "1000/((100/10)/2)" are redundant,
    #             since they don't influence the operation priority. So you should return "1000/(100/10/2)".
    #         Other cases:
    #         1000/(100/10)/2 = 50
    #         1000/(100/(10/2)) = 50
    #         1000/100/10/2 = 0.5
    #         1000/100/(10/2) = 2
    # nums = [1000, 100, 10, 2]

    # Example 2: Output: "2/(3/4)"
    # nums = [2, 3, 4]

    # Example 3: Output: "2"
    nums = [2]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.optimalDivision(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
