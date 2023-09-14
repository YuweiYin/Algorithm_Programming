#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0332-Reconstruct-Itinerary.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-09-14
=================================================================="""

import sys
import time
from typing import List
import heapq
import collections
# import functools
# import itertools

"""
LeetCode - 0332 - (Hard) Reconstruct Itinerary
https://leetcode.com/problems/reconstruct-itinerary/

Description & Requirement:
    You are given a list of airline tickets where tickets[i] = [fromi, to_i] represent 
    the departure and the arrival airports of one flight. 
    Reconstruct the itinerary in order and return it.

    All of the tickets belong to a man who departs from "JFK", thus, 
    the itinerary must begin with "JFK". If there are multiple valid itineraries, 
    you should return the itinerary that has the smallest lexical order when read as a single string.

    For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].

    You may assume all tickets form at least one valid itinerary. 
    You must use all the tickets once and only once.

Example 1:
    Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
    Output: ["JFK","MUC","LHR","SFO","SJC"]
Example 2:
    Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
    Explanation: Another possible reconstruction is 
        ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.

Constraints:
    1 <= tickets.length <= 300
    tickets[i].length == 2
    from_i.length == 3
    to_i.length == 3
    from_i and to_i consist of uppercase English letters.
    from_i != to_i
"""


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # exception case
        assert isinstance(tickets, list) and len(tickets) >= 1
        # main method: (DFS: Hierholzer algorithm)
        return self._findItinerary(tickets)

    def _findItinerary(self, tickets: List[List[str]]) -> List[str]:
        assert isinstance(tickets, list) and len(tickets) >= 1

        stack = []

        def __dfs(cur_node: str):
            while vec[cur_node]:
                tmp = heapq.heappop(vec[cur_node])
                __dfs(tmp)
            stack.append(cur_node)

        vec = collections.defaultdict(list)
        for depart, arrive in tickets:
            vec[depart].append(arrive)

        for key in vec:
            heapq.heapify(vec[key])

        __dfs("JFK")

        return stack[::-1]


def main():
    # Example 1: Output: ["JFK","MUC","LHR","SFO","SJC"]
    tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]

    # Example 2: Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
    # tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.findItinerary(tickets)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
