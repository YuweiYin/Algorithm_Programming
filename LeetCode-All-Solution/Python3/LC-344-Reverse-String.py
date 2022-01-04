#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-344-Reverse-String.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-04
=================================================================="""

import sys
import time
from typing import List

"""
LeetCode - 344 - (Easy) - Reverse String
https://leetcode.com/problems/reverse-string/

Description:
    Write a function that reverses a string. 
    The input string is given as an array of characters s.

Requirement:
    You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
    Input: s = ["h","e","l","l","o"]
    Output: ["o","l","l","e","h"]
Example 2:
    Input: s = ["H","a","n","n","a","h"]
    Output: ["h","a","n","n","a","H"]

Constraints:
    1 <= s.length <= 10^5
    s[i] is a printable ascii character.
"""


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # exception case
        if not isinstance(s, list) or len(s) <= 1:
            return
        # main method: (reverse list in place)
        self._reverseString(s)

    def _reverseString(self, s: List[str]) -> None:
        self._reverse_list_in_place(s, 0, len(s) - 1)

    @staticmethod
    def _reverse_list_in_place(nums: List, start_index: int, end_index: int) -> None:
        while start_index < end_index:
            temp_num = nums[start_index]
            nums[start_index] = nums[end_index]
            nums[end_index] = temp_num
            start_index += 1
            end_index -= 1


def main():
    # Example 1: Output: ["o","l","l","e","h"]
    s = ["h", "e", "l", "l", "o"]

    # Example 2: Output: ["h","a","n","n","a","H"]
    # s = ["H", "a", "n", "n", "a", "h"]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    solution.reverseString(s)
    ans = s
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
