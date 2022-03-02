#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0383-Ransom-Note.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-02
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 0383 - (Easy) - Ransom Note
https://leetcode.com/problems/ransom-note/

Description & Requirement:
    Given two strings ransomNote and magazine, 
    return true if ransomNote can be constructed from magazine and false otherwise.

    Each letter in magazine can only be used once in ransomNote.

Example 1:
    Input: ransomNote = "a", magazine = "b"
    Output: false
Example 2:
    Input: ransomNote = "aa", magazine = "ab"
    Output: false
Example 3:
    Input: ransomNote = "aa", magazine = "aab"
    Output: true

Constraints:
    1 <= ransomNote.length, magazine.length <= 10^5
    ransomNote and magazine consist of lowercase English letters.
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # exception case
        if not isinstance(ransomNote, str) or not isinstance(magazine, str):
            return False
        if len(ransomNote) > len(magazine):
            return False
        if len(ransomNote) == 0:
            return True
        # main method: (store char counter of magazine in hash dict and scan ransomNote)
        # other method: return not collections.Counter(ransomNote) - collections.Counter(magazine)
        return self._canConstruct(ransomNote, magazine)

    def _canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_dict = dict({})
        for char in magazine:
            if char not in hash_dict:
                hash_dict[char] = 1
            else:
                hash_dict[char] += 1

        for char in ransomNote:
            if char not in hash_dict:  # no such char in magazine
                return False
            else:
                if hash_dict[char] <= 0:  # no rest such char in magazine
                    return False
                else:  # use one such char in magazine to construct ransomNote
                    hash_dict[char] -= 1

        return True


def main():
    # Example 1: Output: false
    ransomNote = "a"
    magazine = "b"

    # Example 2: Output: false
    # ransomNote = "aa"
    # magazine = "ab"

    # Example 3: Output: true
    # ransomNote = "aa"
    # magazine = "aab"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.canConstruct(ransomNote, magazine)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
