#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0306-Additive-Number.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-10
=================================================================="""

import sys
import time
from typing import List

"""
LeetCode - 0306 - (Medium) - Additive Number
https://leetcode.com/problems/additive-number/

Description:
    An additive number is a string whose digits can form an additive sequence.
    
    A valid additive sequence should contain at least three numbers. 
    Except for the first two numbers, each subsequent number in the sequence 
    must be the sum of the preceding two.

Requirement:
    Given a string containing only digits, return true if it is an additive number or false otherwise.
    
    Note: Numbers in the additive sequence cannot have leading zeros, 
    so sequence 1, 2, 03 or 1, 02, 3 is invalid.

Example 1:
    Input: "112358"
    Output: true
    Explanation: 
        The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
        1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
Example 2:
    Input: "199100199"
    Output: true
    Explanation: 
        The additive sequence is: 1, 99, 100, 199. 
        1 + 99 = 100, 99 + 100 = 199

Constraints:
    1 <= num.length <= 35
    num consists only of digits.
"""


class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        # exception case
        if not isinstance(num, str) or len(num) <= 2:
            return False
        if len(num) == 3 and num[0] == "0":
            return True if num[1] == num[2] else False
        # main method: (reverse list in place)
        return self._isAdditiveNumber(num)

    def _isAdditiveNumber(self, num: str) -> bool:
        """
        Runtime: 24 ms, faster than 97.13% of Python3 online submissions for Additive Number.
        Memory Usage: 14.1 MB, less than 85.34% of Python3 online submissions for Additive Number.
        """
        # assert isinstance(num, str) and len(num) >= 3 and num[0] != "0"
        assert isinstance(num, str) and len(num) >= 3
        len_num = len(num)
        max_first_end = len_num >> 1  # the length of first number can't be equal to or longer than (len_num // 2)

        def __valid_additive_sequence(f_end: int, s_end: int):
            # Numbers in the additive sequence cannot have leading zeros (but a can be "0", so can b)
            if f_end > 0 and num[0] == "0":
                return False
            if s_end <= f_end or (s_end > (f_end + 1) and num[f_end + 1] == "0"):
                return False
            first_num = int(num[0: f_end + 1])  # convert first number to int
            second_num = int(num[f_end + 1: s_end + 1])  # convert second number to int
            cur_sum_index = s_end + 1  # record sum_position
            while cur_sum_index <= len_num:
                cur_sum_num = first_num + second_num  # do sum
                cur_sum_str = str(cur_sum_num)  # convert to str
                if cur_sum_str == num[s_end + 1: s_end + 1 + len(cur_sum_str)]:
                    first_num = second_num
                    second_num = cur_sum_num
                    s_end += len(cur_sum_str)
                    cur_sum_index += len(cur_sum_str)
                    if cur_sum_index == len_num:  # exactly matched all num[0: len_num]
                        return True
                    else:
                        continue
                else:
                    return False
            return False

        first_end = 0
        while first_end < max_first_end:
            # if num[first_end + 1] == "0":
            #     first_end += 1
            #     continue
            # the length of second number can't be longer than (len_num // 2)
            max_second_end = first_end + ((len_num - first_end - 1) >> 1)
            second_end = first_end + 1
            while second_end <= max_second_end:
                if __valid_additive_sequence(first_end, second_end):
                    return True
                second_end += 1
            first_end += 1

        return False


def main():
    # Example 1: Output: true
    num = "112358"

    # Example 2: Output: true
    # num = "199100199"

    # Example 3: Output: true
    # num = "101"

    # Example 4: Output: true
    # num = "000"

    # Example 5: Output: true
    # num = "211738"

    # Example 6: Output: false
    # num = "0235813"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.isAdditiveNumber(num)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
