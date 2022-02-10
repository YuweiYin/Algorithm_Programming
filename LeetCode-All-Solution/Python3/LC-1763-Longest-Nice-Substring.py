#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1763-Longest-Nice-Substring.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-01
=================================================================="""

import sys
import time
# from typing import List
# import collections

"""
LeetCode - 1763 - (Easy) - Longest Nice Substring
https://leetcode.com/problems/longest-nice-substring/

Description & Requirement:
    A string s is nice if, for every letter of the alphabet that s contains, 
    it appears both in uppercase and lowercase. 
    For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. 
    However, "abA" is not because 'b' appears, but 'B' does not.

    Given a string s, return the longest substring of s that is nice. 
    If there are multiple, return the substring of the earliest occurrence. 
    If there are none, return an empty string.

Example 1:
    Input: s = "YazaAay"
    Output: "aAa"
    Explanation:
    "aAa" is a nice string because 'A/a' is the only letter of the alphabet in s, and both 'A' and 'a' appear.
    "aAa" is the longest nice substring.
Example 2:
    Input: s = "Bb"
    Output: "Bb"
    Explanation: "Bb" is a nice string because both 'B' and 'b' appear. The whole string is a substring.
Example 3:
    Input: s = "c"
    Output: ""
    Explanation: There are no nice substrings.

Constraints:
    1 <= s.length <= 100
    s consists of uppercase and lowercase English letters.
"""


class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        # exception case
        if not isinstance(s, str) or len(s) <= 0 or not s.isalpha():
            return ""  # Error input type
        if len(s) == 1:
            return ""
        if len(s) == 2:
            return s if s[0] != s[1] and s[0].lower() == s[1].lower() else ""
        # main method: (Divide & Conquer)
        #     idea: if a substr s[i: j+1] is not a nice substring, then there must be some not-paired char in it
        #     divide the s[i: j+1] into several smaller intervals, and recursively find out if small intervals are nice
        return self._longestNiceSubstring(s)

    def _longestNiceSubstring(self, s: str) -> str:
        len_s = len(s)
        assert len_s >= 2

        def __divide_and_conquer(start: int, end: int) -> str:
            if start >= end:  # border case 1: len(substring) <= 1
                return ""
            if start + 1 == end:  # border case 2: len(substring) == 2
                return s[start: end + 1] if s[start] != s[end] and s[start].lower() == s[end].lower() else ""

            # use letter_dict to record if letters are paired
            letter_dict = dict({})  # key: lower case letter. value: {"upper": [idx, ...], "lower": [idx, ...]}

            for idx, letter in enumerate(s[start: end + 1]):  # statistics
                assert isinstance(letter, str)
                upper_letter = letter.upper()
                lower_letter = letter.lower()
                if lower_letter not in letter_dict:
                    if letter == upper_letter:
                        letter_dict[lower_letter] = dict({"upper": [start + idx], "lower": []})
                    elif letter == lower_letter:
                        letter_dict[lower_letter] = dict({"upper": [], "lower": [start + idx]})
                    else:
                        pass  # error path
                else:
                    if letter == upper_letter:
                        letter_dict[lower_letter]["upper"].append(start + idx)
                    elif letter == lower_letter:
                        letter_dict[lower_letter]["lower"].append(start + idx)
                    else:
                        pass  # error path

            unpaired_idx = []
            for k, v in letter_dict.items():  # key: lower_letter. value: {"upper": [idx, ...], "lower": [idx, ...]}
                assert len(v["upper"]) > 0 or len(v["lower"]) > 0  # at least one of cases exist (len of idx_list > 0)
                if len(v["upper"]) == 0:  # get the idx of unpaired lower case letter
                    for idx in v["lower"]:
                        unpaired_idx.append(idx)
                elif len(v["lower"]) == 0:  # get the idx of unpaired upper case letter
                    for idx in v["upper"]:
                        unpaired_idx.append(idx)

            if len(unpaired_idx) == 0:  # s[start: end + 1] is a nice substring
                return s[start: end + 1]

            # Divide & Conquer
            longest_nice_substr = ""

            start_idx = start - 1
            idx_index = 0
            while idx_index < len(unpaired_idx):  # divide
                # get rid of the unpaired idx and go DFS
                cur_nice_substr = __divide_and_conquer(start_idx + 1, unpaired_idx[idx_index] - 1)  # dfs, conquer
                if len(cur_nice_substr) > len(longest_nice_substr):
                    longest_nice_substr = cur_nice_substr
                # modify the interval
                start_idx = unpaired_idx[idx_index]
                idx_index += 1
            # last interval
            cur_nice_substr = __divide_and_conquer(unpaired_idx[-1] + 1, end)  # dfs, conquer
            if len(cur_nice_substr) > len(longest_nice_substr):
                longest_nice_substr = cur_nice_substr

            return longest_nice_substr

        res = __divide_and_conquer(0, len_s - 1)
        return res


def main():
    # Example 1: Output: "aAa"
    s = "YazaAay"

    # Example 2: Output: "Bb"
    # s = "Bb"

    # Example 3: Output: ""
    # s = "c"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.longestNiceSubstring(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
