#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0049-Group-Anagrams.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-18
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0049 - (Medium) - Group Anagrams
https://leetcode.com/problems/group-anagrams/

Description & Requirement:
    Given an array of strings strs, group the anagrams together. You can return the answer in any order.

    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
    typically using all the original letters exactly once.

Example 1:
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:
    Input: strs = [""]
    Output: [[""]]
Example 3:
    Input: strs = ["a"]
    Output: [["a"]]

Constraints:
    1 <= strs.length <= 10^4
    0 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters.
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # exception case
        assert isinstance(strs, list) and len(strs) > 0
        # main method: (store each string and its sorted string)
        #     if two strings are anagrams, then their sorted string must be the same
        return self._groupAnagrams(strs)

    def _groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        len_strs = len(strs)
        assert len_strs > 0

        anagram_dict = dict({})  # key: sorted string; value: original string
        for string in strs:
            sorted_string = "".join(sorted(string))  # 0 <= strs[i].length <= 100, Time: O(log 100)
            if sorted_string not in anagram_dict:
                anagram_dict[sorted_string] = [string]
            else:
                anagram_dict[sorted_string].append(string)

        res = []
        for original_string in anagram_dict.values():
            res.append(original_string)

        return res


def main():
    # Example 1: Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

    # Example 2: Output: [[""]]
    # strs = [""]

    # Example 3: Output: [["a"]]
    # strs = ["a"]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.groupAnagrams(strs)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
