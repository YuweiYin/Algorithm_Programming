#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2272-Substring-With-Largest-Variance.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-07-09
=================================================================="""

import sys
import time
import collections
# from typing import List
# import functools
# import itertools

"""
LeetCode - 2272 - (Hard) - Substring With Largest Variance
https://leetcode.com/problems/substring-with-largest-variance/

Description & Requirement:
    The variance of a string is defined as the largest difference between the number of occurrences 
    of any 2 characters present in the string. Note the two characters may or may not be the same.

    Given a string s consisting of lowercase English letters only, 
    return the largest variance possible among all substrings of s.

    A substring is a contiguous sequence of characters within a string.

Example 1:
    Input: s = "aababbb"
    Output: 3
    Explanation:
        All possible variances along with their respective substrings are listed below:
        - Variance 0 for substrings "a", "aa", "ab", "abab", "aababb", "ba", "b", "bb", and "bbb".
        - Variance 1 for substrings "aab", "aba", "abb", "aabab", "ababb", "aababbb", and "bab".
        - Variance 2 for substrings "aaba", "ababbb", "abbb", and "babb".
        - Variance 3 for substring "babbb".
        Since the largest possible variance is 3, we return it.
Example 2:
    Input: s = "abcde"
    Output: 0
    Explanation:
        No letter occurs more than once in s, so the variance of every substring is 0.

Constraints:
    1 <= s.length <= 10^4
    s consists of lowercase English letters.
"""


class Solution:
    def largestVariance(self, s: str) -> int:
        # exception case
        assert isinstance(s, str) and len(s) >= 1
        # main method: (dynamic programming)
        return self._largestVariance(s)

    def _largestVariance(self, s: str) -> int:
        assert isinstance(s, str) and len(s) >= 1

        pos = collections.defaultdict(list)
        for i, ch in enumerate(s):
            pos[ch].append(i)

        res = 0
        for c0, pos0 in pos.items():
            for c1, pos1 in pos.items():
                if c0 != c1:
                    i = j = 0
                    f, g = 0, -int(1e9+7)
                    while i < len(pos0) or j < len(pos1):
                        if j == len(pos1) or (i < len(pos0) and pos0[i] < pos1[j]):
                            f, g = max(f, 0) + 1, g + 1
                            i += 1
                        else:
                            f, g = max(f, 0) - 1, max(f, g, 0) - 1
                            j += 1
                        res = max(res, g)

        return res


def main():
    # Example 1: Output: 3
    s = "aababbb"

    # Example 2: Output: 0
    # s = "abcde"

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.largestVariance(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
