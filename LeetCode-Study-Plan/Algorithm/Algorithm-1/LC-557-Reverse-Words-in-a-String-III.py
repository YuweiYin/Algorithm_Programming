#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/Study-Plan/Algorithm/Algorithm-1
@File    : LC-557-Reverse-Words-in-a-String-III.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-04
=================================================================="""

import sys
import time
from typing import List

"""
LeetCode - 557 - (Easy) - Reverse Words in a String III
https://leetcode.com/problems/reverse-words-in-a-string-iii/

Description & Requirement:
    Given a string s, reverse the order of characters in each word within a sentence 
    while still preserving whitespace and initial word order.

Example 1:
    Input: s = "Let's take LeetCode contest"
    Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:
    Input: s = "God Ding"
    Output: "doG gniD"

Constraints:
    1 <= s.length <= 5 * 10^4
    s contains printable ASCII characters.
    s does not contain any leading or trailing spaces.
    There is at least one word in s.
    All the words in s are separated by a single space.
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        # exception case
        if not isinstance(s, str) or len(s) <= 1:
            return s
        # main method: (1. split the str into several words; 2. reverse each word in place; 3. merge the words.)
        return self._reverseWords(s)

    def _reverseWords(self, s: str) -> str:
        s_list = s.split()  # 1. split the str into several words
        word_count = len(s_list)
        if word_count <= 0:  # exception case
            return s
        cur_word_index = 0
        while cur_word_index < word_count:
            # 2. reverse each word in place (str -> list -> rev(list) -> str)
            cur_word_str = s_list[cur_word_index]
            cur_word_list = list(cur_word_str)
            self._reverse_list_in_place(cur_word_list, 0, len(cur_word_list) - 1)
            rev_word_str = "".join(cur_word_list)
            s_list[cur_word_index] = rev_word_str
            cur_word_index += 1
        return " ".join(s_list)  # 3. merge the words.

    @staticmethod
    def _reverse_list_in_place(nums: List, start_index: int, end_index: int) -> None:
        while start_index < end_index:
            temp_num = nums[start_index]
            nums[start_index] = nums[end_index]
            nums[end_index] = temp_num
            start_index += 1
            end_index -= 1


def main():
    # Example 1: Output: "s'teL ekat edoCteeL tsetnoc"
    s = "Let's take LeetCode contest"

    # Example 2: Output: "doG gniD"
    # s = "God Ding"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.reverseWords(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
