#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1016-Binary-String-With-Substrings-Representing-1-To-N.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-05-11
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 1016 - (Medium) - Binary String With Substrings Representing 1 To N
https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/

Description & Requirement:
    Given a binary string s and a positive integer n, 
    return true if the binary representation of all the integers in the range [1, n] 
    are substrings of s, or false otherwise.

    A substring is a contiguous sequence of characters within a string.

Example 1:
    Input: s = "0110", n = 3
    Output: true
Example 2:
    Input: s = "0110", n = 4
    Output: false

Constraints:
    1 <= s.length <= 1000
    s[i] is either '0' or '1'.
    1 <= n <= 10^9
"""


class Solution:
    def queryString(self, s: str, n: int) -> bool:
        # exception case
        assert isinstance(s, str) and len(s) >= 1
        assert isinstance(n, int) and n >= 1
        # main method: (sliding window + hashing set)
        return self._queryString(s, n)

    def _queryString(self, s: str, n: int) -> bool:
        assert isinstance(s, str) and len(s) >= 1
        assert isinstance(n, int) and n >= 1

        def __check(s, k, mi, ma):
            st = set()
            t = 0
            for r in range(len(s)):
                t = t * 2 + (int)(s[r])
                if r >= k:
                    t -= int(s[r - k]) << k
                if r >= k - 1 and mi <= t <= ma:
                    st.add(t)
            return len(st) == ma - mi + 1

        if n == 1:
            return s.find('1') != -1

        k = 30
        while (1 << k) >= n:
            k -= 1

        if len(s) < (1 << (k - 1)) + k - 1 or len(s) < n - (1 << k) + k + 1:
            return False

        return __check(s, k, 1 << (k - 1), (1 << k) - 1) and __check(s, k + 1, 1 << k, n)


def main():
    # Example 1: Output: true
    s = "0110"
    n = 3

    # Example 2: Output: false
    # s = "0110"
    # n = 4

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.queryString(s, n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
