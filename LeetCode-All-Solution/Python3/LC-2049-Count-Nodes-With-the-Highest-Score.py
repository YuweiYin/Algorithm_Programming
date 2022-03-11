#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2049-Count-Nodes-With-the-Highest-Score.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-11
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 2049 - (Medium) - Count Nodes With the Highest Score
https://leetcode.com/problems/count-nodes-with-the-highest-score/

Description & Requirement:
    There is a binary tree rooted at 0 consisting of n nodes. The nodes are labeled from 0 to n - 1. 
    You are given a 0-indexed integer array parents representing the tree, 
    where parents[i] is the parent of node i. Since node 0 is the root, parents[0] == -1.

    Each node has a score. To find the score of a node, 
    consider if the node and the edges connected to it were removed. 
    The tree would become one or more non-empty subtrees. 
    The size of a subtree is the number of the nodes in it. 
    The score of the node is the product of the sizes of all those subtrees.

    Return the number of nodes that have the highest score.

Example 1:
    Input: parents = [-1,2,0,2,0]
    Output: 3
    Explanation:
        - The score of node 0 is: 3 * 1 = 3
        - The score of node 1 is: 4 = 4
        - The score of node 2 is: 1 * 1 * 2 = 2
        - The score of node 3 is: 4 = 4
        - The score of node 4 is: 4 = 4
        The highest score is 4, and three nodes (node 1, node 3, and node 4) have the highest score.
Example 2:
    Input: parents = [-1,2,0]
    Output: 2
    Explanation:
        - The score of node 0 is: 2 = 2
        - The score of node 1 is: 2 = 2
        - The score of node 2 is: 1 * 1 = 1
        The highest score is 2, and two nodes (node 0 and node 1) have the highest score.

Constraints:
    n == parents.length
    2 <= n <= 10^5
    parents[0] == -1
    0 <= parents[i] <= n - 1 for i != 0
    parents represents a valid binary tree.
"""


class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        # exception case
        assert isinstance(parents, list) and len(parents) >= 2
        # main method: (DFS preprocess get the size of every subtree)
        #     when a node has been deleted, at most 3 subtrees will be count (left/right child and root to its parent)
        return self._countHighestScoreNodes(parents)

    def _countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        assert n >= 2

        # get tree
        tree_dict = dict({})  # key: node; value: it's direct child list
        for node in range(n):
            tree_dict[node] = []
        for node, parent in enumerate(parents):
            if parent in tree_dict:
                tree_dict[parent].append(node)

        # DFS preprocess get the size of every subtree
        subtree_size = [0 for _ in range(n)]

        def __dfs(cur_node: int):
            if len(tree_dict[cur_node]) == 0:  # cur_node is a leaf, subtree size == 1
                subtree_size[cur_node] = 1
                return 1
            else:  # cur_node has child, subtree size == 1 + sum(every child subtree size)
                _size = sum([__dfs(child_node) for child_node in tree_dict[cur_node]]) + 1
                subtree_size[cur_node] = _size
                return _size

        __dfs(0)

        # now consider deleting every node
        score_dict = dict({})  # key: score; value: counter
        root_subtree_size = subtree_size[0]
        for delete_node in range(n):
            cur_score = 1
            for child in tree_dict[delete_node]:  # all children
                if  subtree_size[child] > 0:
                    cur_score *= subtree_size[child]
            # root_node minus delete_node
            parent_subtree_size = root_subtree_size - subtree_size[delete_node]
            if parent_subtree_size > 0:
                cur_score *= parent_subtree_size
            # update score_dict
            if cur_score not in score_dict:
                score_dict[cur_score] = 1
            else:
                score_dict[cur_score] += 1

        # get the counter of the best score
        max_score = 0
        res = 0
        for score, counter in score_dict.items():
            if score > max_score:
                max_score = score
                res = counter

        return res


def main():
    # Example 1: Output: 3
    parents = [-1, 2, 0, 2, 0]

    # Example 2: Output: 2
    # parents = [-1, 2, 0]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.countHighestScoreNodes(parents)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
