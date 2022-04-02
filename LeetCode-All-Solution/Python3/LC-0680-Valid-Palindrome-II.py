#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0680-Valid-Palindrome-II.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-02
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 0680 - (Easy) - Valid Palindrome II
https://leetcode.com/problems/valid-palindrome-ii/

Description & Requirement:
    A password is considered strong if the below conditions are all met:
        It has at least 6 characters and at most 20 characters.
        It contains at least one lowercase letter, at least one uppercase letter, and at least one digit.
        It does not contain three repeating characters in a row 
            (i.e., "...aaa..." is weak, but "...aa...a..." is strong, assuming other conditions are met).

    Given a string password, return the minimum number of steps required to make password strong. if password is already strong, return 0.

    In one step, you can:
        Insert one character to password,
        Delete one character from password, or
        Replace one character of password with another character.

Example 1:
    Input: password = "a"
    Output: 5
Example 2:
    Input: password = "aA1"
    Output: 3
Example 3:
    Input: password = "1337C0d3"
    Output: 0

Constraints:
    1 <= password.length <= 50
    password consists of letters, digits, dot '.' or exclamation mark '!'.
"""


class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        # exception case
        assert isinstance(password, str) and len(password) >= 1
        # main method: (3 types: len < 6, 6 <= len <= 20, and len > 20)
        return self._strongPasswordChecker(password)

    def _strongPasswordChecker(self, password: str) -> int:
        pass_len = len(password)

        # check the lower, upper, and digit conditions
        has_lower = 0
        has_upper = 0
        has_digit = 0
        for ch in password:
            if ch.islower():
                has_lower = 1
            elif ch.isupper():
                has_upper = 1
            elif ch.isdigit():
                has_digit = 1
            else:
                continue

        if 1 <= pass_len <= 5:  # only need to insert
            return max(6 - pass_len, 3 - has_lower - has_upper - has_digit)
        elif 6 <= pass_len <= 20:  # only need to replace
            replace_operation = 0
            consecutive_counter = 0
            last_ch = "*"  # "*" is not in the password
            for ch in password:
                if ch == last_ch:
                    consecutive_counter += 1
                else:
                    replace_operation += consecutive_counter // 3  # replace 1 char in 3 consecutive chars (if < 3, + 0)
                    consecutive_counter = 1
                    last_ch = ch
            replace_operation += consecutive_counter // 3
            # either do replace to avoid 3 more consecutive chars, or replace to add lower, upper, and digit chars
            return max(replace_operation, 3 - has_lower - has_upper - has_digit)
        elif 21 <= pass_len <= 50:  # TODO: need to delete and/or replace
            replace_operation = 0
            delete_operation = pass_len - 20
            consecutive_counter = 0
            rm2 = 0
            last_ch = "*"  # "*" is not in the password
            for ch in password:
                if ch == last_ch:
                    consecutive_counter += 1
                else:
                    if delete_operation > 0 and consecutive_counter >= 3:
                        if consecutive_counter % 3 == 0:
                            replace_operation -= 1
                            delete_operation -= 1
                        elif consecutive_counter % 3 == 1:
                            rm2 += 1
                        else:
                            pass
                    replace_operation += consecutive_counter // 3  # replace 1 char in 3 consecutive chars (if < 3, + 0)
                    consecutive_counter = 1
                    last_ch = ch

            if delete_operation > 0 and consecutive_counter >= 3:
                if consecutive_counter % 3 == 0:
                    replace_operation -= 1
                    delete_operation -= 1
                elif consecutive_counter % 3 == 1:
                    rm2 += 1
                else:
                    pass
            replace_operation += consecutive_counter // 3

            use2 = min(replace_operation, rm2, delete_operation >> 1)
            replace_operation -= use2
            delete_operation -= use2 << 1

            use3 = min(replace_operation, delete_operation // 3)
            replace_operation -= use3
            delete_operation -= use3 // 3

            return pass_len - 20 + max(replace_operation, 3 - has_lower - has_upper - has_digit)
        else:  # error
            return 0


def main():
    # Example 1: Output: 5
    password = "a"

    # Example 2: Output: 3
    # password = "aA1"

    # Example 3: Output: 0
    # password = "1337C0d3"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.strongPasswordChecker(password)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
