#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0038-Count-and-Say.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-08-31
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 0038 - (Medium) - Count and Say
https://leetcode.com/problems/count-and-say/

Description & Requirement:
    The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
        countAndSay(1) = "1"
        countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), 
            which is then converted into a different digit string.

    To determine how you "say" a digit string, split it into the minimal number of substrings such that 
    each substring contains exactly one unique digit. Then for each substring, say the number of digits, 
    then say the digit. Finally, concatenate every said digit.

    For example, the saying and conversion for digit string "3322251":

    Given a positive integer n, return the nth term of the count-and-say sequence.

Example 1:
    Input: n = 1
    Output: "1"
    Explanation: This is the base case.
Example 2:
    Input: n = 4
    Output: "1211"
    Explanation:
        countAndSay(1) = "1"
        countAndSay(2) = say "1" = one 1 = "11"
        countAndSay(3) = say "11" = two 1's = "21"
        countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"

Constraints:
    1 <= n <= 30
"""


class Solution:
    def countAndSay(self, n: int) -> str:
        # exception case
        assert isinstance(n, int) and n >= 1
        # main method: (recursion)
        return self._countAndSay(n)

    def _countAndSay(self, n: int) -> str:
        """
        Runtime: 64 ms, faster than 67.37% of Python3 online submissions for Count and Say.
        Memory Usage: 13.8 MB, less than 86.23% of Python3 online submissions for Count and Say.
        """
        assert isinstance(n, int) and n >= 1

        res = "1"
        for _ in range(n - 1):
            cur = ""
            start = 0
            end = 0
            len_res = len(res)

            while end < len_res:
                while end < len_res and res[end] == res[start]:
                    end += 1
                cur += str(end - start) + res[start]
                start = end
            res = cur

        return res


def main():
    # Example 1: Output: "1"
    # n = 1

    # Example 2: Output: "1211"
    n = 4

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.countAndSay(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
