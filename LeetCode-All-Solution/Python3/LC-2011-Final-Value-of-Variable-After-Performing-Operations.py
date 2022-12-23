#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2011-Final-Value-of-Variable-After-Performing-Operations.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-12-23
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 2011 - (Easy) - Final Value of Variable After Performing Operations
https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

Description & Requirement:
    There is a programming language with only four operations and one variable X:
        ++X and X++ increments the value of the variable X by 1.
        --X and X-- decrements the value of the variable X by 1.

    Initially, the value of X is 0.

    Given an array of strings operations containing a list of operations, 
    return the final value of X after performing all the operations.

Example 1:
    Input: operations = ["--X","X++","X++"]
    Output: 1
    Explanation: The operations are performed as follows:
        Initially, X = 0.
        --X: X is decremented by 1, X =  0 - 1 = -1.
        X++: X is incremented by 1, X = -1 + 1 =  0.
        X++: X is incremented by 1, X =  0 + 1 =  1.
Example 2:
    Input: operations = ["++X","++X","X++"]
    Output: 3
    Explanation: The operations are performed as follows:
        Initially, X = 0.
        ++X: X is incremented by 1, X = 0 + 1 = 1.
        ++X: X is incremented by 1, X = 1 + 1 = 2.
        X++: X is incremented by 1, X = 2 + 1 = 3.
Example 3:
    Input: operations = ["X++","++X","--X","X--"]
    Output: 0
    Explanation: The operations are performed as follows:
        Initially, X = 0.
        X++: X is incremented by 1, X = 0 + 1 = 1.
        ++X: X is incremented by 1, X = 1 + 1 = 2.
        --X: X is decremented by 1, X = 2 - 1 = 1.
        X--: X is decremented by 1, X = 1 - 1 = 0.

Constraints:
    1 <= operations.length <= 100
    operations[i] will be either "++X", "X++", "--X", or "X--".
"""


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        # exception case
        assert isinstance(operations, list) and len(operations) >= 1
        # main method: (simulate the process)
        return self._finalValueAfterOperations(operations)

    def _finalValueAfterOperations(self, operations: List[str]) -> int:
        """
        Time: beats 90.97%; Space: beats 96.81%
        """
        assert isinstance(operations, list) and len(operations) >= 1

        return sum(1 if op[1] == '+' else -1 for op in operations)


def main():
    # Example 1: Output: 1
    # operations = ["--X", "X++", "X++"]

    # Example 2: Output: 3
    # operations = ["++X", "++X", "X++"]

    # Example 3: Output: 0
    operations = ["X++", "++X", "--X", "X--"]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.finalValueAfterOperations(operations)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
