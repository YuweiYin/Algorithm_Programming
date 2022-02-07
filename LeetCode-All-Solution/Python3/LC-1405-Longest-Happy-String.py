#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1405-Longest-Happy-String.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-07
=================================================================="""

import sys
import time
# from typing import List
# import collections

"""
LeetCode - 1405 - (Medium) - Longest Happy String
https://leetcode.com/problems/longest-happy-string/

Description & Requirement:
    A string s is called happy if it satisfies the following conditions:
        s only contains the letters 'a', 'b', and 'c'.
        s does not contain any of "aaa", "bbb", or "ccc" as a substring.
        s contains at most a occurrences of the letter 'a'.
        s contains at most b occurrences of the letter 'b'.
        s contains at most c occurrences of the letter 'c'.
    Given three integers a, b, and c, return the longest possible happy string. 
    If there are multiple longest happy strings, return any of them. 
    If there is no such string, return the empty string "".

    A substring is a contiguous sequence of characters within a string.

Example 1:
    Input: a = 1, b = 1, c = 7
    Output: "ccaccbcc"
    Explanation: "ccbccacc" would also be a correct answer.
Example 2:
    Input: a = 7, b = 1, c = 0
    Output: "aabaa"
    Explanation: It is the only correct answer in this case.

Constraints:
    0 <= a, b, c <= 100
    a + b + c > 0
"""


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # exception case
        if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
            return ""  # Error input type
        if not (a >= 0 and b >= 0 and c >= 0):
            return ""  # Error input type
        # main method: (Greedy: each step, choose the max rest one char (a xor b xor c))
        return self._longestDiverseString(a, b, c)

    def _longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ""
        char_counter = [["a", a], ["b", b], ["c", c]]  # each loop, sort this list to find max, mid, min chars

        while char_counter[0][1] > 0 or char_counter[1][1] > 0 or char_counter[2][1] > 0:
            # select the char (a xor b xor c) that remains the most
            char_counter.sort(key=lambda x: -x[1])  # sort by a, b, c in descending order

            # choose only one char (one time) to add to res string
            have_choice = False
            for idx, c_c in enumerate(char_counter):
                char, counter = c_c
                if counter <= 0:  # the max rest one is 0, break the loop
                    break
                if len(res) >= 2 and res[-2] == res[-1] == char:  # check if 3 same chars are adjacent
                    continue  # if it is, then choose the second max rest one char
                # now, there's a char to choose
                have_choice = True
                res += char
                char_counter[idx][1] -= 1
                break
            # if there's no choice in a loop, then there'll never be a choice in the future, just break the loop
            if not have_choice:
                break

        return res


def main():
    # Example 1: Output: "ccaccbcc"
    # a = 1
    # b = 1
    # c = 7

    # Example 2: Output: "aabaa"
    # a = 7
    # b = 1
    # c = 0

    # Example 3: Output: "ccbccbbccbbccbbccbc"
    a = 0
    b = 8
    c = 11

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.longestDiverseString(a, b, c)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
