#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0804-Unique-Morse-Code-Words.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-10
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0804 - (Easy) - Unique Morse Code Words
https://leetcode.com/problems/unique-morse-code-words/

Description & Requirement:
    International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, 
    as follows:
        'a' maps to ".-",
        'b' maps to "-...",
        'c' maps to "-.-.", and so on.

    For convenience, the full table for the 26 letters of the English alphabet is given below:
        [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--",
        "-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

    Given an array of strings words where each word can be written as a concatenation of the Morse code of each letter.

    For example, "cab" can be written as "-.-..--...", which is the concatenation of "-.-.", ".-", and "-...". 
    We will call such a concatenation the transformation of a word.

    Return the number of different transformations among all words we have.

Example 1:
    Input: words = ["gin","zen","gig","msg"]
    Output: 2
    Explanation: The transformation of each word is:
        "gin" -> "--...-."
        "zen" -> "--...-."
        "gig" -> "--...--."
        "msg" -> "--...--."
        There are 2 different transformations: "--...-." and "--...--.".
Example 2:
    Input: words = ["a"]
    Output: 1

Constraints:
    1 <= words.length <= 100
    1 <= words[i].length <= 12
    words[i] consists of lowercase English letters.
"""


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        # exception case
        assert isinstance(words, list) and len(words) >= 1
        # main method: (convert each word into Morse code, store in a set)
        return self._uniqueMorseRepresentations(words)

    def _uniqueMorseRepresentations(self, words: List[str]) -> int:
        """
        Runtime: 35 ms, faster than 95.85% of Python3 online submissions for Unique Morse Code Words.
        Memory Usage: 13.9 MB, less than 24.27% of Python3 online submissions for Unique Morse Code Words.
        """
        len_words = len(words)
        assert len_words >= 1

        morse_code = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
            "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."
        ]
        # assert len(morse_code) == 26

        if len_words == 1:
            return 1

        res_set = set()

        ord_a = ord("a")
        # convert each word into Morse code
        for word in words:
            cur_morse = ""
            for ch in word:
                # assert ch.islower()
                cur_morse += morse_code[ord(ch) - ord_a]
            if cur_morse not in res_set:
                res_set.add(cur_morse)

        return len(res_set)


def main():
    # Example 1: Output: 2
    words = ["gin", "zen", "gig", "msg"]

    # Example 2: Output: 1
    # words = ["a"]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.uniqueMorseRepresentations(words)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
