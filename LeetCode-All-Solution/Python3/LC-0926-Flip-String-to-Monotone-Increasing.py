#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0926-Flip-String-to-Monotone-Increasing.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-06-11
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 0926 - (Medium) - Flip String to Monotone Increasing
https://leetcode.com/problems/flip-string-to-monotone-increasing/

Description & Requirement:
    A binary string is monotone increasing if it consists of some number of 0's (possibly none), 
    followed by some number of 1's (also possibly none).

    You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.

    Return the minimum number of flips to make s monotone increasing.

Example 1:
    Input: s = "00110"
    Output: 1
    Explanation: We flip the last digit to get 00111.
Example 2:
    Input: s = "010110"
    Output: 2
    Explanation: We flip to get 011111, or alternatively 000111.
Example 3:
    Input: s = "00011000"
    Output: 2
    Explanation: We flip to get 00000000.

Constraints:
    1 <= s.length <= 10^5
    s[i] is either '0' or '1'.
"""


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        # exception case
        assert isinstance(s, str) and len(s) >= 1
        for ch in s:
            assert ch == "0" or ch == "1"
        # main method: (1. prefix sum; 2. dynamic programming)
        return self._minFlipsMonoIncr(s)

    def _minFlipsMonoIncr(self, s: str) -> int:
        assert isinstance(s, str) and len(s) >= 1
        len_s = len(s)

        prefix_sum = [0]
        for ch in s:
            prefix_sum.append(prefix_sum[-1] + int(ch))

        res = len_s
        # i partition the target nums into 2 parts: chars in nums[:i] are all "0" and those in nums[i:] are all "1"
        for i in range(len(prefix_sum)):
            res = min(res, prefix_sum[i] + len_s - i - (prefix_sum[-1] - prefix_sum[i]))
        return res


def main():
    # Example 1: Output: 1
    # s = "00110"

    # Example 2: Output: 2
    # s = "010110"

    # Example 3: Output: 2
    s = "00011000"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minFlipsMonoIncr(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
