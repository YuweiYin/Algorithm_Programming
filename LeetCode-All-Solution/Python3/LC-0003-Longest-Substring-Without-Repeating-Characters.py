#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0003-Longest-Substring-Without-Repeating-Characters.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-06
=================================================================="""
# import functools
import sys
import time
# from typing import List

"""
LeetCode - 0003 - (Medium) - Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Description & Requirement:
    Given a string s, find the length of the longest substring without repeating characters.

Example 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.
Example 2:
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.
Example 3:
    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
    0 <= s.length <= 5 * 10^4
    s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # exception case
        if not isinstance(s, str) or len(s) <= 0:
            return 0
        # border case
        if len(s) == 1:
            return 1
        if len(s) == 2:
            return 1 if s[0] == s[1] else 2
        # main method: Slide window & Two pointers
        return self._lengthOfLongestSubstring(s)

    def _lengthOfLongestSubstring(self, s: str) -> int:
        len_s = len(s)  # now, 3 <= len_s
        longest_length = 1  # default: the first char only, so 1
        current_length = 1

        # longest_length cannot be longer than the number of distinct chars in s, so the upper bound can be determined
        max_length = 0
        set_stat = set({})
        for ch in s:
            if ch not in set_stat:
                set_stat.add(ch)
                max_length += 1
        if max_length == len_s:  # all chars are distinct in s
            return max_length

        # use a dict to guarantee there's no repeated char in current substring
        dict_subs = dict({})  # key: char; value: the index of this char in the whole string
        # if a char is in the current substring, then its value of dict_subs is >= 0; else, the value is -1
        left_subs = 0  # the left index of current slide window
        dict_subs[s[left_subs]] = left_subs

        right_subs = 1  # the right index of current slide window
        while right_subs < len_s:
            if s[right_subs] in dict_subs:
                if dict_subs[s[right_subs]] >= 0:  # this char has existed in the current substring, slide window now
                    # now, s[repeated_index] == s[right_subs], so s[left_subs: repeated_index + 1] should be disregarded
                    # continue from s[repeated_index + 1: right_subs]
                    # find the repeated char by the value (index) of dict_subs, re-start from its right one
                    repeated_index = dict_subs[s[right_subs]]
                    if left_subs == repeated_index:  # the leftmost char in substring is the one that is repeated
                        dict_subs[s[right_subs]] = right_subs
                        left_subs += 1
                        right_subs += 1
                        continue  # keep the size of window and slide it by 1 step (keep current_length the same, too)
                    while left_subs < repeated_index:  # remove all char in s[left_subs: repeated_index]
                        # assert s[left_subs] in dict_subs
                        dict_subs[s[left_subs]] = -1  # remove from dict_subs
                        current_length -= 1  # (shrink) decrease current_length
                        left_subs += 1
                    # now, left_subs == repeated_index
                    left_subs += 1  # continue from s[repeated_index + 1: right_subs]
                    dict_subs[s[left_subs]] = left_subs
                    dict_subs[s[right_subs]] = right_subs  # use right_subs to replace repeated_index
                    right_subs += 1
                else:  # this char is not in the current substring, put it in
                    current_length += 1
                    longest_length = max(longest_length, current_length)
                    if longest_length == max_length:
                        return max_length
                    dict_subs[s[right_subs]] = right_subs  # put it in the dict to avoid repetition
                    right_subs += 1  # keep moving
            else:  # new char, just put it in and expand the window
                current_length += 1
                longest_length = max(longest_length, current_length)
                if longest_length == max_length:
                    return max_length
                dict_subs[s[right_subs]] = right_subs  # put it in the dict to avoid repetition
                right_subs += 1  # keep moving

        return longest_length


def main():
    # Example 1: Output: 3
    # s = "abcabcbb"

    # Example 2: Output: 1
    # s = "bbbbb"

    # Example 3: Output: 3
    # s = "pwwkew"

    # Example 4: Output: 3
    # s = "abcbacbb"

    # Example 5: Output: 6
    s = "wobgrovw"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.lengthOfLongestSubstring(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
