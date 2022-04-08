#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0429-N-ary-Tree-Level-Order-Traversal.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-08
=================================================================="""

# import collections
import sys
import time
from typing import List, Optional

"""
LeetCode - 0429 - (Medium) - N-ary Tree Level Order Traversal
https://leetcode.com/problems/n-ary-tree-level-order-traversal/

Description:
    Given an n-ary tree, return the level order traversal of its nodes' values.

    Nary-Tree input serialization is represented in their level order traversal, 
    each group of children is separated by the null value.

Example 1:
    Input: root = [1,null,3,2,4,null,5,6]
    Output: [[1],[3,2,4],[5,6]]
Example 2:
    Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
    Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]

Constraints:
    The height of the n-ary tree is less than or equal to 1000
    The total number of nodes is between [0, 10^4]
"""


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: Optional[Node]) -> List[List[int]]:
        # exception case
        if not isinstance(root, Node):
            return []
        # main method: (BFS)
        return self._levelOrder(root)

    def _levelOrder(self, root: Optional[Node]) -> List[List[int]]:
        res = []

        bfs_queue = [root]
        while len(bfs_queue) > 0:
            new_bfs_queue = []
            cur_layer = []
            for node in bfs_queue:
                cur_layer.append(node.val)
                if isinstance(node.children, list) and len(node.children) > 0:
                    new_bfs_queue.extend(node.children)
            res.append(cur_layer)
            bfs_queue = new_bfs_queue

        return res


def main():
    # Example 1: Output: [[1],[3,2,4],[5,6]]
    # root = [1, None, 3, 2, 4, None, 5, 6]

    # Example 2: Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
    # root = [1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10,
    #         None, None, 11, None, 12, None, 13, None, None, 14]

    node_1 = Node(val=1)
    node_2 = Node(val=2)
    node_3 = Node(val=3)
    node_4 = Node(val=4)
    node_5 = Node(val=5)
    node_6 = Node(val=6)
    node_1.children = [node_3, node_2, node_4]
    node_3.children = [node_5, node_6]
    root_node = node_1

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.levelOrder(root_node)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
