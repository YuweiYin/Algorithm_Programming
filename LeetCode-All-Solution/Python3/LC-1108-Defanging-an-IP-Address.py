#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1108-Defanging-an-IP-Address.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-06-21
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 1108 - (Easy) - Defanging an IP Address
https://leetcode.com/problems/defanging-an-ip-address/

Description & Requirement:
    Given a valid (IPv4) IP address, return a defanged version of that IP address.

    A defanged IP address replaces every period "." with "[.]".

Example 1:
    Input: address = "1.1.1.1"
    Output: "1[.]1[.]1[.]1"
Example 2:
    Input: address = "255.100.50.0"
    Output: "255[.]100[.]50[.]0"

Constraints:
    The given address is a valid IPv4 address.
"""


class Solution:
    def defangIPaddr(self, address: str) -> str:
        # exception case
        assert isinstance(address, str) and len(address) >= 1
        # main method: (just replace all "." with "[.]")
        return self._defangIPaddr(address)

    def _defangIPaddr(self, address: str) -> str:
        assert isinstance(address, str) and len(address) >= 1

        return address.replace(".", "[.]")


def main():
    # Example 1: Output: "1[.]1[.]1[.]1"
    # address = "1.1.1.1"

    # Example 2: Output: "255[.]100[.]50[.]0"
    address = "255.100.50.0"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.defangIPaddr(address)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
