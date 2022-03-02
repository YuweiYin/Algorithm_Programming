#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0242-Valid-Anagram.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-02
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 0242 - (Easy) - Valid Anagram
https://leetcode.com/problems/valid-anagram/

Description & Requirement:
    Given two strings s and t, 
    return true if t is an anagram of s, and false otherwise.

    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
    typically using all the original letters exactly once.

Example 1:
    Input: s = "anagram", t = "nagaram"
    Output: true
Example 2:
    Input: s = "rat", t = "car"
    Output: false

Constraints:
    1 <= s.length, t.length <= 5 * 10^4
    s and t consist of lowercase English letters.

Follow up:
    What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # exception case
        if not isinstance(s, str) or not isinstance(t, str):
            return False
        if len(s) != len(t):
            return False
        if len(s) == 0:
            return True
        # main method: (store char counter of magazine in hash dict and scan ransomNote)
        # other method: return not collections.Counter(ransomNote) - collections.Counter(magazine)
        return self._isAnagram(s, t)

    def _isAnagram(self, s: str, t: str) -> bool:
        hash_dict = dict({})
        for char in s:
            if char not in hash_dict:
                hash_dict[char] = 1
            else:
                hash_dict[char] += 1

        for char in t:
            if char not in hash_dict:  # no such char in s
                return False
            else:
                if hash_dict[char] <= 0:  # no rest such char in s
                    return False
                else:  # use one such char in s to construct t
                    hash_dict[char] -= 1

        return True


def main():
    # Example 1: Output: true
    # s = "anagram"
    # t = "nagaram"

    # Example 2: Output: false
    s = "rat"
    t = "car"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.isAnagram(s, t)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
