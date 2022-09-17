#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1624-Largest-Substring-Between-Two-Equal-Characters.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-09-17
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 1624 - (Easy) - Largest Substring Between Two Equal Characters
https://leetcode.com/problems/largest-substring-between-two-equal-characters/

Description & Requirement:
    Given a string s, return the length of the longest substring between two equal characters, 
    excluding the two characters. If there is no such substring return -1.

    A substring is a contiguous sequence of characters within a string.

Example 1:
    Input: s = "aa"
    Output: 0
    Explanation: The optimal substring here is an empty substring between the two 'a's.
Example 2:
    Input: s = "abca"
    Output: 2
    Explanation: The optimal substring here is "bc".
Example 3:
    Input: s = "cbzxy"
    Output: -1
    Explanation: There are no characters that appear twice in s.

Constraints:
    1 <= s.length <= 300
    s contains only lowercase English letters.
"""


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        # exception case
        assert isinstance(s, str) and len(s) >= 1
        # main method: (hash dict, store the leftmost and rightmost indices of the same char)
        return self._maxLengthBetweenEqualCharacters(s)

    def _maxLengthBetweenEqualCharacters(self, s: str) -> int:
        """
        Runtime: 36 ms, faster than 88.15% of Python3 submissions for Largest Substring Between Two Equal Characters.
        Memory Usage: 13.9 MB, less than 62.54% of Python3 submissions for Largest Substring Between Two Equal Chars.
        """
        assert isinstance(s, str) and len(s) >= 1

        ch_index = dict({})
        for idx, ch in enumerate(s):
            if ch not in ch_index:
                ch_index[ch] = [idx]
            else:
                ch_index[ch].append(idx)

        res = -1
        for idx_list in ch_index.values():
            if len(idx_list) >= 2:
                res = max(res, idx_list[-1] - idx_list[0] - 1)

        return res


def main():
    # Example 1: Output: 0
    # s = "aa"

    # Example 2: Output: 2
    # s = "abca"

    # Example 3: Output: -1
    s = "cbzxy"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maxLengthBetweenEqualCharacters(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
