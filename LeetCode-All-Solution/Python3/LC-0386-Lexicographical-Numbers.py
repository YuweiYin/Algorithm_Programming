#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0386-Lexicographical-Numbers.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-18
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0386 - (Medium) - Lexicographical Numbers
https://leetcode.com/problems/lexicographical-numbers/

Description & Requirement:
    Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

    You must write an algorithm that runs in O(n) time and uses O(1) extra space. 

Example 1:
    Input: n = 13
    Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]
Example 2:
    Input: n = 2
    Output: [1,2]

Constraints:
    1 <= n <= 5 * 10^4
"""


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        # exception case
        assert isinstance(n, int) and n >= 1
        # main method: (greedily prepend "1" to the current number)
        return self._lexicalOrder(n)

    def _lexicalOrder(self, n: int) -> List[int]:
        """
        Runtime: 96 ms, faster than 96.71% of Python3 online submissions for Lexicographical Numbers.
        Memory Usage: 20.1 MB, less than 56.03% of Python3 online submissions for Lexicographical Numbers.
        """
        res = [0 for _ in range(n)]

        cur_num = 1  # start from 1
        for idx in range(n):
            res[idx] = cur_num
            if cur_num * 10 <= n:  # prepend "1" to cur_num
                cur_num *= 10
            else:  # now, cur_num * 10 > n, can not prepend "1"
                # cur_num % 10 == 9 means cur_num is max number with all those prepended "1" and needs to //= 10
                while cur_num % 10 == 9 or cur_num >= n:
                    cur_num //= 10
                cur_num += 1

        return res


def main():
    # Example 1: Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]
    n = 13

    # Example 2: Output: [1,2]
    # n = 2

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.lexicalOrder(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
