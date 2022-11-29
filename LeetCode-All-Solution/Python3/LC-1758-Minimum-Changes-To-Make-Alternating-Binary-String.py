#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1758-Minimum-Changes-To-Make-Alternating-Binary-String.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-11-29
=================================================================="""

import sys
import time
# from typing import List
# import itertools

"""
LeetCode - 1758 - (Easy) - Minimum Changes To Make Alternating Binary String
https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/

Description & Requirement:
    You are given a string s consisting only of the characters '0' and '1'. 
    In one operation, you can change any '0' to '1' or vice versa.

    The string is called alternating if no two adjacent characters are equal. 
    For example, the string "010" is alternating, while the string "0100" is not.

    Return the minimum number of operations needed to make s alternating.

Example 1:
    Input: s = "0100"
    Output: 1
    Explanation: If you change the last character to '1', s will be "0101", which is alternating.
Example 2:
    Input: s = "10"
    Output: 0
    Explanation: s is already alternating.
Example 3:
    Input: s = "1111"
    Output: 2
    Explanation: You need two operations to reach "0101" or "1010".

Constraints:
    1 <= s.length <= 10^4
    s[i] is either '0' or '1'.
"""


class Solution:
    def minOperations(self, s: str) -> int:
        # exception case
        assert isinstance(s, str) and len(s) >= 1
        # main method: (sum the 0/1 int list)
        return self._minOperations(s)

    def _minOperations(self, s: str) -> int:
        assert isinstance(s, str) and len(s) >= 1

        cnt = sum(int(ch) != idx % 2 for idx, ch in enumerate(s))

        return min(cnt, len(s) - cnt)


def main():
    # Example 1: Output: 1
    # s = "0100"

    # Example 2: Output: 0
    # s = "10"

    # Example 3: Output: 2
    s = "1111"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minOperations(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
