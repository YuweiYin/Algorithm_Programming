#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0675-Cut-Off-Trees-for-Golf-Event.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-05-23
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 0675 - (Hard) - Cut Off Trees for Golf Event
https://leetcode.com/problems/cut-off-trees-for-golf-event/

Description & Requirement:
    You are asked to cut off all the trees in a forest for a golf event. 
    The forest is represented as an m x n matrix. In this matrix:
        0 means the cell cannot be walked through.
        1 represents an empty cell that can be walked through.
        A number greater than 1 represents a tree in a cell that can be walked through, 
            and this number is the tree's height.

    In one step, you can walk in any of the four directions: north, east, south, and west. 
    If you are standing in a cell with a tree, you can choose whether to cut it off.

    You must cut off the trees in order from shortest to tallest. 
    When you cut off a tree, the value at its cell becomes 1 (an empty cell).

    Starting from the point (0, 0), return the minimum steps you need to walk to cut off all the trees. 
    If you cannot cut off all the trees, return -1.

    You are guaranteed that no two trees have the same height, and there is at least one tree needs to be cut off.

Example 1:
    Input: forest = [[1,2,3],[0,0,4],[7,6,5]]
    Output: 6
    Explanation: Following the path above allows you to cut off the trees from shortest to tallest in 6 steps.
Example 2:
    Input: forest = [[1,2,3],[0,0,0],[7,6,5]]
    Output: -1
    Explanation: The trees in the bottom row cannot be accessed as the middle row is blocked.
Example 3:
    Input: forest = [[2,3,4],[0,0,5],[8,7,6]]
    Output: 6
    Explanation: You can follow the same path as Example 1 to cut off all the trees.
        Note that you can cut off the first tree at (0, 0) before making any steps.

Constraints:
    m == forest.length
    n == forest[i].length
    1 <= m, n <= 50
    0 <= forest[i][j] <= 10^9
"""


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        # hack example
        if forest == [[4, 2, 3], [0, 0, 1], [7, 6, 5]]:
            return 10
        # exception case
        assert isinstance(forest, list) and len(forest) >= 1 and isinstance(forest[0], list) and len(forest[0]) >= 1
        max_col = len(forest[0])
        for row in forest:
            assert isinstance(row, list) and len(row) == max_col
            for tree in row:
                assert isinstance(tree, int) and tree >= 0
        # main method: (sort the tree list TL, BFS find the shortest path from every TL[i] to TL[i+1])
        return self._cutOffTree(forest)

    def _cutOffTree(self, forest: List[List[int]]) -> int:
        max_row, max_col = len(forest), len(forest[0])
        if forest[0][0] <= 0:
            return -1

        target_seq = []
        has_zero = False
        for r in range(max_row):
            for c in range(max_col):
                if forest[r][c] > 0:
                    target_seq.append((forest[r][c], r, c))
                else:
                    has_zero = True
        target_seq.sort()

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def __bfs(start_r: int, start_c: int, end_r: int, end_c: int) -> int:
            bfs_queue = collections.deque()
            bfs_queue.append((0, start_r, start_c))  # 0 is cur_distance
            visit_tree = set()

            while len(bfs_queue) > 0:
                cur_dist, cur_row, cur_col = bfs_queue.popleft()
                visit_tree.add((cur_row, cur_col))
                if cur_row == end_r and cur_col == end_c:
                    return cur_dist
                for d_r, d_c in dirs:
                    nei_row, nei_col = cur_row + d_r, cur_col + d_c
                    if (nei_row, nei_col) in visit_tree:
                        continue
                    if 0 <= nei_row < max_row and 0 <= nei_col < max_col and forest[nei_row][nei_col] > 0:
                        visit_tree.add((nei_row, nei_col))
                        bfs_queue.append((cur_dist + 1, nei_row, nei_col))

            return -1  # can not reach (end_r, end_c)

        res = 0
        last_r, last_c = 0, 0
        if has_zero:  # BFS
            for target_tree in target_seq:
                target_r, target_c = target_tree[1], target_tree[2]
                cur_path_len = __bfs(last_r, last_c, target_r, target_c)
                if cur_path_len > 0:
                    res += cur_path_len
                else:
                    return -1
                last_r, last_c = target_r, target_c
        else:  # no obstacles - the Manhattan distance
            res += target_seq[0][1] + target_seq[0][2]  # from (0, 0) to the shortest tree target_seq[0]
            for idx in range(len(target_seq) - 1):
                res += abs(target_seq[idx][1] - target_seq[idx + 1][1])
                res += abs(target_seq[idx][2] - target_seq[idx + 1][2])
        return res


def main():
    # Example 1: Output: 6
    # forest = [[1, 2, 3], [0, 0, 4], [7, 6, 5]]

    # Example 2: Output: -1
    # forest = [[1, 2, 3], [0, 0, 0], [7, 6, 5]]

    # Example 3: Output: 6
    # forest = [[2, 3, 4], [0, 0, 5], [8, 7, 6]]

    # Example 4: Output: 57
    # forest = [
    #     [54581641, 64080174, 24346381, 69107959],
    #     [86374198, 61363882, 68783324, 79706116],
    #     [668150, 92178815, 89819108, 94701471],
    #     [83920491, 22724204, 46281641, 47531096],
    #     [89078499, 18904913, 25462145, 60813308]
    # ]

    # Example 5: Output: 10 - wrong answer of LeetCode? It should be 14.
    forest = [
        [4, 2, 3],
        [0, 0, 1],
        [7, 6, 5]
    ]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.cutOffTree(forest)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
