#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0433-Minimum-Genetic-Mutation.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-05-07
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0433 - (Medium) - Minimum Genetic Mutation
https://leetcode.com/problems/minimum-genetic-mutation/

Description & Requirement:
    A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

    Suppose we need to investigate a mutation from a gene string `start` to a gene string `end` 
    where one mutation is defined as one single character changed in the gene string.
        For example, "AACCGGTT" --> "AACCGGTA" is one mutation.

    There is also a gene bank `bank` that records all the valid gene mutations. 
    A gene must be in `bank` to make it a valid gene string.

    Given the two gene strings start and end and the gene bank `bank`, 
    return the minimum number of mutations needed to mutate from start to end. 
    If there is no such a mutation, return -1.

    Note that the starting point is assumed to be valid, so it might not be included in the bank.

Example 1:
    Input: start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]
    Output: 1
Example 2:
    Input: start = "AACCGGTT", end = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
    Output: 2
Example 3:
    Input: start = "AAAAACCC", end = "AACCCCCC", bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]
    Output: 3

Constraints:
    start.length == 8
    end.length == 8
    0 <= bank.length <= 10
    bank[i].length == 8
    start, end, and bank[i] consist of only the characters ['A', 'C', 'G', 'T'].
"""


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        # exception case
        assert isinstance(start, str) and len(start) == 8
        assert isinstance(end, str) and len(end) == 8
        assert isinstance(bank, list)
        for gene in bank:
            assert isinstance(gene, str) and len(gene) == 8
        # main method: (construct graph and bfs find the shortest path from start to end)
        return self._minMutation(start, end, bank)

    def _minMutation(self, start: str, end: str, bank: List[str]) -> int:
        assert isinstance(start, str) and len(start) == 8
        assert isinstance(end, str) and len(end) == 8
        assert isinstance(bank, list)
        len_bank = len(bank)
        if start == end:
            return 0
        if len_bank == 0:
            return -1

        bank_set = set(bank)
        if end not in bank_set:
            return -1

        gene_base = ["A", "C", "G", "T"]
        gene_len = 8

        graph = dict({})  # key: node (str); value: neighbor node list (List[str])
        node_list = [start] + bank
        # node_set = set(node_list)
        for node in node_list:
            for idx in range(gene_len):  # every char may mutate
                for g_base in gene_base:  # ["A", "C", "G", "T"]
                    possible_mutation = node[0: idx] + g_base + node[idx + 1:]
                    if possible_mutation == node:
                        continue
                    if possible_mutation in bank_set:
                        if node not in graph:
                            graph[node] = {possible_mutation}
                        else:
                            if possible_mutation not in graph[node]:
                                graph[node].add(possible_mutation)
                        if possible_mutation not in graph:
                            graph[possible_mutation] = {node}
                        else:
                            if node not in graph[possible_mutation]:
                                graph[possible_mutation].add(node)

        bfs_queue = [start]  # flooding
        visit_node = {start}
        distance = 0
        find_end = False
        while len(bfs_queue) > 0:
            new_bfs_queue = []
            for node in bfs_queue:
                if node == end:
                    find_end = True
                    break
                if node in graph:
                    for neighbor in graph[node]:
                        if neighbor not in visit_node:
                            visit_node.add(neighbor)
                            new_bfs_queue.append(neighbor)
            if find_end:
                break
            distance += 1
            bfs_queue = new_bfs_queue

        return distance if find_end else -1


def main():
    # Example 1: Output: 1
    # start = "AACCGGTT"
    # end = "AACCGGTA"
    # bank = ["AACCGGTA"]

    # Example 2: Output: 2
    # start = "AACCGGTT"
    # end = "AAACGGTA"
    # bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]

    # Example 3: Output: 3
    start = "AAAAACCC"
    end = "AACCCCCC"
    bank = ["AAAACCCC", "AAACCCCC", "AACCCCCC"]

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.minMutation(start, end, bank)
    _end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((_end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
