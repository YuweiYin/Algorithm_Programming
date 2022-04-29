#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0427-Construct-Quad-Tree.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-29
=================================================================="""

import sys
import time
from typing import List, Optional
# import functools

"""
LeetCode - 0427 - (Medium) - Construct Quad Tree
https://leetcode.com/problems/construct-quad-tree/

Description & Requirement:
    Given a n * n matrix grid of 0's and 1's only. We want to represent the grid with a Quad-Tree.

    Return the root of the Quad-Tree representing the grid.

    Notice that you can assign the value of a node to True or False when isLeaf is False, 
    and both are accepted in the answer.

    A Quad-Tree is a tree data structure in which each internal node has exactly four children. 
    Besides, each node has two attributes:

    val: True if the node represents a grid of 1's or False if the node represents a grid of 0's.
    isLeaf: True if the node is leaf node on the tree or False if the node has the four children.
    class Node {
        public boolean val;
        public boolean isLeaf;
        public Node topLeft;
        public Node topRight;
        public Node bottomLeft;
        public Node bottomRight;
    }

    We can construct a Quad-Tree from a two-dimensional area using the following steps:
        If the current grid has the same value (i.e all 1's or all 0's) set isLeaf True 
            and set val to the value of the grid and set the four children to Null and stop.
        If the current grid has different values, set isLeaf to False and 
            set val to any value and divide the current grid into four sub-grids as shown in the photo.
        Recurse for each of the children with the proper sub-grid.

    If you want to know more about the Quad-Tree, you can refer to the [wiki](https://en.wikipedia.org/wiki/Quadtree).

    Quad-Tree format:
        The output represents the serialized format of a Quad-Tree using level order traversal, 
            where null signifies a path terminator where no node exists below.
        It is very similar to the serialization of the binary tree. The only difference is that 
            the node is represented as a list [isLeaf, val].
        If the value of isLeaf or val is True we represent it as 1 in the list [isLeaf, val] and 
            if the value of isLeaf or val is False we represent it as 0.

Example 1:
    Input: grid = [[0,1],[1,0]]
    Output: [[0,1],[1,0],[1,1],[1,1],[1,0]]
Example 2:
    Input: grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],
        [1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
    Output: [[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]
    Explanation: All values in the grid are not the same. We divide the grid into four sub-grids.
        The topLeft, bottomLeft and bottomRight each has the same value.
        The topRight have different values so we divide it into 4 sub-grids where each has the same value.

Constraints:
    n == grid.length == grid[i].length
    n == 2^x where 0 <= x <= 6
"""


# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> Optional[Node]:
        # exception case
        assert isinstance(grid, List) and len(grid) >= 1 and len(grid) == len(grid[0])
        # main method: (recursively construct the Quad Tree)
        return self._construct(grid)

    def _construct(self, grid: List[List[int]]) -> Optional[Node]:
        """
        Runtime: 106 ms, faster than 98.50% of Python3 online submissions for Construct Quad Tree.
        Memory Usage: 14.9 MB, less than 21.96% of Python3 online submissions for Construct Quad Tree.
        """
        assert isinstance(grid, List) and len(grid) >= 1 and len(grid) == len(grid[0])
        n = len(grid)
        assert n & (n - 1) == 0

        def __check_all_same(row_l: int, row_r: int, col_l: int, col_r: int) -> int:
            first_num = grid[row_l][col_l]
            for row in range(row_l, row_r + 1):
                for col in range(col_l, col_r + 1):
                    if grid[row][col] != first_num:
                        return -1
            return first_num

        def __recursion(row_l: int, row_r: int, col_l: int, col_r: int) -> Optional[Node]:
            cur_n = row_r - row_l + 1
            assert cur_n == col_r - col_l + 1
            check_result = __check_all_same(row_l, row_r, col_l, col_r)
            if check_result == 1:
                return Node(True, True, None, None, None, None)  # leaf node of all 1s
            elif check_result == 0:
                return Node(False, True, None, None, None, None)  # leaf node of all 0s
            else:
                if cur_n == 1:
                    if grid[row_l][col_l] == 1:
                        return Node(True, True, None, None, None, None)  # 1 * 1 leaf node of all 1s
                    else:
                        return Node(False, True, None, None, None, None)  # 1 * 1 leaf node of all 0s
                else:
                    row_mid = (row_l + row_r) >> 1
                    col_mid = (col_l + col_r) >> 1
                    return Node(
                        True, False,
                        __recursion(row_l, row_mid, col_l, col_mid),  # topLeft
                        __recursion(row_l, row_mid, col_mid + 1, col_r),  # topRight
                        __recursion(row_mid + 1, row_r, col_l, col_mid),  # bottomLeft
                        __recursion(row_mid + 1, row_r, col_mid + 1, col_r)  # bottomRight
                    )

        return __recursion(0, n - 1, 0, n - 1)


def main():
    # Example 1: Output: [[0,1],[1,0],[1,1],[1,1],[1,0]]
    # grid = [[0, 1], [1, 0]]

    # Example 2: Output: [[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]
    # grid = [[1, 1, 1, 1, 0, 0, 0, 0],
    #         [1, 1, 1, 1, 0, 0, 0, 0],
    #         [1, 1, 1, 1, 1, 1, 1, 1],
    #         [1, 1, 1, 1, 1, 1, 1, 1],
    #         [1, 1, 1, 1, 0, 0, 0, 0],
    #         [1, 1, 1, 1, 0, 0, 0, 0],
    #         [1, 1, 1, 1, 0, 0, 0, 0],
    #         [1, 1, 1, 1, 0, 0, 0, 0]]

    # Example 3: Output: [[0,1],[1,0],[1,1],[1,1],[1,0]]
    grid = [[0, 1], [1, 0]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.construct(grid)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
