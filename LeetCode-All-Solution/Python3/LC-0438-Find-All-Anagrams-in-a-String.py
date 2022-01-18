#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0438-Find-All-Anagrams-in-a-String.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-18
=================================================================="""

import sys
import time
from typing import List

"""
LeetCode - 0438 - (Medium) - Find All Anagrams in a String
https://leetcode.com/problems/find-all-anagrams-in-a-string/

Description & Requirement:
    Given two strings s and p, return an array of all the start indices of p's anagrams in s. 
    You may return the answer in any order.

    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
    typically using all the original letters exactly once.

Example 1:
    Input: s = "cbaebabacd", p = "abc"
    Output: [0,6]
    Explanation:
        The substring with start index = 0 is "cba", which is an anagram of "abc".
        The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:
    Input: s = "abab", p = "ab"
    Output: [0,1,2]
    Explanation:
        The substring with start index = 0 is "ab", which is an anagram of "ab".
        The substring with start index = 1 is "ba", which is an anagram of "ab".
        The substring with start index = 2 is "ab", which is an anagram of "ab".

Constraints:
    1 <= s.length, p.length <= 3 * 10^4
    s and p consist of lowercase English letters.
"""


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # exception case
        if not isinstance(s, str) or len(s) <= 0 or not isinstance(p, str) or len(p) <= 0:
            return []  # Error input type
        if len(s) < len(p):
            return []
        # main method: (two pointer, slide window)
        #     key idea: if not match, don't always go back from beginning to match the whole p again
        #     optimization: needn't consider the order of char, so just sum them up!
        #         for each window, judge if sum([ord(char) for char in window_str]) == sum([ord(char) for char in p])
        #         slide window: detract the ord(leftmost_char) and add the ord(new_char).
        return self._findAnagrams(s, p)

    def _findAnagrams(self, s: str, p: str) -> List[int]:
        len_s = len(s)
        len_p = len(p)
        assert len_s > 0 and len_p > 0 and len_s >= len_p

        dict_p = dict({})
        for char in p:
            if char not in dict_p:
                dict_p[char] = 1  # how many this char are left to be matched
            else:
                dict_p[char] += 1

        res = []
        # window_size = len_p
        window_start = 0
        max_window_start = len_s - len_p

        cur_char_index = window_start  # first: the start index of the current window
        while window_start <= max_window_start:
            cur_max_index = window_start + len_p - 1  # the end index of the current window
            while cur_char_index <= cur_max_index:  # scan each char and do matching
                if s[cur_char_index] in dict_p and dict_p[s[cur_char_index]] > 0:  # matched
                    dict_p[s[cur_char_index]] -= 1  # counter --
                    cur_char_index += 1  # move on
                else:  # not match
                    break
            if cur_char_index <= cur_max_index:  # not match, happen at char s[cur_char_index]
                # if s[cur_char_index] is not in dict_p, then window slide to its right position
                if s[cur_char_index] not in dict_p:  # any window containing this char won't match p
                    # recover all char of s[window_start: cur_char_index]
                    for idx in range(window_start, cur_char_index):
                        assert s[idx] in dict_p
                        dict_p[s[idx]] += 1
                    # next window start from (cur_char_index + 1)
                    window_start = cur_char_index + 1
                    cur_char_index = window_start  # next window, scan from the start
                else:
                    assert dict_p[s[cur_char_index]] == 0
                    if s[window_start] == s[cur_char_index]:  # move window for one step can make up for it
                        window_start += 1
                        cur_char_index += 1  # move cur_char_index because the former char has been matched
                        continue
                    else:  # can't use s[window_start] to make up s[cur_char_index], so do regular window sliding
                        assert s[window_start] in dict_p
                        dict_p[s[window_start]] += 1  # recover s[window_start]
                        window_start += 1
                        continue  # don't move cur_char_index
            elif cur_char_index == cur_max_index + 1:
                res.append(window_start)
                # slide window one step right: recover one char s[window_start] and keep cur_char_index still
                assert s[window_start] in dict_p
                dict_p[s[window_start]] += 1
                window_start += 1
            else:
                # error branch
                break

        return res


def main():
    # Example 1: Output: [0,6]
    # s = "cbaebabacd"
    # p = "abc"

    # Example 2: Output: [0,1,2]
    # s = "abab"
    # p = "ab"

    # Example 3: Output: [3,4,6]
    s = "abaacbabc"
    p = "abc"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.findAnagrams(s, p)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
