#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2047-Number-of-Valid-Words-in-a-Sentence.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-27
=================================================================="""

import sys
import time
# from typing import List
# import collections

"""
LeetCode - 2047 - (Easy) - Number of Valid Words in a Sentence
https://leetcode.com/problems/number-of-valid-words-in-a-sentence/

Description & Requirement:
    A sentence consists of lowercase letters ('a' to 'z'), digits ('0' to '9'), 
    hyphens ('-'), punctuation marks ('!', '.', and ','), and spaces (' ') only. 
    Each sentence can be broken down into one or more tokens separated by one or more spaces ' '.

    A token is a valid word if all three of the following are true:
        It only contains lowercase letters, hyphens, and/or punctuation (no digits).
        There is at most one hyphen '-'. If present, it must be surrounded by lowercase characters 
            ("a-b" is valid, but "-ab" and "ab-" are not valid).
        There is at most one punctuation mark. If present, it must be at the end of the token 
            ("ab,", "cd!", and "." are valid, but "a!b" and "c.," are not valid).
    Examples of valid words include "a-b.", "afad", "ba-c", "a!", and "!".

    Given a string sentence, return the number of valid words in sentence.

Example 1:
    Input: sentence = "cat and  dog"
    Output: 3
    Explanation: The valid words in the sentence are "cat", "and", and "dog".
Example 2:
    Input: sentence = "!this  1-s b8d!"
    Output: 0
    Explanation: There are no valid words in the sentence.
        "!this" is invalid because it starts with a punctuation mark.
        "1-s" and "b8d" are invalid because they contain digits.
Example 3:
    Input: sentence = "alice and  bob are playing stone-game10"
    Output: 5
    Explanation: The valid words in the sentence are "alice", "and", "bob", "are", and "playing".
        "stone-game10" is invalid because it contains digits.

Constraints:
    1 <= sentence.length <= 1000
    sentence only contains lowercase English letters, digits, ' ', '-', '!', '.', and ','.
    There will be at least 1 token.
"""


class Solution:
    def countValidWords(self, sentence: str) -> int:
        # exception case
        if not isinstance(sentence, str) or len(sentence) <= 0:
            return 0  # Error input type
        # main method: (easy rules)
        return self._countValidWords(sentence)

    def _countValidWords(self, sentence: str) -> int:
        """
        Runtime: 44 ms, faster than 79.77% of Python3 online submissions for Number of Valid Words in a Sentence.
        Memory Usage: 14 MB, less than 99.02% of Python3 online submissions for Number of Valid Words in a Sentence.
        """
        assert len(sentence) > 0
        word_list = sentence.strip().split()  # get word list, split by " " or consecutive " "

        # hyphens = {"-"}
        punctuation_marks = {"!", ".", ","}

        def __check_word(word: str) -> bool:
            if len(word) <= 0:  # empty, not valid
                return False
            if len(word) == 1:  # only one char, either is a lower letter or a punctuation mark
                return True if word.islower() or word in punctuation_marks else False
            if not word[0].islower():  # the first char must be a lower letter
                return False
            if word[-1] == "-":  # the last char can't be a hyphen
                return False
            if word[-1] in punctuation_marks:  # remove the last punctuation mark
                word = word[:-1]
            # find hyphens
            hyphen_counter = 0
            for idx, char in enumerate(word):
                if char == "-":
                    if not (idx - 1 >= 0 and idx + 1 < len(word) and
                            word[idx - 1].islower() and word[idx + 1].islower()):
                        return False  # hyphen "-" must be surrounded by lower letters
                    hyphen_counter += 1
                    if hyphen_counter > 1:  # only one hyphen
                        return False
                else:
                    if not char.islower():  # apart from hyphen, the inner part must be a lower letter
                        return False
            return True

        valid_counter = 0
        for w in word_list:
            if __check_word(w):  # check each word
                valid_counter += 1

        return valid_counter


def main():
    # Example 1: Output: 3
    # sentence = "cat and  dog"

    # Example 2: Output: 0
    # sentence = "!this  1-s b8d!"

    # Example 3: Output: 5
    # sentence = "alice and  bob are playing stone-game10"

    # Example 4: Output: 49
    sentence = " 62   nvtk0wr4f  8 qt3r! w1ph 1l ,e0d 0n 2v 7c.  n06huu2n9 s9   ui4 nsr!d7olr  q-, " \
               "vqdo!btpmtmui.bb83lf g .!v9-lg 2fyoykex uy5a 8v whvu8 .y sc5 -0n4 zo pfgju 5u 4 3x,3!wl  fv4   s  " \
               "aig cf j1 a i  8m5o1  !u n!.1tz87d3 .9    n a3  .xb1p9f  b1i a j8s2 cugf l494cx1! hisceovf3 8d93 sg " \
               "4r.f1z9w   4- cb r97jo hln3s h2 o .  8dx08as7l!mcmc isa49afk i1 fk,s e !1 ln rt2vhu 4ks4zq c w  o- " \
               "6  5!.n8ten0 6mk 2k2y3e335,yj  h p3 5 -0  5g1c  tr49, ,qp9 -v p  7p4v110926wwr h x wklq u zo 16. !8  " \
               "u63n0c l3 yckifu 1cgz t.i   lh w xa l,jt   hpi ng-gvtk8 9 j u9qfcd!2  kyu42v dmv.cst6i5fo rxhw4wvp2 " \
               "1 okc8!  z aribcam0  cp-zp,!e x  agj-gb3 !om3934 k vnuo056h g7 t-6j! 8w8fncebuj-lq    inzqhw v39,  " \
               "f e 9. 50 , ru3r  mbuab  6  wz dw79.av2xp . gbmy gc s6pi pra4fo9fwq k   j-ppy -3vpf   o k4hy3 -!..5s " \
               ",2 k5 j p38dtd   !i   b!fgj,nx qgif "

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.countValidWords(sentence)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
