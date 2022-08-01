#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1374-Generate-a-String-With-Characters-That-Have-Odd-Counts.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-08-01
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 1374 - (Easy) - Generate a String With Characters That Have Odd Counts
https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/

Description & Requirement:
    Given an integer n, return a string with n characters such that 
    each character in such string occurs an odd number of times.

    The returned string must contain only lowercase English letters. 
    If there are multiples valid strings, return any of them.  

Example 1:
    Input: n = 4
    Output: "pppz"
    Explanation: "pppz" is a valid string since the character 'p' occurs three times and the character 'z' occurs once. Note that there are many other valid strings such as "ohhh" and "love".
Example 2:
    Input: n = 2
    Output: "xy"
    Explanation: "xy" is a valid string since the characters 'x' and 'y' occur once. Note that there are many other valid strings such as "ag" and "ur".
Example 3:
    Input: n = 7
    Output: "holasss"

Constraints:
    1 <= n <= 500
"""


class Solution:
    def generateTheString(self, n: int) -> str:
        # exception case
        assert isinstance(n, int) and n >= 1
        # main method: (easy generation)
        return self._generateTheString(n)

    def _generateTheString(self, n: int) -> str:
        assert isinstance(n, int) and n >= 1

        if n & 0x01 == 1:  # odd -> "a...a"
            return "".join(["a" for _ in range(n)])
        else:  # even -> "a...ab"
            return "".join(["a" for _ in range(n - 1)]) + "b"


def main():
    # Example 1:
    n = 10

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.generateTheString(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
