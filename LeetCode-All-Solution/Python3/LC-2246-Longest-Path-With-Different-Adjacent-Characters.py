#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2287-Rearrange-Characters-to-Make-Target-String.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-01-13
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 2287 - (Hard) - Longest Path With Different Adjacent Characters
https://leetcode.com/problems/longest-path-with-different-adjacent-characters/

Description & Requirement:
    You are given a tree (i.e. a connected, undirected graph that has no cycles) rooted at node 0 
    consisting of n nodes numbered from 0 to n - 1. The tree is represented by a 0-indexed array parent of size n, 
    where parent[i] is the parent of node i. Since node 0 is the root, parent[0] == -1.

    You are also given a string s of length n, where s[i] is the character assigned to node i.

    Return the length of the longest path in the tree such that 
    no pair of adjacent nodes on the path have the same character assigned to them.

Example 1:
    Input: parent = [-1,0,0,1,1,2], s = "abacbe"
    Output: 3
    Explanation: The longest path where each two adjacent nodes have different characters in the tree is the path: 
        0 -> 1 -> 3. The length of this path is 3, so 3 is returned.
        It can be proven that there is no longer path that satisfies the conditions. 
Example 2:
    Input: parent = [-1,0,0,0], s = "aabc"
    Output: 3
    Explanation: The longest path where each two adjacent nodes have different characters is the path: 2 -> 0 -> 3. 
        The length of this path is 3, so 3 is returned.

Constraints:
    n == parent.length == s.length
    1 <= n <= 10^5
    0 <= parent[i] <= n - 1 for all i >= 1
    parent[0] == -1
    parent represents a valid tree.
    s consists of only lowercase English letters.
"""


class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        # exception case
        assert isinstance(parent, list) and len(parent) >= 1
        assert isinstance(s, str) and len(s) == len(parent)
        # main method: (Tree DP)
        return self._longestPath(parent, s)

    def _longestPath(self, parent: List[int], s: str) -> int:
        """
        Time: beats 95.75%; Space: beats 87.25%
        """
        assert isinstance(parent, list) and len(parent) >= 1
        assert isinstance(s, str) and len(s) == len(parent)

        n = len(parent)
        graph = [[] for _ in range(n)]
        for i in range(1, n):
            graph[parent[i]].append(i)

        res = [0]

        def __dfs(x: int) -> int:
            max_len = 0
            for y in graph[x]:
                cur_len = __dfs(y) + 1
                if s[y] != s[x]:
                    res[0] = max(res[0], max_len + cur_len)
                    max_len = max(max_len, cur_len)
            return max_len

        __dfs(0)

        return res[0] + 1


def main():
    # Example 1: Output: 3
    parent = [-1, 0, 0, 1, 1, 2]
    s = "abacbe"

    # Example 2: Output: 3
    # parent = [-1, 0, 0, 0]
    # s = "aabc"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.longestPath(parent, s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
