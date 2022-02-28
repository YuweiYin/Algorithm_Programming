#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1601-Maximum-Number-of-Achievable-Transfer-Requests.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-28
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 1601 - (Hard) - Maximum Number of Achievable Transfer Requests
https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/

Description & Requirement:
    We have n buildings numbered from 0 to n - 1. Each building has a number of employees. 
    It's transfer season, and some employees want to change the building they reside in.

    You are given an array requests where requests[i] = [from_i, to_i] represents 
    an employee's request to transfer from building from_i to building to_i.

    All buildings are full, so a list of requests is achievable only if for each building, 
    the net change in employee transfers is zero. This means the number of employees leaving 
    is equal to the number of employees moving in. For example if n = 3 and two employees are leaving building 0, 
    one is leaving building 1, and one is leaving building 2, there should be two employees moving to building 0, 
    one employee moving to building 1, and one employee moving to building 2.

    Return the maximum number of achievable requests.

Example 1:
    Input: n = 5, requests = [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]
    Output: 5
    Explanation: Let's see the requests:
        From building 0 we have employees x and y and both want to move to building 1.
        From building 1 we have employees a and b and they want to move to buildings 2 and 0 respectively.
        From building 2 we have employee z and they want to move to building 0.
        From building 3 we have employee c and they want to move to building 4.
        From building 4 we don't have any requests.
        We can achieve the requests of users x and b by swapping their places.
        We can achieve the requests of users y, a and z by swapping the places in the 3 buildings.
Example 2:
    Input: n = 3, requests = [[0,0],[1,2],[2,1]]
    Output: 3
    Explanation: Let's see the requests:
        From building 0 we have employee x and they want to stay in the same building 0.
        From building 1 we have employee y and they want to move to building 2.
        From building 2 we have employee z and they want to move to building 1.
        We can achieve all the requests. 
Example 3:
    Input: n = 4, requests = [[0,3],[3,1],[1,2],[2,0]]
    Output: 4

Constraints:
    1 <= n <= 20
    1 <= requests.length <= 16
    requests[i].length == 2
    0 <= from_i, to_i < n
