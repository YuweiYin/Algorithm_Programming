#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0008-String-to-Integer-atoi.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-14
=================================================================="""

import sys
import time
# from typing import List

"""
LeetCode - 0008 - (Medium) - String to Integer (atoi)
https://leetcode.com/problems/string-to-integer-atoi/

Description & Requirement:
    Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer 
    (similar to C/C++'s atoi function).

    The algorithm for myAtoi(string s) is as follows:

    Read in and ignore any leading whitespace.
    Check if the next character (if not already at the end of the string) is '-' or '+'. 
    Read this character in if it is either. 
    This determines if the final result is negative or positive respectively. 
    Assume the result is positive if neither is present.
    Read in next the characters until the next non-digit character or the end of the input is reached. 
    The rest of the string is ignored.

    Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, 
    then the integer is 0. Change the sign as necessary (from step 2).
    If the integer is out of the 32-bit signed integer range [-2^31, 2^31 - 1], 
    then clamp the integer so that it remains in the range. Specifically, 
    integers less than -2^31 should be clamped to -2^31, and integers greater than 
    2^31 - 1 should be clamped to 2^31 - 1.

    Return the integer as the final result.

Note:
    Only the space character ' ' is considered a whitespace character.
    Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.

Example 1:
    Input: s = "42"
    Output: 42
    Explanation: The underlined characters are what is read in, the caret is the current reader position.
        Step 1: "42" (no characters read because there is no leading whitespace)
                 ^
        Step 2: "42" (no characters read because there is neither a '-' nor '+')
                 ^
        Step 3: "42" ("42" is read in)
                   ^
        The parsed integer is 42.
        Since 42 is in the range [-231, 231 - 1], the final result is 42.
Example 2:
    Input: s = "   -42"
    Output: -42
    Explanation:
        Step 1: "   -42" (leading whitespace is read and ignored)
                    ^
        Step 2: "   -42" ('-' is read, so the result should be negative)
                     ^
        Step 3: "   -42" ("42" is read in)
                       ^
        The parsed integer is -42.
        Since -42 is in the range [-231, 231 - 1], the final result is -42.
Example 3:
    Input: s = "4193 with words"
    Output: 4193
    Explanation:
        Step 1: "4193 with words" (no characters read because there is no leading whitespace)
                 ^
        Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')
                 ^
        Step 3: "4193 with words" ("4193" is read in; reading stops because the next character is a non-digit)
                     ^
        The parsed integer is 4193.
        Since 4193 is in the range [-231, 231 - 1], the final result is 4193.

Constraints:
    0 <= s.length <= 200
    s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.
"""


class Solution:
    def myAtoi(self, s: str) -> int:
        # exception case
        if not isinstance(s, str) or len(s) <= 0:
            return 0  # Error input type
        # main method: (scan string to find a valid number)
        #     other: regular expression: int(*re.findall('^[\+\-]?\d+', s.strip()))
        return self._myAtoi(s)

    def _myAtoi(self, s: str) -> int:
        """
        Runtime: 32 ms, faster than 86.58% of Python3 online submissions for String to Integer (atoi).
        Memory Usage: 14.3 MB, less than 24.99% of Python3 online submissions for String to Integer (atoi).
        """
        s = s.strip()
        len_s = len(s)
        if len_s <= 0:
            return 0

        res_str = ''
        if s[0] == '+':
            sign = True  # True: +, False: -
            cur_char_index = 1  # start from s[1]
        elif s[0] == '-':
            sign = False  # True: +, False: -
            cur_char_index = 1  # start from s[1]
        elif not s[0].isdigit():
            return 0  # not a number
        else:  # digit
            sign = True  # default +
            cur_char_index = 0  # start from s[0]

        while cur_char_index < len_s:
            cur_char = s[cur_char_index]
            if cur_char.isdigit():
                res_str += cur_char
            else:  # not digit
                break
            cur_char_index += 1

        if len(res_str) <= 0 or not res_str.isdigit():
            return 0

        raw_res = int(res_str) if sign else (- int(res_str))
        MAX_INT32 = (1 << 31) - 1
        MIN_INT32 = - (1 << 31)
        return min(max(raw_res, MIN_INT32), MAX_INT32)


def main():
    # Example 1: Output: 42
    # s = "42"

    # Example 2: Output: -42
    # s = "   -42"

    # Example 3: Output: 4193
    # s = "4193 with words"

    # Example 4: -2147483648
    s = "-91283472332"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.myAtoi(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
