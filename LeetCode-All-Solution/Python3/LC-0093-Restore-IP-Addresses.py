#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0093-Restore-IP-Addresses.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-01-21
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0093 - (Medium) - Restore IP Addresses
https://leetcode.com/problems/restore-ip-addresses/

Description & Requirement:
    A valid IP address consists of exactly four integers separated by single dots. 
    Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

        For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, 
        but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.

    Given a string s containing only digits, return all possible valid IP addresses that 
    can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. 
    You may return the valid IP addresses in any order.

Example 1:
    Input: s = "25525511135"
    Output: ["255.255.11.135","255.255.111.35"]
Example 2:
    Input: s = "0000"
    Output: ["0.0.0.0"]
Example 3:
    Input: s = "101023"
    Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

Constraints:
    1 <= s.length <= 20
    s consists of digits only.
"""


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # exception case
        assert isinstance(s, str) and len(s) >= 1 and s.isdigit()
        # main method: (DFS backtrace)
        return self._restoreIpAddresses(s)

    def _restoreIpAddresses(self, s: str) -> List[str]:
        assert isinstance(s, str) and len(s) >= 1 and s.isdigit()

        IP_SEGMENT = 4  # IPv4

        res = []
        segments = [0] * IP_SEGMENT

        def __dfs(seg_id: int, seg_start: int):
            if seg_id == IP_SEGMENT:
                if seg_start == len(s):
                    ipAddr = ".".join(str(seg) for seg in segments)
                    res.append(ipAddr)
                return

            if seg_start == len(s):
                return

            if s[seg_start] == "0":
                segments[seg_id] = 0
                __dfs(seg_id + 1, seg_start + 1)

            addr = 0
            for segEnd in range(seg_start, len(s)):
                addr = addr * 10 + (ord(s[segEnd]) - ord("0"))
                if 0 < addr <= 0xFF:
                    segments[seg_id] = addr
                    __dfs(seg_id + 1, segEnd + 1)
                else:
                    break

        __dfs(0, 0)
        return res


def main():
    # Example 1: Output: ["255.255.11.135","255.255.111.35"]
    # s = "25525511135"

    # Example 2: Output: ["0.0.0.0"]
    # s = "0000"

    # Example 3: Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
    s = "101023"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.restoreIpAddresses(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
