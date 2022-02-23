#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0133-Clone-Graph.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-23
=================================================================="""

import sys
import time
from typing import List, Optional
# import collections

"""
LeetCode - 0133 - (Medium) - Clone Graph
https://leetcode.com/problems/clone-graph/

Description & Requirement:
    Given a reference of a node in a connected undirected graph.

    Return a deep copy (clone) of the graph.

    Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
        class Node {
            public int val;
            public List<Node> neighbors;
        }

    Test case format:
        For simplicity, each node's value is the same as the node's index (1-indexed). 
        For example, the first node with val == 1, the second node with val == 2, and so on. 
        The graph is represented in the test case using an adjacency list.

        An adjacency list is a collection of unordered lists used to represent a finite graph. 
        Each list describes the set of neighbors of a node in the graph.

        The given node will always be the first node with val = 1. 
        You must return the copy of the given node as a reference to the cloned graph.

Example 1:
    Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
    Output: [[2,4],[1,3],[2,4],[1,3]]
    Explanation: There are 4 nodes in the graph.
        1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
        2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
        3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
        4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
Example 2:
    Input: adjList = [[]]
    Output: [[]]
    Explanation: Note that the input contains one empty list. 
        The graph consists of only one node with val = 1 and it does not have any neighbors.
Example 3:
    Input: adjList = []
    Output: []
    Explanation: This an empty graph, it does not have any nodes.

Constraints:
    The number of nodes in the graph is in the range [0, 100].
    1 <= Node.val <= 100
    Node.val is unique for each node.
    There are no repeated edges and no self-loops in the graph.
    The Graph is connected and all nodes can be visited starting from the given node.
"""


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        # exception case
        if not isinstance(node, Node):
            return None  # amount == 0, no change is needed
        # main method: (DFS traverse graph, use hash dict to store nodes that have been dealt)
        return self._cloneGraph(node)

    def _cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        node_dict = dict({})  # key: a Node object; value: its clone Node object

        def __dfs(cur_node: Optional[Node]):
            if not isinstance(cur_node, Node):
                return None

            if cur_node in node_dict:  # have cloned this node
                return node_dict[cur_node]

            # do deep cloning, first clone value and create Node object
            clone_node = Node(val=cur_node.val, neighbors=[])

            # record this node in dict
            node_dict[cur_node] = clone_node

            # then DFS clone neighbor nodes
            for neighbor in cur_node.neighbors:
                clone_node.neighbors.append(__dfs(neighbor))

            return clone_node

        return __dfs(node)

    @staticmethod
    def construct_graph(adjList: list) -> list:
        len_nodes = len(adjList)
        if len_nodes == 0:
            return []
        node_list = []
        for node_idx, neighbor_list in enumerate(adjList):
            new_node = Node(val=node_idx + 1, neighbors=neighbor_list)
            node_list.append(new_node)
        return node_list


def main():
    # Example 1: Output: [[2,4],[1,3],[2,4],[1,3]]
    adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]

    # Example 2: Output: [[]]
    # adjList = [[]]

    # Example 3: Output: []
    # adjList = []

    # init instance
    solution = Solution()

    # construct graph
    node_list = solution.construct_graph(adjList)

    # run & time
    start = time.process_time()
    ans = solution.cloneGraph(node_list[0])
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans.val)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
