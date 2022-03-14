#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0599-Minimum-Index-Sum-of-Two-Lists.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-14
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0599 - (Easy) - Minimum Index Sum of Two Lists
https://leetcode.com/problems/minimum-index-sum-of-two-lists/

Description & Requirement:
    Suppose Andy and Doris want to choose a restaurant for dinner, 
    and they both have a list of favorite restaurants represented by strings.

    You need to help them find out their common interest with the least list index sum. 
    If there is a choice tie between answers, output all of them with no order requirement. 
    You could assume there always exists an answer.

Example 1:
    Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
    Output: ["Shogun"]
    Explanation: The only restaurant they both like is "Shogun".
Example 2:
    Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]
    Output: ["Shogun"]
    Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).

Constraints:
    1 <= list1.length, list2.length <= 1000
    1 <= list1[i].length, list2[i].length <= 30
    list1[i] and list2[i] consist of spaces ' ' and English letters.
    All the stings of list1 are unique.
    All the stings of list2 are unique.
"""


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        # exception case
        assert isinstance(list1, list) and len(list1) > 0
        assert isinstance(list2, list) and len(list2) > 0
        # main method: (hash dict, key: restaurant; value: index list.)
        return self._findRestaurant(list1, list2)

    def _findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        len_list1 = len(list1)
        len_list2 = len(list2)
        assert len_list1 > 0 and len_list2 > 0

        hash_dict = dict({})  # key: restaurant; value: index list

        for idx, res in enumerate(list1):
            if res not in hash_dict:
                hash_dict[res] = [idx]
            else:
                hash_dict[res].append(idx)

        for idx, res in enumerate(list2):
            if res not in hash_dict:
                hash_dict[res] = [idx]
            else:
                hash_dict[res].append(idx)

        min_sum = len_list1 + len_list2  # default max
        for res, idx_list in hash_dict.items():  # get min_sum
            if len(idx_list) == 2 and sum(idx_list) < min_sum:
                min_sum = sum(idx_list)

        result = []
        for res, idx_list in hash_dict.items():  # get all res that sum(idx_list) == min_sum
            if len(idx_list) == 2 and sum(idx_list) == min_sum:
                result.append(res)

        return result


def main():
    # Example 1: Output: ["Shogun"]
    # list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    # list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]

    # Example 2: Output: ["Shogun"]
    list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    list2 = ["KFC", "Shogun", "Burger King"]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.findRestaurant(list1, list2)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
