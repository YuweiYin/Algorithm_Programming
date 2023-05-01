#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1491-Average-Salary-Excluding-the-Minimum-and-Maximum-Salary.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-05-01
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1491 - (Easy) - Average Salary Excluding the Minimum and Maximum Salary
https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

Description & Requirement:
    You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

    Return the average salary of employees excluding the minimum and maximum salary. 
    Answers within 10-5 of the actual answer will be accepted.

Example 1:
    Input: salary = [4000,3000,1000,2000]
    Output: 2500.00000
    Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
        Average salary excluding minimum and maximum salary is (2000+3000) / 2 = 2500
Example 2:
    Input: salary = [1000,2000,3000]
    Output: 2000.00000
    Explanation: Minimum salary and maximum salary are 1000 and 3000 respectively.
        Average salary excluding minimum and maximum salary is (2000) / 1 = 2000

Constraints:
    3 <= salary.length <= 100
    1000 <= salary[i] <= 10^6
    All the integers of salary are unique.
"""


class Solution:
    def average(self, salary: List[int]) -> float:
        # exception case
        assert isinstance(salary, list) and len(salary) >= 3
        # main method: (simulate the process)
        return self._average(salary)

    def _average(self, salary: List[int]) -> float:
        assert isinstance(salary, list) and len(salary) >= 3

        return float((sum(salary) - max(salary) - min(salary)) / (len(salary) - 2))


def main():
    # Example 1: Output: 2500.00000
    salary = [4000, 3000, 1000, 2000]

    # Example 2: Output: 2000.00000
    # salary = [1000, 2000, 3000]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.average(salary)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
