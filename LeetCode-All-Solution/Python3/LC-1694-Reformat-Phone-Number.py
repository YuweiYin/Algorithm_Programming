#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1694-Reformat-Phone-Number.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-10-01
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 1694 - (Easy) - Reformat Phone Number
https://leetcode.com/problems/reformat-phone-number/

Description & Requirement:
    You are given a phone number as a string number. number consists of digits, spaces ' ', and/or dashes '-'.

    You would like to reformat the phone number in a certain manner. Firstly, remove all spaces and dashes. 
    Then, group the digits from left to right into blocks of length 3 until there are 4 or fewer digits. 
    The final digits are then grouped as follows:
        2 digits: A single block of length 2.
        3 digits: A single block of length 3.
        4 digits: Two blocks of length 2 each.

    The blocks are then joined by dashes. Notice that the reformatting process should never produce any blocks 
    of length 1 and produce at most two blocks of length 2.

    Return the phone number after formatting.

Example 1:
    Input: number = "1-23-45 6"
    Output: "123-456"
    Explanation: The digits are "123456".
        Step 1: There are more than 4 digits, so group the next 3 digits. The 1st block is "123".
        Step 2: There are 3 digits remaining, so put them in a single block of length 3. The 2nd block is "456".
        Joining the blocks gives "123-456".
Example 2:
    Input: number = "123 4-567"
    Output: "123-45-67"
    Explanation: The digits are "1234567".
        Step 1: There are more than 4 digits, so group the next 3 digits. The 1st block is "123".
        Step 2: There are 4 digits left, so split them into two blocks of length 2. The blocks are "45" and "67".
        Joining the blocks gives "123-45-67".
Example 3:
    Input: number = "123 4-5678"
    Output: "123-456-78"
    Explanation: The digits are "12345678".
        Step 1: The 1st block is "123".
        Step 2: The 2nd block is "456".
        Step 3: There are 2 digits left, so put them in a single block of length 2. The 3rd block is "78".
        Joining the blocks gives "123-456-78".

Constraints:
    2 <= number.length <= 100
    number consists of digits and the characters '-' and ' '.
    There are at least two digits in number.
"""


class Solution:
    def reformatNumber(self, number: str) -> str:
        # exception case
        assert isinstance(number, str) and len(number) >= 2
        # main method: (extract all digits and reformat the list as the rule tells)
        return self._reformatNumber(number)

    def _reformatNumber(self, number: str) -> str:
        assert isinstance(number, str) and len(number) >= 2

        digit_list = []
        for ch in number:
            if ch.isdigit():
                digit_list.append(ch)

        n = len(digit_list)
        LEN = 3
        div, mod = divmod(n, LEN)

        res = ""
        if mod == 1:  # 1 + 3 == 2 + 2
            for idx in range(div - 1):
                res += "".join(digit_list[idx * LEN: (idx + 1) * LEN]) + "-"
            res += "".join(digit_list[-4: -2]) + "-" + "".join(digit_list[-2:])
        elif mod == 2:  # 2 == 2
            for idx in range(div):
                res += "".join(digit_list[idx * LEN: (idx + 1) * LEN]) + "-"
            res += "".join(digit_list[-2:])
        else:  # mod == 0
            for idx in range(div - 1):
                res += "".join(digit_list[idx * LEN: (idx + 1) * LEN]) + "-"
            res += "".join(digit_list[-3:])

        return res


def main():
    # Example 1: Output: "123-456"
    # number = "1-23-45 6"

    # Example 2: Output: "123-45-67"
    # number = "123 4-567"

    # Example 3: Output: "123-456-78"
    number = "123 4-5678"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.reformatNumber(number)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
