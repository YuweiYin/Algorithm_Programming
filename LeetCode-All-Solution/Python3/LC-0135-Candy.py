#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0135-Candy.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-07-04
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0135 - (Hard) - Candy
https://leetcode.com/problems/candy/

Description & Requirement:
    There are n children standing in a line. 
    Each child is assigned a rating value given in the integer array ratings.

    You are giving candies to these children subjected to the following requirements:
        Each child must have at least one candy.
        Children with a higher rating get more candies than their neighbors.

    Return the minimum number of candies you need to have to distribute the candies to the children.

Example 1:
    Input: ratings = [1,0,2]
    Output: 5
    Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:
    Input: ratings = [1,2,2]
    Output: 4
    Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
        The third child gets 1 candy because it satisfies the above two conditions.

Constraints:
    n == ratings.length
    1 <= n <= 2 * 10^4
    0 <= ratings[i] <= 2 * 10^4
"""


class Solution:
    def candy(self, ratings: List[int]) -> int:
        # exception case
        assert isinstance(ratings, list) and len(ratings) >= 1
        # main method: (left-to-right scan and right-to-left scan, then get the minimum number of candy)
        return self._candy(ratings)

    def _candy(self, ratings: List[int]) -> int:
        assert isinstance(ratings, list) and len(ratings) >= 1

        kids = len(ratings)
        left_scan = [1 for _ in range(kids)]  # at least one candy for each child
        for idx in range(1, kids):
            if ratings[idx - 1] < ratings[idx]:  # increasing
                left_scan[idx] = left_scan[idx - 1] + 1

        right_scan = 1  # at least one candy for the rightmost child
        res = max(left_scan[-1], right_scan)  # first, deal with the last child
        for idx in range(kids - 2, -1, -1):
            if ratings[idx] > ratings[idx + 1]:  # decreasing
                right_scan += 1
            else:
                right_scan = 1
            res += max(left_scan[idx], right_scan)

        return res


def main():
    # Example 1: Output: 5
    # ratings = [1, 0, 2]

    # Example 2: Output: 4
    ratings = [1, 2, 2]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.candy(ratings)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
