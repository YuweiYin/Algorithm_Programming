#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0315-Count-of-Smaller-Numbers-After-Self.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-07-23
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0315 - (Hard) - Count of Smaller Numbers After Self
https://leetcode.com/problems/count-of-smaller-numbers-after-self/

Description & Requirement:
    You are given an integer array nums and you have to return a new counts array.
    The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example 1:
    Input: nums = [5,2,6,1]
    Output: [2,1,1,0]
    Explanation:
        To the right of 5 there are 2 smaller elements (2 and 1).
        To the right of 2 there is only 1 smaller element (1).
        To the right of 6 there is 1 smaller element (1).
        To the right of 1 there is 0 smaller element.
Example 2:
    Input: nums = [-1]
    Output: [0]
Example 3:
    Input: nums = [-1,-1]
    Output: [0,0]

Constraints:
    1 <= nums.length <= 10^5
    -10^4 <= nums[i] <= 10^4
"""


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        # main method: (1. tree array & maintain prefix sum; 2. merge sort)
        return self._countSmaller(nums)

    def _countSmaller(self, nums: List[int]) -> List[int]:
        assert isinstance(nums, list) and len(nums) >= 1
        len_nums = len(nums)

        array = nums[:]
        res = [0 for _ in range(len_nums)]
        index = list(range(len_nums))
        temp = [0 for _ in range(len_nums)]
        temp_idx = [0 for _ in range(len_nums)]

        def __merge_sort(_l: int, _r: int):
            if _l < _r:
                mid = (_l + _r) >> 1
                __merge_sort(_l, mid)
                __merge_sort(mid + 1, _r)
                __merge(_l, mid, _r)

        def __merge(_l: int, mid: int, _r: int):
            i, j, t = _l, mid + 1, _l
            while i <= mid and j <= _r:
                if array[i] <= array[j]:
                    temp[t] = array[i]
                    temp_idx[t] = index[i]
                    res[index[i]] += j - mid - 1
                    i += 1
                else:
                    temp[t] = array[j]
                    temp_idx[t] = index[j]
                    j += 1
                t += 1

            while i <= mid:
                temp[t] = array[i]
                temp_idx[t] = index[i]
                res[index[i]] += j - mid - 1
                i += 1
                t += 1
            while j <= _r:
                temp[t] = array[j]
                temp_idx[t] = index[j]
                j += 1
                t += 1

            for k in range(_l, _r + 1):
                index[k] = temp_idx[k]
                array[k] = temp[k]

        __merge_sort(0, len_nums - 1)
        return res


def main():
    # Example 1: Output: [2,1,1,0]
    # nums = [5, 2, 6, 1]

    # Example 2: Output: [0]
    # nums = [-1]

    # Example 3: Output: [0,0]
    # nums = [-1, -1]

    nums = [26, 78, 27, 100, 33, 67, 90, 23, 66, 5, 38, 7, 35, 23, 52, 22, 83, 51, 98, 69, 81, 32, 78, 28, 94, 13, 2,
            97, 3, 76, 99, 51, 9, 21, 84, 66, 65, 36, 100, 41]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.countSmaller(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
