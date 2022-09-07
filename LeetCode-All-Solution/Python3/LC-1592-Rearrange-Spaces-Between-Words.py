#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1592-Rearrange-Spaces-Between-Words.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-09-07
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 1592 - (Easy) - Rearrange Spaces Between Words
https://leetcode.com/problems/rearrange-spaces-between-words/

Description & Requirement:
    You are given a string text of words that are placed among some number of spaces. 
    Each word consists of one or more lowercase English letters and are separated by at least one space. 
    It's guaranteed that text contains at least one word.

    Rearrange the spaces so that there is an equal number of spaces between every pair of adjacent words 
    and that number is maximized. If you cannot redistribute all the spaces equally, place the extra spaces at the end, 
    meaning the returned string should be the same length as text.

    Return the string after rearranging the spaces.

Example 1:
    Input: text = "  this   is  a sentence "
    Output: "this   is   a   sentence"
    Explanation: There are a total of 9 spaces and 4 words. 
        We can evenly divide the 9 spaces between the words: 9 / (4-1) = 3 spaces.
Example 2:
    Input: text = " practice   makes   perfect"
    Output: "practice   makes   perfect "
    Explanation: There are a total of 7 spaces and 3 words. 7 / (3-1) = 3 spaces plus 1 extra space. 
        We place this extra space at the end of the string.

Constraints:
    1 <= text.length <= 100
    text consists of lowercase English letters and ' '.
    text contains at least one word.
"""


class Solution:
    def reorderSpaces(self, text: str) -> str:
        # exception case
        assert isinstance(text, str) and len(text) >= 1
        # main method: (integer divide)
        return self._reorderSpaces(text)

    def _reorderSpaces(self, text: str) -> str:
        """
        Runtime: 33 ms, faster than 90.59% of Python3 online submissions for Rearrange Spaces Between Words.
        Memory Usage: 13.9 MB, less than 16.35% of Python3 online submissions for Rearrange Spaces Between Words.
        """
        assert isinstance(text, str) and len(text) >= 1
        n = len(text)

        space_counter = 0
        word_list = []
        idx = 0
        while idx < n:
            if text[idx] == " ":
                space_counter += 1
                idx += 1
            else:
                cur_word = ""
                while idx < n and text[idx] != " ":
                    cur_word += text[idx]
                    idx += 1
                word_list.append(cur_word)

        if len(word_list) == 0:
            return " " * space_counter if space_counter > 0 else ""
        if len(word_list) == 1:
            return word_list[0] + (" " * space_counter) if space_counter > 0 else word_list[0]

        gap_counter = len(word_list) - 1
        gap_space, rest_space = divmod(space_counter, gap_counter)

        res = word_list[0]
        for word in word_list[1:]:
            res += " " * gap_space
            res += word
        if rest_space > 0:
            res += " " * rest_space

        return res


def main():
    # Example 1: Output: "this   is   a   sentence"
    # text = "  this   is  a sentence "

    # Example 2: Output: "practice   makes   perfect "
    text = " practice   makes   perfect"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.reorderSpaces(text)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
