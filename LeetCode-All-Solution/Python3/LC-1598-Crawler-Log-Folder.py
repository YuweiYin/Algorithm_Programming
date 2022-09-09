#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1598-Crawler-Log-Folder.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-09-09
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1598 - (Easy) - Crawler Log Folder
https://leetcode.com/problems/crawler-log-folder/

Description & Requirement:
    The Leetcode file system keeps a log each time some user performs a change folder operation.

    The operations are described below:
        "../" : Move to the parent folder of the current folder. 
            (If you are already in the main folder, remain in the same folder).
        "./" : Remain in the same folder.
        "x/" : Move to the child folder named x (This folder is guaranteed to always exist).

    You are given a list of strings logs where logs[i] is the operation performed by the user at the ith step.

    The file system starts in the main folder, then the operations in logs are performed.

    Return the minimum number of operations needed to go back to the main folder after the change folder operations.

Example 1:
    Input: logs = ["d1/","d2/","../","d21/","./"]
    Output: 2
    Explanation: Use this change folder operation "../" 2 times and go back to the main folder.
Example 2:
    Input: logs = ["d1/","d2/","./","d3/","../","d31/"]
    Output: 3
Example 3:
    Input: logs = ["d1/","../","../","../"]
    Output: 0

Constraints:
    1 <= logs.length <= 10^3
    2 <= logs[i].length <= 10
    logs[i] contains lowercase English letters, digits, '.', and '/'.
    logs[i] follows the format described in the statement.
    Folder names consist of lowercase English letters and digits.
"""


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        # exception case
        assert isinstance(logs, list) and len(logs) >= 1
        # main method: (compute the depth of the current folder)
        return self._minOperations(logs)

    def _minOperations(self, logs: List[str]) -> int:
        """
        Runtime: 46 ms, faster than 96.06% of Python3 online submissions for Crawler Log Folder.
        Memory Usage: 14.1 MB, less than 87.36% of Python3 online submissions for Crawler Log Folder.
        """
        assert isinstance(logs, list) and len(logs) >= 1

        depth = 0
        for log in logs:
            if log == "../":
                depth = depth - 1 if depth > 0 else 0
            elif log == "./":
                continue
            else:
                depth += 1

        return depth


def main():
    # Example 1: Output: 2
    # logs = ["d1/", "d2/", "../", "d21/", "./"]

    # Example 2: Output: 3
    # logs = ["d1/", "d2/", "./", "d3/", "../", "d31/"]

    # Example 3: Output: 0
    logs = ["d1/", "../", "../", "../"]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minOperations(logs)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
