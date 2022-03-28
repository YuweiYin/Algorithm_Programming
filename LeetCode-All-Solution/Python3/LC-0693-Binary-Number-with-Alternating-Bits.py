#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0693-Binary-Number-with-Alternating-Bits.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-28
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 0693 - (Easy) - Binary Number with Alternating Bits
https://leetcode.com/problems/binary-number-with-alternating-bits/

Description & Requirement:
    Given a positive integer, check whether it has alternating bits: 
    namely, if two adjacent bits will always have different values.

Example 1:
    Input: n = 5
    Output: true
    Explanation: The binary representation of 5 is: 101
Example 2:
    Input: n = 7
    Output: false
    Explanation: The binary representation of 7 is: 111.
Example 3:
    Input: n = 11
    Output: false
    Explanation: The binary representation of 11 is: 1011.

Constraints:
    1 <= n <= 2^31 - 1
"""


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # exception case
        assert isinstance(n, int) and n > 0
        # main method: (bitwise stimulate)
        return self._hasAlternatingBits(n)

    def _hasAlternatingBits(self, n: int) -> bool:
        """
        Runtime: 26 ms, faster than 95.22% of Python3 online submissions for Binary Number with Alternating Bits.
        Memory Usage: 13.9 MB, less than 13.66% of Python3 online submissions for Binary Number with Alternating Bits.
        """
        bi_n = bin(n)[2:]
        test_flag = True  # True, 1; False, 0
        for bit in bi_n:
            if test_flag:
                if bit != "1":
                    return False
            else:
                if bit != "0":
                    return False
            test_flag = not test_flag

        return True


def main():
    # Example 1: Output: true
    # n = 5

    # Example 2: Output: false
    # n = 7

    # Example 3: Output: false
    n = 11

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.hasAlternatingBits(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
