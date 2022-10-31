#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0481-Magical-String.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-10-31
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 0481 - (Medium) - Magical String
https://leetcode.com/problems/magical-string/

Description & Requirement:
    A magical string s consists of only '1' and '2' and obeys the following rules:
        The string s is magical because concatenating the number of contiguous occurrences of characters '1' and '2' 
            generates the string s itself.
        The first few elements of s is s = "1221121221221121122……". If we group the consecutive 1's and 2's in s, 
            it will be "1 22 11 2 1 22 1 22 11 2 11 22 ......" and the occurrences of 1's or 2's in each group 
            are "1 2 2 1 1 2 1 2 2 1 2 2 ......". You can see that the occurrence sequence is s itself.

    Given an integer n, return the number of 1's in the first n number in the magical string s.

Example 1:
    Input: n = 6
    Output: 3
    Explanation: The first 6 elements of magical string s is "122112" and it contains three 1's, so return 3.
Example 2:
    Input: n = 1
    Output: 1

Constraints:
    1 <= n <= 10^5
"""


class Solution:
    def magicalString(self, n: int) -> int:
        # exception case
        assert isinstance(n, int) and n >= 1
        # main method: (construct the string s)
        return self._magicalString(n)

    def _magicalString(self, n: int) -> int:
        assert isinstance(n, int) and n >= 1

        if n < 4:
            return 1
        s = ["" for _ in range(n)]
        s[:3] = "122"

        res = 1
        i, j = 2, 3
        while j < n:
            size = int(s[i])
            num = 3 - int(s[j - 1])
            while size and j < n:
                s[j] = str(num)
                if num == 1:
                    res += 1
                j += 1
                size -= 1
            i += 1

        return res


def main():
    # Example 1: Output: 3
    n = 6

    # Example 2: Output: 1
    # n = 1

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.magicalString(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
