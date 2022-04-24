#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0868-Binary-Gap.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-24
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 0868 - (Easy) - Binary Gap
https://leetcode.com/problems/binary-gap/

Description & Requirement:
    Given a positive integer n, find and return the longest distance between any two adjacent 1's 
    in the binary representation of n. If there are no two adjacent 1's, return 0.

    Two 1's are adjacent if there are only 0's separating them (possibly no 0's). 
    The distance between two 1's is the absolute difference between their bit positions. 
    For example, the two 1's in "1001" have a distance of 3.

Example 1:
    Input: n = 22
    Output: 2
    Explanation: 22 in binary is "10110".
        The first adjacent pair of 1's is "10110" with a distance of 2.
        The second adjacent pair of 1's is "10110" with a distance of 1.
        The answer is the largest of these two distances, which is 2.
        Note that "10110" is not a valid pair since there is a 1 separating the two 1's underlined.
Example 2:
    Input: n = 8
    Output: 0
    Explanation: 8 in binary is "1000".
        There are not any adjacent pairs of 1's in the binary representation of 8, so we return 0.
Example 3:
    Input: n = 5
    Output: 2
    Explanation: 5 in binary is "101".

Constraints:
    1 <= n <= 10^9
"""


class Solution:
    def binaryGap(self, n: int) -> int:
        # exception case
        assert isinstance(n, int) and n >= 1
        # main method: (convert integer n into string, then scan it)
        return self._binaryGap(n)

    def _binaryGap(self, n: int) -> int:
        """
        Runtime: 40 ms, faster than 60.13% of Python3 online submissions for Binary Gap.
        Memory Usage: 13.8 MB, less than 96.88% of Python3 online submissions for Binary Gap.
        """
        assert isinstance(n, int) and n >= 1
        res = 0

        n_str = bin(n)[2:]
        last_1 = -1
        for idx, bit in enumerate(n_str):
            if bit == "1":
                if last_1 != -1:
                    res = max(res, idx - last_1)
                last_1 = idx

        return res


def main():
    # Example 1: Output: 2
    n = 22

    # Example 2: Output: 0
    # n = 8

    # Example 3: Output: 2
    # n = 5

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.binaryGap(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
