#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0904-Fruit-Into-Baskets.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-10-17
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0904 - (Medium) - Fruit Into Baskets
https://leetcode.com/problems/fruit-into-baskets/

Description & Requirement:
    You are visiting a farm that has a single row of fruit trees arranged from left to right. 
    The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

    You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:
        You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
        Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
        Once you reach a tree with fruit that cannot fit in your baskets, you must stop.

    Given the integer array fruits, return the maximum number of fruits you can pick.

Example 1:
    Input: fruits = [1,2,1]
    Output: 3
    Explanation: We can pick from all 3 trees.
Example 2:
    Input: fruits = [0,1,2,2]
    Output: 3
    Explanation: We can pick from trees [1,2,2].
        If we had started at the first tree, we would only pick from trees [0,1].
Example 3:
    Input: fruits = [1,2,3,2,2]
    Output: 4
    Explanation: We can pick from trees [2,3,2,2].
        If we had started at the first tree, we would only pick from trees [1,2].

Constraints:
    1 <= fruits.length <= 10^5
    0 <= fruits[i] < fruits.length
"""


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # exception case
        assert isinstance(fruits, list) and len(fruits) >= 1
        n = len(fruits)
        for fruit in fruits:
            assert isinstance(fruit, int) and 0 <= fruit < n
        # main method: (sliding window and hash set)
        return self._totalFruit(fruits)

    def _totalFruit(self, fruits: List[int]) -> int:
        """
        Runtime: 975 ms, faster than 93.00% of Python3 online submissions for Fruit Into Baskets.
        Memory Usage: 20.6 MB, less than 14.58% of Python3 online submissions for Fruit Into Baskets.
        """
        assert isinstance(fruits, list) and len(fruits) >= 1
        n = len(fruits)

        if len(set(fruits)) <= 2:
            return n

        fruit_dict = dict()
        res = 0
        left = 0
        for right, fruit in enumerate(fruits):
            if fruit in fruit_dict:
                fruit_dict[fruit] += 1
            else:
                fruit_dict[fruit] = 1
            while len(fruit_dict) > 2:
                fruit_dict[fruits[left]] -= 1
                if fruit_dict[fruits[left]] == 0:
                    fruit_dict.pop(fruits[left])
                left += 1
            res = max(res, right - left + 1)

        return res


def main():
    # Example 1: Output: 3
    # fruits = [1, 2, 1]

    # Example 2: Output: 3
    # fruits = [0, 1, 2, 2]

    # Example 3: Output: 4
    # fruits = [1, 2, 3, 2, 2]

    # Example 4: Output: 5
    fruits = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.totalFruit(fruits)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
