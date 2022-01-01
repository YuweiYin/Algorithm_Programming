#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/Study-Plan/Algorithm/Algorithm-1
@File    : LC-278-First-Bad-Version.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-01
=================================================================="""

import sys
import time
# from typing import List

"""
LeetCode - 278 - (Easy) - First Bad Version
https://leetcode.com/problems/first-bad-version/

Description:
    You are a product manager and currently leading a team to develop a new product. 
    Unfortunately, the latest version of your product fails the quality check. 
    Since each version is developed based on the previous version, 
    all the versions after a bad version are also bad.

    Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, 
    which causes all the following ones to be bad.

Requirement:
    You are given an API bool isBadVersion(version) which returns whether version is bad. 
    Implement a function to find the first bad version.
    You should minimize the number of calls to the API.

Example 1:
    Input: n = 5, bad = 4
    Output: 4
    Explanation:
    call isBadVersion(3) -> false
    call isBadVersion(5) -> true
    call isBadVersion(4) -> true
    Then 4 is the first bad version.
Example 2:
    Input: n = 1, bad = 1
    Output: 1

Constraints:
    1 <= bad <= n <= 2^31 - 1
"""


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def __init__(self, bad):
        self.bad = bad

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # exception case
        if not isinstance(n, int) or n <= 0:
            return 0
        # main method: (loop) binary search of a list that the left part is good and the right part is bad
        return self._firstBadVersion(n)

    def _firstBadVersion(self, n: int) -> int:
        start, end = 1, n
        min_bad = n + 1
        while start <= end:
            cur = (end + start) >> 1  # current cursor
            if self.isBadVersion(cur):  # 1. current bad: go left
                min_bad = min(min_bad, cur)  # record the bad one
                end = cur - 1
            else:  # 1. current good: go right
                start = cur + 1  # change interval
        return min_bad

    def isBadVersion(self, version):
        return version >= self.bad


def main():
    # Example 1:
    #     Input: n = 5, bad = 4
    #     Output: 4
    #     Explanation:
    #     call isBadVersion(3) -> false
    #     call isBadVersion(5) -> true
    #     call isBadVersion(4) -> true
    #     Then 4 is the first bad version.
    n = 5
    bad = 4

    # Example 2:
    #     Input: n = 1, bad = 1
    #     Output: 1
    # n = 1
    # bad = 1

    # init instance
    solution = Solution(bad)

    # run & time
    start = time.process_time()
    ans = solution.firstBadVersion(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
