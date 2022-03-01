#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0006-Zigzag-Conversion.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-01
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 0006 - (Medium) - Zigzag Conversion
https://leetcode.com/problems/zigzag-conversion/

Description & Requirement:
    The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
    (you may want to display this pattern in a fixed font for better legibility)
        P   A   H   N
        A P L S I I G
        Y   I   R
    And then read line by line: "PAHNAPLSIIGYIR"

    Write the code that will take a string and make this conversion given a number of rows:
        string convert(string s, int numRows);

Example 1:
    Input: s = "PAYPALISHIRING", numRows = 3
    Output: "PAHNAPLSIIGYIR"
Example 2:
    Input: s = "PAYPALISHIRING", numRows = 4
    Output: "PINALSIGYAHRPI"
    Explanation:
        P     I    N
        A   L S  I G
        Y A   H R
        P     I
Example 3:
    Input: s = "A", numRows = 1
    Output: "A"

Constraints:
    1 <= s.length <= 1000
    s consists of English letters (lower-case and upper-case), ',' and '.'.
    1 <= numRows <= 1000
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # exception case
        assert isinstance(s, str) and len(s) > 0
        assert isinstance(numRows, int) and numRows > 0
        if len(s) <= numRows or numRows == 1:  # only zig, no zag
            return s
        if numRows == 2:
            even_idx_chars = [s[idx] for idx in range(0, len(s), 2)]
            odd_idx_chars = [s[idx] for idx in range(1, len(s), 2)]
            return "".join(even_idx_chars + odd_idx_chars)
        # main method: (simulate the zigzag process)
        #     create a matrix: for each row, the length == numRows
        #     repeat: col_idx from 0 to numRows-1, then row_idx += 1; col_idx from numRows-2 to 1, then row_idx += 1
        return self._convert(s, numRows)  # Time: O(n); Space: O(n)

    def _convert(self, s: str, numRows: int) -> str:
        len_s = len(s)

        zigzag_matrix = [["" for _ in range(numRows)]]
        zigzag_tag = True  # True: col_idx from 0 to numRows-1; False: col_idx from numRows-2 to 1
        row_idx = 0
        col_idx = 0
        ch_idx = 0
        while ch_idx < len_s:
            zigzag_matrix[row_idx][col_idx] = s[ch_idx]
            if zigzag_tag:  # col_idx from 0 to numRows-1
                col_idx += 1
                if col_idx == numRows:  # reach the rightmost index, change direction
                    zigzag_matrix.append(["" for _ in range(numRows)])  # new row
                    zigzag_tag = False  # change direction
                    row_idx += 1  # new row idx
                    col_idx = numRows - 2  # new col idx
            else:  # col_idx from numRows-2 to 1
                col_idx -= 1
                if col_idx == 0:  # reach the leftmost index, change direction
                    zigzag_matrix.append(["" for _ in range(numRows)])  # new row
                    zigzag_tag = True  # change direction
                    row_idx += 1  # new row idx
            ch_idx += 1  # char keep moving nonstop

        res = []
        max_row = len(zigzag_matrix)
        for col in range(numRows):  # col-wise extract chars in zigzag_matrix
            res += [zigzag_matrix[row][col] for row in range(max_row)]

        return "".join(res)


def main():
    # Example 1: Output: "PAHNAPLSIIGYIR"
    # s = "PAYPALISHIRING"
    # numRows = 3

    # Example 2: Output: "PINALSIGYAHRPI"
    s = "PAYPALISHIRING"
    numRows = 4

    # Example 3: Output: "A"
    # s = "A"
    # numRows = 1

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.convert(s, numRows)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
