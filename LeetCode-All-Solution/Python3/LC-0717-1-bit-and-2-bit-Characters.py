#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0717-1-bit-and-2-bit-Characters.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-20
=================================================================="""

import sys
import time
from typing import List
# import collections

"""
LeetCode - 0717 - (Easy) - 1-bit and 2-bit Characters
https://leetcode.com/problems/1-bit-and-2-bit-characters/

Description & Requirement:
    We have two special characters:
        The first character can be represented by one bit 0.
        The second character can be represented by two bits (10 or 11).

    Given a binary array bits that ends with 0, 
    return true if the last character must be a one-bit character.

Example 1:
    Input: bits = [1,0,0]
    Output: true
    Explanation: The only way to decode it is two-bit character and one-bit character.
        So the last character is one-bit character.
Example 2:
    Input: bits = [1,1,1,0]
    Output: false
    Explanation: The only way to decode it is two-bit character and two-bit character.
        So the last character is not one-bit character.

Constraints:
    1 <= bits.length <= 1000
    bits[i] is either 0 or 1.
"""


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        # exception case
        assert isinstance(bits, list) and len(bits) >= 1
        for bit in bits:
            assert bit == 0 or bit == 1
        # main method: (simulate the decoding process)
        return self._isOneBitCharacter(bits)

    def _isOneBitCharacter(self, bits: List[int]) -> bool:
        len_bits = len(bits)
        assert len_bits >= 1

        cursor = 0
        while cursor < len_bits:
            if bits[cursor] == 0:
                if cursor == len_bits - 1:
                    return True
                else:
                    # decode "0"
                    cursor += 1
            elif bits[cursor] == 1:
                if cursor == len_bits - 1:
                    return False
                else:
                    # decode "10" or "11"
                    cursor += 2
            else:
                cursor += 1  # error bit

        return False


def main():
    # Example 1: Output: true
    # bits = [1, 0, 0]

    # Example 2: Output: false
    bits = [1, 1, 1, 0]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.isOneBitCharacter(bits)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
