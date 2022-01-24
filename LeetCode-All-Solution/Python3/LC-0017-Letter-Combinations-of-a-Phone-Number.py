#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0017-Letter-Combinations-of-a-Phone-Number.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-24
=================================================================="""

import sys
import time
from typing import List
# import collections

"""
LeetCode - 0017 - (Medium) - Letter Combinations of a Phone Number
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Description & Requirement:
    Given a string containing digits from 2-9 inclusive, 
    return all possible letter combinations that the number could represent. 
    Return the answer in any order.

    A mapping of digit to letters (just like on the telephone buttons) is given below. 
    Note that 1 does not map to any letters.
        1 -> 
        2 -> a, b, c
        3 -> d, e, f
        4 -> g, h, i
        5 -> j, k, l
        6 -> m, n, o
        7 -> p, q, r, s
        8 -> t, u, v
        9 -> w, x, y, z

Example 1:
    Input: digits = "23"
    Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:
    Input: digits = ""
    Output: []
Example 3:
    Input: digits = "2"
    Output: ["a","b","c"]

Constraints:
    0 <= digits.length <= 4
    digits[i] is a digit in the range ['2', '9'].

"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # exception case
        if not isinstance(digits, str) or len(digits) <= 0:
            return []  # Error input type
        # main method: (Descartes product. dfs & backtrace.)
        return self._letterCombinations(digits)

    def _letterCombinations(self, digits: str) -> List[str]:
        """
        Runtime: 24 ms, faster than 97.15% of Python3 online submissions for Letter Combinations of a Phone Number.
        Memory Usage: 14.5 MB, less than 5.10% of Python3 online submissions for Letter Combinations of a Phone Number.
        """
        len_digits = len(digits)
        assert len_digits > 0

        digit2letter = dict({
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        })

        for digit in digits:
            assert digit in digit2letter

        res_list = []

        def __dfs(cur_combo: List[str], cur_digit_index: int):
            if len(cur_combo) == len_digits:
                res_list.append("".join(cur_combo[:]))
                return
            for next_letter in digit2letter[digits[cur_digit_index]]:
                cur_combo.append(next_letter)
                __dfs(cur_combo, cur_digit_index + 1)  # go deeper
                cur_combo.pop()  # backtrace

        for start_letter in digit2letter[digits[0]]:  # start from every letter that the first digit maps to
            __dfs([start_letter], 1)
        return res_list


def main():
    # Example 1: Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    digits = "23"

    # Example 2: Output: []
    # digits = ""

    # Example 3: Output: ["a","b","c"]
    # digits = "2"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.letterCombinations(digits)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
