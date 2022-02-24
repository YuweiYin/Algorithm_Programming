#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0040-Combination-Sum-II.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-23
=================================================================="""

import sys
import time
from typing import List
# import collections

"""
LeetCode - 0040 - (Medium) - Combination Sum II
https://leetcode.com/problems/combination-sum-ii/

Description & Requirement:
    Given a collection of candidate numbers (candidates) and a target number (target), 
    find all unique combinations in candidates where the candidate numbers sum to target.

    Each number in candidates may only be used once in the combination.

    Note: The solution set must not contain duplicate combinations.

Example 1:
    Input: candidates = [10,1,2,7,6,1,5], target = 8
    Output: [
        [1,1,6],
        [1,2,5],
        [1,7],
        [2,6]
    ]
Example 2:
Input: candidates = [2,5,2,1,2], target = 5
    Output: [
        [1,2,2],
        [5]
    ]

Constraints:
    1 <= candidates.length <= 100
    1 <= candidates[i] <= 50
    1 <= target <= 30

Related Problem:
    LC-0039-Combination-Sum
    LC-0040-Combination-Sum-II
    LC-0216-Combination-Sum-III
    LC-0377-Combination-Sum-IV
"""


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # exception case
        if not isinstance(candidates, list) or len(candidates) <= 0 or not isinstance(target, int):
            return []  # Error input type
        if len(candidates) == 1:
            return [candidates] if candidates[0] == target else []
        # main method: (sort & dfs & backtrace.) optimize: prune search tree
        # return self._combinationSum2(candidates, target)
        return self._combinationSum2New(candidates, target)

    def _combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        len_nums = len(candidates)
        assert len_nums > 1

        res_list = []
        cur_combo = []
        dup_set = set()  # to avoid duplication

        candidates.sort()  # more easily to find duplication

        dfs_start = 0

        # hack many 1 case
        counter_1 = 0  # how many 1 in candidates
        next_to_1 = -1  # the num that next to 1
        assert candidates[0] >= 1
        for num in candidates:
            if num == 1:
                counter_1 += 1
            else:
                next_to_1 = num
                break
        if counter_1 == len_nums:  # all 1
            if len(candidates) >= target:
                return [[1 for _ in range(target)]]
            else:
                return []
        assert counter_1 < len_nums and next_to_1 > 1
        if counter_1 >= target:  # there are enough 1s to form a valid [1, 1, ..., 1]
            valid_1 = [1 for _ in range(target)]
            if tuple(valid_1) not in dup_set:
                dup_set.add(tuple(valid_1))
                res_list.append(valid_1)
        # if counter_1 > next_to_1:  # skip some 1
        #     dfs_start = max(0, next_to_1)

        def __dfs(cur_sum: int, cur_num_index: int):
            if cur_sum >= target:
                if cur_sum == target and tuple(cur_combo) not in dup_set:
                    dup_set.add(tuple(cur_combo))
                    res_list.append(cur_combo[:])
                return  # optimize: prune search tree
            for next_num_index in range(cur_num_index + 1, len_nums):
                cur_combo.append(candidates[next_num_index])
                __dfs(cur_sum + candidates[next_num_index], next_num_index)  # go deeper
                cur_combo.pop()  # backtrace

        all_sum = sum(candidates)
        if all_sum == target:
            return [candidates]
        if all_sum < target:
            return []
        else:
            for start_index in range(dfs_start, len_nums):
                cur_combo.append(candidates[start_index])
                __dfs(candidates[start_index], start_index)
                cur_combo.pop()
        return res_list

    def _combinationSum2New(self, candidates: List[int], target: int) -> List[List[int]]:
        import collections

        num_counter = sorted(collections.Counter(candidates).items())  # num_c[i][1] is the count of number num_c[i][0]
        res_list = []
        cur_combo = []

        def __dfs(index: int, rest_sum: int):
            nonlocal cur_combo
            if rest_sum == 0:  # no rest sum, bingo
                res_list.append(cur_combo[:])
                return
            if index == len(num_counter) or rest_sum < num_counter[index][0]:
                return

            __dfs(index + 1, rest_sum)  # go deeper

            max_index = min(rest_sum // num_counter[index][0], num_counter[index][1])
            for i in range(1, max_index + 1):  # explore all possible next number
                cur_combo.append(num_counter[index][0])
                __dfs(index + 1, rest_sum - i * num_counter[index][0])
            cur_combo = cur_combo[: -max_index]  # backtrace

        __dfs(0, target)
        return res_list


def main():
    # Example 1: Output: [
    #     [1,1,6],
    #     [1,2,5],
    #     [1,7],
    #     [2,6]
    # ]
    # candidates = [10, 1, 2, 7, 6, 1, 5]
    # target = 8

    # Example 2: Output: [
    #     [1,2,2],
    #     [5]
    # ]
    # candidates = [2, 5, 2, 1, 2]
    # target = 5

    # Example 3: Output: [
    #     [5,6,6,9],[5,6,7,8],[5,6,15],[5,7,14],[5,9,12],[5,10,11],[5,21],
    #     [6,6,6,8],[6,6,7,7],[6,6,14],[6,8,12],[6,9,11],[6,10,10],[6,20],
    #     [7,7,12],[7,8,11],[7,9,10],[7,19],[8,8,10],[8,9,9],[8,18],[9,17],[11,15],[12,14],[26]]
    # candidates = [
    #     20, 34, 8, 30, 26, 33, 28, 19, 21, 28, 22, 15, 33, 19, 12, 9, 17, 9, 11, 7, 5, 14, 31, 14, 12, 6,
    #     29, 20, 27, 24, 23, 34, 23, 18, 29, 6, 8, 23, 20, 25, 8, 30, 27, 7, 6, 34, 11, 10, 8, 9, 34, 30, 10
    # ]
    # target = 26

    # Example 4: Output:
    candidates = [
        14, 22, 8, 31, 30, 26, 9, 34, 20, 13, 10, 22, 6, 12, 18, 22, 28, 19, 14, 17, 24, 24, 22, 14, 27, 30,
        6, 23, 25, 14, 33, 5, 23, 7, 23, 18, 28, 20, 9, 5, 20, 14, 22, 21, 21, 6, 9, 6, 12, 10, 19, 31, 21,
        28, 32, 14, 23, 33, 32, 14
    ]
    target = 29

    # Example 5: Output: []
    # candidates = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    # target = 27

    # Example 6: Output: [1, 1, ..., 1]
    # candidates = [
    #     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    #     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    #     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
    # ]
    # target = 30

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.combinationSum2(candidates, target)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
