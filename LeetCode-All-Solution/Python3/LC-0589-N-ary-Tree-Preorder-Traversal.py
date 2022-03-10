#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0589-N-ary-Tree-Preorder-Traversal.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-10
=================================================================="""

import sys
import time
from typing import List, Optional

"""
LeetCode - 0589 - (Easy) - N-ary Tree Preorder Traversal
https://leetcode.com/problems/n-ary-tree-preorder-traversal/

Description & Requirement:
    Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

    Nary-Tree input serialization is represented in their level order traversal. 
    Each group of children is separated by the null value (See examples)

Example 1:
    Input: root = [1,null,3,2,4,null,5,6]
    Output: [1,3,5,6,2,4]
Example 2:
    Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
    Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]

Constraints:
    The number of nodes in the tree is in the range [0, 10^4].
    0 <= Node.val <= 10^4
    The height of the n-ary tree is less than or equal to 1000.
"""


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

    @staticmethod
    def build_tree_layer(val_list):
        node_list = []
        group_nodes = []
        for val in val_list:
            if val is None:
                if len(group_nodes) > 0:
                    node_list.append(group_nodes[:])
                    group_nodes = []
                continue
            new_node = Node(val=val)
            group_nodes.append(new_node)
        if len(group_nodes) > 0:
            node_list.append(group_nodes)

        pass  # TODO


class Solution:
    def preorder(self, root: Optional[Node]) -> List[int]:
        # exception case
        if not isinstance(root, Node):
            return []
        # main method: (pre-order traverse)
        return self._preorder(root)

    def _preorder(self, root: Optional[Node]) -> List[int]:

        res = []

        def __dfs(cur_node: Optional[Node]):
            if isinstance(cur_node, Node):
                res.append(cur_node.val)
                for child in cur_node.children:
                    __dfs(child)

        __dfs(root)
        return res


def main():
    # Example 1: Output: [1,3,5,6,2,4]
    root = [1, None, 3, 2, 4, None, 5, 6]

    # Example 2: Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]
    # root = [
    #     1,
    #     None, 2, 3, 4, 5,
    #     None, None, 6, 7, None, 8, None, 9, 10,
    #     None, None, 11, None, 12, None, 13, None,
    #     None, 14
    # ]

    root_node = Node.build_tree_layer(root)  # TODO

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.preorder(root_node)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
