#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0969-Pancake-Sorting.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-19
=================================================================="""

import sys
import time
from typing import List
# import collections

"""
LeetCode - 0969 - (Medium) - Pancake Sorting
https://leetcode.com/problems/pancake-sorting/

Description & Requirement:
    Given an array of integers arr, sort the array by performing a series of pancake flips.

    In one pancake flip we do the following steps:
        Choose an integer k where 1 <= k <= arr.length  (1-indexed).
        Reverse the sub-array arr[0...k-1]  (0-indexed).

    For example, if arr = [3,2,1,4] and we performed a pancake flip choosing k = 3, 
    we reverse the sub-array [3,2,1], so arr = [1,2,3,4] after the pancake flip at k = 3.

    Return an array of the k-values corresponding to a sequence of pancake flips that sort arr. 
    Any valid answer that sorts the array within 10 * arr.length flips will be judged as correct.

Example 1:
    Input: arr = [3,2,4,1]
    Output: [4,2,4,3]
    Explanation: 
        We perform 4 pancake flips, with k values 4, 2, 4, and 3.
        Starting state: arr = [3, 2, 4, 1]
        After 1st flip (k = 4): arr = [1, 4, 2, 3]
        After 2nd flip (k = 2): arr = [4, 1, 2, 3]
        After 3rd flip (k = 4): arr = [3, 2, 1, 4]
        After 4th flip (k = 3): arr = [1, 2, 3, 4], which is sorted.
Example 2:
    Input: arr = [1,2,3]
    Output: []
    Explanation: The input is already sorted, so there is no need to flip anything.
        Note that other answers, such as [3, 3], would also be accepted.

Constraints:
    1 <= arr.length <= 100
    1 <= arr[i] <= arr.length
    All integers in arr are unique (i.e. arr is a permutation of the integers from 1 to arr.length).
"""


class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        # exception case
        if not isinstance(arr, list) or len(arr) <= 0:
            return []  # Error input type
        if len(arr) == 1:
            return []
        if len(arr) == 2:
            return [] if arr[0] <= arr[1] else [2]
        # main method: (simulation)
        #     each step, find the max number of the left unsorted part, flip it into the leftmost pos
        #     then flip it into the rightmost pos, then deal with the rest unsorted part
        # e.g., arr = [3, 2, 4, 1]
        #     step 1: find max of [3, 2, 4, 1] is 4, and 4 is not on the rightmost pos,
        #             so flip [3, 2, 4] get arr = [4, 2, 3, 1], then flip [4, 2, 3, 1] get arr = [1, 3, 2, 4]
        #             now 4 is on the right position
        #     step 2: find max of [1, 3, 2] is 3, and 3 is not on the rightmost pos,
        #             so flip [1, 3] get arr = [3, 1, 2, 4], then flip [3, 1, 2] get arr = [2, 1, 3, 4],
        #             now 3 and 4 are both on the right position
        #     step 3: find max of [2, 1] is 2, and 2 is not on the rightmost pos,
        #             since 2 is already on the leftmost pos, just flip [2, 1] get arr = [1, 2, 3, 4], bingo!
        return self._pancakeSort(arr)

    def _pancakeSort(self, arr: List[int]) -> List[int]:
        len_arr = len(arr)
        assert len_arr >= 3

        aim_arr = sorted(arr)

        def __reverse_subarray(left_idx: int, right_idx: int):
            while left_idx < right_idx:
                arr[left_idx], arr[right_idx] = arr[right_idx], arr[left_idx]
                left_idx += 1
                right_idx -= 1

        flip_idx = []
        for rightmost_idx in reversed(range(1, len_arr)):
            if arr[rightmost_idx] == aim_arr[rightmost_idx]:
                continue  # the current max number is on the right position
            cur_max_num = arr[0]
            cur_max_idx = 0
            # find max
            for cur_idx in range(1, rightmost_idx):
                if arr[cur_idx] > cur_max_num:
                    cur_max_num = arr[cur_idx]
                    cur_max_idx = cur_idx

            # if cur_max_num is on the rightmost position, skip flipping
            if cur_max_idx == rightmost_idx:
                continue

            # else, if cur_max_num is not on the leftmost position (idx==0), flip it
            if cur_max_idx != 0:
                flip_idx.append(cur_max_idx + 1)
                __reverse_subarray(0, cur_max_idx)

            # now flip cur_max_num to the rightmost position
            flip_idx.append(rightmost_idx + 1)
            __reverse_subarray(0, rightmost_idx)

        return flip_idx


def main():
    # Example 1: Output: [4,2,4,3]
    arr = [3, 2, 4, 1]
    # Example 2: Output: []
    # arr = [1, 2, 3]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.pancakeSort(arr)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
