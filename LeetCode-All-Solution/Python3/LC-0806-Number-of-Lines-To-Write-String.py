#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0806-Number-of-Lines-To-Write-String.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-12
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0806 - (Easy) - Number of Lines To Write String
https://leetcode.com/problems/number-of-lines-to-write-string/

Description & Requirement:
    You are given a string s of lowercase English letters and an array widths denoting how many pixels wide each 
    lowercase English letter is. Specifically, widths[0] is the width of 'a', widths[1] is the width of 'b', and so on.

    You are trying to write s across several lines, where each line is no longer than 100 pixels. 
    Starting at the beginning of s, write as many letters on the first line such that 
    the total width does not exceed 100 pixels. Then, from where you stopped in s, 
    continue writing as many letters as you can on the second line. 
    Continue this process until you have written all of s.

    Return an array result of length 2 where:
        result[0] is the total number of lines.
        result[1] is the width of the last line in pixels.

Example 1:
    Input: widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], s = "abcdefghijklmnopqrstuvwxyz"
    Output: [3,60]
    Explanation: You can write s as follows:
        abcdefghij  // 100 pixels wide
        klmnopqrst  // 100 pixels wide
        uvwxyz      // 60 pixels wide
        There are a total of 3 lines, and the last line is 60 pixels wide.
Example 2:
    Input: widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], s = "bbbcccdddaaa"
    Output: [2,4]
    Explanation: You can write s as follows:
        bbbcccdddaa  // 98 pixels wide
        a            // 4 pixels wide
        There are a total of 2 lines, and the last line is 4 pixels wide.

Constraints:
    widths.length == 26
    2 <= widths[i] <= 10
    1 <= s.length <= 1000
    s contains only lowercase English letters.
"""


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        # exception case
        assert isinstance(widths, list) and len(widths) == 26
        assert isinstance(s, str) and len(s) >= 1
        # main method: (simulate the process)
        return self._numberOfLines(widths, s)

    def _numberOfLines(self, widths: List[int], s: str) -> List[int]:
        assert isinstance(widths, list) and len(widths) == 26
        assert isinstance(s, str) and len(s) >= 1

        res = [1, 0]  # start from the first line, index=0 place
        LIMIT = 100

        ord_a = ord("a")
        cur_len = 0
        for ch in s:
            ch_len = widths[ord(ch) - ord_a]
            if cur_len + ch_len <= LIMIT:
                cur_len += ch_len
            else:  # next line
                cur_len = ch_len
                res[0] += 1
            res[1] = cur_len

        return res


def main():
    # Example 1: Output: [3,60]
    # widths = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    # s = "abcdefghijklmnopqrstuvwxyz"

    # Example 2: Output: [2,4]
    widths = [4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    s = "bbbcccdddaaa"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.numberOfLines(widths, s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
