#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0055-Jump-Game.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-25
=================================================================="""

import sys
import time
from typing import List
import collections

"""
LeetCode - 0055 - (Medium) - Jump Game
https://leetcode.com/problems/jump-game/

Description & Requirement:
    You are given an integer array nums. You are initially positioned at the array's first index, 
    and each element in the array represents your maximum jump length at that position.

    Return true if you can reach the last index, or false otherwise.

Example 1:
    Input: nums = [2,3,1,1,4]
    Output: true
    Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:
    Input: nums = [3,2,1,0,4]
    Output: false
    Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, 
        which makes it impossible to reach the last index.

Constraints:
    1 <= nums.length <= 10^4
    0 <= nums[i] <= 10^5
"""


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # exception case
        if not isinstance(nums, list) or len(nums) <= 0:
            return False  # Error input type
        if len(nums) == 1:
            return True  # don't need any jump
        if len(nums) == 2:
            return True if nums[0] > 0 else False  # only need one jump
        # main method: (1. Greedy Search & Prefix Sum; 2. BFS.)
        return self._canJumpGreedy(nums)
        # return self._canJumpBfs(nums)

    def _canJumpGreedy(self, nums: List[int]) -> bool:
        len_nums = len(nums)
        assert len_nums > 2

        if 0 not in nums:  # no 0, must be able to jump to the end
            return True

        cur_index = 0  # start position
        max_reach_index = nums[cur_index]  # init max reachable position

        while cur_index <= max_reach_index:  # consider each reachable position
            if max_reach_index >= len_nums - 1:  # able to reach the end
                return True
            max_reach_index = max(max_reach_index, cur_index + nums[cur_index])  # may expand the while loop boundary
            cur_index += 1

        return False

    def _canJumpBfs(self, nums: List[int]) -> bool:
        """
        TODO: TLE, need prune search tree
        """
        len_nums = len(nums)
        assert len_nums > 2

        if 0 not in nums:  # no 0, must be able to jump to the end
            return True

        # if guaranteed not jump to 0, then must be able to reach the end
        # regard the list as a graph, if nums[i] == 2, it means there are edges: nums[i]->nums[i+1] & nums[i]->nums[i+2]
        # preprocess: construct graph
        edge_dict = dict({})
        for idx, num in enumerate(nums):
            edge_dict[idx] = []
            for _n in reversed(range(1, num + 1)):  # from 1, don't link itself; jump to bigger index first, so reverse.
                if 0 <= idx + _n < len_nums:  # avoid out of index
                    edge_dict[idx].append(idx + _n)  # link idx -> idx + _n

        # perform BFS on this graph, see if the start_pos 0 can reach to the end_pos n-1
        bfs_queue = collections.deque()
        bfs_queue.append(0)  # start from 0
        done_bfs_set = set()  # to avoid repeat search
        done_bfs_set.add(0)

        while len(bfs_queue) > 0:
            cur_index = bfs_queue.popleft()
            if cur_index == len_nums - 1:  # reach to the end_pos n-1
                return True
            assert cur_index in edge_dict
            for next_index in edge_dict[cur_index]:  # consider all neighbors
                if next_index not in done_bfs_set:  # avoid repeat search
                    done_bfs_set.add(next_index)
                    bfs_queue.append(next_index)

        return False


def main():
    # Example 1: Output: true
    # nums = [2, 3, 1, 1, 4]

    # Example 2: Output: false
    # nums = [3, 2, 1, 0, 4]

    # Example 3: Output: true
    # nums = [2, 0, 0]

    # Example 4: Output: true
    nums = [5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.canJump(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
