#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0954-Array-of-Doubled-Pairs.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-01
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0954 - (Medium) - Array of Doubled Pairs
https://leetcode.com/problems/array-of-doubled-pairs/

Description & Requirement:
    Given an integer array of even length arr, 
    return true if it is possible to reorder arr 
    such that arr[2 * i + 1] = 2 * arr[2 * i] for every 0 <= i < len(arr) / 2, or false otherwise.

Example 1:
    Input: arr = [3,1,3,6]
    Output: false
Example 2:
    Input: arr = [2,1,2,6]
    Output: false
Example 3:
    Input: arr = [4,-2,2,-4]
    Output: true
    Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].

Constraints:
    2 <= arr.length <= 3 * 10^4
    arr.length is even.
    -10^5 <= arr[i] <= 10^5
"""


class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        # exception case
        assert isinstance(arr, list) and len(arr) >= 2 and len(arr) & 0x01 == 0
        # main method: (hash dict record counter, and then sort by keys, greedily match every valid pair)
        return self._canReorderDoubled(arr)

    def _canReorderDoubled(self, arr: List[int]) -> bool:
        """
        Runtime: 672 ms, faster than 87.34% of Python3 online submissions for Array of Doubled Pairs.
        Memory Usage: 16.7 MB, less than 39.35% of Python3 online submissions for Array of Doubled Pairs.
        """
        hash_dict = ({})
        for num in arr:
            if num not in hash_dict:
                hash_dict[num] = 1
            else:
                hash_dict[num] += 1

        sort_keys = list(hash_dict.keys())
        sort_keys.sort()  # ascending order
        for num in sort_keys:
            if hash_dict[num] == 0:
                continue
            # first, pair with smaller numbers
            half_num = num / 2
            if half_num in hash_dict:
                while hash_dict[num] > 0 and hash_dict[half_num] > 0:
                    hash_dict[half_num] -= 1
                    hash_dict[num] -= 1
            # then, pair with larger numbers
            double_num = num * 2
            if double_num in hash_dict:
                while hash_dict[num] > 0 and hash_dict[double_num] > 0:
                    hash_dict[double_num] -= 1
                    hash_dict[num] -= 1
            # if any number remains unpaired, return False
            if hash_dict[num] > 0:
                return False

        return True


def main():
    # Example 1: Output: false
    # arr = [3, 1, 3, 6]

    # Example 2: Output: false
    # arr = [2, 1, 2, 6]

    # Example 3: Output: true
    # arr = [4, -2, 2, -4]

    arr = [0, 4, 0, 2, -6, -4, 8, -3, 0, 0, 2, -6, -3, -6, -2, -3, 1, 4]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.canReorderDoubled(arr)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
