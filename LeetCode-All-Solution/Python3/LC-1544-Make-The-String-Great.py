#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1544-Make-The-String-Great.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-11-08
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 1544 - (Easy) - Make The String Great
https://leetcode.com/problems/make-the-string-great/

Description & Requirement:
    Given a string s of lower and upper case English letters.

    A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:
        0 <= i <= s.length - 2
        s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.

    To make the string good, you can choose two adjacent characters that make the string bad and remove them. 
    You can keep doing this until the string becomes good.

    Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

    Notice that an empty string is also good.

Example 1:
    Input: s = "leEeetcode"
    Output: "leetcode"
    Explanation: In the first step, either you choose i = 1 or i = 2, 
        both will result "leEeetcode" to be reduced to "leetcode".
Example 2:
    Input: s = "abBAcC"
    Output: ""
    Explanation: We have many possible scenarios, and all lead to the same answer. For example:
        "abBAcC" --> "aAcC" --> "cC" --> ""
        "abBAcC" --> "abBA" --> "aA" --> ""
Example 3:
    Input: s = "s"
    Output: "s"

Constraints:
    1 <= s.length <= 100
    s contains only lower and upper case English letters.
"""


class Solution:
    def makeGood(self, s: str) -> str:
        # exception case
        assert isinstance(s, str) and len(s) >= 1
        # main method: (stack)
        return self._makeGood(s)

    def _makeGood(self, s: str) -> str:
        assert isinstance(s, str) and len(s) >= 1

        def __is_bad(ch_1: str, ch_2: str) -> bool:
            return len(ch_1) == len(ch_2) == 1 and ch_1.lower() == ch_2.lower() and ch_1 != ch_2

        stack = []
        for ch in s:
            if len(stack) == 0:
                stack.append(ch)
            else:
                if __is_bad(stack[-1], ch):
                    stack.pop()
                else:
                    stack.append(ch)

        return "".join(stack) if len(stack) > 0 else ""


def main():
    # Example 1: Output: "leetcode"
    s = "leEeetcode"

    # Example 2: Output: ""
    # s = "abBAcC"

    # Example 3: Output: "s"
    # s = "s"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.makeGood(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
