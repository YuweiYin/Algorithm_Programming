#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0039-Combination-Sum.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-23
=================================================================="""

import sys
import time
from typing import List
# import collections

"""
LeetCode - 0039 - (Medium) - Combination Sum
https://leetcode.com/problems/combination-sum/

Description & Requirement:
    Given an array of distinct integers candidates and a target integer target, 
    return a list of all unique combinations of candidates where the chosen numbers sum to target. 
    You may return the combinations in any order.

    The same number may be chosen from candidates an unlimited number of times. 
    Two combinations are unique if the frequency of at least one of the chosen numbers is different.

    It is guaranteed that the number of unique combinations 
    that sum up to target is less than 150 combinations for the given input.

Example 1:
    Input: candidates = [2,3,6,7], target = 7
    Output: [[2,2,3],[7]]
    Explanation:
        2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
        7 is a candidate, and 7 = 7.
        These are the only two combinations.
Example 2:
    Input: candidates = [2,3,5], target = 8
    Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:
    Input: candidates = [2], target = 1
    Output: []

Constraints:
    1 <= candidates.length <= 30
    1 <= candidates[i] <= 200
    All elements of candidates are distinct.
    1 <= target <= 500

Related Problem:
    LC-0039-Combination-Sum
    LC-0040-Combination-Sum-II
    LC-0216-Combination-Sum-III
    LC-0377-Combination-Sum-IV
"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # exception case
        if not isinstance(candidates, list) or len(candidates) <= 0 or not isinstance(target, int):
            return []  # Error input type
        # main method: (sort & dfs & backtrace.)
        return self._combinationSum(candidates, target)

    def _combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        len_nums = len(candidates)
        assert len_nums > 0

        res_list = []
        dup_set = set()  # to avoid duplication

        candidates.sort()  # more easily to find duplication

        def __dfs(cur_combo: List[int], cur_sum: int, cur_num_index: int):
            if cur_num_index >= len_nums or cur_sum > target:
                return
            cur_combo.append(candidates[cur_num_index])
            cur_sum += candidates[cur_num_index]
            if cur_sum > target:
                return
            if cur_sum == target:
                if tuple(cur_combo) not in dup_set:
                    dup_set.add(tuple(cur_combo))
                    res_list.append(cur_combo[:])
            for next_num_index in range(cur_num_index, len_nums):  # explore more numbers (numbers can be reused)
                __dfs(cur_combo, cur_sum, next_num_index)  # go deeper
                cur_combo.pop()  # backtrace

        for start_num_index in range(len_nums):  # start from every number
            __dfs([], 0, start_num_index)
        return res_list


def main():
    # Example 1: Output: [[2,2,3],[7]]
    # candidates = [2, 3, 6, 7]
    # target = 7

    # Example 2: Output: [[2,2,2,2],[2,3,3],[3,5]]
    candidates = [2, 3, 5]
    target = 8

    # Example 3: Output: []
    # candidates = [2]
    # target = 1

    # Example 4: Output: [[1,1]]
    # candidates = [1]
    # target = 2

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.combinationSum(candidates, target)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
