#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0923-3Sum-With-Multiplicity.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-06
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0923 - (Medium) - 3Sum With Multiplicity
https://leetcode.com/problems/3sum-with-multiplicity/

Description & Requirement:
    Given an integer array arr, and an integer target, return the number of tuples i, j, k 
    such that i < j < k and arr[i] + arr[j] + arr[k] == target.

    As the answer can be very large, return it modulo 10^9 + 7.

Example 1:
    Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8
    Output: 20
    Explanation: 
        Enumerating by the values (arr[i], arr[j], arr[k]):
        (1, 2, 5) occurs 8 times;
        (1, 3, 4) occurs 8 times;
        (2, 2, 4) occurs 2 times;
        (2, 3, 3) occurs 2 times.
Example 2:
    Input: arr = [1,1,2,2,2,2], target = 5
    Output: 12
    Explanation: 
        arr[i] = 1, arr[j] = arr[k] = 2 occurs 12 times:
        We choose one 1 from [1,1] in 2 ways,
        and two 2s from [2,2,2,2] in 6 ways.

Constraints:
    3 <= arr.length <= 3000
    0 <= arr[i] <= 100
    0 <= target <= 300
"""


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        # exception case
        assert isinstance(arr, list) and len(arr) >= 3
        assert isinstance(target, int) and target >= 0
        # main method: (sort, two pointers - 2 sum. note: deal with the duplication)
        return self._threeSumMulti(arr, target)

    def _threeSumMulti(self, arr: List[int], target: int) -> int:
        len_arr = len(arr)
        assert len_arr >= 3

        MOD = int(1e9+7)
        res = 0

        arr.sort()
        for i, num in enumerate(arr):
            two_sum_target = target - num
            j, k = i + 1, len_arr - 1  # two pointers find two sum target

            while j < k:
                if arr[j] + arr[k] < two_sum_target:
                    j += 1  # need to be larger
                elif arr[j] + arr[k] > two_sum_target:
                    k -= 1  # need to be smaller
                else:  # now, arr[j] + arr[k] == two_sum_target
                    if arr[j] != arr[k]:  # find all duplicate arr[j] and arr[k]
                        j_counter = 1
                        k_counter = 1
                        while j + 1 < k and arr[j] == arr[j + 1]:
                            j_counter += 1
                            j += 1
                        while k - 1 > j and arr[k] == arr[k - 1]:
                            k_counter += 1
                            k -= 1
                        res += int(j_counter * k_counter) % MOD
                        # prepare for the next loop
                        j += 1
                        k -= 1
                    else:  # arr[j] == arr[k] == two_sum_target / 2
                        interval_len = k - j + 1
                        res += (int(interval_len * (interval_len - 1)) % MOD) >> 1
                        res %= MOD
                        break

        return res


def main():
    # Example 1: Output: 20
    # arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
    # target = 8

    # Example 2: Output: 12
    arr = [1, 1, 2, 2, 2, 2]
    target = 5

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.threeSumMulti(arr, target)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
