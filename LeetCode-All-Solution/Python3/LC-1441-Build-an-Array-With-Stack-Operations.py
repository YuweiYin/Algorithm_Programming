#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1441-Build-an-Array-With-Stack-Operations.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-10-15
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1441 - (Medium) - Build an Array With Stack Operations
https://leetcode.com/problems/build-an-array-with-stack-operations/

Description & Requirement:
    You are given an integer array target and an integer n.

    You have an empty stack with the two following operations:
        "Push": pushes an integer to the top of the stack.
        "Pop": removes the integer on the top of the stack.

    You also have a stream of the integers in the range [1, n].

    Use the two stack operations to make the numbers in the stack (from the bottom to the top) equal to target. 
    You should follow the following rules:
        If the stream of the integers is not empty, 
            pick the next integer from the stream and push it to the top of the stack.
        If the stack is not empty, pop the integer at the top of the stack.
        If, at any moment, the elements in the stack (from the bottom to the top) are equal to target, 
            do not read new integers from the stream and do not do more operations on the stack.

    Return the stack operations needed to build target following the mentioned rules. 
    If there are multiple valid answers, return any of them.

Example 1:
    Input: target = [1,3], n = 3
    Output: ["Push","Push","Pop","Push"]
    Explanation: Initially the stack s is empty. The last element is the top of the stack.
        Read 1 from the stream and push it to the stack. s = [1].
        Read 2 from the stream and push it to the stack. s = [1,2].
        Pop the integer on the top of the stack. s = [1].
        Read 3 from the stream and push it to the stack. s = [1,3].
Example 2:
    Input: target = [1,2,3], n = 3
    Output: ["Push","Push","Push"]
    Explanation: Initially the stack s is empty. The last element is the top of the stack.
        Read 1 from the stream and push it to the stack. s = [1].
        Read 2 from the stream and push it to the stack. s = [1,2].
        Read 3 from the stream and push it to the stack. s = [1,2,3].
Example 3:
    Input: target = [1,2], n = 4
    Output: ["Push","Push"]
    Explanation: Initially the stack s is empty. The last element is the top of the stack.
        Read 1 from the stream and push it to the stack. s = [1].
        Read 2 from the stream and push it to the stack. s = [1,2].
        Since the stack (from the bottom to the top) is equal to target, we stop the stack operations.
        The answers that read integer 3 from the stream are not accepted.

Constraints:
    1 <= target.length <= 100
    1 <= n <= 100
    1 <= target[i] <= n
    target is strictly increasing.
"""


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        # exception case
        assert isinstance(target, list) and len(target) >= 1
        assert isinstance(n, int) and n >= 1
        for num in target:
            assert isinstance(num, int) and 1 <= num <= n
        # main method: (process simulation)
        return self._buildArray(target, n)

    def _buildArray(self, target: List[int], n: int) -> List[str]:
        assert isinstance(target, list) and len(target) >= 1
        assert isinstance(n, int) and n >= 1

        res = []
        pre = 0
        for num in target:
            for _ in range(num - pre - 1):
                res.append('Push')
                res.append('Pop')
            res.append('Push')
            pre = num

        return res


def main():
    # Example 1: Output: ["Push","Push","Pop","Push"]
    # target = [1, 3]
    # n = 3

    # Example 2: Output: ["Push","Push","Push"]
    target = [1, 2, 3]
    n = 3

    # Example 3: Output: ["Push","Push"]
    # target = [1, 2]
    # n = 4

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.buildArray(target, n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
