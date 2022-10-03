#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1784-Check-if-Binary-String-Has-at-Most-One-Segment-of-Ones.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-10-03
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 1784 - (Easy) - Check if Binary String Has at Most One Segment of Ones
https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/

Description & Requirement:
    Given a binary string s without leading zeros, 
    return true if s contains at most one contiguous segment of ones. 
    Otherwise, return false.

Example 1:
    Input: s = "1001"
    Output: false
    Explanation: The ones do not form a contiguous segment.
Example 2:
    Input: s = "110"
    Output: true

Constraints:
    1 <= s.length <= 100
    s[i] is either '0' or '1'.
    s[0] is '1'.
"""


class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        # exception case
        assert isinstance(s, str) and len(s) >= 1
        # main method: (just scan the string)
        return self._checkOnesSegment(s)

    def _checkOnesSegment(self, s: str) -> bool:
        assert isinstance(s, str) and len(s) >= 1

        cnt = 0
        n = len(s)
        idx = 0
        while idx < n:
            if s[idx] == "1":
                cnt += 1
                idx += 1
                while idx < n and s[idx] == "1":
                    idx += 1
            idx += 1

        return cnt <= 1


def main():
    # Example 1: Output: false
    s = "1001"

    # Example 2: Output: true
    # s = "110"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.checkOnesSegment(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
