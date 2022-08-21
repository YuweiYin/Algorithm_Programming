#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0936-Stamping-The-Sequence.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-08-21
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 0936 - (Hard) - Stamping The Sequence
https://leetcode.com/problems/stamping-the-sequence/

Description & Requirement:
    You are given two strings stamp and target. Initially, 
    there is a string s of length target.length with all s[i] == '?'.

    In one turn, you can place stamp over s and replace every letter in the s with the corresponding letter from stamp.

    For example, if stamp = "abc" and target = "abcba", then s is "?????" initially. In one turn you can:
        place stamp at index 0 of s to obtain "abc??",
        place stamp at index 1 of s to obtain "?abc?", or
        place stamp at index 2 of s to obtain "??abc".
        Note that stamp must be fully contained in the boundaries of s in order to stamp 
            (i.e., you cannot place stamp at index 3 of s).
    We want to convert s to target using at most 10 * target.length turns.

    Return an array of the index of the left-most letter being stamped at each turn. 
    If we cannot obtain target from s within 10 * target.length turns, return an empty array.

Example 1:
    Input: stamp = "abc", target = "ababc"
    Output: [0,2]
    Explanation: Initially s = "?????".
        - Place stamp at index 0 to get "abc??".
        - Place stamp at index 2 to get "ababc".
        [1,0,2] would also be accepted as an answer, as well as some other answers.
Example 2:
    Input: stamp = "abca", target = "aabcaca"
    Output: [3,0,1]
    Explanation: Initially s = "???????".
        - Place stamp at index 3 to get "???abca".
        - Place stamp at index 0 to get "abcabca".
        - Place stamp at index 1 to get "aabcaca".

Constraints:
    1 <= stamp.length <= target.length <= 1000
    stamp and target consist of lowercase English letters.
"""


class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        # exception case
        assert isinstance(stamp, str) and isinstance(target, str) and len(target) >= len(stamp) >= 1
        # main method: (perform the reverse process)
        return self._movesToStamp(stamp, target)

    def _movesToStamp(self, stamp: str, target: str) -> List[int]:
        assert isinstance(stamp, str) and isinstance(target, str) and len(target) >= len(stamp) >= 1

        res, ans = [], []
        len_s, len_t = len(stamp), len(target)
        queue = collections.deque()
        done = [False for _ in range(len_t)]

        for idx in range(len_t - len_s + 1):
            made, todo = set(), set()
            for j, ch in enumerate(stamp):
                a = target[idx + j]
                if a == ch:
                    made.add(idx + j)
                else:
                    todo.add(idx + j)
            ans.append((made, todo))

            if not todo:
                res.append(idx)
                for j in range(idx, idx + len(stamp)):
                    if not done[j]:
                        queue.append(j)
                        done[j] = True

        while len(queue) > 0:
            idx = queue.popleft()
            for j in range(max(0, idx - len_s + 1), min(len_t - len_s, idx) + 1):
                if idx in ans[j][1]:
                    ans[j][1].discard(idx)
                    if not ans[j][1]:
                        res.append(j)
                        for m in ans[j][0]:
                            if not done[m]:
                                queue.append(m)
                                done[m] = True

        return res[::-1] if all(done) else []


def main():
    # Example 1: Output: [0,2]
    stamp = "abc"
    target = "ababc"

    # Example 2: Output: [3,0,1]
    # stamp = "abca"
    # target = "aabcaca"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.movesToStamp(stamp, target)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
