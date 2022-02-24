#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0216-Combination-Sum-III.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-23
=================================================================="""

import sys
import time
from typing import List
# import collections

"""
LeetCode - 0216 - (Medium) - Combination Sum III
https://leetcode.com/problems/combination-sum-iii/

Description & Requirement:
    Find all valid combinations of k numbers that sum up to n 
    such that the following conditions are true:
        Only numbers 1 through 9 are used.
        Each number is used at most once.

    Return a list of all possible valid combinations. 
    The list must not contain the same combination twice, 
    and the combinations may be returned in any order.

Example 1:
    Input: k = 3, n = 7
    Output: [[1,2,4]]
    Explanation:
        1 + 2 + 4 = 7
        There are no other valid combinations.
Example 2:
    Input: k = 3, n = 9
    Output: [[1,2,6],[1,3,5],[2,3,4]]
    Explanation:
        1 + 2 + 6 = 9
        1 + 3 + 5 = 9
        2 + 3 + 4 = 9
        There are no other valid combinations.
Example 3:
    Input: k = 4, n = 1
    Output: []
    Explanation: There are no valid combinations.
        Using 4 different numbers in the range [1,9], 
        the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.

Constraints:
    2 <= k <= 9
    1 <= n <= 60

Related Problem:
    LC-0039-Combination-Sum
    LC-0040-Combination-Sum-II
    LC-0216-Combination-Sum-III
    LC-0377-Combination-Sum-IV
"""


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # exception case
        assert isinstance(k, int) and 2 <= k <= 9 and isinstance(n, int) and 1 <= n <= 60
        # main method: (sort & dfs & backtrace.)
        return self._combinationSum3(k, n)

    def _combinationSum3(self, k: int, n: int) -> List[List[int]]:
        """
        Runtime: 24 ms, faster than 98.44% of Python3 online submissions for Combination Sum III.
        Memory Usage: 13.9 MB, less than 65.89% of Python3 online submissions for Combination Sum III.
        """
        res_list = []
        dup_set = set()  # to avoid duplication

        candidates = [number for number in range(1, 10)]  # 1, 2, 3, ..., 9
        len_nums = len(candidates)

        def __dfs(cur_combo: List[int], cur_sum: int, cur_num_index: int):
            if cur_num_index >= len_nums or cur_sum > n:
                return
            cur_combo.append(candidates[cur_num_index])
            cur_sum += candidates[cur_num_index]
            if cur_sum > n:
                return
            if len(cur_combo) == k:  # add new combination when length == k and sum == n and not duplicated
                if cur_sum == n:
                    if tuple(cur_combo) not in dup_set:
                        dup_set.add(tuple(cur_combo))
                        res_list.append(cur_combo[:])
                else:
                    return
            elif len(cur_combo) > k:
                return
            else:
                for next_num_index in range(cur_num_index + 1, len_nums):  # explore more numbers
                    __dfs(cur_combo, cur_sum, next_num_index)  # go deeper
                    cur_combo.pop()  # backtrace

        for start_num_index in range(len_nums):  # start from every number
            __dfs([], 0, start_num_index)
        return res_list


def main():
    # Example 1: Output: [[1,2,4]]
    # k, n = 3, 7

    # Example 2: Output: [[1,2,6],[1,3,5],[2,3,4]]
    k, n = 3, 9

    # Example 3: Output: []
    # k, n = 4, 1

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.combinationSum3(k, n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
