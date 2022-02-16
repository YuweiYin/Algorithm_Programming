#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1719-Number-Of-Ways-To-Reconstruct-A-Tree.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-16
=================================================================="""

import sys
import time
from typing import List
# import collections

"""
LeetCode - 1719 - (Hard) - Number Of Ways To Reconstruct A Tree
https://leetcode.com/problems/number-of-ways-to-reconstruct-a-tree/

Description & Requirement:
    You are given an array pairs, where pairs[i] = [x_i, y_i], and:
        There are no duplicates.
        x_i < y_i

    Let ways be the number of rooted trees that satisfy the following conditions:
        The tree consists of nodes whose values appeared in pairs.
        A pair [x_i, y_i] exists in pairs if and only if x_i is an ancestor of y_i or y_i is an ancestor of x_i.
        Note: the tree does not have to be a binary tree.

    Two ways are considered to be different if there is at least one node that has different parents in both ways.

    Return:
        0 if ways == 0
        1 if ways == 1
        2 if ways > 1

    A rooted tree is a tree that has a single root node, 
        and all edges are oriented to be outgoing from the root.

    An ancestor of a node is any node on the path from the root to that node 
        (excluding the node itself). The root has no ancestors.

Example 1:
    Input: pairs = [[1,2],[2,3]]
    Output: 1
    Explanation: There is exactly one valid rooted tree, which is shown in the above figure.
Example 2:
    Input: pairs = [[1,2],[2,3],[1,3]]
    Output: 2
    Explanation: There are multiple valid rooted trees.
Example 3:
    Input: pairs = [[1,2],[2,3],[2,4],[1,5]]
    Output: 0
    Explanation: There are no valid rooted trees.

Constraints:
    1 <= pairs.length <= 10^5
    1 <= x_i < y_i <= 500
    The elements in pairs are unique.
"""


class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        # exception case
        assert isinstance(pairs, list) and len(pairs) > 0
        for pair in pairs:
            assert isinstance(pair, list) and len(pair) == 2
        if len(pairs) == 1:
            return 2
        # main method: (try to reconstruct the tree)
        #     if it can't be rebuilt, then return 0;
        #     if built, but exist node that can change position with its ancestor, then return 2; else return 1.
        return self._checkWays(pairs)

    def _checkWays(self, pairs: List[List[int]]) -> int:
        """
        Runtime: 1804 ms, faster than 94.74% of Python3 online submissions for Number Of Ways To Reconstruct A Tree.
        Memory Usage: 45.1 MB, less than 81.58% of Python3 online submissions for Number Of Ways To Reconstruct A Tree.
        """
        len_pairs = len(pairs)
        assert len_pairs >= 2

        # convert paris into ancestor links, if two nodes have a link, then one of them is the ancestor of the other
        ancestor_dict = dict({})
        for pair in pairs:
            if pair[0] == pair[1]:
                continue
            # pair[0] -> pair[1]
            if pair[0] not in ancestor_dict:
                ancestor_dict[pair[0]] = {pair[1]}
            else:
                if pair[1] not in ancestor_dict[pair[0]]:
                    ancestor_dict[pair[0]].add(pair[1])
            # pair[1] -> pair[0]
            if pair[1] not in ancestor_dict:
                ancestor_dict[pair[1]] = {pair[0]}
            else:
                if pair[0] not in ancestor_dict[pair[1]]:
                    ancestor_dict[pair[1]].add(pair[0])

        # a valid root node must be the ancestor of all others
        possible_root = []
        for cur_node, ancestor_node_set in ancestor_dict.items():
            if len(ancestor_node_set) == len(ancestor_dict) - 1:
                possible_root.append(cur_node)

        if len(possible_root) <= 0:
            return 0  # no valid root

        # len(possible_root) may > 1, just choose one of them
        root_node = possible_root[0]

        res = 1  # default: can rebuild only one tree
        for cur_node, ancestor_node_set in ancestor_dict.items():
            # the root_node has no ancestor, so skip checking it (have checked root node is the ancestor of all others)
            if cur_node == root_node:
                continue

            # for every rest node, check if it can find a valid parent node, based on len(ancestor_link_set)
            #     if node_i is the ancestor of node_j, then len(ancestor_dict[node_i]) >= len(ancestor_dict[node_j])
            cur_ancestor_node_len = len(ancestor_node_set)
            parent_node = -int(1e9+7)  # Constraint: 1 <= x_i < y_i <= 500
            parent_ancestor_node_len = int(1e9+7)  # Constraint: 1 <= pairs.length <= 10^5

            # now, find an ancestor to be the parent node of the current node
            for ancestor_node in ancestor_node_set:
                # "parent" is the lowest ancestor
                if cur_ancestor_node_len <= len(ancestor_dict[ancestor_node]) < parent_ancestor_node_len:
                    parent_node = ancestor_node
                    parent_ancestor_node_len = len(ancestor_dict[ancestor_node])

            # can't find a valid parent, so can't rebuild the tree
            if parent_node < 0:
                return 0

            # now check if ancestor_dict[cur_node] is a subset of ancestor_dict[parent_node]
            for ancestor_node in ancestor_node_set:
                if ancestor_node != parent_node and ancestor_node not in ancestor_dict[parent_node]:
                    return 0

            # now check if len(ancestor_dict[cur_node]) == len(ancestor_dict[parent_node])
            #     if so, cur_node and parent_node are exchangeable in the rebuilt tree
            if cur_ancestor_node_len == parent_ancestor_node_len:
                res = 2  # if the tree can be built at last, then `return res` will be `return 2` rather than 1

        return res


def main():
    # Example 1: Output: 1
    # pairs = [[1, 2], [2, 3]]

    # Example 2: Output: 2
    # pairs = [[1, 2], [2, 3], [1, 3]]

    # Example 3: Output: 0
    # pairs = [[1, 2], [2, 3], [2, 4], [1, 5]]

    # Example 4: Output: 0
    pairs = [[9, 14], [5, 13], [8, 14], [12, 13], [7, 14], [7, 8], [3, 5], [6, 14], [10, 14], [8, 13], [5, 8], [3, 9],
             [3, 13], [3, 10], [5, 10], [10, 13], [4, 14], [3, 12], [6, 13], [12, 14], [13, 14], [5, 7], [3, 15],
             [11, 14], [14, 15], [2, 3], [3, 8], [9, 15], [2, 14], [3, 14], [1, 14], [1, 3], [2, 11], [3, 6], [1, 2],
             [7, 13], [3, 11], [5, 14]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.checkWays(pairs)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
