#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1796-Second-Largest-Digit-in-a-String.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-12-03
=================================================================="""

import sys
import time
# from typing import List
# import itertools

"""
LeetCode - 1796 - (Easy) - Second Largest Digit in a String
https://leetcode.com/problems/second-largest-digit-in-a-string/

Description & Requirement:
    Given an alphanumeric string s, 
    return the second largest numerical digit that appears in s, or -1 if it does not exist.

    An alphanumeric string is a string consisting of lowercase English letters and digits.

Example 1:
    Input: s = "dfa12321afd"
    Output: 2
    Explanation: The digits that appear in s are [1, 2, 3]. The second largest digit is 2.
Example 2:
    Input: s = "abc1111"
    Output: -1
    Explanation: The digits that appear in s are [1]. There is no second largest digit. 

Constraints:
    1 <= s.length <= 500
    s consists of only lowercase English letters and/or digits.
"""


class Solution:
    def secondHighest(self, s: str) -> int:
        # exception case
        assert isinstance(s, str) and len(s) >= 1
        # main method: (scan and record the largest and second-largest number)
        return self._secondHighest(s)

    def _secondHighest(self, s: str) -> int:
        """
        Runtime: 34 ms, faster than 95.97% of Python3 online submissions for Second Largest Digit in a String.
        Memory Usage: 14 MB, less than 18.28% of Python3 online submissions for Second Largest Digit in a String.
        """
        assert isinstance(s, str) and len(s) >= 1

        if len(s) == 1:
            return -1

        largest = -1
        s_largest = -1
        for ch in s:
            if ch.isdigit():
                cur_num = int(ch)
                if cur_num > largest:
                    if largest >= 0:
                        s_largest = largest
                    largest = cur_num
                elif largest > cur_num > s_largest:
                    s_largest = cur_num

        return s_largest


def main():
    # Example 1: Output: 2
    s = "dfa12321afd"

    # Example 2: Output: -1
    # s = "abc1111"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.secondHighest(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
