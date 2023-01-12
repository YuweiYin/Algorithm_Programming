#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1807-Evaluate-the-Bracket-Pairs-of-a-String.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-01-12
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1807 - (Medium) - Evaluate the Bracket Pairs of a String
https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/

Description & Requirement:
    You are given a string s that contains some bracket pairs, with each pair containing a non-empty key.
    
        For example, in the string "(name)is(age)yearsold", 
        there are two bracket pairs that contain the keys "name" and "age".

    You know the values of a wide range of keys. This is represented by a 2D string array knowledge 
    where each knowledge[i] = [key_i, value_i] indicates that key key_i has a value of value_i.

    You are tasked to evaluate all of the bracket pairs. 
    When you evaluate a bracket pair that contains some key key_i, you will:

        Replace key_i and the bracket pair with the key's corresponding value_i.
        If you do not know the value of the key, you will replace key_i and the bracket pair with a question mark "?" 
            (without the quotation marks).

    Each key will appear at most once in your knowledge. There will not be any nested brackets in s.

    Return the resulting string after evaluating all of the bracket pairs.

Example 1:
    Input: s = "(name)is(age)yearsold", knowledge = [["name","bob"],["age","two"]]
    Output: "bobistwoyearsold"
    Explanation:
        The key "name" has a value of "bob", so replace "(name)" with "bob".
        The key "age" has a value of "two", so replace "(age)" with "two".
Example 2:
    Input: s = "hi(name)", knowledge = [["a","b"]]
    Output: "hi?"
    Explanation: As you do not know the value of the key "name", replace "(name)" with "?".
Example 3:
    Input: s = "(a)(a)(a)aaa", knowledge = [["a","yes"]]
    Output: "yesyesyesaaa"
    Explanation: The same key can appear multiple times.
        The key "a" has a value of "yes", so replace all occurrences of "(a)" with "yes".
        Notice that the "a"s not in a bracket pair are not evaluated.

Constraints:
    1 <= s.length <= 10^5
    0 <= knowledge.length <= 10^5
    knowledge[i].length == 2
    1 <= key_i.length, value_i.length <= 10
    s consists of lowercase English letters and round brackets '(' and ')'.
    Every open bracket '(' in s will have a corresponding close bracket ')'.
    The key in each bracket pair of s will be non-empty.
    There will not be any nested bracket pairs in s.
    key_i and value_i consist of lowercase English letters.
    Each key_i in knowledge is unique.
"""


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        # exception case
        assert isinstance(s, str) and len(s) >= 1
        assert isinstance(knowledge, list) and len(knowledge) >= 0
        # main method: (hash dict)
        return self._evaluate(s, knowledge)

    def _evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        assert isinstance(s, str) and len(s) >= 1
        assert isinstance(knowledge, list) and len(knowledge) >= 0

        k_dict = dict({})
        for k in knowledge:
            k_dict[k[0]] = k[1]

        res, start = [], -1
        for idx, ch in enumerate(s):
            if ch == '(':
                start = idx
            elif ch == ')':
                res.append(k_dict.get(s[start + 1: idx], '?'))
                start = -1
            elif start < 0:
                res.append(ch)

        return "".join(res)


def main():
    # Example 1: Output: "bobistwoyearsold"
    # s = "(name)is(age)yearsold"
    # knowledge = [["name", "bob"], ["age", "two"]]

    # Example 2: Output: "hi?"
    # s = "hi(name)"
    # knowledge = [["a", "b"]]

    # Example 3: Output: "yesyesyesaaa"
    s = "(a)(a)(a)aaa"
    knowledge = [["a", "yes"]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.evaluate(s, knowledge)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
