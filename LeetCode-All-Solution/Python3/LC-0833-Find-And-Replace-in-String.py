#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0833-Find-And-Replace-in-String.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-08-15
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools
# import itertools

"""
LeetCode - 0833 - (Medium) Find And Replace in String
https://leetcode.com/problems/find-and-replace-in-string/

Description & Requirement:
    You are given a 0-indexed string s that you must perform k replacement operations on. 
    The replacement operations are given as three 0-indexed parallel arrays, 
    indices, sources, and targets, all of length k.

    To complete the ith replacement operation:

        1. Check if the substring sources[i] occurs at index indices[i] in the original string s.
        2. If it does not occur, do nothing.
        3. Otherwise if it does occur, replace that substring with targets[i].

    For example, if s = "abcd", indices[i] = 0, sources[i] = "ab", and targets[i] = "eee", 
    then the result of this replacement will be "eeecd".

    All replacement operations must occur simultaneously, meaning the replacement operations 
    should not affect the indexing of each other. The testcases will be generated such that 
    the replacements will not overlap.

    For example, a testcase with s = "abc", indices = [0, 1], and sources = ["ab","bc"] will not 
    be generated because the "ab" and "bc" replacements overlap.

    Return the resulting string after performing all replacement operations on s.

    A substring is a contiguous sequence of characters in a string.

Example 1:
    Input: s = "abcd", indices = [0, 2], sources = ["a", "cd"], targets = ["eee", "ffff"]
    Output: "eeebffff"
    Explanation:
        "a" occurs at index 0 in s, so we replace it with "eee".
        "cd" occurs at index 2 in s, so we replace it with "ffff".
Example 2:
    Input: s = "abcd", indices = [0, 2], sources = ["ab","ec"], targets = ["eee","ffff"]
    Output: "eeecd"
    Explanation:
        "ab" occurs at index 0 in s, so we replace it with "eee".
        "ec" does not occur at index 2 in s, so we do nothing.

Constraints:
    1 <= s.length <= 1000
    k == indices.length == sources.length == targets.length
    1 <= k <= 100
    0 <= indexes[i] < s.length
    1 <= sources[i].length, targets[i].length <= 50
    s consists of only lowercase English letters.
    sources[i] and targets[i] consist of only lowercase English letters.
"""


class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        # exception case
        assert isinstance(s, str) and len(s) >= 1
        assert isinstance(indices, list) and isinstance(sources, list) and isinstance(targets, list)
        assert len(indices) == len(sources) == len(targets) >= 1
        # main method: (hashing)
        return self._findReplaceString(s, indices, sources, targets)

    def _findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        assert isinstance(s, str) and len(s) >= 1
        assert isinstance(indices, list) and isinstance(sources, list) and isinstance(targets, list)
        assert len(indices) == len(sources) == len(targets) >= 1

        n, m = len(s), len(indices)

        ops = collections.defaultdict(list)
        for i, index in enumerate(indices):
            ops[index].append(i)

        res = []
        i = 0
        while i < n:
            succeed = False
            if i in ops:
                for pt in ops[i]:
                    if s[i:i + len(sources[pt])] == sources[pt]:
                        succeed = True
                        res.append(targets[pt])
                        i += len(sources[pt])
                        break
            if not succeed:
                res.append(s[i])
                i += 1

        return "".join(res)


def main():
    # Example 1: Output: "eeebffff"
    s = "abcd"
    indices = [0, 2]
    sources = ["a", "cd"]
    targets = ["eee", "ffff"]

    # Example 2: Output: "eeecd"
    # s = "abcd"
    # indices = [0, 2]
    # sources = ["ab", "ec"]
    # targets = ["eee", "ffff"]

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.findReplaceString(s, indices, sources, targets)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
