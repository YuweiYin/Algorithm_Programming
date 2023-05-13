#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2466-Count-Ways-To-Build-Good-Strings.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-05-13
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 2466 - (Medium) - Count Ways To Build Good Strings
https://leetcode.com/problems/count-ways-to-build-good-strings/

Description & Requirement:
    Given the integers zero, one, low, and high, we can construct a string by starting with an empty string, 
    and then at each step perform either of the following:
        Append the character '0' zero times.
        Append the character '1' one times.

    This can be performed any number of times.

    A good string is a string constructed by the above process having a length between low and high (inclusive).

    Return the number of different good strings that can be constructed satisfying these properties. 
    Since the answer can be large, return it modulo 10^9 + 7.

Example 1:
    Input: low = 3, high = 3, zero = 1, one = 1
    Output: 8
    Explanation: 
        One possible valid good string is "011". 
        It can be constructed as follows: "" -> "0" -> "01" -> "011". 
        All binary strings from "000" to "111" are good strings in this example.
Example 2:
    Input: low = 2, high = 3, zero = 1, one = 2
    Output: 5
    Explanation: The good strings are "00", "11", "000", "110", and "011".

Constraints:
    1 <= low <= high <= 10^5
    1 <= zero, one <= low
"""


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        # exception case
        assert isinstance(low, int) and low >= 1
        assert isinstance(high, int) and high >= low
        assert isinstance(zero, int) and 1 <= zero <= low
        assert isinstance(one, int) and 1 <= one <= low
        # main method: (similar to [LC-0070 Climbing Stairs](https://leetcode.com/problems/climbing-stairs/))
        return self._countGoodStrings(low, high, zero, one)

    def _countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        assert isinstance(low, int) and low >= 1
        assert isinstance(high, int) and high >= low
        assert isinstance(zero, int) and 1 <= zero <= low
        assert isinstance(one, int) and 1 <= one <= low

        MOD = int(1e9+7)
        dp = [1] + [0] * high
        for i in range(1, high + 1):
            if i >= one:
                dp[i] = (dp[i] + dp[i - one]) % MOD
            if i >= zero:
                dp[i] = (dp[i] + dp[i - zero]) % MOD

        return sum(dp[low:]) % MOD


def main():
    # Example 1: Output: 8
    # low = 3
    # high = 3
    # zero = 1
    # one = 1

    # Example 2: Output: 5
    low = 2
    high = 3
    zero = 1
    one = 2

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.countGoodStrings(low, high, zero, one)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
