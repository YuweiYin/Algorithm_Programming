#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0917-Reverse-Only-Letters.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-23
=================================================================="""

import sys
import time
# from typing import List
# import collections

"""
LeetCode - 0917 - (Easy) - Reverse Only Letters
https://leetcode.com/problems/reverse-only-letters/

Description & Requirement:
    Given a string s, reverse the string according to the following rules:
        All the characters that are not English letters remain in the same position.
        All the English letters (lowercase or uppercase) should be reversed.

    Return s after reversing it.

Example 1:
    Input: s = "ab-cd"
    Output: "dc-ba"
Example 2:
    Input: s = "a-bC-dEf-ghIj"
    Output: "j-Ih-gfE-dCba"
Example 3:
    Input: s = "Test1ng-Leet=code-Q!"
    Output: "Qedo1ct-eeLg=ntse-T!"

Constraints:
    1 <= s.length <= 100
    s consists of characters with ASCII values in the range [33, 122].
    s does not contain '\"' or '\\'.
"""


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        # exception case
        if not isinstance(s, str) or len(s) <= 0:
            return ""  # Error input type
        # main method: (record the mapping of non-English letter chars and their indices in original string s)
        return self._reverseOnlyLetters(s)

    def _reverseOnlyLetters(self, s: str) -> str:
        len_s = len(s)
        assert len_s >= 1

        # ord_lower_a = ord("a")
        # ord_lower_z = ord("z")
        # ord_upper_a = ord("A")
        # ord_upper_z = ord("Z")

        def __reverse_list(origin_list: list):
            left_idx, right_idx = 0, len(origin_list) - 1
            while left_idx < right_idx:
                origin_list[left_idx], origin_list[right_idx] = origin_list[right_idx], origin_list[left_idx]
                left_idx += 1
                right_idx -= 1

        non_eng_map = dict({})
        eng_list = []
        for idx, char in enumerate(s):
            # if not (ord_lower_a <= ord(char) <= ord_lower_z or ord_upper_a <= ord(char) <= ord_upper_z):
            if char.isalpha():
                eng_list.append(char)
            else:
                non_eng_map[idx] = char

        # do reversion
        __reverse_list(eng_list)

        res_s_list = ["" for _ in range(len_s)]

        # put in non-English letter chars first
        for idx, char in non_eng_map.items():
            res_s_list[idx] = char
        # then put in reversed eng_list
        s_idx = 0
        eng_idx = 0
        while s_idx < len_s:
            if res_s_list[s_idx] == "":
                res_s_list[s_idx] = eng_list[eng_idx]
                eng_idx += 1
                s_idx += 1
            else:  # skip the current non-English letter char
                s_idx += 1

        return "".join(res_s_list)


def main():
    # Example 1: Output: "dc-ba"
    # s = "ab-cd"

    # Example 2: Output: "j-Ih-gfE-dCba"
    # s = "a-bC-dEf-ghIj"

    # Example 3: Output: "Qedo1ct-eeLg=ntse-T!"
    s = "Test1ng-Leet=code-Q!"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.reverseOnlyLetters(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
