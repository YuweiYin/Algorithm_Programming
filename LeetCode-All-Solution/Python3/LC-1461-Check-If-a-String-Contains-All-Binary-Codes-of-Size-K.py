#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1461-Check-If-a-String-Contains-All-Binary-Codes-of-Size-K.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-05-31
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 1461 - (Medium) - Check If a String Contains All Binary Codes of Size K
https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/

Description & Requirement:
    Given a binary string s and an integer k, 
    return true if every binary code of length k is a substring of s. 
    Otherwise, return false.

Example 1:
    Input: s = "00110110", k = 2
    Output: true
    Explanation: The binary codes of length 2 are "00", "01", "10" and "11". 
        They can be all found as substrings at indices 0, 1, 3 and 2 respectively.
Example 2:
    Input: s = "0110", k = 1
    Output: true
    Explanation: The binary codes of length 1 are "0" and "1", it is clear that both exist as a substring. 
Example 3:
    Input: s = "0110", k = 2
    Output: false
    Explanation: The binary code "00" is of length 2 and does not exist in the array.

Constraints:
    1 <= s.length <= 5 * 10^5
    s[i] is either '0' or '1'.
    1 <= k <= 20
"""


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # exception case
        assert isinstance(s, str) and len(s) >= 1
        for ch in s:
            assert ch == "0" or ch == "1"
        assert isinstance(k, int) and k >= 1
        # main method: (sliding window. idea: if there are 2^k different substrings of s wrt. len(substring) <= k)
        return self._hasAllCodes(s, k)

    def _hasAllCodes(self, s: str, k: int) -> bool:
        assert isinstance(s, str) and len(s) >= 1
        assert isinstance(k, int) and k >= 1
        len_s = len(s)

        if len_s < (1 << k) + k - 1:
            return False

        num_set = set()
        cur_num = int(s[:k], base=2)
        num_set.add(cur_num)
        ord_0 = ord("0")
        target_counter = 1 << k

        for idx in range(1, len_s - k + 1):
            # remove s[idx - 1], append s[idx + k - 1]
            cur_num -= (ord(s[idx - 1]) - ord_0) << (k - 1)
            cur_num <<= 1
            cur_num += ord(s[idx + k - 1]) - ord_0
            num_set.add(cur_num)
            if len(num_set) == target_counter:
                return True

        return len(num_set) == target_counter


def main():
    # Example 1: Output: true
    # s = "00110110"
    # k = 2

    # Example 2: Output: true
    # s = "0110"
    # k = 1

    # Example 3: Output: false
    s = "0110"
    k = 2

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.hasAllCodes(s, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
