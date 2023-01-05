#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1803-Count-Pairs-With-XOR-in-a-Range.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-01-05
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1803 - (Hard) - Count Pairs With XOR in a Range
https://leetcode.com/problems/count-pairs-with-xor-in-a-range/

Description & Requirement:
    Given a (0-indexed) integer array nums and two integers low and high, return the number of nice pairs.

    A nice pair is a pair (i, j) where 0 <= i < j < nums.length and low <= (nums[i] XOR nums[j]) <= high.

Example 1:
    Input: nums = [1,4,2,7], low = 2, high = 6
    Output: 6
    Explanation: All nice pairs (i, j) are as follows:
        - (0, 1): nums[0] XOR nums[1] = 5 
        - (0, 2): nums[0] XOR nums[2] = 3
        - (0, 3): nums[0] XOR nums[3] = 6
        - (1, 2): nums[1] XOR nums[2] = 6
        - (1, 3): nums[1] XOR nums[3] = 3
        - (2, 3): nums[2] XOR nums[3] = 5
Example 2:
    Input: nums = [9,8,4,2,1], low = 5, high = 14
    Output: 8
    Explanation: All nice pairs (i, j) are as follows:
        - (0, 2): nums[0] XOR nums[2] = 13
        - (0, 3): nums[0] XOR nums[3] = 11
        - (0, 4): nums[0] XOR nums[4] = 8
        - (1, 2): nums[1] XOR nums[2] = 12
        - (1, 3): nums[1] XOR nums[3] = 10
        - (1, 4): nums[1] XOR nums[4] = 9
        - (2, 3): nums[2] XOR nums[3] = 6
        - (2, 4): nums[2] XOR nums[4] = 5

Constraints:
    1 <= nums.length <= 2 * 10^4
    1 <= nums[i] <= 2 * 10^4
    1 <= low <= high <= 2 * 10^4
"""


class TrieNode:
    def __init__(self):
        self.children = [None, None]
        self.sum = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.HIGH_BIT = 14

    def add(self, num: int) -> None:
        cur_node = self.root
        for k in range(self.HIGH_BIT, -1, -1):
            bit = (num >> k) & 1
            if not isinstance(cur_node.children[bit], TrieNode):
                cur_node.children[bit] = TrieNode()
            cur_node = cur_node.children[bit]
            cur_node.sum += 1

    def get(self, num: int, x: int) -> int:
        res = 0
        cur_node = self.root
        for k in range(self.HIGH_BIT, -1, -1):
            bit = (num >> k) & 1
            if (x >> k) & 1:
                if cur_node.children[bit]:
                    res += cur_node.children[bit].sum
                if not cur_node.children[bit ^ 1]:
                    return res
                cur_node = cur_node.children[bit ^ 1]
            else:
                if not cur_node.children[bit]:
                    return res
                cur_node = cur_node.children[bit]

        res += cur_node.sum
        return res


class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        assert isinstance(low, int) and isinstance(high, int) and 1 <= low <= high
        # main method: (Trie)
        return self._countPairs(nums, low, high)

    def _countPairs(self, nums: List[int], low: int, high: int) -> int:
        assert isinstance(nums, list) and len(nums) >= 1
        assert isinstance(low, int) and isinstance(high, int) and 1 <= low <= high

        def _trie(nums: List[int], x: int) -> int:
            res = 0
            trie = Trie()
            for i in range(1, len(nums)):
                trie.add(nums[i - 1])
                res += trie.get(nums[i], x)
            return res

        return _trie(nums, high) - _trie(nums, low - 1)


def main():
    # Example 1: Output: 6
    # nums = [1, 4, 2, 7]
    # low = 2
    # high = 6

    # Example 2: Output: 8
    nums = [9, 8, 4, 2, 1]
    low = 5
    high = 14

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.countPairs(nums, low, high)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
