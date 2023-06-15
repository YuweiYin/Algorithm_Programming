#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1375-Number-of-Times-Binary-String-Is-Prefix-Aligned.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-06-14
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1375 - (Medium) - Number of Times Binary String Is Prefix-Aligned
https://leetcode.com/problems/number-of-times-binary-string-is-prefix-aligned/

Description & Requirement:
    You have a 1-indexed binary string of length n where all the bits are 0 initially. 
    We will flip all the bits of this binary string (i.e., change them from 0 to 1) one by one. 
    You are given a 1-indexed integer array flips where flips[i] indicates that 
    the bit at index i will be flipped in the ith step.

    A binary string is prefix-aligned if, after the ith step, 
    all the bits in the inclusive range [1, i] are ones and all the other bits are zeros.

    Return the number of times the binary string is prefix-aligned during the flipping process.

Example 1:
    Input: flips = [3,2,4,1,5]
    Output: 2
    Explanation: The binary string is initially "00000".
        After applying step 1: The string becomes "00100", which is not prefix-aligned.
        After applying step 2: The string becomes "01100", which is not prefix-aligned.
        After applying step 3: The string becomes "01110", which is not prefix-aligned.
        After applying step 4: The string becomes "11110", which is prefix-aligned.
        After applying step 5: The string becomes "11111", which is prefix-aligned.
        We can see that the string was prefix-aligned 2 times, so we return 2.
Example 2:
    Input: flips = [4,1,2,3]
    Output: 1
    Explanation: The binary string is initially "0000".
        After applying step 1: The string becomes "0001", which is not prefix-aligned.
        After applying step 2: The string becomes "1001", which is not prefix-aligned.
        After applying step 3: The string becomes "1101", which is not prefix-aligned.
        After applying step 4: The string becomes "1111", which is prefix-aligned.
        We can see that the string was prefix-aligned 1 time, so we return 1.

Constraints:
    n == flips.length
    1 <= n <= 5 * 10^4
    flips is a permutation of the integers in the range [1, n].
"""


class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        # exception case
        assert isinstance(flips, list) and len(flips) >= 1
        # main method: (scan the array)
        return self._numTimesAllBlue(flips)

    def _numTimesAllBlue(self, flips: List[int]) -> int:
        assert isinstance(flips, list) and len(flips) >= 1

        res = right = 0
        for idx, flip in enumerate(flips):
            right = max(right, flip)
            if right == idx + 1:
                res += 1

        return res


def main():
    # Example 1: Output: 2
    flips = [3, 2, 4, 1, 5]

    # Example 2: Output: 1
    # flips = [4, 1, 2, 3]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.numTimesAllBlue(flips)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
