#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0567-Permutation-in-String.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-06
=================================================================="""
# import functools
import sys
import time
# from typing import List

"""
LeetCode - 0567 - (Medium) - Permutation in String
https://leetcode.com/problems/permutation-in-string/

Description & Requirement:
    Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

    In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
    Input: s1 = "ab", s2 = "eidbaooo"
    Output: true
    Explanation: s2 contains one permutation of s1 ("ba").
Example 2:
    Input: s1 = "ab", s2 = "eidboaoo"
    Output: false

Constraints:
    1 <= s1.length, s2.length <= 10^4
    s1 and s2 consist of lowercase English letters.
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # exception case
        if not isinstance(s1, str) or not isinstance(s2, str) or len(s2) <= 0 or len(s2) < len(s1):
            return False
        # border case
        if len(s1) == 0:
            return True  # Error input
        if len(s1) == 1:
            return s1 in s2
        # 1. main method: expand & shrink slide window, partial match (slightly similar to KMP Knuth-Morris-Pratt)
        # 2. slide window (slow): find all substring whose length == len_s1, check if this substring == s1's permutation
        return self._checkInclusion(s1, s2)

    def _checkInclusion(self, s1: str, s2: str) -> bool:
        # now, 2 <= len_s1 <= len_s2
        len_s1 = len(s1)
        len_s2 = len(s2)

        # preprocess s1 into a dict, key: char c; value: how many c left to be matched
        dict_s1 = dict({})
        for ch in s1:
            if ch in dict_s1:
                dict_s1[ch] += 1
            else:
                dict_s1[ch] = 1

        left_list = []  # every possible left_subs index
        for idx, ch in enumerate(s2):
            if ch in dict_s1:
                left_list.append(idx)
        len_left_list = len(left_list)
        if len_left_list <= 0:  # no char matched
            return False

        left_index = 0
        left_subs = left_list[left_index]  # the left index of current slide window
        if (len_s2 - left_subs) < len_s1:
            return False  # the rest length is less than len_s1, so it's not possible to match s1's permutation
        dict_s1[s2[left_subs]] -= 1

        match_counter = 1  # if matched_counter == len_s1, bingo, return True
        right_subs = left_subs + 1  # the right index of current slide window
        while right_subs < len_s2:
            if s2[right_subs] in dict_s1:  # this char is in s1
                if dict_s1[s2[right_subs]] > 0:  # this char is in s1 and can be matched, so keep moving right (expand)
                    dict_s1[s2[right_subs]] -= 1
                    match_counter += 1  # increase match_counter (expand)
                    if match_counter == len_s1:
                        return True
                    else:
                        right_subs += 1  # keep moving
                else:  # this char is in s1 but cannot be matched, so move left (shrink & slide)
                    left_index += 1
                    if left_index >= len_left_list:  # no next left_subs
                        return False
                    next_left_subs = left_list[left_index]
                    if (len_s2 - next_left_subs) < len_s1:  # out of length limit
                        return False
                    assert next_left_subs == left_subs + 1
                    dict_s1[s2[left_subs]] += 1  # recover
                    match_counter -= 1  # decrease match_counter (shrink)
                    left_subs = next_left_subs  # move left_subs to next matchable char
                    if left_subs < right_subs:
                        # don't move right_subs, try match that char again, since one char has been released just now
                        pass
                    elif left_subs == right_subs:
                        dict_s1[s2[left_subs]] -= 1  # match left
                        match_counter += 1  # increase match_counter (expand)
                        right_subs += 1
                    else:
                        assert False  # error
            else:  # this char is not in s1, so it can never be matched, so move left (shrink & slide) to skip this char
                while left_subs < right_subs:  # recover all chars in s2[left_subs: right_subs]
                    assert s2[left_subs] in dict_s1
                    dict_s1[s2[left_subs]] += 1
                    left_subs += 1
                while left_list[left_index] <= right_subs:  # move next left_subs to the right side of right_subs
                    left_index += 1
                    if left_index >= len_left_list:  # no next left_subs
                        return False
                    if (len_s2 - left_list[left_index]) < len_s1:  # out of length limit
                        return False
                left_subs = left_list[left_index]
                dict_s1[s2[left_subs]] -= 1
                match_counter = 1  # reset match_counter (shrink)
                right_subs = left_subs + 1

        return False


def main():
    # Example 1: Output: true
    # s1 = "ab"
    # s2 = "eidbaooo"

    # Example 2: Output: false
    # s1 = "ab"
    # s2 = "eidboaoo"

    # Example 3: Output: true
    # s1 = "adc"
    # s2 = "dcda"

    # Example 4: Output: false
    # s1 = "hello"
    # s2 = "ooolleoooleh"

    # Example 5: Output: true
    s1 = "trinitrophenylmethylnitramine"
    s2 = "dinitrophenylhydrazinetrinitrophenylmethylnitramine"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.checkInclusion(s1, s2)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
