#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0646-Maximum-Length-of-Pair-Chain.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-09-03
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0646 - (Medium) - Maximum Length of Pair Chain
https://leetcode.com/problems/maximum-length-of-pair-chain/

Description & Requirement:
    You are given an array of n pairs pairs where pairs[i] = [left_i, right_i] and left_i < right_i.

    A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.

    Return the length longest chain which can be formed.

    You do not need to use up all the given intervals. You can select pairs in any order.

Example 1:
    Input: pairs = [[1,2],[2,3],[3,4]]
    Output: 2
    Explanation: The longest chain is [1,2] -> [3,4].
Example 2:
    Input: pairs = [[1,2],[7,8],[4,5]]
    Output: 3
    Explanation: The longest chain is [1,2] -> [4,5] -> [7,8].

Constraints:
    n == pairs.length
    1 <= n <= 1000
    -1000 <= left_i < right_i <= 1000
"""


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # exception case
        assert isinstance(pairs, list) and len(pairs) >= 1
        # main method: (sorting & greedy)
        return self._findLongestChain(pairs)

    def _findLongestChain(self, pairs: List[List[int]]) -> int:
        assert isinstance(pairs, list) and len(pairs) >= 1
        # n = len(pairs)

        pairs.sort(key=lambda x: x[1])
        cur_right = - int(1e9+7)
        res = 1

        for left, right in pairs:
            if cur_right < left:
                cur_right = right
                res += 1

        return res


def main():
    # Example 1: Output: 2
    # pairs = [[1, 2], [2, 3], [3, 4]]

    # Example 2: Output: 3
    pairs = [[1, 2], [7, 8], [4, 5]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.findLongestChain(pairs)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
