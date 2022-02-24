#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0279-Perfect-Squares.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-24
=================================================================="""

import sys
import time
# from typing import List
# import collections

"""
LeetCode - 0279 - (Medium) - Perfect Squares
https://leetcode.com/problems/perfect-squares/

Description & Requirement:
    Given an integer n, return the least number of perfect square numbers that sum to n.

    A perfect square is an integer that is the square of an integer; 
    in other words, it is the product of some integer with itself. 
    For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

Example 1:
    Input: n = 12
    Output: 3
    Explanation: 12 = 4 + 4 + 4.
Example 2:
    Input: n = 13
    Output: 2
    Explanation: 13 = 4 + 9.

Constraints:
    1 <= n <= 10^4
"""


class Solution:
    def numSquares(self, n: int) -> int:
        # exception case
        assert isinstance(n, int) and n > 0
        if n == 1:
            return 1
        # main method: (1. dfs & backtrace; 2. dynamic programming. 3. mathematics)
        # [Lagrange's four-square theorem](https://en.wikipedia.org/wiki/Lagrange%27s_four-square_theorem)
        #     Lagrange's four-square theorem, also known as Bachet's conjecture,
        #     states that every natural number can be represented as the sum of four integer squares.
        #     That is, the squares form an additive basis of order four.
        # return self._numSquaresDfs(n)  # TLE
        # return self._numSquaresDp(n)  # Time: O(n * \sqrt(n)); Space: O(n)
        return self._numSquaresMath(n)  # Time: O(\sqrt(n)); Space: O(n) or O(1)

    def _numSquaresDfs(self, n: int) -> int:
        assert n >= 2

        def __get_perfect_square_list(limit: int) -> list:
            _ps_list = []
            _num = 1
            while _num * _num <= limit:
                _ps_list.append(_num * _num)
                _num += 1
            return _ps_list

        def __reverse_list(origin_list: list):
            left_idx, right_idx = 0, len(origin_list) - 1
            while left_idx < right_idx:
                origin_list[left_idx], origin_list[right_idx] = origin_list[right_idx], origin_list[left_idx]
                left_idx += 1
                right_idx -= 1

        # 1 <= n <= 10^4, so 1 <= len(ps_list) <= 100
        ps_list = __get_perfect_square_list(n)  # now ps_list is ascending order
        if n in ps_list:
            return 1
        __reverse_list(ps_list)  # now ps_list is descending order, greedily find the min len combination
        len_ps = len(ps_list)

        res = [4]  # at most 4, according to Lagrange's four-square theorem

        def __dfs(cur_combo_len: int, cur_sum: int, cur_ps_index: int):
            if cur_combo_len >= res[0] or cur_ps_index >= len_ps or cur_sum > n:
                return
            if cur_sum > n:
                return
            if cur_sum == n:
                if cur_combo_len == 2:
                    res[0] = 2
                if cur_combo_len < res[0]:
                    res[0] = cur_combo_len
                return
            for next_ps_index in range(cur_ps_index, len_ps):  # explore more numbers (numbers can be reused)
                __dfs(cur_combo_len + 1, cur_sum + ps_list[cur_ps_index], next_ps_index)  # go deeper

        for start_ps_index in range(len_ps):  # start from every number
            if res[0] == 2:
                return 2
            __dfs(0, 0, start_ps_index)

        return res[0]

    def _numSquaresDp(self, n: int) -> int:
        """
        dp[i] is the min len of combination to make up integer i
        dp equation: dp[i] = 1 + min(dp[i - j * j]), where j is an integer such that j * j <= i
        dp init: all elements = 4, according to Lagrange's four-square theorem
        dp aim: get dp[-1]
        """
        assert n >= 2

        # dp[i] is the min len of combination to make up integer i
        # dp init: all elements = 4, according to Lagrange's four-square theorem
        dp = [4 for _ in range(n + 1)]
        dp[0] = 0

        # dp equation: dp[i] = 1 + min(dp[i - j * j]), where j is an integer such that j * j <= i
        for i in range(1, n + 1):
            cur_min = 4
            j = 1
            while j * j <= i:
                cur_min = min(cur_min, dp[i - j * j])
                j += 1
            dp[i] = min(4, cur_min + 1)

        # dp aim: get dp[-1]
        return dp[-1]

    def _numSquaresMath(self, n: int) -> int:
        """
        if n == 4^k * (8m + 7), then n can only be represented as the sum of 4 perfect square numbers
        if result == 1, then n == k^2, just check if n is a perfect square number
        if result == 2, then n can be represented as (i^2 + j^2), so just enumerate all (n - i^2), see if it's a ps
        else n can only be represented as the sum of 3 perfect square numbers

        Runtime: 42 ms, faster than 98.58% of Python3 online submissions for Perfect Squares.
        Memory Usage: 14.2 MB, less than 76.60% of Python3 online submissions for Perfect Squares.
        """
        assert n >= 2

        def __get_perfect_square_list_set(limit: int):
            _ps_list = []
            _ps_set = set()
            _num = 1
            while _num * _num <= limit:
                _num_square = _num * _num
                _ps_list.append(_num_square)
                _ps_set.add(_num_square)
                _num += 1
            return _ps_list, _ps_set

        # 1 <= n <= 10^4, so 1 <= len(ps_list) <= 100
        ps_list, ps_set = __get_perfect_square_list_set(n)  # now ps_list is ascending order

        # if result == 1, then n == k^2, just check if n is a perfect square number
        if n in ps_set:
            return 1

        # if n == 4^k * (8m + 7), then n can only be represented as the sum of 4 perfect square numbers
        test_4 = n
        while test_4 > 4 and test_4 & 3 == 0:  # get rid of 4^k factors (& 3 == 0  <->  % 4 == 0)
            test_4 >>= 2
        if test_4 % 8 == 7:
            return 4

        # if result == 2, then n can be represented as (i^2 + j^2), so just enumerate all (n - i^2), see if it's a ps
        for ps in ps_list:
            if (n - ps) in ps_set:
                return 2

        # else n can only be represented as the sum of 3 perfect square numbers
        return 3


def main():
    # Example 1: Output: 3
    # n = 12

    # Example 2: Output: 2
    # n = 13

    # Example 3: Output: 4  (DFS (TLE) 4161.92700 ms; DP 203.00500 ms; Math 0.03900 ms)
    n = 8935

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.numSquares(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
