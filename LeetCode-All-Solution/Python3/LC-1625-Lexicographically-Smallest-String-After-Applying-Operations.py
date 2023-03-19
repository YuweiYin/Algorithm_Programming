#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1625-Lexicographically-Smallest-String-After-Applying-Operations.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-03-19
=================================================================="""

import sys
import time
import collections
# from typing import List
# import functools

"""
LeetCode - 1625 - (Medium) - Lexicographically Smallest String After Applying Operations
https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/

Description & Requirement:
    You are given a string s of even length consisting of digits from 0 to 9, and two integers a and b.

    You can apply either of the following two operations any number of times and in any order on s:
        Add a to all odd indices of s (0-indexed). Digits post 9 are cycled back to 0. For example, 
            if s = "3456" and a = 5, s becomes "3951".
        Rotate s to the right by b positions. For example, if s = "3456" and b = 1, s becomes "6345".

    Return the lexicographically smallest string you can obtain 
    by applying the above operations any number of times on s.

    A string a is lexicographically smaller than a string b (of the same length) if in the first position 
    where a and b differ, string a has a letter that appears earlier in the alphabet than the corresponding letter in b.
    For example, "0158" is lexicographically smaller than "0190" because 
    the first position they differ is at the third letter, and '5' comes before '9'.

Example 1:
    Input: s = "5525", a = 9, b = 2
    Output: "2050"
    Explanation: We can apply the following operations:
        Start:  "5525"
        Rotate: "2555"
        Add:    "2454"
        Add:    "2353"
        Rotate: "5323"
        Add:    "5222"
        Add:    "5121"
        Rotate: "2151"
        Add:    "2050"
        There is no way to obtain a string that is lexicographically smaller then "2050".
Example 2:
    Input: s = "74", a = 5, b = 1
    Output: "24"
    Explanation: We can apply the following operations:
        Start:  "74"
        Rotate: "47"
        Add:    "42"
        Rotate: "24"
        There is no way to obtain a string that is lexicographically smaller then "24".
Example 3:
    Input: s = "0011", a = 4, b = 2
    Output: "0011"
    Explanation: There are no sequence of operations that will give us a lexicographically smaller string than "0011".

Constraints:
    2 <= s.length <= 100
    s.length is even.
    s consists of digits from 0 to 9 only.
    1 <= a <= 9
    1 <= b <= s.length - 1
"""


class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        # exception case
        assert isinstance(s, str) and len(s) >= 2 and len(s) & 0x01 == 0
        assert isinstance(a, int) and 1 <= a <= 9
        assert isinstance(b, int) and 1 <= b <= len(s) - 1
        # main method: (BFS)
        return self._findLexSmallestString(s, a, b)

    def _findLexSmallestString(self, s: str, a: int, b: int) -> str:
        assert isinstance(s, str) and len(s) >= 2 and len(s) & 0x01 == 0
        assert isinstance(a, int) and 1 <= a <= 9
        assert isinstance(b, int) and 1 <= b <= len(s) - 1

        queue = collections.deque([s])
        visited = {s}
        res = s
        while len(queue) > 0:
            cur_s = queue.popleft()
            if res > cur_s:
                res = cur_s
            next_1 = ''.join([str((int(ch) + a) % 10) if idx & 1 else ch for idx, ch in enumerate(cur_s)])
            next_2 = cur_s[-b:] + cur_s[:-b]
            for next_s in (next_1, next_2):
                if next_s not in visited:
                    visited.add(next_s)
                    queue.append(next_s)

        return res


def main():
    # Example 1: Output: "2050"
    s = "5525"
    a = 9
    b = 2

    # Example 2: Output: "24"
    # s = "74"
    # a = 5
    # b = 1

    # Example 3: Output: "0011"
    # s = "0011"
    # a = 4
    # b = 2

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.findLexSmallestString(s, a, b)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
