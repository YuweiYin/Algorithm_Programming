#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1663-Smallest-String-With-A-Given-Numeric-Value.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-22
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 1663 - (Medium) - Smallest String With A Given Numeric Value
https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/

Description & Requirement:
    The numeric value of a lowercase character is defined as its position (1-indexed) in the alphabet, 
    so the numeric value of a is 1, the numeric value of b is 2, the numeric value of c is 3, and so on.

    The numeric value of a string consisting of lowercase characters is defined as the sum of 
    its characters' numeric values. For example, the numeric value of the string "abe" is equal to 1 + 2 + 5 = 8.

    You are given two integers n and k. Return the lexicographically smallest string 
    with length equal to n and numeric value equal to k.

    Note that a string x is lexicographically smaller than string y if x comes before y in dictionary order, 
    that is, either x is a prefix of y, or if i is the first position such that x[i] != y[i], 
    then x[i] comes before y[i] in alphabetic order.

Example 1:
    Input: n = 3, k = 27
    Output: "aay"
    Explanation: The numeric value of the string is 1 + 1 + 25 = 27, 
        and it is the smallest string with such a value and length equal to 3.
Example 2:
    Input: n = 5, k = 73
    Output: "aaszz"

Constraints:
    1 <= n <= 10^5
    n <= k <= 26 * n
"""


class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        # exception case
        assert isinstance(n, int) and n > 0
        assert isinstance(k, int) and n <= k <= 26 * n
        # main method: (greedily set the tail of string as large as possible)
        return self._getSmallestString(n, k)

    def _getSmallestString(self, n: int, k: int) -> str:
        res = []
        cur_sum = 0

        div = k // 26
        for _ in range(n - div):
            # res.append("a")
            res.append(1)
            cur_sum += 1
        for _ in range(div):
            # res.append("z")
            res.append(26)
            cur_sum += 26
        # now res is "aaa...zzz" and len(res) == n, now modify some char
        if cur_sum == k:
            pass
        elif cur_sum > k:
            idx = n - div  # from the first "z"
            while cur_sum > k:
                if res[idx] > 1:
                    res[idx] -= 1
                    cur_sum -= 1
                else:
                    idx += 1  # move the index
                    res[idx] -= 1
                    cur_sum -= 1
        else:
            idx = n - div - 1  # from the last "a"
            while cur_sum < k:
                if res[idx] < 26:
                    res[idx] += 1
                    cur_sum += 1
                else:
                    idx -= 1  # move the index
                    res[idx] += 1
                    cur_sum += 1

        # convert int to char
        ord_a = ord("a")
        return "".join([chr(num - 1 + ord_a) for num in res])


def main():
    # Example 1: Output: "aay"
    # n = 3
    # k = 27

    # Example 2: Output: "aaszz"
    n = 5
    k = 73

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.getSmallestString(n, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
