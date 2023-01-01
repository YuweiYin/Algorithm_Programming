#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2351-First-Letter-to-Appear-Twice.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-01-01
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 2351 - (Easy) - First Letter to Appear Twice
https://leetcode.com/problems/first-letter-to-appear-twice/

Description & Requirement:
    Given a string s consisting of lowercase English letters, return the first letter to appear twice.

    Note:
        A letter a appears twice before another letter b if the second occurrence of a is before the second occurrence of b.
        s will contain at least one letter that appears twice.

Example 1:
    Input: s = "abccbaacz"
    Output: "c"
    Explanation:
        The letter 'a' appears on the indexes 0, 5 and 6.
        The letter 'b' appears on the indexes 1 and 4.
        The letter 'c' appears on the indexes 2, 3 and 7.
        The letter 'z' appears on the index 8.
        The letter 'c' is the first letter to appear twice, 
            because out of all the letters the index of its second occurrence is the smallest.
Example 2:
    Input: s = "abcdd"
    Output: "d"
    Explanation:
        The only letter that appears twice is 'd' so we return 'd'.

Constraints:
    2 <= s.length <= 100
    s consists of lowercase English letters.
    s has at least one repeated letter.
"""


class Solution:
    def repeatedCharacter(self, s: str) -> str:
        # exception case
        assert isinstance(s, str) and len(s) >= 2
        # main method: (hash set)
        return self._repeatedCharacter(s)

    def _repeatedCharacter(self, s: str) -> str:
        assert isinstance(s, str) and len(s) >= 2

        counter = set()
        for ch in s:
            if ch not in counter:
                counter.add(ch)
            else:
                return ch

        return ""


def main():
    # Example 1: Output: "c"
    # s = "abccbaacz"

    # Example 2: Output: "d"
    s = "abcdd"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.repeatedCharacter(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
