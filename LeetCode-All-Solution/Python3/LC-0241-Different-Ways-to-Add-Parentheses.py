#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0241-Different-Ways-to-Add-Parentheses.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-07-01
=================================================================="""

import sys
import time
from typing import List
import functools

"""
LeetCode - 0241 - (Medium) - Different Ways to Add Parentheses
https://leetcode.com/problems/different-ways-to-add-parentheses/

Description & Requirement:
    Given a string expression of numbers and operators, 
    return all possible results from computing all the different possible ways to group numbers and operators. 
    You may return the answer in any order.

    The test cases are generated such that the output values fit in a 32-bit integer and 
    the number of different results does not exceed 10^4.

Example 1:
    Input: expression = "2-1-1"
    Output: [0,2]
    Explanation:
        ((2-1)-1) = 0 
        (2-(1-1)) = 2
Example 2:
    Input: expression = "2*3-4*5"
    Output: [-34,-14,-10,-10,10]
    Explanation:
        (2*(3-(4*5))) = -34 
        ((2*3)-(4*5)) = -14 
        ((2*(3-4))*5) = -10 
        (2*((3-4)*5)) = -10 
        (((2*3)-4)*5) = 10

Constraints:
    1 <= expression.length <= 20
    expression consists of digits and the operator '+', '-', and '*'.
    All the integer values in the input expression are in the range [0, 99].
"""


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # exception case
        assert isinstance(expression, str) and len(expression) >= 1
        # main method: (DFS & memorized search)
        return self._diffWaysToCompute(expression)

    def _diffWaysToCompute(self, expression: str) -> List[int]:
        """
        Runtime: 38 ms, faster than 89.71% of Python3 online submissions for Different Ways to Add Parentheses.
        Memory Usage: 14.2 MB, less than 19.11% of Python3 online submissions for Different Ways to Add Parentheses.
        """
        assert isinstance(expression, str) and len(expression) >= 1

        ADD = -1  # ADDITION
        SUB = -2  # SUBTRACTION
        MUL = -3  # MULTIPLICATION

        ops = []  # operators
        idx, n = 0, len(expression)
        while idx < n:
            if expression[idx].isdigit():
                x = 0
                while idx < n and expression[idx].isdigit():
                    x = x * 10 + int(expression[idx])
                    idx += 1
                ops.append(x)
            else:
                if expression[idx] == '+':
                    ops.append(ADD)
                elif expression[idx] == '-':
                    ops.append(SUB)
                else:
                    ops.append(MUL)
                idx += 1

        @functools.lru_cache(maxsize=None)
        def __dfs(_l: int, _r: int) -> List[int]:
            if _l == _r:
                return [ops[_l]]
            res = []
            for i in range(_l, _r, 2):
                left = __dfs(_l, i)
                right = __dfs(i + 2, _r)
                for x in left:
                    for y in right:
                        if ops[i + 1] == ADD:
                            res.append(x + y)
                        elif ops[i + 1] == SUB:
                            res.append(x - y)
                        else:
                            res.append(x * y)
            return res

        return __dfs(0, len(ops) - 1)


def main():
    # Example 1: Output: [0,2]
    # expression = "2-1-1"

    # Example 2: Output: [-34,-14,-10,-10,10]
    expression = "2*3-4*5"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.diffWaysToCompute(expression)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
