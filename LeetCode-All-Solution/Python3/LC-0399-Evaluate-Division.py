#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0399-Evaluate-Division.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-30
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0399 - (Medium) - Evaluate Division
https://leetcode.com/problems/evaluate-division/

Description & Requirement:
    You are given an array of variable pairs equations and an array of real numbers values, 
    where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. 
    Each Ai or Bi is a string that represents a single variable.

    You are also given some queries, where queries[j] = [Cj, Dj] represents 
        the jth query where you must find the answer for Cj / Dj = ?.

    Return the answers to all queries. If a single answer cannot be determined, return -1.0.

    Note: The input is always valid. You may assume that evaluating the queries will not result in 
        division by zero and that there is no contradiction.

Example 1:
    Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], 
        queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
    Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
    Explanation: 
        Given: a / b = 2.0, b / c = 3.0
        queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
        return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
Example 2:
    Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], 
        queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
    Output: [3.75000,0.40000,5.00000,0.20000]
Example 3:
    Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
    Output: [0.50000,2.00000,-1.00000,-1.00000]

Constraints:
    1 <= equations.length <= 20
    equations[i].length == 2
    1 <= Ai.length, Bi.length <= 5
    values.length == equations.length
    0.0 < values[i] <= 20.0
    1 <= queries.length <= 20
    queries[i].length == 2
    1 <= Cj.length, Dj.length <= 5
    Ai, Bi, Cj, Dj consist of lower case English letters and digits.
"""


class UnionFindSet:
    def __init__(self, n):
        self.n = n  # the number of initial sets
        # self.rank = [1 for _ in range(n)]  # initially, each set has only 1 element with rank 1 (rank: set length)
        self.disjoint_set = list(range(n))  # if d_s[i] == d_s[j], then element i and j are in the same set
        self.value = [float(1.0) for _ in range(n)]   # if x/y == 2, then self.disjoint_set[x] = b, self.value[a] = 2

    def find_set(self, x: int) -> int:
        if self.disjoint_set[x] == x:  # x is the root element of a set, just return it
            return x
        origin_x = self.disjoint_set[x]
        self.disjoint_set[x] = self.find_set(self.disjoint_set[x])  # recursively merge links to the root of the set
        self.value[x] *= self.value[origin_x]
        return self.disjoint_set[x]

    def union_set(self, x: int, y: int, val: float) -> bool:
        set_x, set_y = self.find_set(x), self.find_set(y)  # find the set roots of element x and y separately
        if set_x == set_y:  # no need to union
            return False

        # if self.rank[set_x] < self.rank[set_y]:  # let set_x be the larger set (with larger rank)
        #     set_x, set_y = set_y, set_x

        # self.rank[set_x] += self.rank[set_y]
        # self.disjoint_set[set_y] = set_x
        self.disjoint_set[set_x] = set_y
        self.value[set_x] = self.value[y] * val / self.value[x]  # calculate the root value
        return True


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # exception case
        assert isinstance(equations, list) and len(equations) >= 1
        assert isinstance(values, list) and len(values) == len(equations)
        assert isinstance(queries, list) and len(queries) >= 1
        # main method: (construct graph, use UnionFindSet)
        return self._calcEquation(equations, values, queries)

    def _calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        assert isinstance(equations, list) and len(equations) >= 1
        assert isinstance(values, list) and len(values) == len(equations)
        assert isinstance(queries, list) and len(queries) >= 1

        equ_len = len(equations)
        ufs = UnionFindSet(equ_len << 1)

        graph = dict({})  # key: node (str); value: node_id (int) in UnionFindSet
        node_id = 0
        for idx in range(equ_len):
            cur_equ = equations[idx]
            cur_node1, cur_node2 = cur_equ[0], cur_equ[1]
            if cur_node1 not in graph:
                graph[cur_node1] = node_id
                node_id += 1
            if cur_node2 not in graph:
                graph[cur_node2] = node_id
                node_id += 1
            ufs.union_set(graph[cur_node1], graph[cur_node2], values[idx])

        # query
        query_len = len(queries)
        res = []
        for idx in range(query_len):
            cur_node1, cur_node2 = queries[idx][0], queries[idx][1]
            node_id1 = graph[cur_node1] if cur_node1 in graph else None
            node_id2 = graph[cur_node2] if cur_node2 in graph else None

            if node_id1 is None or node_id2 is None:
                res.append(float(-1.0))
            else:
                set1, set2 = ufs.find_set(node_id1), ufs.find_set(node_id2)
                if set1 == set2:  # node_id1 and node_id2 are linked together
                    res.append(float(ufs.value[node_id1] / ufs.value[node_id2]))
                else:
                    res.append(float(-1.0))

        return res


def main():
    # Example 1: Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
    # equations = [["a", "b"], ["b", "c"]]
    # values = [2.0, 3.0]
    # queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]

    # Example 2: Output: [3.75000,0.40000,5.00000,0.20000]
    # equations = [["a", "b"], ["b", "c"], ["bc", "cd"]]
    # values = [1.5, 2.5, 5.0]
    # queries = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]

    # Example 3: Output: [0.50000,2.00000,-1.00000,-1.00000]
    equations = [["a", "b"]]
    values = [0.5]
    queries = [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.calcEquation(equations, values, queries)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
