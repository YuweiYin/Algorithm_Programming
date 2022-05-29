#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0468-Validate-IP-Address.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-05-29
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 0468 - (Medium) - Validate IP Address
https://leetcode.com/problems/validate-ip-address/

Description & Requirement:
    Given a string queryIP, return "IPv4" if IP is a valid IPv4 address, 
    "IPv6" if IP is a valid IPv6 address or 
    "Neither" if IP is not a correct IP of any type.

    A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 
        0 <= xi <= 255 and xi cannot contain leading zeros. 

    For example, "192.168.1.1" and "192.168.1.0" are valid IPv4 addresses 
    while "192.168.01.1", "192.168.1.00", and "192.168@1.1" are invalid IPv4 addresses.

    A valid IPv6 address is an IP in the form "x1:x2:x3:x4:x5:x6:x7:x8" where:
        1 <= xi.length <= 4
        xi is a hexadecimal string which may contain digits, lowercase English letter ('a' to 'f') and 
            upper-case English letters ('A' to 'F').
        Leading zeros are allowed in xi.

    For example, "2001:0db8:85a3:0000:0000:8a2e:0370:7334" and 
    "2001:db8:85a3:0:0:8A2E:0370:7334" are valid IPv6 addresses, while "2001:0db8:85a3::8A2E:037j:7334" and 
    "02001:0db8:85a3:0000:0000:8a2e:0370:7334" are invalid IPv6 addresses.

Example 1:
    Input: queryIP = "172.16.254.1"
    Output: "IPv4"
    Explanation: This is a valid IPv4 address, return "IPv4".
Example 2:
    Input: queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
    Output: "IPv6"
    Explanation: This is a valid IPv6 address, return "IPv6".
Example 3:
    Input: queryIP = "256.256.256.256"
    Output: "Neither"
    Explanation: This is neither a IPv4 address nor a IPv6 address.

Constraints:
    queryIP consists only of English letters, digits and the characters '.' and ':'.
"""


class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        # exception case
        assert isinstance(queryIP, str)
        # main method: (just follow the rules)
        return self._validIPAddress(queryIP)

    def _validIPAddress(self, queryIP: str) -> str:
        assert isinstance(queryIP, str)

        valid_ipv6_ch = set()
        ord_0 = ord("0")
        for digit in range(10):
            valid_ipv6_ch.add(chr(ord_0 + digit))
        ord_a = ord("a")
        for digit in range(6):
            valid_ipv6_ch.add(chr(ord_a + digit))
        ord_A = ord("A")
        for digit in range(6):
            valid_ipv6_ch.add(chr(ord_A + digit))

        first_five = queryIP[:5]
        if "." in first_five:  # check IPv4
            ip_list = queryIP.split(".")
            if len(ip_list) != 4:
                return "Neither"
            for _ip in ip_list:
                if _ip == "0":
                    continue
                if not (1 <= len(_ip) <= 3 and _ip[0] != "0" and _ip.isdigit() and 0 <= int(_ip) <= 255):
                    return "Neither"
            return "IPv4"
        elif ":" in first_five:  # check IPv6
            ip_list = queryIP.split(":")
            if len(ip_list) != 8:
                return "Neither"
            for _ip in ip_list:
                if not 1 <= len(_ip) <= 4:
                    return "Neither"
                for ch in _ip:
                    if ch not in valid_ipv6_ch:
                        return "Neither"
            return "IPv6"
        else:
            return "Neither"


def main():
    # Example 1: Output: "IPv4"
    # queryIP = "172.16.254.1"

    # Example 2: Output: "IPv6"
    queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"

    # Example 3: Output: "Neither"
    # queryIP = "256.256.256.256"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.validIPAddress(queryIP)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
