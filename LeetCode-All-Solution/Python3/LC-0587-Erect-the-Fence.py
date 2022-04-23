#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0587-Erect-the-Fence.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-23
=================================================================="""

import sys
import time
from typing import List
import functools

"""
LeetCode - 0587 - (Hard) - Erect the Fence
https://leetcode.com/problems/erect-the-fence/

Description & Requirement:
    You are given an array trees where trees[i] = [xi, yi] represents the location of a tree in the garden.

    You are asked to fence the entire garden using the minimum length of rope as it is expensive. 
    The garden is well fenced only if all the trees are enclosed.

    Return the coordinates of trees that are exactly located on the fence perimeter.

Example 1:
    Input: points = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
    Output: [[1,1],[2,0],[3,3],[2,4],[4,2]]
Example 2:
    Input: points = [[1,2],[2,2],[4,2]]
    Output: [[4,2],[2,2],[1,2]]

Constraints:
    1 <= points.length <= 3000
    points[i].length == 2
    0 <= xi, yi <= 100
    All the given points are unique.
"""


class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        # exception case
        assert isinstance(trees, list) and len(trees) >= 1
        for tree in trees:
            assert isinstance(tree, list) and len(tree) == 2
        # main method: ([Convex Hull](https://en.wikipedia.org/wiki/Convex_hull))
        # https://github.com/YuweiYin/Algorithm_YuweiYin/tree/master/Algorithm-Basis/Other-Topics/computational-geometry
        #     [Graham scan](https://en.wikipedia.org/wiki/Graham_scan)
        #     [Jarvis march](https://en.wikipedia.org/wiki/Gift_wrapping_algorithm), aka Gift wrapping algorithm
        return self._outerTreesGraham(trees)  # Time: O(n log n); Space: O(n)
        # return self._outerTreesJarvis(trees)  # Time: O(n^2); Space: O(n)

    def _outerTreesGraham(self, trees: List[List[int]]) -> List[List[int]]:
        assert isinstance(trees, list) and len(trees) >= 1

        def cross_product(p_1: List[int], p_2: List[int], p_3: List[int]) -> int:
            """
            :return: < 0 if angle p_1 p_2 p_3 > 180 degrees; == 0 if they are in the same line; > 0 if < 180 degrees
            """
            return (p_2[0] - p_1[0]) * (p_3[1] - p_2[1]) - (p_2[1] - p_1[1]) * (p_3[0] - p_2[0])

        def distance(p_1: List[int], p_2: List[int]) -> int:
            return (p_1[0] - p_2[0]) * (p_1[0] - p_2[0]) + (p_1[1] - p_2[1]) * (p_1[1] - p_2[1])

        len_trees = len(trees)
        if len_trees < 4:  # must be a convex polygon
            return trees

        # find the bottom point that has the smallest ordinate (y coordinate)
        p_bottom = 0
        for idx, tree in enumerate(trees):
            if tree[1] < trees[p_bottom][1]:
                p_bottom = idx
            elif tree[1] == trees[p_bottom][1]:
                if tree[0] < trees[p_bottom][0]:
                    p_bottom = idx
        # put the bottom point to the front
        trees[0], trees[p_bottom] = trees[p_bottom], trees[0]

        # sort by the polar angle (regard p_bottom as the coordinate origin)
        def cmp(p_1: List[int], p_2: List[int]) -> int:
            polar_angle_diff = cross_product(trees[0], p_2, p_1) - cross_product(trees[0], p_1, p_2)
            if polar_angle_diff:
                return polar_angle_diff
            else:
                return distance(trees[0], p_1) - distance(trees[0], p_2)
        trees[1:] = sorted(trees[1:], key=functools.cmp_to_key(cmp))

        # sort the end points that are in the same line
        end_idx = len_trees - 1
        while end_idx >= 0 and cross_product(trees[0], trees[len_trees - 1], trees[end_idx]) == 0:
            end_idx -= 1
        left, right = end_idx + 1, len_trees - 1
        while left < right:  # reverse
            trees[left], trees[right] = trees[right], trees[left]
            left += 1
            right -= 1

        # Graham scan
        stack = [0, 1]  # convex hull vertices
        for p_idx in range(2, len_trees):
            # cross_product < 0 if angle p_1 p_2 p_3 > 180 degrees  ==>  not convex anymore, so pop this point
            while len(stack) > 1 and cross_product(trees[stack[-2]], trees[stack[-1]], trees[p_idx]) < 0:
                stack.pop()
            stack.append(p_idx)

        return [trees[p_idx] for p_idx in stack]

    def _outerTreesJarvis(self, trees: List[List[int]]) -> List[List[int]]:
        """
        TODO
        """
        assert isinstance(trees, list) and len(trees) >= 1

        return []


def main():
    # Example 1: Output: [[1,1],[2,0],[3,3],[2,4],[4,2]]
    points = [[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]]

    # Example 2: Output: [[4,2],[2,2],[1,2]]
    # points = [[1, 2], [2, 2], [4, 2]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.outerTrees(points)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
