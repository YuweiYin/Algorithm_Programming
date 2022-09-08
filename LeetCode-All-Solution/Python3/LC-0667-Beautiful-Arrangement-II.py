#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0667-Beautiful-Arrangement-II.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-09-08
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0667 - (Medium) - Beautiful Arrangement II
https://leetcode.com/problems/beautiful-arrangement-ii/

Description & Requirement:
    Given two integers n and k, construct a list answer that contains n different positive integers 
    ranging from 1 to n and obeys the following requirement:
        Suppose this list is answer = [a1, a2, a3, ... , an], 
        then the list [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] has exactly k distinct integers.

    Return the list answer. If there multiple valid answers, return any of them.

Example 1:
    Input: n = 3, k = 1
    Output: [1,2,3]
    Explanation: The [1,2,3] has three different positive integers ranging from 1 to 3, 
        and the [1,1] has exactly 1 distinct integer: 1
Example 2:
    Input: n = 3, k = 2
    Output: [1,3,2]
    Explanation: The [1,3,2] has three different positive integers ranging from 1 to 3, 
        and the [2,1] has exactly 2 distinct integers: 1 and 2.

Constraints:
    1 <= k < n <= 10^4
"""


class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        # exception case
        assert isinstance(n, int) and isinstance(k, int) and 1 <= k < n
        # main method: (construct [1, 2, ..., n−k, n, n−k+1, n−1, n−k+2, ...] if k > 1)
        return self._constructArray(n, k)

    def _constructArray(self, n: int, k: int) -> List[int]:
        """
        Runtime: 45 ms, faster than 96.57% of Python3 online submissions for Beautiful Arrangement II.
        Memory Usage: 15.1 MB, less than 50.86% of Python3 online submissions for Beautiful Arrangement II.
        """
        assert isinstance(n, int) and isinstance(k, int) and 1 <= k < n

        if k == 1:
            return list(range(1, n + 1))

        res = list(range(1, n - k))
        i, j = n - k, n
        while i <= j:
            res.append(i)
            if i != j:
                res.append(j)
            i, j = i + 1, j - 1

        return res


def main():
    # Example 1: Output: [1,2,3]
    # n = 3
    # k = 1

    # Example 2: Output: [1,3,2]
    n = 3
    k = 2

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.constructArray(n, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
