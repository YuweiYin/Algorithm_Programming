#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1023-Camelcase-Matching.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-04-14
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1023 - (Medium) - Camelcase Matching
https://leetcode.com/problems/camelcase-matching/

Description & Requirement:
    Given an array of strings queries and a string pattern, 
    return a boolean array answer where answer[i] is true if queries[i] matches pattern, 
    and false otherwise.

    A query word queries[i] matches pattern if you can insert lowercase English letters pattern so that 
    it equals the query. You may insert each character at any position and you may not insert any characters.

Example 1:
    Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"
    Output: [true,false,true,true,false]
    Explanation: "FooBar" can be generated like this "F" + "oo" + "B" + "ar".
        "FootBall" can be generated like this "F" + "oot" + "B" + "all".
        "FrameBuffer" can be generated like this "F" + "rame" + "B" + "uffer".
Example 2:
    Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBa"
    Output: [true,false,true,false,false]
    Explanation: "FooBar" can be generated like this "Fo" + "o" + "Ba" + "r".
        "FootBall" can be generated like this "Fo" + "ot" + "Ba" + "ll".
Example 3:
    Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBaT"
    Output: [false,true,false,false,false]
    Explanation: "FooBarTest" can be generated like this "Fo" + "o" + "Ba" + "r" + "T" + "est".

Constraints:
    1 <= pattern.length, queries.length <= 100
    1 <= queries[i].length <= 100
    queries[i] and pattern consist of English letters.
"""


class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        # exception case
        assert isinstance(queries, list) and len(queries) >= 1
        assert isinstance(pattern, str) and len(pattern) >= 1
        # main method: (two pointers)
        return self._camelMatch(queries, pattern)

    def _camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        assert isinstance(queries, list) and len(queries) >= 1
        assert isinstance(pattern, str) and len(pattern) >= 1

        len_q = len(queries)
        res = [True for _ in range(len_q)]
        for q_idx in range(len_q):
            p_idx = 0
            for w in queries[q_idx]:
                if p_idx < len(pattern) and pattern[p_idx] == w:
                    p_idx += 1
                elif w.isupper():
                    res[q_idx] = False
                    break
            if p_idx < len(pattern):
                res[q_idx] = False

        return res


def main():
    # Example 1: Output: [true,false,true,true,false]
    # queries = ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"]
    # pattern = "FB"

    # Example 2: Output: [true,false,true,false,false]
    # queries = ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"]
    # pattern = "FoBa"

    # Example 3: Output: [false,true,false,false,false]
    queries = ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"]
    pattern = "FoBaT"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.camelMatch(queries, pattern)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
