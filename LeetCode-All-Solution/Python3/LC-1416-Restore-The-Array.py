#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1416-Restore-The-Array.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-04-23
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 1416 - (Hard) - Restore The Array
https://leetcode.com/problems/restore-the-array/

Description & Requirement:
    A program was supposed to print an array of integers. The program forgot to print whitespaces 
    and the array is printed as a string of digits s and all we know is that 
    all integers in the array were in the range [1, k] and there are no leading zeros in the array.

    Given the string s and the integer k, return the number of the possible arrays that can be printed 
    as s using the mentioned program. Since the answer may be very large, return it modulo 10^9 + 7.

Example 1:
    Input: s = "1000", k = 10000
    Output: 1
    Explanation: The only possible array is [1000]
Example 2:
    Input: s = "1000", k = 10
    Output: 0
    Explanation: There cannot be an array that was printed this way and has all integer >= 1 and <= 10.
Example 3:
    Input: s = "1317", k = 2000
    Output: 8
    Explanation: Possible arrays are [1317],[131,7],[13,17],[1,317],[13,1,7],[1,31,7],[1,3,17],[1,3,1,7]

Constraints:
    1 <= s.length <= 10^5
    s consists of only digits and does not contain leading zeros.
    1 <= k <= 10^9
"""


class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        # exception case
        assert isinstance(s, str) and len(s) >= 1
        assert isinstance(k, int) and k >= 1
        # main method: (dynamic programming)
        return self._numberOfArrays(s, k)

    def _numberOfArrays(self, s: str, k: int) -> int:
        assert isinstance(s, str) and len(s) >= 1
        assert isinstance(k, int) and k >= 1

        MOD = int(1e9+7)
        n = len(s)
        dp = [1] + [0] * n

        for i in range(1, n + 1):
            num, base = 0, 1
            j = i - 1
            while j >= 0 and i - j <= 10:
                num += (ord(s[j]) - 48) * base
                if num > k:
                    break
                if s[j] != "0":
                    dp[i] += dp[j]
                base *= 10
                j -= 1
            dp[i] %= MOD

        return dp[-1]


def main():
    # Example 1: Output: 1
    s = "1000"
    k = 10000

    # Example 2: Output: 0
    # s = "1000"
    # k = 10

    # Example 3: Output: 8
    # s = "1317"
    # k = 2000

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.numberOfArrays(s, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
