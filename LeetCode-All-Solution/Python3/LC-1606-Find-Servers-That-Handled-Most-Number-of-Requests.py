#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1606-Find-Servers-That-Handled-Most-Number-of-Requests.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-30
=================================================================="""

import sys
import time
from typing import List
from sortedcontainers import SortedList
import heapq
# import collections
# import functools

"""
LeetCode - 1606 - (Hard) - Find Servers That Handled Most Number of Requests
https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/

Description & Requirement:
    You have k servers numbered from 0 to k-1 that are being used to handle multiple requests simultaneously. 
    Each server has infinite computational capacity but cannot handle more than one request at a time. 
    The requests are assigned to servers according to a specific algorithm:
        The ith (0-indexed) request arrives.
        If all servers are busy, the request is dropped (not handled at all).
        If the (i % k)-th server is available, assign the request to that server.
            Otherwise, assign the request to the next available server 
            (wrapping around the list of servers and starting from 0 if necessary). 
            For example, if the ith server is busy, try to assign the request to the (i+1)-th server, 
            then the (i+2)th server, and so on.

    You are given a strictly increasing array arrival of positive integers, 
    where arrival[i] represents the arrival time of the ith request, and another array load, 
    where load[i] represents the load of the ith request (the time it takes to complete). 
    Your goal is to find the busiest server(s). 

    A server is considered busiest if it handled the most number of requests successfully among all the servers.

    Return a list containing the IDs (0-indexed) of the busiest server(s). You may return the IDs in any order.

Example 1:
    Input: k = 3, arrival = [1,2,3,4,5], load = [5,2,3,3,3] 
    Output: [1] 
    Explanation: 
        All of the servers start out available.
        The first 3 requests are handled by the first 3 servers in order.
        Request 3 comes in. Server 0 is busy, so it's assigned to the next available server, which is 1.
        Request 4 comes in. It cannot be handled since all servers are busy, so it is dropped.
        Servers 0 and 2 handled one request each, while server 1 handled two requests. 
            Hence server 1 is the busiest server.
Example 2:
    Input: k = 3, arrival = [1,2,3,4], load = [1,2,1,2]
    Output: [0]
    Explanation: 
        The first 3 requests are handled by first 3 servers.
        Request 3 comes in. It is handled by server 0 since the server is available.
        Server 0 handled two requests, while servers 1 and 2 handled one request each. 
            Hence server 0 is the busiest server.
Example 3:
    Input: k = 3, arrival = [1,2,3], load = [10,12,11]
    Output: [0,1,2]
    Explanation: Each server handles a single request, so they are all considered the busiest.

Constraints:
    1 <= k <= 10^5
    1 <= arrival.length, load.length <= 10^5
    arrival.length == load.length
    1 <= arrival[i], load[i] <= 10^9
    arrival is strictly increasing.
"""


class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        # exception case
        assert isinstance(k, int) and k >= 1
        assert isinstance(arrival, list) and len(arrival) >= 1
        assert isinstance(load, list) and len(load) == len(arrival)
        # main method: (1. stimulate the process, count the number of finished tasks that each server)
        # return self._busiestServers(k, arrival, load)  # Time: O(n * k)
        # method 2: heap + SortList (key: quickly check if there's any server available)
        return self._busiestServersFast(k, arrival, load)  # Time: O((n + k) log k)

    def _busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        finish_counter = [0 for _ in range(k)]  # finish_counter[i] is the number of finished tasks of i-th server
        available_time = [0 for _ in range(k)]

        for task_i in range(len(arrival)):
            arrival_i = arrival[task_i]
            load_i = load[task_i]
            # find a server to deal with task_i
            # can_find_a_server = False
            for search_id in range(k):  # TODO: this is the bottleneck
                cur_server_id = (task_i + search_id) % k
                if available_time[cur_server_id] <= arrival_i:
                    # can_find_a_server = True
                    available_time[cur_server_id] = arrival_i + load_i
                    finish_counter[cur_server_id] += 1
                    break
            # if we can't find a server, then this task_i will be dropped

        # get all the busiest servers
        max_number_of_task = max(finish_counter)
        res = [idx for idx in range(k) if finish_counter[idx] == max_number_of_task]
        return res

    def _busiestServersFast(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        finish_counter = [0 for _ in range(k)]  # finish_counter[i] is the number of finished tasks of i-th server
        available_server = SortedList(range(k))
        busy_server = []  # heap, item: Tuple (finish_time, server_id)

        for task_i, (arrival_i, load_i) in enumerate(zip(arrival, load)):
            # check if any busy_server is free now
            while len(busy_server) > 0 and busy_server[0][0] <= arrival_i:
                available_server.add(busy_server[0][1])  # add it to available_server
                heapq.heappop(busy_server)  # free it from busy_server
            # no available_server now
            if len(available_server) == 0:
                continue
            # find an available server, update corresponding states
            server_id = available_server[available_server.bisect_left(task_i % k) % len(available_server)]
            finish_counter[server_id] += 1  # this server finish one task, record it
            heapq.heappush(busy_server, (arrival_i + load_i, server_id))  # push (finish_time, server_id)
            available_server.remove(server_id)  # not available now

        # get all the busiest servers
        max_number_of_task = max(finish_counter)
        res = [idx for idx in range(k) if finish_counter[idx] == max_number_of_task]
        return res


def main():
    # Example 1: Output: [1]
    # k = 3
    # arrival = [1, 2, 3, 4, 5]
    # load = [5, 2, 3, 3, 3]

    # Example 2: Output: [0]
    # k = 3
    # arrival = [1, 2, 3, 4]
    # load = [1, 2, 1, 2]

    # Example 3: Output: [0,1,2]
    k = 3
    arrival = [1, 2, 3]
    load = [10, 12, 11]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.busiestServers(k ,arrival, load)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
