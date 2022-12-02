#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1769-Minimum-Number-of-Operations-to-Move-All-Balls-to-Each-Box.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-12-02
=================================================================="""

import sys
import time
from typing import List
# import itertools

"""
LeetCode - 1769 - (Medium) - Minimum Number of Operations to Move All Balls to Each Box
https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/

Description & Requirement:
    You have n boxes. You are given a binary string boxes of length n, 
    where boxes[i] is '0' if the i-th box is empty, and '1' if it contains one ball.

    In one operation, you can move one ball from a box to an adjacent box. 
    Box i is adjacent to box j if abs(i - j) == 1. 
    Note that after doing so, there may be more than one ball in some boxes.

    Return an array answer of size n, 
    where answer[i] is the minimum number of operations needed to move all the balls to the i-th box.

    Each answer[i] is calculated considering the initial state of the boxes.

Example 1:
    Input: boxes = "110"
    Output: [1,1,3]
    Explanation: The answer for each box is as follows:
        1) First box: you will have to move one ball from the second box to the first box in one operation.
        2) Second box: you will have to move one ball from the first box to the second box in one operation.
        3) Third box: you will have to move one ball from the first box to the third box in two operations, 
            and move one ball from the second box to the third box in one operation.
Example 2:
    Input: boxes = "001011"
    Output: [11,8,5,4,3,4]

Constraints:
    n == boxes.length
    1 <= n <= 2000
    boxes[i] is either '0' or '1'.
"""


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # exception case
        assert isinstance(boxes, str) and len(boxes) >= 1
        # main method: (scan from left to right and right to left)
        return self._minOperations(boxes)

    def _minOperations(self, boxes: str) -> List[int]:
        """
        Runtime: 85 ms, faster than 90.02% of submissions for Minimum Number of Ops to Move All Balls to Each Box.
        Memory Usage: 14.4 MB, less than 27.90% of submissions for Minimum Number of Ops to Move All Balls to Each Box.
        """
        assert isinstance(boxes, str) and len(boxes) >= 1

        left, right, operations = int(boxes[0]), 0, 0
        for idx in range(1, len(boxes)):
            if boxes[idx] == '1':
                right += 1
                operations += idx

        res = [operations]
        for idx in range(1, len(boxes)):
            operations += left - right
            if boxes[idx] == '1':
                left += 1
                right -= 1
            res.append(operations)

        return res


def main():
    # Example 1: Output: [1,1,3]
    # boxes = "110"

    # Example 2: Output: [11,8,5,4,3,4]
    boxes = "001011"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minOperations(boxes)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
