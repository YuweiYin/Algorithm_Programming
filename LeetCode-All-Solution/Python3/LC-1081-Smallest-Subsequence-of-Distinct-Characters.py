#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1081-Smallest-Subsequence-of-Distinct-Characters.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-18
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 1081 - (Medium) - Smallest Subsequence of Distinct Characters
https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

Description & Requirement:
    Given a string s, return the lexicographically smallest subsequence of s 
    that contains all the distinct characters of s exactly once.

Example 1:
    Input: s = "bcabc"
    Output: "abc"
Example 2:
    Input: s = "cbacdcbc"
    Output: "acdb"

Constraints:
    1 <= s.length <= 1000
    s consists of lowercase English letters.

Note:
    This question is the same as 316: https://leetcode.com/problems/remove-duplicate-letters/
"""


class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # exception case
        assert isinstance(s, str) and len(s) > 0
        # main method: (hash dict counter, then use monotonic stack)
        return self._smallestSubsequence(s)

    def _smallestSubsequence(self, s: str) -> str:
        len_s = len(s)
        assert len_s > 0

        letter_counter = dict({})  # key: letter; value: counter
        for ch in s:
            if ch not in letter_counter:
                letter_counter[ch] = 1
            else:
                letter_counter[ch] += 1

        stack = []
        used_letter = set()
        for ch in s:
            if ch not in used_letter:
                # pop stack top that is larger than the current letter
                while len(stack) > 0 and stack[-1] > ch:
                    if letter_counter[stack[-1]] > 0:
                        used_letter.discard(stack[-1])  # actually, each letter can only appear in stack once at a time
                        stack.pop()
                    else:
                        break
                # now stack[-1] <= ch, push in the current letter
                used_letter.add(ch)
                stack.append(ch)
            # anyway, the current letter has been used, decrease the counter
            letter_counter[ch] -= 1

        return "".join(stack)


def main():
    # Example 1: Output: "abc"
    # s = "bcabc"

    # Example 2: Output: "acdb"
    s = "cbacdcbc"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.smallestSubsequence(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
