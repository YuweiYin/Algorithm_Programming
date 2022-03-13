#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0393-UTF-8-Validation.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-13
=================================================================="""

import sys
import time
from typing import List

# import functools

"""
LeetCode - 0393 - (Medium) - UTF-8 Validation
https://leetcode.com/problems/utf-8-validation/

Description & Requirement:
    Given an integer array data representing the data, 
    return whether it is a valid UTF-8 encoding.

    A character in UTF8 can be from 1 to 4 bytes long, subjected to the following rules:
        For a 1-byte character, the first bit is a 0, followed by its Unicode code.
        For an n-bytes character, the first n bits are all one's, the n + 1 bit is 0, 
            followed by n - 1 bytes with the most significant 2 bits being 10.

    This is how the UTF-8 encoding would work:
       Char. number range  |        UTF-8 octet sequence
          (hexadecimal)    |              (binary)
       --------------------+---------------------------------------------
       0000 0000-0000 007F | 0xxxxxxx
       0000 0080-0000 07FF | 110xxxxx 10xxxxxx
       0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
       0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

    Note: The input is an array of integers. Only the least significant 8 bits of each integer 
    is used to store the data. This means each integer represents only 1 byte of data.

Example 1:
    Input: data = [197,130,1]
    Output: true
    Explanation: data represents the octet sequence: 11000101 10000010 00000001.
        It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte character.
Example 2:
    Input: data = [235,140,4]
    Output: false
    Explanation: data represented the octet sequence: 11101011 10001100 00000100.
        The first 3 bits are all one's and the 4th bit is 0 means it is a 3-bytes character.
        The next byte is a continuation byte which starts with 10 and that's correct.
        But the second continuation byte does not start with 10, so it is invalid.

Constraints:
    1 <= data.length <= 2 * 10^4
    0 <= data[i] <= 255
"""


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        # exception case
        assert isinstance(data, list) and len(data) > 0
        for datum in data:
            assert isinstance(datum, int) and 0 <= datum <= 255
        # main method: (convert every datum to its binary string representation, scan each one)
        return self._validUtf8(data)

    def _validUtf8(self, data: List[int]) -> bool:
        len_data = len(data)
        assert len_data > 0

        data_bin = [bin(datum)[2:] for datum in data]
        index = 0
        while index < len_data:
            cur_datum = data_bin[index]
            if len(cur_datum) < 8:  # one byte
                index += 1
                continue
            else:  # 0 <= datum <= 255, len(cur_datum) must be 8
                if cur_datum[0: 3] == "110":  # two bytes
                    if index + 1 < len_data and \
                            len(data_bin[index + 1]) == 8 and data_bin[index + 1][0: 2] == "10":
                        index += 2
                        continue
                    return False
                elif cur_datum[0: 4] == "1110":  # three bytes
                    if index + 2 < len_data and \
                            len(data_bin[index + 1]) == 8 and data_bin[index + 1][0: 2] == "10" and \
                            len(data_bin[index + 2]) == 8 and data_bin[index + 2][0: 2] == "10":
                        index += 3
                        continue
                    return False
                elif cur_datum[0: 5] == "11110":  # four bytes
                    if index + 3 < len_data and \
                            len(data_bin[index + 1]) == 8 and data_bin[index + 1][0: 2] == "10" and \
                            len(data_bin[index + 2]) == 8 and data_bin[index + 2][0: 2] == "10" and \
                            len(data_bin[index + 3]) == 8 and data_bin[index + 3][0: 2] == "10":
                        index += 4
                        continue
                    return False
                else:  # not valid
                    return False

        return True


def main():
    # Example 1: Output: true
    # data = [197, 130, 1]

    # Example 2: Output: false
    data = [235, 140, 4]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.validUtf8(data)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
