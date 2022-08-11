#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1417-Reformat-The-String.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-08-11
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 1417 - (Easy) - Reformat The String
https://leetcode.com/problems/reformat-the-string/

Description & Requirement:
    You are given an alphanumeric string s. 
    (Alphanumeric string is a string consisting of lowercase English letters and digits).

    You have to find a permutation of the string where no letter is followed by another letter 
    and no digit is followed by another digit. That is, no two adjacent characters have the same type.

    Return the reformatted string or return an empty string if it is impossible to reformat the string.

Example 1:
    Input: s = "a0b1c2"
    Output: "0a1b2c"
    Explanation: No two adjacent characters have the same type in "0a1b2c". "a0b1c2", "0a1b2c", "0c2a1b" are also valid permutations.
Example 2:
    Input: s = "leetcode"
    Output: ""
    Explanation: "leetcode" has only characters so we cannot separate them by digits.
Example 3:
    Input: s = "1229857369"
    Output: ""
    Explanation: "1229857369" has only digits so we cannot separate them by characters.

Constraints:
    1 <= s.length <= 500
    s consists of only lowercase English letters and/or digits.
"""


class Solution:
    def reformat(self, s: str) -> str:
        # exception case
        assert isinstance(s, str) and len(s) >= 1
        # main method: (count numbers and chars)
        return self._reformat(s)

    def _reformat(self, s: str) -> str:
        """
        Runtime: 57 ms, faster than 74.10% of Python3 online submissions for Reformat The String.
        Memory Usage: 13.8 MB, less than 86.92% of Python3 online submissions for Reformat The String.
        """
        assert isinstance(s, str) and len(s) >= 1

        number = []
        char = []
        for ch in s:
            if ch.isdigit():
                number.append(ch)
            elif ch.isalpha():
                char.append(ch)
            else:
                continue

        len_n = len(number)
        len_c = len(char)
        if abs(len_n - len_c) > 1:
            return ""

        res = ""
        if len_n > len_c:
            for idx in range(len_c):
                res += number[idx]
                res += char[idx]
            res += number[-1]
        elif len_n < len_c:
            for idx in range(len_n):
                res += char[idx]
                res += number[idx]
            res += char[-1]
        else:
            for idx in range(len_c):
                res += number[idx]
                res += char[idx]

        return res


def main():
    # Example 1: Output: "0a1b2c"
    s = "a0b1c2"

    # Example 2: Output: ""
    # s = "leetcode"

    # Example 3: Output: ""
    # s = "1229857369"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.reformat(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
