#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0899-Orderly-Queue.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-08-03
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 0899 - (Hard) - Orderly Queue
https://leetcode.com/problems/orderly-queue/

Description & Requirement:
    You are given a string s and an integer k. 
    You can choose one of the first k letters of s and append it at the end of the string..

    Return the lexicographically smallest string you could have after applying the mentioned step any number of moves.

Example 1:
    Input: s = "cba", k = 1
    Output: "acb"
    Explanation: 
        In the first move, we move the 1st character 'c' to the end, obtaining the string "bac".
        In the second move, we move the 1st character 'b' to the end, obtaining the final result "acb".
Example 2:
    Input: s = "baaca", k = 3
    Output: "aaabc"
    Explanation: 
        In the first move, we move the 1st character 'b' to the end, obtaining the string "aacab".
        In the second move, we move the 3rd character 'c' to the end, obtaining the final result "aaabc".

Constraints:
    1 <= k <= s.length <= 1000
    s consist of lowercase English letters.
"""


class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        # exception case
        assert isinstance(k, int) and k >= 1
        assert isinstance(s, str) and len(s) >= k
        # main method: (if k == 1, try len(s) answers; if k >= 2, s can always be permuted to sorted array)
        # advanced: use minimal-string representation: https://oi-wiki.org/string/minimal-string
        return self._orderlyQueue(s, k)

    def _orderlyQueue(self, s: str, k: int) -> str:
        """
        Runtime: 34 ms, faster than 97.62% of Python3 online submissions for Orderly Queue.
        Memory Usage: 13.9 MB, less than 39.29% of Python3 online submissions for Orderly Queue.
        """
        assert isinstance(k, int) and k >= 1
        assert isinstance(s, str) and len(s) >= k

        if k == 1:
            res = s
            for _ in range(len(s) - 1):
                s = s[1:] + s[0]
                res = min(res, s)
            return res
        else:
            return "".join(sorted(s))


def main():
    # Example 1: Output: "acb"
    # s = "cba"
    # k = 1

    # Example 2: Output: "aaabc"
    s = "baaca"
    k = 3

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.orderlyQueue(s, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
