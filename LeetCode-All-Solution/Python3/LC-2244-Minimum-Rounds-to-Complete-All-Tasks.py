#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2244-Minimum-Rounds-to-Complete-All-Tasks.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-01-04
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 2244 - (Medium) - Minimum Rounds to Complete All Tasks
https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/

Description & Requirement:
    You are given a 0-indexed integer array tasks, where tasks[i] represents the difficulty level of a task. 
    In each round, you can complete either 2 or 3 tasks of the same difficulty level.

    Return the minimum rounds required to complete all the tasks, 
    or -1 if it is not possible to complete all the tasks.

Example 1:
    Input: tasks = [2,2,3,3,2,4,4,4,4,4]
    Output: 4
    Explanation: To complete all the tasks, a possible plan is:
        - In the first round, you complete 3 tasks of difficulty level 2. 
        - In the second round, you complete 2 tasks of difficulty level 3. 
        - In the third round, you complete 3 tasks of difficulty level 4. 
        - In the fourth round, you complete 2 tasks of difficulty level 4.  
        It can be shown that all the tasks cannot be completed in fewer than 4 rounds, so the answer is 4.
Example 2:
    Input: tasks = [2,3,3]
    Output: -1
    Explanation: There is only 1 task of difficulty level 2, but in each round, 
        you can only complete either 2 or 3 tasks of the same difficulty level. 
        Hence, you cannot complete all the tasks, and the answer is -1.

Constraints:
    1 <= tasks.length <= 10^5
    1 <= tasks[i] <= 10^9
"""


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        # exception case
        assert isinstance(tasks, list) and len(tasks) >= 1
        # main method: (deal with different cases separately)
        return self._minimumRounds(tasks)

    def _minimumRounds(self, tasks: List[int]) -> int:
        assert isinstance(tasks, list) and len(tasks) >= 1

        cnt = dict({})
        for task in tasks:
            if task not in cnt:
                cnt[task] = 1
            else:
                cnt[task] += 1

        res = 0
        for k, v in cnt.items():
            if v == 1:
                return -1
            elif v == 2:
                res += 1
            elif v % 3 == 0:
                res += int(v // 3)
            else:
                res += int(v // 3) + 1

        return res


def main():
    # Example 1: Output: 4
    # tasks = [2, 2, 3, 3, 2, 4, 4, 4, 4, 4]

    # Example 2: Output: -1
    tasks = [2, 3, 3]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minimumRounds(tasks)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
