#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1630-Arithmetic-Subarrays.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-03-23
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1630 - (Medium) - Arithmetic Subarrays
https://leetcode.com/problems/arithmetic-subarrays/

Description & Requirement:
    A sequence of numbers is called arithmetic if it consists of at least two elements, 
    and the difference between every two consecutive elements is the same. More formally, 
    a sequence s is arithmetic if and only if s[i+1] - s[i] == s[1] - s[0] for all valid i.

    For example, these are arithmetic sequences:
        1, 3, 5, 7, 9
        7, 7, 7, 7
        3, -1, -5, -9

    The following sequence is not arithmetic:
        1, 1, 2, 5, 7

    You are given an array of n integers, nums, and two arrays of m integers each, l and r, 
    representing the m range queries, where the ith query is the range [l[i], r[i]]. 
    All the arrays are 0-indexed.

    Return a list of boolean elements answer, where answer[i] is true if the subarray 
    nums[l[i]], nums[l[i]+1], ... , nums[r[i]] can be rearranged to form 
    an arithmetic sequence, and false otherwise.

Example 1:
    Input: nums = [4,6,5,9,3,7], l = [0,0,2], r = [2,3,5]
    Output: [true,false,true]
    Explanation:
        In the 0th query, the subarray is [4,6,5]. 
            This can be rearranged as [6,5,4], which is an arithmetic sequence.
        In the 1st query, the subarray is [4,6,5,9]. 
            This cannot be rearranged as an arithmetic sequence.
        In the 2nd query, the subarray is [5,9,3,7]. 
            This can be rearranged as [3,5,7,9], which is an arithmetic sequence.
Example 2:
    Input: nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], l = [0,1,6,4,8,7], r = [4,4,9,7,9,10]
    Output: [false,true,false,false,true,true]

Constraints:
    n == nums.length
    m == l.length
    m == r.length
    2 <= n <= 500
    1 <= m <= 500
    0 <= l[i] < r[i] < n
    -10^5 <= nums[i] <= 10^5
"""


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 2
        assert isinstance(l, list) and isinstance(r, list) and len(l) == len(r) >= 1
        # main method: (enumerate)
        return self._checkArithmeticSubarrays(nums, l, r)

    def _checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        assert isinstance(nums, list) and len(nums) >= 2
        assert isinstance(l, list) and isinstance(r, list) and len(l) == len(r) >= 1

        res = []
        for left, right in zip(l, r):
            min_v = min(nums[left: right + 1])
            max_v = max(nums[left: right + 1])

            if min_v == max_v:
                res.append(True)
                continue

            if (max_v - min_v) % (right - left) != 0:
                res.append(False)
                continue

            diff = (max_v - min_v) // (right - left)
            flag = True
            seen = set()
            for j in range(left, right + 1):
                if (nums[j] - min_v) % diff != 0:
                    flag = False
                    break
                t = (nums[j] - min_v) // diff
                if t in seen:
                    flag = False
                    break
                seen.add(t)
            res.append(flag)

        return res


def main():
    # Example 1: Output: [true,false,true]
    # nums = [4, 6, 5, 9, 3, 7]
    # l = [0, 0, 2]
    # r = [2, 3, 5]

    # Example 2: Output: [false,true,false,false,true,true]
    nums = [-12, -9, -3, -12, -6, 15, 20, -25, -20, -15, -10]
    l = [0, 1, 6, 4, 8, 7]
    r = [4, 4, 9, 7, 9, 10]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.checkArithmeticSubarrays(nums, l, r)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
