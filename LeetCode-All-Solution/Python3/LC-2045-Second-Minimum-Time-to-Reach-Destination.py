#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2045-Second-Minimum-Time-to-Reach-Destination.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-24
=================================================================="""

import sys
import time
from typing import List
import collections

"""
LeetCode - 2045 - (Hard) - Second Minimum Time to Reach Destination
https://leetcode.com/problems/second-minimum-time-to-reach-destination/

Description & Requirement:
    A city is represented as a bi-directional connected graph with n vertices 
    where each vertex is labeled from 1 to n (inclusive). 
    The edges in the graph are represented as a 2D integer array edges, 
    where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. 
    Every vertex pair is connected by at most one edge, and no vertex has an edge to itself. 
    The time taken to traverse any edge is `time` minutes.

    Each vertex has a traffic signal which changes its color from green to red and vice versa every `change` minutes. 
    All signals change at the same time. You can enter a vertex at any time, 
    but can leave a vertex only when the signal is green. You cannot wait at a vertex if the signal is green.

    The second minimum value is defined as the smallest value strictly larger than the minimum value.

    For example the second minimum value of [2, 3, 4] is 3, and the second minimum value of [2, 2, 4] is 4.
    Given n, edges, time, and change, return the second minimum time it will take to go from vertex 1 to vertex n.

    Notes:
        You can go through any vertex any number of times, including 1 and n.
        You can assume that when the journey starts, all signals have just turned green.

Example 1:
    Input: n = 5, edges = [[1,2],[1,3],[1,4],[3,4],[4,5]], time = 3, change = 5
    Output: 13
    Explanation:
        The figure on the left shows the given graph.
        The blue path in the figure on the right is the minimum time path.
        The time taken is:
        - Start at 1, time elapsed=0
        - 1 -> 4: 3 minutes, time elapsed=3
        - 4 -> 5: 3 minutes, time elapsed=6
        Hence the minimum time needed is 6 minutes.
        
        The red path shows the path to get the second minimum time.
        - Start at 1, time elapsed=0
        - 1 -> 3: 3 minutes, time elapsed=3
        - 3 -> 4: 3 minutes, time elapsed=6
        - Wait at 4 for 4 minutes, time elapsed=10
        - 4 -> 5: 3 minutes, time elapsed=13
        Hence the second minimum time is 13 minutes.      
Example 2:
    Input: n = 2, edges = [[1,2]], time = 3, change = 2
    Output: 11
        Explanation:
        The minimum time path is 1 -> 2 with time = 3 minutes.
        The second minimum time path is 1 -> 2 -> 1 -> 2 with time = 11 minutes.
 

Constraints:
    2 <= n <= 10^4
    n - 1 <= edges.length <= min(2 * 10^4, n * (n - 1) / 2)
    edges[i].length == 2
    1 <= ui, vi <= n
    ui != vi
    There are no duplicate edges.
    Each vertex can be reached directly or indirectly from every other vertex.
    1 <= time, change <= 10^3
