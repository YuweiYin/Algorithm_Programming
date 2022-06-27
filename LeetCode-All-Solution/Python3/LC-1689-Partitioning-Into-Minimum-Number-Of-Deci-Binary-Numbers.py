#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1689-Partitioning-Into-Minimum-Number-Of-Deci-Binary-Numbers.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-06-27
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 1689 - (Medium) - Partitioning Into Minimum Number Of Deci-Binary Numbers
https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/

Description & Requirement:
    A decimal number is called deci-binary if each of its digits is either 0 or 1 without any leading zeros. 
    For example, 101 and 1100 are deci-binary, while 112 and 3001 are not.

    Given a string n that represents a positive decimal integer, 
    return the minimum number of positive deci-binary numbers needed so that they sum up to n.

Example 1:
    Input: n = "32"
    Output: 3
    Explanation: 10 + 11 + 11 = 32
Example 2:
    Input: n = "82734"
    Output: 8
Example 3:
    Input: n = "27346209830709182346"
    Output: 9

Constraints:
    1 <= n.length <= 10^5
    n consists of only digits.
    n does not contain any leading zeros and represents a positive integer.
"""


class Solution:
    def minPartitions(self, n: str) -> int:
        # exception case
        assert isinstance(n, str) and len(n) >= 1
        # main method: (just return the largest digit in n)
        return self._minPartitions(n)

    def _minPartitions(self, n: str) -> int:
        assert isinstance(n, str) and len(n) >= 1

        return int(max(n))


def main():
    # Example 1: Output: 3
    # n = "32"

    # Example 2: Output: 8
    # n = "82734"

    # Example 3: Output: 9
    n = "27346209830709182346"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minPartitions(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
