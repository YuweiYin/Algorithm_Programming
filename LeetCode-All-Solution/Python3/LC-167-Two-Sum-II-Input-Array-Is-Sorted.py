#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/Study-Plan/Algorithm/Algorithm-1
@File    : LC-167-Two-Sum-II-Input-Array-Is-Sorted.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-03
=================================================================="""

import sys
import time
from typing import List

"""
LeetCode - 167 - (Easy) - Two Sum II - Input Array Is Sorted
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Description:
    Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
    find two numbers such that they add up to a specific target number. 
    Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

    Return the indices of the two numbers, index1 and index2, added by one 
    as an integer array [index1, index2] of length 2.

Requirement:
    The tests are generated such that there is exactly one solution. 
    You may not use the same element twice.

Example 1:
    Input: numbers = [2,7,11,15], target = 9
    Output: [1,2]
    Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:
    Input: numbers = [2,3,4], target = 6
    Output: [1,3]
    Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:
    Input: numbers = [-1,0], target = -1
    Output: [1,2]
    Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

Constraints:
    2 <= numbers.length <= 3 * 10^4
    -1000 <= numbers[i] <= 1000
    numbers is sorted in non-decreasing order.
    -1000 <= target <= 1000
    The tests are generated such that there is exactly one solution.
"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # exception case
        if not isinstance(numbers, list) or len(numbers) <= 0:
            return []
        if len(numbers) == 1:
            if numbers[0] == target:
                return [1]
            else:
                return []
        if len(numbers) == 2:
            if (numbers[0] + numbers[1]) == target:
                return [1, 2]
            else:
                return []
        # main method: (hash dict)
        return self._twoSum(numbers, target)

    def _twoSum(self, numbers: List[int], target: int) -> List[int]:
        len_num = len(numbers)
        diff_dict = dict({target - numbers[0]: 0})  # key: target - numbers[index]; value: index
        cur_index = 1
        while cur_index < len_num:
            cur_num = numbers[cur_index]
            if cur_num in diff_dict:
                # Requirement: Return the indices of the two numbers, index1 and index2, added by one
                return [diff_dict[cur_num] + 1, cur_index + 1]
            else:
                diff_dict[target - cur_num] = cur_index
            cur_index += 1
        return []


def main():
    # Example 1: Output: [1,2]
    #     Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
    numbers = [2, 7, 11, 15]
    target = 9

    # Example 2: Output: [1,3]
    #     Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
    # numbers = [2, 3, 4]
    # target = 6

    # Example 3: Output: [1,2]
    #     Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
    # numbers = [-1, 0]
    # target = -1

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.twoSum(numbers, target)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
