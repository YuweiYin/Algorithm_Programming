#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0942-DI-String-Match.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-05-09
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0942 - (Easy) - DI String Match
https://leetcode.com/problems/di-string-match/

Description & Requirement:
    A permutation perm of n + 1 integers of all the integers in the range [0, n] 
    can be represented as a string s of length n where:
        s[i] == 'I' if perm[i] < perm[i + 1], and
        s[i] == 'D' if perm[i] > perm[i + 1].

    Given a string s, reconstruct the permutation perm and return it. 
    If there are multiple valid permutations perm, return any of them.

Example 1:
    Input: s = "IDID"
    Output: [0,4,1,3,2]
Example 2:
    Input: s = "III"
    Output: [0,1,2,3]
Example 3:
    Input: s = "DDI"
    Output: [3,2,0,1]

Constraints:
    1 <= s.length <= 10^5
    s[i] is either 'I' or 'D'.
"""


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        # exception case
        assert isinstance(s, str) and len(s) >= 1
        # main method: (reverse all consecutive "D"s)
        return self._diStringMatch(s)

    def _diStringMatch(self, s: str) -> List[int]:
        assert isinstance(s, str) and len(s) >= 1
        len_s = len(s)
        s_list = list(range(len_s + 1))

        idx = 0
        while idx < len_s:
            if s[idx] == "D":
                start_idx = idx
                while idx + 1 < len_s and s[idx + 1] == "D":
                    idx += 1
                # reverse subarray
                end_idx = idx + 1
                while start_idx < end_idx:
                    s_list[start_idx], s_list[end_idx] = s_list[end_idx], s_list[start_idx]
                    start_idx += 1
                    end_idx -= 1
            idx += 1

        return s_list


def main():
    # Example 1: Output: [0,4,1,3,2]
    # s = "IDID"

    # Example 2: Output: [0,1,2,3]
    # s = "III"

    # Example 3: Output: [3,2,0,1]
    s = "DDI"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.diStringMatch(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
