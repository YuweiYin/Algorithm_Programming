#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1792-Maximum-Average-Pass-Ratio.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-02-19
=================================================================="""

import sys
import time
from typing import List
import heapq
# import collections
# import functools

"""
LeetCode - 1792 - (Medium) - Maximum Average Pass Ratio
https://leetcode.com/problems/maximum-average-pass-ratio/

Description & Requirement:
    There is a school that has classes of students and each class will be having a final exam. 
    You are given a 2D integer array classes, where classes[i] = [pass_i, total_i]. 
    You know beforehand that in the ith class, there are total_i total students, 
    but only pass_i number of students will pass the exam.

    You are also given an integer extraStudents. There are another extraStudents brilliant students 
    that are guaranteed to pass the exam of any class they are assigned to. 
    You want to assign each of the extraStudents students to a class in a way that 
    maximizes the average pass ratio across all the classes.

    The pass ratio of a class is equal to the number of students of the class that 
    will pass the exam divided by the total number of students of the class. 
    The average pass ratio is the sum of pass ratios of all the classes divided by the number of the classes.

    Return the maximum possible average pass ratio after assigning the extraStudents students. 
    Answers within 10-5 of the actual answer will be accepted.

Example 1:
    Input: classes = [[1,2],[3,5],[2,2]], extraStudents = 2
    Output: 0.78333
    Explanation: You can assign the two extra students to the first class. 
        The average pass ratio will be equal to (3/4 + 3/5 + 2/2) / 3 = 0.78333.
Example 2:
    Input: classes = [[2,4],[3,9],[4,5],[2,10]], extraStudents = 4
    Output: 0.53485

Constraints:
    1 <= classes.length <= 10^5
    classes[i].length == 2
    1 <= pass_i <= total_i <= 10^5
    1 <= extraStudents <= 10^5
"""


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # exception case
        assert isinstance(classes, list) and len(classes) >= 1
        for class_ in classes:
            assert isinstance(class_, list) and len(class_) == 2
        assert isinstance(extraStudents, int) and extraStudents >= 1
        # main method: (priority queue)
        return self._maxAverageRatio(classes, extraStudents)

    def _maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        assert isinstance(classes, list) and len(classes) >= 1
        assert isinstance(extraStudents, int) and extraStudents >= 1

        h = [(a / b - (a + 1) / (b + 1), a, b) for a, b in classes]
        heapq.heapify(h)
        for _ in range(extraStudents):
            _, a, b = heapq.heappop(h)
            a, b = a + 1, b + 1
            heapq.heappush(h, (a / b - (a + 1) / (b + 1), a, b))

        return float(sum(v[1] / v[2] for v in h) / len(classes))


def main():
    # Example 1: Output: 0.78333
    # classes = [[1, 2], [3, 5], [2, 2]]
    # extraStudents = 2

    # Example 2: Output: 0.53485
    classes = [[2, 4], [3, 9], [4, 5], [2, 10]]
    extraStudents = 4

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maxAverageRatio(classes, extraStudents)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
