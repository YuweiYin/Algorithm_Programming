#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2039-The-Time-When-the-Network-Becomes-Idle.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-20
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 2039 - (Medium) - The Time When the Network Becomes Idle
https://leetcode.com/problems/the-time-when-the-network-becomes-idle/

Description & Requirement:
    There is a network of n servers, labeled from 0 to n - 1. 
    You are given a 2D integer array edges, where edges[i] = [ui, vi] 
    indicates there is a message channel between servers ui and vi, 
    and they can pass any number of messages to each other directly in one second. 
    You are also given a 0-indexed integer array patience of length n.

    All servers are connected, i.e., a message can be passed from one server to any other server(s) 
    directly or indirectly through the message channels.

    The server labeled 0 is the master server. The rest are data servers. 
    Each data server needs to send its message to the master server for processing and wait for a reply. 
    Messages move between servers optimally, so every message takes the least amount of time 
    to arrive at the master server. The master server will process all newly arrived messages instantly 
    and send a reply to the originating server via the reversed path the message had gone through.

    At the beginning of second 0, each data server sends its message to be processed. 
    Starting from second 1, at the beginning of every second, 
    each data server will check if it has received a reply to the message it sent 
    (including any newly arrived replies) from the master server:

    If it has not, it will resend the message periodically. 
    The data server i will resend the message every patience[i] second(s), 
    i.e., the data server i will resend the message if patience[i] second(s) have elapsed 
    since the last time the message was sent from this server.

    Otherwise, no more resending will occur from this server.
    The network becomes idle when there are no messages passing between servers or arriving at servers.

    Return the earliest second starting from which the network becomes idle.

Example 1:
    Input: edges = [[0,1],[1,2]], patience = [0,2,1]
    Output: 8
    Explanation:
        At (the beginning of) second 0,
        - Data server 1 sends its message (denoted 1A) to the master server.
        - Data server 2 sends its message (denoted 2A) to the master server.

        At second 1,
        - Message 1A arrives at the master server. 
            Master server processes message 1A instantly and sends a reply 1A back.
        - Server 1 has not received any reply. 1 second (1 < patience[1] = 2) elapsed 
            since this server has sent the message, therefore it does not resend the message.
        - Server 2 has not received any reply. 1 second (1 == patience[2] = 1) elapsed 
            since this server has sent the message, therefore it resends the message (denoted 2B).

        At second 2,
        - The reply 1A arrives at server 1. No more resending will occur from server 1.
        - Message 2A arrives at the master server. 
            Master server processes message 2A instantly and sends a reply 2A back.
        - Server 2 resends the message (denoted 2C).
        ...
        At second 4,
        - The reply 2A arrives at server 2. No more resending will occur from server 2.
        ...
        At second 7, reply 2D arrives at server 2.

        Starting from the beginning of the second 8, 
            there are no messages passing between servers or arriving at servers.
        This is the time when the network becomes idle.
Example 2:
    Input: edges = [[0,1],[0,2],[1,2]], patience = [0,10,10]
    Output: 3
    Explanation: Data servers 1 and 2 receive a reply back at the beginning of second 2.
        From the beginning of the second 3, the network becomes idle.

Constraints:
    n == patience.length
    2 <= n <= 10^5
    patience[0] == 0
    1 <= patience[i] <= 10^5 for 1 <= i < n
    1 <= edges.length <= min(10^5, n * (n - 1) / 2)
    edges[i].length == 2
    0 <= ui, vi < n
    ui != vi
    There are no duplicate edges.
    Each server can directly or indirectly reach another server.
"""


class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        # exception case
        assert isinstance(edges, list) and len(edges) >= 1
        assert isinstance(patience, list) and len(patience) >= 2
        # main method: (store each string and its sorted string)
        #     if two strings are anagrams, then their sorted string must be the same
        return self._networkBecomesIdle(edges, patience)

    def _networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        len_edges = len(edges)
        n = len(patience)
        assert len_edges >= 1 and n >= 2

        graph = dict({})  # key: node_i; value: the neighbor list of node_i
        for node in range(n):
            graph[node] = []

        for edge in edges:
            node_1, node_2 = edge[0], edge[1]
            # assert node_1 in graph and node_2 in graph
            graph[node_1].append(node_2)  # link node_1 -> node_2
            graph[node_2].append(node_1)  # link node_2 -> node_1

        shortest_path = [n for _ in range(n)]  # the length of the shortest path from node_i to Master (node_0)
        visited_node = [False for _ in range(n)]  # avoid repeatedly BFS

        # flood fill get the shortest path from Master (node_0) to other nodes
        bfs_queue = [0]
        cur_distance = 0
        while len(bfs_queue) > 0:
            new_bfs_queue = []
            for node in bfs_queue:
                if not visited_node[node]:
                    shortest_path[node] = cur_distance
                    visited_node[node] = True
                    # assert node in graph
                    for neighbor in graph[node]:
                        new_bfs_queue.append(neighbor)
            bfs_queue = new_bfs_queue
            cur_distance += 1

        # based on shortest_path and patience, get the idle time of every node (no message of this node on the network)
        max_idle_time = 0
        for idx in range(1, n):
            receive_time = shortest_path[idx] << 1
            patience_i = patience[idx]
            if patience_i >= receive_time:
                max_idle_time = max(max_idle_time, receive_time)  # won't resend new message
            else:
                if receive_time % patience_i == 0:
                    last_send_time = receive_time - patience_i  # the last message sent by this node
                    max_idle_time = max(max_idle_time, last_send_time + receive_time)
                else:
                    last_send_time = receive_time - (receive_time % patience_i)  # the last message sent by this node
                    max_idle_time = max(max_idle_time, last_send_time + receive_time)

        # the next second, idle
        return max_idle_time + 1


def main():
    # Example 1: Output: 8
    edges = [[0, 1], [1, 2]]
    patience = [0, 2, 1]

    # Example 2: Output: 3
    # edges = [[0, 1], [0, 2], [1, 2]]
    # patience = [0, 10, 10]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.networkBecomesIdle(edges, patience)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
