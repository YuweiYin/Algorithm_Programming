#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1338-Reduce-Array-Size-to-The-Half.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-08-18
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1338 - (Medium) - Reduce Array Size to The Half
https://leetcode.com/problems/reduce-array-size-to-the-half/

Description & Requirement:
    You are given an integer array arr. You can choose a set of integers and 
    remove all the occurrences of these integers in the array.

    Return the minimum size of the set so that at least half of the integers of the array are removed.

Example 1:
    Input: arr = [3,3,3,3,5,5,5,2,2,7]
    Output: 2
    Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] 
        which has size 5 (i.e equal to half of the size of the old array).
        Possible sets of size 2 are {3,5},{3,2},{5,2}.
        Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] 
        which has a size greater than half of the size of the old array.
Example 2:
    Input: arr = [7,7,7,7,7,7]
    Output: 1
    Explanation: The only possible set you can choose is {7}. This will make the new array empty.

Constraints:
    2 <= arr.length <= 10^5
    arr.length is even.
    1 <= arr[i] <= 10^5
"""


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        # exception case
        assert isinstance(arr, list) and len(arr) >= 2
        # main method: (hash dict counter)
        return self._minSetSize(arr)

    def _minSetSize(self, arr: List[int]) -> int:
        """
        Runtime: 676 ms, faster than 84.75% of Python3 online submissions for Reduce Array Size to The Half.
        Memory Usage: 37.9 MB, less than 22.62% of Python3 online submissions for Reduce Array Size to The Half.
        """
        assert isinstance(arr, list) and len(arr) >= 2
        len_arr = len(arr)

        counter = dict({})
        for num in arr:
            if num not in counter:
                counter[num] = 1
            else:
                counter[num] += 1

        k_v_list = []
        for k, v in counter.items():
            k_v_list.append([k, v])

        k_v_list.sort(key=lambda x: x[1], reverse=True)
        res = 0
        start, target = len_arr, len_arr >> 1
        for k, v in k_v_list:
            res += 1
            start -= v
            if start <= target:
                break

        return res


def main():
    # Example 1: Output: 2
    # arr = [3, 3, 3, 3, 5, 5, 5, 2, 2, 7]

    # Example 2: Output: 1
    arr = [7, 7, 7, 7, 7, 7]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minSetSize(arr)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
