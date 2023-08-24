#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0068-Text-Justification.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-08-24
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools
# import itertools

"""
LeetCode - 0068 - (Hard) Text Justification
https://leetcode.com/problems/text-justification/

Description & Requirement:
    Given an array of strings words and a width maxWidth, format the text such that 
    each line has exactly maxWidth characters and is fully (left and right) justified.

    You should pack your words in a greedy approach; that is, 
    pack as many words as you can in each line. Pad extra spaces ' ' when necessary 
    so that each line has exactly maxWidth characters.

    Extra spaces between words should be distributed as evenly as possible. 
    If the number of spaces on a line does not divide evenly between words, 
    the empty slots on the left will be assigned more spaces than the slots on the right.

    For the last line of text, it should be left-justified, 
    and no extra space is inserted between words.

    Note:
        A word is defined as a character sequence consisting of non-space characters only.
        Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
        The input array words contains at least one word.

Example 1:
    Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
    Output:
        [
           "This    is    an",
           "example  of text",
           "justification.  "
        ]
Example 2:
    Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
    Output:
        [
          "What   must   be",
          "acknowledgment  ",
          "shall be        "
        ]
    Explanation: Note that the last line is "shall be    " instead of "shall     be", 
        because the last line must be left-justified instead of fully-justified.
        Note that the second line is also left-justified because it contains only one word.
Example 3:
    Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to",
        "a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
    Output:
        [
          "Science  is  what we",
          "understand      well",
          "enough to explain to",
          "a  computer.  Art is",
          "everything  else  we",
          "do                  "
        ]

Constraints:
    1 <= words.length <= 300
    1 <= words[i].length <= 20
    words[i] consists of only English letters and symbols.
    1 <= maxWidth <= 100
    words[i].length <= maxWidth
"""


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # exception case
        assert isinstance(words, list) and len(words) >= 1
        assert isinstance(maxWidth, int) and maxWidth >= 1
        # main method: (simulation)
        return self._fullJustify(words, maxWidth)

    def _fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        assert isinstance(words, list) and len(words) >= 1
        assert isinstance(maxWidth, int) and maxWidth >= 1

        res = []
        right, n = 0, len(words)

        def blank(num: int) -> str:
            return ' ' * num

        while True:
            left = right
            sum_len = 0
            while right < n and sum_len + len(words[right]) + right - left <= maxWidth:
                sum_len += len(words[right])
                right += 1

            if right == n:
                s = " ".join(words[left:])
                res.append(s + blank(maxWidth - len(s)))
                break

            num_words = right - left
            num_spaces = maxWidth - sum_len

            if num_words == 1:
                res.append(words[left] + blank(num_spaces))
                continue

            avg_spaces = num_spaces // (num_words - 1)
            extra_spaces = num_spaces % (num_words - 1)
            s1 = blank(avg_spaces + 1).join(words[left: left + extra_spaces + 1])
            s2 = blank(avg_spaces).join(words[left + extra_spaces + 1: right])

            res.append(s1 + blank(avg_spaces) + s2)

        return res


def main():
    # Example 1: Output:
    #     [
    #         "This    is    an",
    #         "example  of text",
    #         "justification.  "
    #     ]
    # words = ["This", "is", "an", "example", "of", "text", "justification."]
    # maxWidth = 16

    # Example 2: Output:
    #     [
    #         "What   must   be",
    #         "acknowledgment  ",
    #         "shall be        "
    #     ]
    # words = ["What", "must", "be", "acknowledgment", "shall", "be"]
    # maxWidth = 16

    # Example 3: Output:
    #     [
    #         "Science  is  what we",
    #         "understand      well",
    #          "enough to explain to",
    #          "a  computer.  Art is",
    #          "everything  else  we",
    #          "do                  "
    #     ]
    words = ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.",
             "Art", "is", "everything", "else", "we", "do"]
    maxWidth = 20

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.fullJustify(words, maxWidth)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
