#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1282-Group-the-People-Given-the-Group-Size-They-Belong-To.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-08-12
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1282 - (Medium) - Group the People Given the Group Size They Belong To
https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/

Description & Requirement:
    There are n people that are split into some unknown number of groups. 
    Each person is labeled with a unique ID from 0 to n - 1.

    You are given an integer array groupSizes, where groupSizes[i] is the size of the group that person i is in. 
    For example, if groupSizes[1] = 3, then person 1 must be in a group of size 3.

    Return a list of groups such that each person i is in a group of size groupSizes[i].

    Each person should appear in exactly one group, and every person must be in a group. 
    If there are multiple answers, return any of them. 
    It is guaranteed that there will be at least one valid solution for the given input.

Example 1:
    Input: groupSizes = [3,3,3,3,3,1,3]
    Output: [[5],[0,1,2],[3,4,6]]
    Explanation: 
        The first group is [5]. The size is 1, and groupSizes[5] = 1.
        The second group is [0,1,2]. The size is 3, and groupSizes[0] = groupSizes[1] = groupSizes[2] = 3.
        The third group is [3,4,6]. The size is 3, and groupSizes[3] = groupSizes[4] = groupSizes[6] = 3.
        Other possible solutions are [[2,1,6],[5],[0,4,3]] and [[5],[0,6,2],[4,3,1]].
Example 2:
    Input: groupSizes = [2,1,3,3,3,2]
    Output: [[1],[0,5],[2,3,4]]

Constraints:
    groupSizes.length == n
    1 <= n <= 500
    1 <= groupSizes[i] <= n
"""


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        # exception case
        assert isinstance(groupSizes, list) and len(groupSizes) >= 1
        n = len(groupSizes)
        for size in groupSizes:
            assert isinstance(size, int) and 1 <= size <= n
        # main method: (record size-to-idx hash dict, and then group)
        return self._groupThePeople(groupSizes)

    def _groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        """
        Runtime: 116 ms, faster than 61.63% of Python3 for Group the People Given the Group Size They Belong To.
        Memory Usage: 14 MB, less than 88.49% of Python3 for Group the People Given the Group Size They Belong To.
        """
        assert isinstance(groupSizes, list) and len(groupSizes) >= 1
        # n = len(groupSizes)

        res = []
        size_to_idx = dict({})
        for idx, size in enumerate(groupSizes):
            if size not in size_to_idx:
                size_to_idx[size] = [idx]
            else:
                size_to_idx[size].append(idx)

        for size, v in size_to_idx.items():
            cur_end = size
            while cur_end <= len(v):
                res.append(v[cur_end - size: cur_end])
                cur_end += size

        return res


def main():
    # Example 1: Output: [[5],[0,1,2],[3,4,6]]
    groupSizes = [3, 3, 3, 3, 3, 1, 3]

    # Example 2: Output: [[1],[0,5],[2,3,4]]
    # groupSizes = [2, 1, 3, 3, 3, 2]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.groupThePeople(groupSizes)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
