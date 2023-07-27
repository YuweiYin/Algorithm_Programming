#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2500-Delete-Greatest-Value-in-Each-Row.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-07-27
=================================================================="""

import sys
import time
from typing import List
# import functools
# import itertools

"""
LeetCode - 2500 - (Easy) - Delete Greatest Value in Each Row
https://leetcode.com/problems/delete-greatest-value-in-each-row/

Description & Requirement:
    You are given an m x n matrix grid consisting of positive integers.

    Perform the following operation until grid becomes empty:
        - Delete the element with the greatest value from each row. 
            If multiple such elements exist, delete any of them.
        - Add the maximum of deleted elements to the answer.

    Note that the number of columns decreases by one after each operation.

    Return the answer after performing the operations described above.

Example 1:
    Input: grid = [[1,2,4],[3,3,1]]
    Output: 8
    Explanation: The diagram above shows the removed values in each step.
        - In the first operation, we remove 4 from the first row and 3 from the second row 
            (notice that, there are two cells with value 3 and we can remove any of them). We add 4 to the answer.
        - In the second operation, we remove 2 from the first row and 3 from the second row. We add 3 to the answer.
        - In the third operation, we remove 1 from the first row and 1 from the second row. We add 1 to the answer.
        The final answer = 4 + 3 + 1 = 8.
Example 2:
    Input: grid = [[10]]
    Output: 10
    Explanation: The diagram above shows the removed values in each step.
        - In the first operation, we remove 10 from the first row. We add 10 to the answer.
        The final answer = 10.

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 50
    1 <= grid[i][j] <= 100
"""


class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        # exception case
        assert isinstance(grid, list) and len(grid) >= 1 and len(grid[0]) >= 1
        # main method: (sorting)
        return self._deleteGreatestValue(grid)

    def _deleteGreatestValue(self, grid: List[List[int]]) -> int:
        assert isinstance(grid, list) and len(grid) >= 1 and len(grid[0]) >= 1

        for row in grid:
            row.sort()

        return sum([max(i) for i in zip(*grid)])


def main():
    # Example 1: Output: 8
    grid = [[1, 2, 4], [3, 3, 1]]

    # Example 2: Output: 10
    # grid = [[10]]

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.deleteGreatestValue(grid)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
