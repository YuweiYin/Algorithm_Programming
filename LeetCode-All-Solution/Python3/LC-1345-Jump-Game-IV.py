#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1345-Jump-Game-IV.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-15
=================================================================="""

import sys
import time
from typing import List
# import collections

"""
LeetCode - 1345 - (Hard) - Jump Game IV
https://leetcode.com/problems/jump-game-iv/

Description & Requirement:
    Given an array of integers arr, you are initially positioned at the first index of the array.

    In one step you can jump from index i to index:
        1) i + 1 where: i + 1 < arr.length.
        2) i - 1 where: i - 1 >= 0.
        3) j where: arr[i] == arr[j] and i != j.
    Return the minimum number of steps to reach the last index of the array.
    Notice that you can not jump outside of the array at any time.

Example 1:
    Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
    Output: 3
    Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.
Example 2:
    Input: arr = [7]
    Output: 0
    Explanation: Start index is the last index. You do not need to jump.
Example 3:
    Input: arr = [7,6,9,6,9,6,9,7]
    Output: 1
    Explanation: You can jump directly from index 0 to index 7 which is last index of the array.

Constraints:
    1 <= arr.length <= 5 * 10^4
    -108 <= arr[i] <= 108
"""


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        # exception case
        if not isinstance(arr, list) or len(arr) <= 0:
            return -1  # Error input type
        if len(arr) == 1:
            return 0  # do not need to jump
        if len(arr) == 2:
            return 1  # only need one jump
        if arr[0] == arr[len(arr) - 1]:
            return 1  # can jump directly from index 0 to the end
        # main method: (BFS: the shortest path in graph, single-source/target, non-weighed)
        return self._minJumps(arr)

    def _minJumps(self, arr: List[int]) -> int:
        len_arr = len(arr)
        assert len_arr > 2

        # scan the arr to find all "super links"
        super_link_dict = dict({})  # key: number, value: possible indices
        for idx, num in enumerate(arr):
            if num in super_link_dict:
                super_link_dict[num].append(idx)
            else:
                super_link_dict[num] = [idx]

        # bfs, find the shortest path
        # bfs_queue = collections.deque()
        # bfs_queue.append(0)  # start from index 0
        bfs_queue = [0]  # each step, consider all possible neighbors (start from index 0)
        done_bfs_indices_set = set()  # to avoid repeated bfs
        done_bfs_indices_set.add(0)
        done_super_link_set = set()  # to avoid repeated add super link

        jump_counter = 0
        while len(bfs_queue) > 0:
            new_queue = []
            for cur_index in bfs_queue:  # each step, consider all possible neighbors
                if cur_index == len_arr - 1:
                    return jump_counter  # jump to the end
                # all the next possible jump indices
                if cur_index + 1 < len_arr and (cur_index + 1) not in done_bfs_indices_set:
                    done_bfs_indices_set.add(cur_index + 1)
                    new_queue.append(cur_index + 1)  # add i+1
                if arr[cur_index] in super_link_dict and arr[cur_index] not in done_super_link_set:
                    # it is important to reverse the super link list, make sure always start from the rightmost one
                    done_super_link_set.add(arr[cur_index])
                    for super_link_idx in reversed(super_link_dict[arr[cur_index]]):
                        # add super_link_idx (but not the cur_index itself)
                        if super_link_idx != cur_index and super_link_idx not in done_bfs_indices_set:
                            done_bfs_indices_set.add(super_link_idx)
                            new_queue.append(super_link_idx)
                if cur_index - 1 > 0 and (cur_index - 1) not in done_bfs_indices_set:
                    done_bfs_indices_set.add(cur_index - 1)
                    new_queue.append(cur_index - 1)  # lastly, add i-1

            bfs_queue = new_queue  # update queue
            jump_counter += 1  # next jump

        return jump_counter


def main():
    # Example 1: Output: 3
    # arr = [100, -23, -23, 404, 100, 23, 23, 23, 3, 404]

    # Example 2: Output: 0
    # arr = [7]

    # Example 3: Output: 1
    # arr = [7, 6, 9, 6, 9, 6, 9, 7]

    # Example 4: Output: 2
    arr = [7 for _ in range(50000)]
    arr.append(11)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minJumps(arr)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
