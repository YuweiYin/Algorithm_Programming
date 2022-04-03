#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0009-Palindrome-Number.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-03
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 0009 - (Easy) - Palindrome Number
https://leetcode.com/problems/palindrome-number/

Description & Requirement:
    Given an integer x, return true if x is palindrome integer.

    An integer is a palindrome when it reads the same backward as forward.

    For example, 121 is a palindrome while 123 is not.

Example 1:
    Input: x = 121
    Output: true
    Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:
    Input: x = -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left, it becomes 121-. 
        Therefore it is not a palindrome.
Example 3:
    Input: x = 10
    Output: false
    Explanation: Reads 01 from right to left. 
        Therefore it is not a palindrome.

Constraints:
    -2^31 <= x <= 2^31 - 1

Follow up:
    Could you solve it without converting the integer to a string?
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # exception case
        assert isinstance(x, int)
        # main method: (convert x to str, then use left/right two pointers)
        return self._isPalindrome(x)

    def _isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        if x < 0:
            return False

        x_str = str(x)
        left, right = 0, len(x_str) - 1
        while left < right:
            if x_str[left] == x_str[right]:
                left += 1
                right -= 1
            else:
                return False
        return True


def main():
    # Example 1: Output: true
    x = 121

    # Example 2: Output: false
    # x = -121

    # Example 3: Output: false
    # x = 10

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.isPalindrome(x)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
