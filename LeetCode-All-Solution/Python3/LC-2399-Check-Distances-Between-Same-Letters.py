#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2399-Check-Distances-Between-Same-Letters.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-04-09
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 2399 - (Easy) - Check Distances Between Same Letters
https://leetcode.com/problems/check-distances-between-same-letters/

Description & Requirement:
    You are given a 0-indexed string s consisting of only lowercase English letters, 
    where each letter in s appears exactly twice. 
    You are also given a 0-indexed integer array distance of length 26.

    Each letter in the alphabet is numbered from 0 to 25 
    (i.e. 'a' -> 0, 'b' -> 1, 'c' -> 2, ... , 'z' -> 25).

    In a well-spaced string, the number of letters between 
    the two occurrences of the i-th letter is distance[i]. 
    If the ith letter does not appear in s, then distance[i] can be ignored.

    Return true if s is a well-spaced string, otherwise return false.

Example 1:
    Input: s = "abaccb", distance = [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    Output: true
    Explanation:
        - 'a' appears at indices 0 and 2 so it satisfies distance[0] = 1.
        - 'b' appears at indices 1 and 5 so it satisfies distance[1] = 3.
        - 'c' appears at indices 3 and 4 so it satisfies distance[2] = 0.
        Note that distance[3] = 5, but since 'd' does not appear in s, it can be ignored.
        Return true because s is a well-spaced string.
Example 2:
    Input: s = "aa", distance = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    Output: false
    Explanation:
        - 'a' appears at indices 0 and 1 so there are zero letters between them.
        Because distance[0] = 1, s is not a well-spaced string.

Constraints:
    2 <= s.length <= 52
    s consists only of lowercase English letters.
    Each letter appears in s exactly twice.
    distance.length == 26
    0 <= distance[i] <= 50
"""


class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        # exception case
        assert isinstance(s, str) and len(s) >= 2 and s.islower()
        assert isinstance(distance, list) and len(distance) == 26
        # main method: (simulate the process)
        return self._checkDistances(s, distance)

    def _checkDistances(self, s: str, distance: List[int]) -> bool:
        assert isinstance(s, str) and len(s) >= 2 and s.islower()
        assert isinstance(distance, list) and len(distance) == 26

        first_index = [0] * 26

        for i in range(len(s)):
            idx = ord(s[i]) - ord('a')
            if first_index[idx] and i - first_index[idx] != distance[idx]:
                return False
            first_index[idx] = i + 1

        return True


def main():
    # Example 1: Output: true
    # s = "abaccb"
    # distance = [1, 3, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # Example 2: Output: false
    s = "aa"
    distance = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.checkDistances(s, distance)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
