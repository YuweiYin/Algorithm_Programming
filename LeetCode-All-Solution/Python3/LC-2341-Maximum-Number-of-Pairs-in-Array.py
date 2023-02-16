#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2341-Maximum-Number-of-Pairs-in-Array.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-02-16
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 2341 - (Easy) - Maximum Number of Pairs in Array
https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

Description & Requirement:
    You are given a 0-indexed integer array nums. In one operation, you may do the following:
        Choose two integers in nums that are equal.
        Remove both integers from nums, forming a pair.

    The operation is done on nums as many times as possible.

    Return a 0-indexed integer array answer of size 2 where answer[0] is the number of pairs 
    that are formed and answer[1] is the number of leftover integers in nums after 
    doing the operation as many times as possible.

Example 1:
    Input: nums = [1,3,2,1,3,2,2]
    Output: [3,1]
    Explanation:
        Form a pair with nums[0] and nums[3] and remove them from nums. Now, nums = [3,2,3,2,2].
        Form a pair with nums[0] and nums[2] and remove them from nums. Now, nums = [2,2,2].
        Form a pair with nums[0] and nums[1] and remove them from nums. Now, nums = [2].
        No more pairs can be formed. A total of 3 pairs have been formed, 
            and there is 1 number leftover in nums.
Example 2:
    Input: nums = [1,1]
    Output: [1,0]
    Explanation: Form a pair with nums[0] and nums[1] and remove them from nums. Now, nums = [].
        No more pairs can be formed. A total of 1 pair has been formed, 
        and there are 0 numbers leftover in nums.
Example 3:
    Input: nums = [0]
    Output: [0,1]
    Explanation: No pairs can be formed, and there is 1 number leftover in nums.

Constraints:
    1 <= nums.length <= 100
    0 <= nums[i] <= 100
"""


class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        # main method: (hash counter)
        return self._numberOfPairs(nums)

    def _numberOfPairs(self, nums: List[int]) -> List[int]:
        assert isinstance(nums, list) and len(nums) >= 1

        res = 0
        cnt = collections.defaultdict(bool)

        for num in nums:
            cnt[num] = not cnt[num]
            if not cnt[num]:
                res += 1

        return [res, len(nums) - (res << 1)]


def main():
    # Example 1: Output: [3,1]
    nums = [1, 3, 2, 1, 3, 2, 2]

    # Example 2: Output: [1,0]
    # nums = [1, 1]

    # Example 3: Output: [0,1]
    # nums = [0]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.numberOfPairs(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
