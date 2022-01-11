#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0784-Letter-Case-Permutation.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-11
=================================================================="""

import sys
import time
from typing import List

"""
LeetCode - 0784 - (Medium) - Letter Case Permutation
https://leetcode.com/problems/letter-case-permutation/

Description & Requirement:
    Given a string s, you can transform every letter individually 
    to be lowercase or uppercase to create another string.

    Return a list of all possible strings we could create. 
    Return the output in any order.

Example 1:
    Input: s = "a1b2"
    Output: ["a1b2","a1B2","A1b2","A1B2"]
Example 2:
    Input: s = "3z4"
    Output: ["3z4","3Z4"]

Constraints:
    1 <= s.length <= 12
    s consists of lowercase English letters, uppercase English letters, and digits.
"""


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        # exception case
        if not isinstance(s, str) or len(s) <= 0 or not s.isalnum():
            return []  # Error input type
        if s.isdigit():  # only digits
            return [s]
        # main method: (dfs (needn't backtrack))
        return self._letterCasePermutation(s)

    def _letterCasePermutation(self, s: str) -> List[str]:
        res_permute = []  # stack
        len_s = len(s)

        def __dfs(cur_permute: str, cur_index: int):
            if len(cur_permute) == len_s:  # end of recursion
                res_permute.append(cur_permute[:])
                return

            cur_char = s[cur_index]
            if cur_char.isdigit():  # if cur_char is a digit, just add it
                __dfs(cur_permute + cur_char, cur_index + 1)  # dfs
            elif cur_char.isalpha():  # if cur_char is an English letter, add its lowercase or uppercase
                __dfs(cur_permute + cur_char.lower(), cur_index + 1)  # dfs lowercase letter
                __dfs(cur_permute + cur_char.upper(), cur_index + 1)  # dfs uppercase letter

        permute = ""
        start_index = 0
        __dfs(permute, start_index)

        return res_permute


def main():
    # Example 1: Output: ["a1b2","a1B2","A1b2","A1B2"]
    # s = "a1b2"

    # Example 2: Output: ["3z4","3Z4"]
    s = "3z4"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.letterCasePermutation(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
