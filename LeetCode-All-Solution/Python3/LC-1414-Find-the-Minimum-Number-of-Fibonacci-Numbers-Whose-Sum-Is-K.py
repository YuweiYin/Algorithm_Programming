#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1414-Find-the-Minimum-Number-of-Fibonacci-Numbers-Whose-Sum-Is-K.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-03
=================================================================="""

import sys
import time
from typing import List
# import collections

"""
LeetCode - 1414 - (Medium) - Find the Minimum Number of Fibonacci Numbers Whose Sum Is K
https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/

Description & Requirement:
    Given an integer k, return the minimum number of Fibonacci numbers whose sum is equal to k. 
    The same Fibonacci number can be used multiple times.

    The Fibonacci numbers are defined as:
        F1 = 1
        F2 = 1
        Fn = Fn-1 + Fn-2 for n > 2.
    It is guaranteed that for the given constraints we can always find such Fibonacci numbers that sum up to k.

Example 1:
    Input: k = 7
    Output: 2 
    Explanation: The Fibonacci numbers are: 1, 1, 2, 3, 5, 8, 13, ... 
        For k = 7 we can use 2 + 5 = 7.
Example 2:
    Input: k = 10
    Output: 2 
    Explanation: For k = 10 we can use 2 + 8 = 10.
Example 3:
    Input: k = 19
    Output: 3 
    Explanation: For k = 19 we can use 1 + 5 + 13 = 19.

Constraints:
    1 <= k <= 10^9
"""


class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        # exception case
        assert isinstance(k, int) and k >= 1
        if k <= 3:
            return 1
        # main method: (Greedy: construct Fibonacci array, then greedily pick each largest number n, such that n <= k)
        return self._findMinFibonacciNumbers(k)

    def _findMinFibonacciNumbers(self, k: int) -> int:
        assert k >= 4

        def __get_fibo_list(limit: int) -> List[int]:
            fibo_list = [1, 1]
            cur_fibo_1 = 1
            cur_fibo_2 = 2
            while cur_fibo_2 <= limit:  # Fn = Fn-1 + Fn-2 for n > 2
                fibo_list.append(cur_fibo_2)
                cur_fibo_1, cur_fibo_2 = cur_fibo_2, cur_fibo_1 + cur_fibo_2
            return fibo_list

        fibo_nums = __get_fibo_list(k)

        res = 0
        cur_fibo_index = len(fibo_nums) - 1
        while k > 0:
            # assert cur_fibo_index >= 0
            while fibo_nums[cur_fibo_index] > k:  # find the largest number n, such that n <= k
                cur_fibo_index -= 1
            k -= fibo_nums[cur_fibo_index]  # k decrease
            res += 1  # res counter += 1

        return res


def main():
    # Example 1: Output: 2
    #     Explanation: The Fibonacci numbers are: 1, 1, 2, 3, 5, 8, 13, ...
    #         For k = 7 we can use 2 + 5 = 7.
    # k = 7

    # Example 2: Output: 2
    #     Explanation: For k = 10 we can use 2 + 8 = 10.
    # k = 10

    # Example 3: Output: 3
    #     Explanation: For k = 19 we can use 1 + 5 + 13 = 19.
    k = 19

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.findMinFibonacciNumbers(k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
