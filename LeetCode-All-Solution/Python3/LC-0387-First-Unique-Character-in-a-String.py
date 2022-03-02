#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0387-First-Unique-Character-in-a-String.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-02
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 0387 - (Easy) - First Unique Character in a String
https://leetcode.com/problems/first-unique-character-in-a-string/

Description & Requirement:
    Given a string s, find the first non-repeating character in it and return its index. 
    If it does not exist, return -1.

Example 1:
    Input: s = "leetcode"
    Output: 0
Example 2:
    Input: s = "loveleetcode"
    Output: 2
Example 3:
    Input: s = "aabb"
    Output: -1

Constraints:
    1 <= s.length <= 10^5
    s consists of only lowercase English letters.
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        # exception case
        if not isinstance(s, str) or len(s) <= 0:
            return -1
        if len(s) == 1:
            return 0
        # main method: (store char counter in hash dict and scan from left)
        return self._firstUniqChar(s)

    def _firstUniqChar(self, s: str) -> int:
        len_s = len(s)
        assert len_s >= 2

        hash_dict = dict({})
        for char in s:
            if char not in hash_dict:
                hash_dict[char] = 1
            else:
                hash_dict[char] += 1

        for idx, char in enumerate(s):
            if hash_dict[char] < 2:
                return idx

        return -1


def main():
    # Example 1: Output: 0
    s = "leetcode"

    # Example 2: Output: 2
    # s = "loveleetcode"

    # Example 3: Output: -1
    # s = "aabb"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.firstUniqChar(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
