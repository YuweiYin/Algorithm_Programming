#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0310-Minimum-Height-Trees.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-06
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 0310 - (Medium) - Minimum Height Trees
https://leetcode.com/problems/minimum-height-trees/

Description & Requirement:
    A tree is an undirected graph in which any two vertices are connected by exactly one path. 
    In other words, any connected graph without simple cycles is a tree.

    Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [a_i, b_i] 
    indicates that there is an undirected edge between the two nodes a_i and b_i in the tree, 
    you can choose any node of the tree as the root. When you select a node x as the root, 
    the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h)) 
    are called minimum height trees (MHTs).

    Return a list of all MHTs' root labels. You can return the answer in any order.

    The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

Example 1:
    Input: n = 4, edges = [[1,0],[1,2],[1,3]]
    Output: [1]
    Explanation: the height of the tree is 1 when the root is the node with label 1 which is the only MHT.
Example 2:
    Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
    Output: [3,4]

Constraints:
    1 <= n <= 2 * 10^4
    edges.length == n - 1
    0 <= a_i, b_i < n
    a_i != b_i
    All the pairs (a_i, b_i) are distinct.
    The given input is guaranteed to be a tree and there will be no repeated edges.
"""


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # exception case
        assert isinstance(n, int) and n >= 1
        assert isinstance(edges, list) and len(edges) == n - 1
        # main method: (bfs)
        return self._findMinHeightTrees(n, edges)

    def _findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # build graph
        graph = dict({})
        for node in range(n):
            graph[node] = []
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        # record the parent node of each node on the bfs traverse path
        parent_nodes = [0 for _ in range(n)]

        def __bfs(source_node: int) -> int:  # find the farthest node from the source_node
            bfs_queue = collections.deque()
            visited = [False for _ in range(n)]

            bfs_queue.append(source_node)
            visited[source_node] = True

            cur_node = source_node

            while len(bfs_queue) > 0:
                cur_node = bfs_queue.popleft()
                for neighbor_node in graph[cur_node]:
                    if not visited[neighbor_node]:
                        visited[neighbor_node] = True
                        bfs_queue.append(neighbor_node)
                        parent_nodes[neighbor_node] = cur_node  # record parent node

            return cur_node

        # find the farthest node from the source_node
        random_source_node = 0
        longest_path_end_1 = __bfs(random_source_node)  # one end of the longest path
        longest_path_end_2 = __bfs(longest_path_end_1)  # the other end of the longest path

        # reconstruct the longest path
        longest_path = []
        parent_nodes[longest_path_end_1] = -1
        while longest_path_end_2 != -1:
            longest_path.append(longest_path_end_2)
            longest_path_end_2 = parent_nodes[longest_path_end_2]

        len_path = len(longest_path)
        if len_path & 0x01 == 1:  # the number of nodes is odd, so the exact middle node is the target root node
            return [longest_path[len_path >> 1]]
        else:  # the number of nodes is even, so the two middle nodes are the target root nodes
            return [longest_path[(len_path >> 1) - 1], longest_path[len_path >> 1]]


def main():
    # Example 1: Output: [1]
    n = 4
    edges = [[1, 0], [1, 2], [1, 3]]

    # Example 2: Output: [3,4]
    # n = 6
    # edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.findMinHeightTrees(n, edges)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
