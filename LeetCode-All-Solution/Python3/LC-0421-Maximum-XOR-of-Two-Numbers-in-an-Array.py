#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0421-Maximum-XOR-of-Two-Numbers-in-an-Array.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-27
=================================================================="""

import sys
import time
from typing import List
# import collections

"""
LeetCode - 0421 - (Medium) - Maximum XOR of Two Numbers in an Array
https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

Description & Requirement:
    Given an integer array nums, 
    return the maximum result of nums[i] XOR nums[j], where 0 <= i <= j < n.

Example 1:
    Input: nums = [3,10,5,25,2,8]
    Output: 28
    Explanation: The maximum result is 5 XOR 25 = 28.
Example 2:
    Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
    Output: 127

Constraints:
    1 <= nums.length <= 2 * 10^5
    0 <= nums[i] <= 2^31 - 1
"""


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        # exception case
        if not isinstance(nums, list) or len(nums) <= 0:
            return 0  # Error input type
        if len(nums) == 1:
            return 0  # nums[0] ^ nums[0] == 0
        if len(nums) == 2:
            return nums[0] ^ nums[1]
        # main method: (Bit Manipulation)
        #     idea: each number can be represented as a 32-bit binary number
        #           from the highest bit, if there exists two number, such that XOR result of this bit is 1,
        #               then this bit of the final XOR result can be 1. otherwise, have to be 0
        return self._findMaximumXOR(nums)

    def _findMaximumXOR(self, nums: List[int]) -> int:
        """
        Trie, left child means this bit is 0, the right child means this bit is 1
        """
        len_nums = len(nums)
        assert len_nums >= 3

        class Trie:
            def __init__(self, left=None, right=None):
                self.left = left  # left child means this bit is 0
                self.right = right  # the right child means this bit is 1

            # def __del__(self):
            #     # traverse all nodes and del them all
            #
            #     def __dfs(node):  # post-order traverse
            #         if isinstance(node, Trie):
            #             __dfs(node.left)
            #             __dfs(node.right)
            #             del node
            #
            #     __dfs(self)

            @staticmethod
            def del_nodes(trie_node):
                # traverse all nodes and del them all

                def __dfs(node):  # post-order traverse
                    if isinstance(node, Trie):
                        __dfs(node.left)
                        __dfs(node.right)
                        del node

                __dfs(trie_node)

        root_node = Trie()
        MAX_BIT = 32  # 0 <= nums[i] <= 2^31 - 1

        def __add_number(node: Trie, number: int) -> None:
            """
            add new node to the Trie
            a path from root of Trie to a leaf means a number
            """
            cur_node = node  # travel pointer
            assert isinstance(cur_node, Trie)
            for mask in range(MAX_BIT, -1, -1):  # set mask, deal with each bit (from the highest to the lowest)
                cur_bit = (number >> mask) & 0x01
                if cur_bit == 0:  # 0, left child
                    if not isinstance(cur_node.left, Trie):
                        cur_node.left = Trie()  # no left child, so create it
                    cur_node = cur_node.left  # go left
                else:
                    if not isinstance(cur_node.right, Trie):
                        cur_node.right = Trie()  # no right child, so create it
                    cur_node = cur_node.right  # go right

        def __do_xor(node: Trie, number: int) -> int:
            """
            do xor, get the max possible result, using number and the current Trie
            """
            cur_node = node  # travel pointer
            assert isinstance(cur_node, Trie)
            max_xor_res = 0

            for mask in range(MAX_BIT, -1, -1):  # set mask, deal with each bit (from the highest to the lowest)
                cur_bit = (number >> mask) & 0x01
                if cur_bit == 0:  # this bit of number is 0, need to find 1 in Trie to get a bit 1
                    if isinstance(cur_node.right, Trie):
                        cur_node = cur_node.right  # go right
                        max_xor_res = (max_xor_res << 1) + 1  # the xor result of this bit is 1 (0 xor 1)
                    else:  # no 1 in Trie, can only do xor with 0, get 0
                        assert isinstance(cur_node.left, Trie)
                        cur_node = cur_node.left
                        max_xor_res <<= 1  # the xor result of this bit is 0 (0 xor 0)
                else:  # this bit of number is 1, need to find 0 in Trie to get a bit 1
                    if isinstance(cur_node.left, Trie):
                        cur_node = cur_node.left  # go left
                        max_xor_res = (max_xor_res << 1) + 1  # the xor result of this bit is 1 (1 xor 0)
                    else:  # no 0 in Trie, can only do xor with 1, get 0
                        assert isinstance(cur_node.right, Trie)
                        cur_node = cur_node.right  # go right
                        max_xor_res <<= 1  # the xor result of this bit is 0 (1 xor 1)

            return max_xor_res

        max_res = 0
        num_idx = 0
        while num_idx < len_nums - 1:
            __add_number(root_node, nums[num_idx])  # put in nums[num_idx]
            max_res = max(max_res, __do_xor(root_node, nums[num_idx + 1]))  # use nums[num_idx + 1] to do xor in Trie
            num_idx += 1

        # del root_node (more: import os;  gc.collect())
        Trie.del_nodes(root_node)
        return max_res


def main():
    # Example 1: Output: 28
    #     Explanation: The maximum result is 5 XOR 25 = 28.
    # nums = [3, 10, 5, 25, 2, 8]

    # Example 2: Output: 127
    nums = [14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.findMaximumXOR(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
