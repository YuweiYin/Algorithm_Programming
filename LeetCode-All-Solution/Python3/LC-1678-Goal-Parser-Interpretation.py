#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1678-Goal-Parser-Interpretation.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-11-06
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 1678 - (Easy) - Goal Parser Interpretation
https://leetcode.com/problems/goal-parser-interpretation/

Description & Requirement:
    You own a Goal Parser that can interpret a string command. 
    The command consists of an alphabet of "G", "()" and/or "(al)" in some order. 
    The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". 
    The interpreted strings are then concatenated in the original order.

    Given the string command, return the Goal Parser's interpretation of command.

Example 1:
    Input: command = "G()(al)"
    Output: "Goal"
    Explanation: The Goal Parser interprets the command as follows:
        G -> G
        () -> o
        (al) -> al
        The final concatenated result is "Goal".
Example 2:
    Input: command = "G()()()()(al)"
    Output: "Gooooal"
Example 3:
    Input: command = "(al)G(al)()()G"
    Output: "alGalooG"

Constraints:
    1 <= command.length <= 100
    command consists of "G", "()", and/or "(al)" in some order.
"""


class Solution:
    def interpret(self, command: str) -> str:
        # exception case
        assert isinstance(command, str) and len(command) >= 1
        # main method: (replace substrings)
        return self._interpret(command)

    def _interpret(self, command: str) -> str:
        assert isinstance(command, str) and len(command) >= 1

        return command.replace("()", "o").replace("(al)", "al")


def main():
    # Example 1: Output: "Goal"
    # command = "G()(al)"

    # Example 2: Output: "Gooooal"
    command = "G()()()()(al)"

    # Example 3: Output: "alGalooG"
    # command = "(al)G(al)()()G"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.interpret(command)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
