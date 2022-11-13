#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0151-Reverse-Words-in-a-String.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-11-13
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 0151 - (Medium) - Reverse Words in a String
https://leetcode.com/problems/reverse-words-in-a-string/

Description & Requirement:
    Given an input string s, reverse the order of the words.

    A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

    Return a string of the words in reverse order concatenated by a single space.

    Note that s may contain leading or trailing spaces or multiple spaces between two words. 
    The returned string should only have a single space separating the words. Do not include any extra spaces.

Example 1:
    Input: s = "the sky is blue"
    Output: "blue is sky the"
Example 2:
    Input: s = "  hello world  "
    Output: "world hello"
    Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:
    Input: s = "a good   example"
    Output: "example good a"
    Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

Constraints:
    1 <= s.length <= 10^4
    s contains English letters (upper-case and lower-case), digits, and spaces ' '.
    There is at least one word in s.

Follow-up:
    If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        # exception case
        assert isinstance(s, str) and len(s) >= 1
        # main method: (just split and reverse the original string)
        return self._reverseWords(s)

    def _reverseWords(self, s: str) -> str:
        assert isinstance(s, str) and len(s) >= 1

        return " ".join(reversed(s.strip().split()))


def main():
    # Example 1: Output: "blue is sky the"
    # s = "the sky is blue"

    # Example 2: Output: "world hello"
    # s = "  hello world  "

    # Example 3: Output: "example good a"
    s = "a good   example"

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
