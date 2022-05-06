#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1209-Remove-All-Adjacent-Duplicates-in-String-II.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-05-06
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 1209 - (Medium) - Remove All Adjacent Duplicates in String II
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

Description & Requirement:
    You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters 
    from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

    We repeatedly make k duplicate removals on s until we no longer can.

    Return the final string after all such duplicate removals have been made.
     It is guaranteed that the answer is unique.

Example 1:
    Input: s = "abcd", k = 2
    Output: "abcd"
    Explanation: There's nothing to delete.
Example 2:
    Input: s = "deeedbbcccbdaa", k = 3
    Output: "aa"
    Explanation: 
        First delete "eee" and "ccc", get "ddbbbdaa"
        Then delete "bbb", get "dddaa"
        Finally delete "ddd", get "aa"
Example 3:
    Input: s = "pbbcggttciiippooaais", k = 2
    Output: "ps"

Constraints:
    1 <= s.length <= 10^5
    2 <= k <= 10^4
    s only contains lower case English letters.
"""


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # exception case
        assert isinstance(s, str) and len(s) >= 1
        assert isinstance(k, int) and k >= 2
        # main method: (stack, pop the top k items if stack[-k] == ... == stack[-1])
        return self._removeDuplicates(s, k)

    def _removeDuplicates(self, s: str, k: int) -> str:
        assert isinstance(s, str) and len(s) >= 1
        assert isinstance(k, int) and k >= 2
        len_s = len(s)
        if len_s == 1:
            return s

        stack = []  # item: [char, consecutive_counter]
        for idx, ch in enumerate(s):
            if len(stack) == 0:
                stack.append([ch, 1])
            else:
                if ch == stack[-1][0]:
                    new_counter = stack[-1][1] + 1
                    if new_counter == k:  # if append the current char, there will be k consecutive chars in the stack
                        for _ in range(k - 1):  # pop top (k-1) chars in the stack
                            stack.pop()
                    else:
                        stack.append([ch, new_counter])
                else:
                    stack.append([ch, 1])

        return "".join([item[0] for item in stack])


def main():
    # Example 1: Output: "abcd"
    s = "abcd"
    k = 2

    # Example 2: Output: "aa"
    # s = "deeedbbcccbdaa"
    # k = 3

    # Example 3: Output: "ps"
    # s = "pbbcggttciiippooaais"
    # k = 2

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.removeDuplicates(s, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
