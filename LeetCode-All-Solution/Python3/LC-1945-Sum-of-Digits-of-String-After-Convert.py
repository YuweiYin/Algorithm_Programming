#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1945-Sum-of-Digits-of-String-After-Convert.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-12-15
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 1945 - (Easy) - Sum of Digits of String After Convert
https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

Description & Requirement:
    You are given a string s consisting of lowercase English letters, and an integer k.

    First, convert s into an integer by replacing each letter with its position in the alphabet 
    (i.e., replace 'a' with 1, 'b' with 2, ..., 'z' with 26). Then, transform the integer by replacing it 
    with the sum of its digits. Repeat the transform operation k times in total.

    For example, if s = "zbax" and k = 2, then the resulting integer would be 8 by the following operations:
        Convert: "zbax" ➝ "(26)(2)(1)(24)" ➝ "262124" ➝ 262124
        Transform #1: 262124 ➝ 2 + 6 + 2 + 1 + 2 + 4 ➝ 17
        Transform #2: 17 ➝ 1 + 7 ➝ 8

    Return the resulting integer after performing the operations described above.

Example 1:
    Input: s = "iiii", k = 1
    Output: 36
    Explanation: The operations are as follows:
        - Convert: "iiii" ➝ "(9)(9)(9)(9)" ➝ "9999" ➝ 9999
        - Transform #1: 9999 ➝ 9 + 9 + 9 + 9 ➝ 36
        Thus the resulting integer is 36.
Example 2:
    Input: s = "leetcode", k = 2
    Output: 6
    Explanation: The operations are as follows:
        - Convert: "leetcode" ➝ "(12)(5)(5)(20)(3)(15)(4)(5)" ➝ "12552031545" ➝ 12552031545
        - Transform #1: 12552031545 ➝ 1 + 2 + 5 + 5 + 2 + 0 + 3 + 1 + 5 + 4 + 5 ➝ 33
        - Transform #2: 33 ➝ 3 + 3 ➝ 6
        Thus the resulting integer is 6.
Example 3:
    Input: s = "zbax", k = 2
    Output: 8

Constraints:
    1 <= s.length <= 100
    1 <= k <= 10
    s consists of lowercase English letters.
"""


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        # exception case
        assert isinstance(s, str) and len(s) >= 1 and s.lower()
        assert isinstance(k, int) and k >= 1
        # main method: (follow the process)
        return self._getLucky(s, k)

    def _getLucky(self, s: str, k: int) -> int:
        assert isinstance(s, str) and len(s) >= 1 and s.lower()
        assert isinstance(k, int) and k >= 1

        ord_a = ord("a")
        digits_str = "".join(str(ord(ch) - ord_a + 1) for ch in s)

        for _ in range(k):
            if len(digits_str) == 1:
                break
            cur_sum = sum(int(ch) for ch in digits_str)
            digits_str = str(cur_sum)

        return int(digits_str)


def main():
    # Example 1: Output: 36
    # s = "iiii"
    # k = 1

    # Example 2: Output: 6
    s = "leetcode"
    k = 3

    # Example 3: Output: 8
    # s = "zbax"
    # k = 2

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.getLucky(s, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
