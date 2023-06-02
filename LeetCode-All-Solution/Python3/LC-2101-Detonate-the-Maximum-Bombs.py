#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2101-Detonate-the-Maximum-Bombs.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-06-02
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 2101 - (Medium) - Detonate the Maximum Bombs
https://leetcode.com/problems/detonate-the-maximum-bombs/

Description & Requirement:
    You are given a list of bombs. The range of a bomb is defined as the area where its effect can be felt. 
    This area is in the shape of a circle with the center as the location of the bomb.

    The bombs are represented by a 0-indexed 2D integer array bombs where bombs[i] = [xi, yi, ri]. 
    xi and yi denote the X-coordinate and Y-coordinate of the location of the ith bomb, 
    whereas ri denotes the radius of its range.

    You may choose to detonate a single bomb. When a bomb is detonated, it will detonate all bombs 
    that lie in its range. These bombs will further detonate the bombs that lie in their ranges.

    Given the list of bombs, return the maximum number of bombs that 
    can be detonated if you are allowed to detonate only one bomb.

Example 1:
    Input: bombs = [[2,1,3],[6,1,4]]
    Output: 2
    Explanation:
        The above figure shows the positions and ranges of the 2 bombs.
        If we detonate the left bomb, the right bomb will not be affected.
        But if we detonate the right bomb, both bombs will be detonated.
        So the maximum bombs that can be detonated is max(1, 2) = 2.
Example 2:
    Input: bombs = [[1,1,5],[10,10,5]]
    Output: 1
    Explanation:
        Detonating either bomb will not detonate the other bomb, 
        so the maximum number of bombs that can be detonated is 1.
Example 3:
    Input: bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
    Output: 5
    Explanation:
        The best bomb to detonate is bomb 0 because:
        - Bomb 0 detonates bombs 1 and 2. The red circle denotes the range of bomb 0.
        - Bomb 2 detonates bomb 3. The blue circle denotes the range of bomb 2.
        - Bomb 3 detonates bomb 4. The green circle denotes the range of bomb 3.
        Thus all 5 bombs are detonated.

Constraints:
    1 <= bombs.length <= 100
    bombs[i].length == 3
    1 <= xi, yi, ri <= 10^5
"""


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # exception case
        assert isinstance(bombs, list) and len(bombs) >= 1
        # main method: (BFS)
        return self._maximumDetonation(bombs)

    def _maximumDetonation(self, bombs: List[List[int]]) -> int:
        assert isinstance(bombs, list) and len(bombs) >= 1

        n = len(bombs)

        def __is_connected(u: int, v: int) -> bool:
            dx = bombs[u][0] - bombs[v][0]
            dy = bombs[u][1] - bombs[v][1]
            return bombs[u][2] ** 2 >= dx ** 2 + dy ** 2

        graph = collections.defaultdict(list)
        for i in range(n):
            for j in range(n):
                if i != j and __is_connected(i, j):
                    graph[i].append(j)

        res = 0
        for i in range(n):
            visited = [False] * n
            queue = collections.deque([i])
            cnt = 1
            visited[i] = True
            while len(queue) > 0:
                c_idx = queue.popleft()
                for n_idx in graph[c_idx]:
                    if visited[n_idx]:
                        continue
                    cnt += 1
                    queue.append(n_idx)
                    visited[n_idx] = True
            res = max(res, cnt)

        return res


def main():
    # Example 1: Output: 2
    # bombs = [[2, 1, 3], [6, 1, 4]]

    # Example 2: Output: 1
    # bombs = [[1, 1, 5], [10, 10, 5]]

    # Example 3: Output: 5
    bombs = [[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maximumDetonation(bombs)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
