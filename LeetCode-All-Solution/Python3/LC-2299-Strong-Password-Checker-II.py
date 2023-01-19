#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2299-Strong-Password-Checker-II.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-01-19
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 2299 - (Easy) - Strong Password Checker II
https://leetcode.com/problems/strong-password-checker-ii/

Description & Requirement:
    A password is said to be strong if it satisfies all the following criteria:
        It has at least 8 characters.
        It contains at least one lowercase letter.
        It contains at least one uppercase letter.
        It contains at least one digit.
        It contains at least one special character. 
            The special characters are the characters in the following string: "!@#$%^&*()-+".
        It does not contain 2 of the same character in adjacent positions 
            (i.e., "aab" violates this condition, but "aba" does not).

    Given a string password, return true if it is a strong password. Otherwise, return false.

Example 1:
    Input: password = "IloveLe3tcode!"
    Output: true
    Explanation: The password meets all the requirements. Therefore, we return true.
Example 2:
    Input: password = "Me+You--IsMyDream"
    Output: false
    Explanation: The password does not contain a digit and also contains 2 of the same character in adjacent positions.
        Therefore, we return false.
Example 3:
    Input: password = "1aB!"
    Output: false
    Explanation: The password does not meet the length requirement. Therefore, we return false.

Constraints:
    1 <= password.length <= 100
    password consists of letters, digits, and special characters: "!@#$%^&*()-+".
"""


class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        # exception case
        assert isinstance(password, str) and len(password) >= 1
        # main method: (simulate the process)
        return self._strongPasswordCheckerII(password)

    def _strongPasswordCheckerII(self, password: str) -> bool:
        assert isinstance(password, str) and len(password) >= 1

        if len(password) < 8:
            return False

        specials = set("!@#$%^&*()-+")
        has_lower = has_upper = has_digit = has_special = False

        for idx, ch in enumerate(password):
            if idx != len(password) - 1 and password[idx] == password[idx + 1]:
                return False

            if ch.islower():
                has_lower = True
            elif ch.isupper():
                has_upper = True
            elif ch.isdigit():
                has_digit = True
            elif ch in specials:
                has_special = True

        return has_lower and has_upper and has_digit and has_special


def main():
    # Example 1: Output: true
    # password = "IloveLe3tcode!"

    # Example 2: Output: false
    password = "Me+You--IsMyDream"

    # Example 3: Output: false
    # password = "1aB!"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.strongPasswordCheckerII(password)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