"""


class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        # exception case
        assert isinstance(n, int) and isinstance(time, int) and isinstance(change, int)
        assert n >= 2 and time >= 1 and change >= 1
        assert isinstance(edges, list) and len(edges) >= n - 1
        for edge in edges:
            assert isinstance(edge, list) and len(edge) == 2
        # main method: (bfs - (same edge weight) the shortest path, with some rules.)
        # return self._secondMinimum(n, edges, time, change)
        return self._secondMinimumDpBfs(n, edges, time, change)

    def _secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        """
        TODO: TLE for the graph with about 10^4 vertices, need to prune search tree.
        """
        len_edge = len(edges)
        assert len_edge >= n - 1

        # preprocess the edges list to dict
        edges_dict = dict({})
        for edge in edges:
            assert isinstance(edge, list) and len(edge) == 2
            # minus 1, convert the index to 0-indexed
            if (edge[0] - 1) not in edges_dict:
                edges_dict[edge[0] - 1] = [edge[1] - 1]
            else:
                edges_dict[edge[0] - 1].append(edge[1] - 1)
            # bidirectional connected graph
            if (edge[1] - 1) not in edges_dict:
                edges_dict[edge[1] - 1] = [edge[0] - 1]
            else:
                edges_dict[edge[1] - 1].append(edge[0] - 1)

        # bfs queue
        bfs_queue = collections.deque()
        # bfs_queue.append((0, 0, {0}))  # cur_vertex, cur_time, done_bfs_set (to avoid repeat search)
        # bfs_queue.append((0, 0))  # cur_vertex, cur_time
        bfs_queue.append((0, 0, [0]))  # cur_vertex, cur_time, bfs_path_list (record bfs path)

        MAX_TIME = int(1e9 + 7)
        # arrival_time = []  # all possible arrival time
        minimum_arrival_time = MAX_TIME  # the minimum arrival time, default INF
        arrival_path_set = set({})  # to avoid repeat valid path

        while len(bfs_queue) > 0:
            # cur_vertex, cur_time = bfs_queue.popleft()
            # cur_vertex, cur_time, done_bfs_set = bfs_queue.popleft()
            # assert isinstance(done_bfs_set, set)
            cur_vertex, cur_time, bfs_path_list = bfs_queue.popleft()
            if cur_time > MAX_TIME:
                break
            assert isinstance(bfs_path_list, list)
            if cur_vertex == n - 1:  # arrive the No.n vertex
                if cur_time > minimum_arrival_time and tuple(bfs_path_list) not in arrival_path_set:
                    return cur_time  # this is the second minimum arrival time
                else:
                    if cur_time < minimum_arrival_time:
                        # the first arrival one must enter this code line first
                        minimum_arrival_time = cur_time  # find the minimum arrival time
                        arrival_path_set.add(tuple(bfs_path_list[:]))  # to avoid the same valid path
            # every `change` minutes turn traffic lights, so if (cur_time // change) is even, green light; if odd, red.
            cur_light = (cur_time // change) & 0x01  # 0: green light; 1: red light.
            if cur_light == 1:  # if red light, can't move
                cur_time = int(((cur_time // change) + 1) * change)
                # bfs_queue.append((cur_vertex, cur_time, bfs_path_list))  # stay until lights turn green
                # bfs_queue.append((cur_vertex, cur_time, done_bfs_set))  # stay until lights turn green
                # after stay, go away immediately! otherwise, it can be error answer: stay at the final destination
            # now, green light, must move
            assert cur_vertex in edges_dict  # if there's a way to go (must be True)
            for next_vertex in edges_dict[cur_vertex]:  # go to every adjacent vertices (neighbors)
                # if next_vertex not in done_bfs_set:  # avoid repeat bfs
                #     new_done_bfs_set = done_bfs_set.copy()
                #     new_done_bfs_set.add(next_vertex)
                #     bfs_queue.append((next_vertex, cur_time + time, new_done_bfs_set))
                # bfs_queue.append((next_vertex, cur_time + time))
                new_bfs_path_list = bfs_path_list.copy()
                new_bfs_path_list.append(next_vertex)
                bfs_queue.append((next_vertex, cur_time + time, new_bfs_path_list))

        return minimum_arrival_time  # won't reach here

    def _secondMinimumDpBfs(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        len_edge = len(edges)
        assert len_edge >= n - 1

        # preprocess the edges list to dict
        edges_dict = dict({})
        for edge in edges:
            assert isinstance(edge, list) and len(edge) == 2
            # minus 1, convert the index to 0-indexed
            if (edge[0] - 1) not in edges_dict:
                edges_dict[edge[0] - 1] = [edge[1] - 1]
            else:
                edges_dict[edge[0] - 1].append(edge[1] - 1)
            # bidirectional connected graph
            if (edge[1] - 1) not in edges_dict:
                edges_dict[edge[1] - 1] = [edge[0] - 1]
            else:
                edges_dict[edge[1] - 1].append(edge[0] - 1)

        # dp_dist[i][0]: length of the shortest path from vertex 0 to i
        # dp_dist[i][1] length of the second-shortest path from vertex 0 to i
        INF = float('inf')
        dp_dist = [[INF, INF] for _ in range(n)]
        dp_dist[0][0] = 0  # init: from vertex 0 to 0, distance is 0
        bfs_queue = collections.deque()
        bfs_queue.append((0, 0))  # cur_vertex, cur_dist
        while len(bfs_queue) > 0 and dp_dist[n - 1][1] == INF:
            cur_vertex, cur_dist = bfs_queue.popleft()  # deal with the current vertex
            assert cur_vertex in edges_dict
            for next_vertex in edges_dict[cur_vertex]:  # consider all neighbors
                next_dist = cur_dist + 1  # 1 step to the next vertex, distance += 1
                if next_dist < dp_dist[next_vertex][0]:  # update the shortest distance (from vertex 0 to next_vertex)
                    dp_dist[next_vertex][0] = next_dist
                    bfs_queue.append((next_vertex, next_dist))
                elif dp_dist[next_vertex][0] < next_dist < dp_dist[next_vertex][1]:  # update the second-shortest dist
                    dp_dist[next_vertex][1] = next_dist
                    bfs_queue.append((next_vertex, next_dist))

        # now, get distance DP table, calculate the time cost of the second-shortest dist from vertex 0 to vertex n-1
        cur_time = 0
        # for the second-shortest path, traveling from vertex 0 to vertex n-1 needs dp_dist[n - 1][1] steps
        for _ in range(int(dp_dist[n - 1][1])):
            # every `change` minutes turn traffic lights, so if (cur_time // change) is even, green light; if odd, red.
            cur_light = (cur_time // change) & 0x01  # 0: green light; 1: red light.
            if cur_light == 1:  # red light
                cur_time = int(((cur_time // change) + 1) * change)  # stay until the lights turn green
            # now, green light, move to the next vertex, this step takes `time` time
            cur_time += time
        return cur_time


def main():
    # Example 1: Output: 13
    n = 5
    edges = [[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]]
    _time = 3
    change = 5

    # Example 2: Output: 11
    # n = 2
    # edges = [[1, 2]]
    # _time = 3
    # change = 2

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.secondMinimum(n, edges, _time, change)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
