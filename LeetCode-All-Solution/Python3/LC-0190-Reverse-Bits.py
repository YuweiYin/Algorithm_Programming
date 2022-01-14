#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0190-Reverse-Bits.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-14
=================================================================="""

import sys
import time
# from typing import List

"""
LeetCode - 0190 - (Easy) - Reverse Bits
https://leetcode.com/problems/reverse-bits/

Description & Requirement:
    Reverse bits of a given 32 bits unsigned integer.

    Note:
        Note that in some languages, such as Java, there is no unsigned integer type. 
        In this case, both input and output will be given as a signed integer type. 
        They should not affect your implementation, 
        as the integer's internal binary representation is the same, 
        whether it is signed or unsigned.

        In Java, the compiler represents the signed integers using 2's complement notation. 
        Therefore, in Example 2 above, the input represents the signed integer -3 and 
        the output represents the signed integer -1073741825.

Example 1:
    Input: n = 00000010100101000001111010011100
    Output:    964176192 (00111001011110000010100101000000)
    Explanation: 
        The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, 
        so return 964176192 which its binary representation is 00111001011110000010100101000000.
Example 2:
    Input: n = 11111111111111111111111111111101
    Output:   3221225471 (10111111111111111111111111111111)
    Explanation: The input binary string 11111111111111111111111111111101 represents 
        the unsigned integer 4294967293, so return 3221225471 which 
        its binary representation is 10111111111111111111111111111111.

Constraints:
    The input must be a binary string of length 32

Follow up:
    If this function is called many times, how would you optimize it?
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        """
        Runtime: 16 ms, faster than 99.95% of Python3 online submissions for Reverse Bits.
        Memory Usage: 14.2 MB, less than 69.42% of Python3 online submissions for Reverse Bits.
        """
        # exception case
        if not isinstance(n, int) or n <= 0:
            return 0  # Error input type
        # main method: (Bit Manipulation)
        # return self._reverseBits(n)
        return self._reverseBitsFast(n)

    def _reverseBits(self, n: int) -> int:
        """
        consider each bit
        """
        res = 0  # 0b000...000
        MAX_BIT = 32
        for cur_bit in range(MAX_BIT):
            # put each cur_bit '1' to res's (MAX_BIT - cur_bit)
            if n & 0x01 == 1:
                res |= (1 << (MAX_BIT - 1 - cur_bit))
            n >>= 1
        return res

    def _reverseBitsFast(self, n: int) -> int:
        """
        Faster: Divide and Conquer:
            Step 1: 2 bits as one group, swap them.
            Step 2: 4 bits (2 * 2 bits) as a group, swap them.
            Step 3: 8 bits (2 * 4 bits) as a group, swap them.
            Step 4: 16 bits (2 * 8 bits) as a group, swap them.
            Step 5: 32 bits (2 * 16 bits) as a group, swap them. bingo!
            "swap" by shift bits and logical bit-and with masks
        """
        MASK_BIT2 = 0b01010101010101010101010101010101
        MASK_BIT4 = 0b00110011001100110011001100110011
        MASK_BIT8 = 0b00001111000011110000111100001111
        MASK_BIT16 = 0b00000000111111110000000011111111
        MASK_BIT32 = 0b00000000000000001111111111111111

        # Step 1: for each 2 bits group, ((n >> 1) & MASK_BIT2) moves the left bit in each group to the right position
        #    ((n & MASK_BIT2) << 1) moves the right bit in each group to the left position. Then logical bit-or. Done
        n = ((n >> 1) & MASK_BIT2) | ((n & MASK_BIT2) << 1)

        # Step 2: for each 4 bits group, ((n >> 2) & MASK_BIT4) moves the left 2 bits in each group to the right 2 pos
        #    ((n & MASK_BIT4) << 2) moves the right 2 bits in each group to the left 2 pos. Then logical bit-or. Done
        n = ((n >> 2) & MASK_BIT4) | ((n & MASK_BIT4) << 2)

        # Step 3: for each 8 bits group, ((n >> 4) & MASK_BIT8) moves the left 4 bits in each group to the right 4 pos
        #    ((n & MASK_BIT8) << 4) moves the right 4 bits in each group to the left 4 pos. Then logical bit-or. Done
        n = ((n >> 4) & MASK_BIT8) | ((n & MASK_BIT8) << 4)

        # Step 4: for each 16 bits group, ((n >> 8) & MASK_BIT16) moves the left 8 bits in each group to the right 8 pos
        #    ((n & MASK_BIT16) << 8) moves the right 8 bits in each group to the left 8 pos. Then logical bit-or. Done
        n = ((n >> 8) & MASK_BIT16) | ((n & MASK_BIT16) << 8)

        # Step 5: for the whole 32 bits, ((n >> 16) & MASK_BIT32) moves the left 16 bits in each group -> right 16 pos
        #     ((n & MASK_BIT32) << 16) moves the right 16 bits in each group -> left 16 pos. Then logical bit-or. Done
        return ((n >> 16) & MASK_BIT32) | ((n & MASK_BIT32) << 16)


def main():
    # Example 1: Output:    964176192 (00111001011110000010100101000000)
    n = 0b00000010100101000001111010011100

    # Example 2: Output:   3221225471 (10111111111111111111111111111111)
    # n = 0b11111111111111111111111111111101

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.reverseBits(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
