#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1207-Unique-Number-of-Occurrences.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-11-30
=================================================================="""

import sys
import time
from typing import List
# import itertools

"""
LeetCode - 1207 - (Easy) - Unique Number of Occurrences
https://leetcode.com/problems/unique-number-of-occurrences/

Description & Requirement:
    Given an array of integers arr, 
    return true if the number of occurrences of each value in the array is unique, or false otherwise.

Example 1:
    Input: arr = [1,2,2,1,1,3]
    Output: true
    Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:
    Input: arr = [1,2]
    Output: false
Example 3:
    Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
    Output: true

Constraints:
    1 <= arr.length <= 1000
    -1000 <= arr[i] <= 1000
"""


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # exception case
        assert isinstance(arr, list) and len(arr) >= 1
        # main method: (use hash dict to count occurrences)
        return self._uniqueOccurrences(arr)

    def _uniqueOccurrences(self, arr: List[int]) -> bool:
        assert isinstance(arr, list) and len(arr) >= 1

        counter = dict({})
        for num in arr:
            if num not in counter:
                counter[num] = 1
            else:
                counter[num] += 1

        occurrences = list(counter.values())
        occur_set = set()
        for occur in occurrences:
            if occur not in occur_set:
                occur_set.add(occur)
            else:
                return False

        return True


def main():
    # Example 1: Output: true
    arr = [1, 2, 2, 1, 1, 3]

    # Example 2: Output: false
    # arr = [1, 2]

    # Example 3: Output: true
    # arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.uniqueOccurrences(arr)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