"""


class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        # exception case
        assert isinstance(requests, list) and len(requests) > 0 and n > 0
        for request in requests:
            assert isinstance(request, list) and len(request) == 2
        # main method: (Graph, vertices is 0 ~ n-1, edges is all requests)
        #     aim is to find circles in the graph and accumulate the length of every circle, including the self-loop
        #     once find a circle, accumulate its length and remove it from graph, then repeat finding until no circles
        #     dfs & backtrace, either find the smallest circle or find the largest circle
        # return self._maximumRequestsGraph(n, requests)
        # method 2: try 2^(len(requests)) cases
        return self._maximumRequests(n, requests)

    def _maximumRequestsGraph(self, n: int, requests: List[List[int]]) -> int:
        """
        pass test cases: 115 / 117
        """
        res = [0]

        # construct graph
        graph = dict({})  # key: node; value: its neighbors
        for node in range(n):
            graph[node] = []
        for request in requests:
            if request[0] == request[1]:  # self-loop
                res[0] += 1
            else:  # not self-loop
                graph[request[0]].append(request[1])

        bfs_queue = collections.deque()  # element: (node_path: list, visit_mask: int)

        def __remove_circle(n_list: list):
            n_list_len = len(n_list)
            for from_node_idx in range(n_list_len):
                to_node_idx = (from_node_idx + 1) % n_list_len
                from_node, to_node = n_list[from_node_idx], n_list[to_node_idx]
                for _node in graph[from_node]:  # remove one link from_node -> to_node
                    if _node == to_node:
                        graph[from_node].remove(to_node)
                        break

        def __recover_circle(n_list: list):
            n_list_len = len(n_list)
            for from_node_idx in range(n_list_len):
                to_node_idx = (from_node_idx + 1) % n_list_len
                from_node, to_node = n_list[from_node_idx], n_list[to_node_idx]
                graph[from_node].append(to_node)  # recover one link from_node -> to_node

        def __find_smallest_circle(start_node: int) -> List[int]:
            """
            :return: the smallest circle from start_node; if no circles from start_node, then return 0
            """
            if len(graph[start_node]) == 0:  # start_node has no neighbors
                return []

            bfs_queue.clear()

            for neighbor in graph[start_node]:  # put in all the neighbors of start_node
                bfs_queue.append(([start_node, neighbor], (1 << start_node) | (1 << neighbor)))

            while len(bfs_queue) > 0:
                node_path, visit_mask = bfs_queue.popleft()
                cur_node = node_path[-1]
                for cur_neighbor in graph[cur_node]:
                    if cur_neighbor == start_node:  # form a circle
                        # remove this circle
                        # print(node_path)
                        # circle_nodes = len(node_path)
                        # __remove_circle(node_path)
                        # return circle length
                        # return circle_nodes
                        return node_path[:]
                    if (1 << cur_neighbor) & visit_mask == 0:
                        new_visit_mask = visit_mask | (1 << cur_neighbor)
                        new_path = node_path.copy()
                        new_path.append(cur_neighbor)
                        bfs_queue.append((new_path, new_visit_mask))
                # del node_path

            # no circles
            return []

        def __find_largest_circle(start_node: int) -> List[int]:
            """
            :return: the largest circle from start_node; if no circles from start_node, then return 0
            """
            if len(graph[start_node]) == 0:  # start_node has no neighbors
                return []

            bfs_queue.clear()
            largest_path = []

            for neighbor in graph[start_node]:  # put in all the neighbors of start_node
                bfs_queue.append(([start_node, neighbor], (1 << start_node) | (1 << neighbor)))

            while len(bfs_queue) > 0:
                node_path, visit_mask = bfs_queue.popleft()
                cur_node = node_path[-1]
                for cur_neighbor in graph[cur_node]:
                    if cur_neighbor == start_node:  # form a circle
                        # remove this circle
                        if len(node_path) > len(largest_path):
                            largest_path = node_path
                    if (1 << cur_neighbor) & visit_mask == 0:
                        new_visit_mask = visit_mask | (1 << cur_neighbor)
                        new_path = node_path.copy()
                        new_path.append(cur_neighbor)
                        bfs_queue.append((new_path, new_visit_mask))

            # remove the largest circle
            # print(largest_path)
            # circle_nodes = len(largest_path)
            # __remove_circle(largest_path)
            # return circle_nodes
            return largest_path[:]

        # has_circle = True
        # while has_circle:
        #     accumulation = 0
        #     for node in range(n):  # start from every node
        #         # accumulation += __find_circle(node)
        #         accumulation += __find_largest_circle(node)
        #     if accumulation == 0:  # no circles
        #         has_circle = False
        #     else:
        #         res[0] += accumulation

        # TODO: dfs & backtrace, either find the smallest circle or find the largest circle

        return res[0]

    def _maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        res = 0

        # use binary number to indicate if choose a request or not (1 <= requests.length <= 16)
        for request_mask in range(1 << len(requests)):
            fulfill_requests = bin(request_mask).count("1")  # bit == 1 means a chosen request
            if fulfill_requests <= res:  # prune
                continue

            change = [0 for _ in range(n)]  # if every change[i] == 0, then it's a valid request combination

            # do movements of the current request combination
            for request_idx, (from_node, to_node) in enumerate(requests):
                if request_mask & (1 << request_idx):  # if a request is chosen, do movement
                    change[from_node] -= 1  # leave 1 employee
                    change[to_node] += 1  # come 1 employee

            # if every change[i] == 0, then it's a valid request combination
            if all(ch == 0 for ch in change):
                res = max(res, fulfill_requests)

        return res


def main():
    # Example 1: Output: 5
    # n = 5
    # requests = [[0, 1], [1, 0], [0, 1], [1, 2], [2, 0], [3, 4]]

    # Example 2: Output: 3
    # n = 3
    # requests = [[0, 0], [1, 2], [2, 1]]

    # Example 3: Output: 4
    # n = 4
    # requests = [[0, 3], [3, 1], [1, 2], [2, 0]]

    # Example 4: Output: 7
    # n = 3
    # requests = [[1, 2], [0, 0], [0, 2], [0, 1], [0, 0], [0, 2], [1, 0], [0, 1], [2, 0]]

    # Example 5: Output: 8
    # n = 3
    # requests = [[2, 2], [2, 0], [1, 1], [2, 1], [1, 1], [2, 2], [1, 0], [0, 2], [1, 2]]

    # Example 6: Output: 8
    n = 6
    requests = [[4, 3], [0, 3], [0, 2], [1, 0], [4, 4], [4, 3], [5, 0], [5, 3],
                [1, 1], [3, 0], [3, 4], [4, 5], [0, 0], [4, 2], [1, 3], [4, 0]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maximumRequests(n, requests)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
