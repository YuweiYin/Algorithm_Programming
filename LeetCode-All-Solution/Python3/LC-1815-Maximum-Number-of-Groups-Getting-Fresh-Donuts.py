#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1815-Maximum-Number-of-Groups-Getting-Fresh-Donuts.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-01-22
=================================================================="""

import sys
import time
from typing import List
import collections
import functools

"""
LeetCode - 1815 - (Hard) - Maximum Number of Groups Getting Fresh Donuts
https://leetcode.com/problems/maximum-number-of-groups-getting-fresh-donuts/

Description & Requirement:
    There is a donuts shop that bakes donuts in batches of batchSize. 
    They have a rule where they must serve all of the donuts of a batch before serving any donuts of the next batch. 
    You are given an integer batchSize and an integer array groups, where groups[i] denotes that 
    there is a group of groups[i] customers that will visit the shop. Each customer will get exactly one donut.

    When a group visits the shop, all customers of the group must be served before serving any of the following groups.
    A group will be happy if they all get fresh donuts. That is, the first customer of the group 
    does not receive a donut that was left over from the previous group.

    You can freely rearrange the ordering of the groups. 
    Return the maximum possible number of happy groups after rearranging the groups.

Example 1:
    Input: batchSize = 3, groups = [1,2,3,4,5,6]
    Output: 4
    Explanation: You can arrange the groups as [6,2,4,5,1,3]. Then the 1st, 2nd, 4th, and 6th groups will be happy.
Example 2:
    Input: batchSize = 4, groups = [1,3,2,5,2,2,1,6]
    Output: 4

Constraints:
    1 <= batchSize <= 9
    1 <= groups.length <= 30
    1 <= groups[i] <= 10^9
"""


class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        # exception case
        assert isinstance(batchSize, int) and batchSize >= 1
        assert isinstance(groups, list) and len(groups) >= 1
        # main method: (dynamic programming on bits)
        return self._maxHappyGroups(batchSize, groups)

    def _maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        assert isinstance(batchSize, int) and batchSize >= 1
        assert isinstance(groups, list) and len(groups) >= 1

        k_width = 5
        k_width_mask = (1 << k_width) - 1

        cnt = collections.Counter(x % batchSize for x in groups)

        start = 0
        for i in range(batchSize - 1, 0, -1):
            start = (start << k_width) | cnt[i]

        @functools.cache
        def __dfs(mask: int) -> int:
            if mask == 0:
                return 0

            total = 0
            for idx in range(1, batchSize):
                amount = ((mask >> ((idx - 1) * k_width)) & k_width_mask)
                total += idx * amount

            best = 0
            for idx in range(1, batchSize):
                amount = ((mask >> ((idx - 1) * k_width)) & k_width_mask)
                if amount > 0:
                    result = __dfs(mask - (1 << ((idx - 1) * k_width)))
                    if (total - idx) % batchSize == 0:
                        result += 1
                    best = max(best, result)

            return best

        res = __dfs(start) + cnt[0]
        __dfs.cache_clear()

        return res


def main():
    # Example 1: Output: 4
    # batchSize = 3
    # groups = [1, 2, 3, 4, 5, 6]

    # Example 2: Output: 4
    batchSize = 4
    groups = [1, 3, 2, 5, 2, 2, 1, 6]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maxHappyGroups(batchSize, groups)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
