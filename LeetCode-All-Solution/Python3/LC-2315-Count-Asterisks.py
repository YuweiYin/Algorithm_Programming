#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2315-Count-Asterisks.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-01-29
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 2315 - (Easy) - Count Asterisks
https://leetcode.com/problems/count-asterisks/

Description & Requirement:
    You are given a string s, where every two consecutive vertical bars '|' are grouped into a pair. 
    In other words, the 1st and 2nd '|' make a pair, the 3rd and 4th '|' make a pair, and so forth.

    Return the number of '*' in s, excluding the '*' between each pair of '|'.

    Note that each '|' will belong to exactly one pair.

Example 1:
    Input: s = "l|*e*et|c**o|*de|"
    Output: 2
    Explanation: The considered characters are underlined: "l|*e*et|c**o|*de|".
        The characters between the first and second '|' are excluded from the answer.
        Also, the characters between the third and fourth '|' are excluded from the answer.
        There are 2 asterisks considered. Therefore, we return 2.
Example 2:
    Input: s = "iamprogrammer"
    Output: 0
    Explanation: In this example, there are no asterisks in s. Therefore, we return 0.
Example 3:
    Input: s = "yo|uar|e**|b|e***au|tifu|l"
    Output: 5
    Explanation: The considered characters are underlined: "yo|uar|e**|b|e***au|tifu|l". 
        There are 5 asterisks considered. Therefore, we return 5.

Constraints:
    1 <= s.length <= 1000
    s consists of lowercase English letters, vertical bars '|', and asterisks '*'.
    s contains an even number of vertical bars '|'.
"""


class Solution:
    def countAsterisks(self, s: str) -> int:
        # exception case
        assert isinstance(s, str) and len(s) >= 1
        # main method: (deal with each character)
        return self._countAsterisks(s)

    def _countAsterisks(self, s: str) -> int:
        assert isinstance(s, str) and len(s) >= 1

        res = 0
        is_valid = True

        for ch in s:
            if ch == '|':
                is_valid = not is_valid
            elif ch == '*' and is_valid:
                res += 1

        return res


def main():
    # Example 1: Output: 2
    # s = "l|*e*et|c**o|*de|"

    # Example 2: Output: 0
    # s = "iamprogrammer"

    # Example 3: Output: 5
    s = "yo|uar|e**|b|e***au|tifu|l"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.countAsterisks(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
