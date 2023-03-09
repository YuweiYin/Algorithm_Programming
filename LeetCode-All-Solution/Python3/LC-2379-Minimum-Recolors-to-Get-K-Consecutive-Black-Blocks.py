#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2379-Minimum-Recolors-to-Get-K-Consecutive-Black-Blocks.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-03-09
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 2379 - (Easy) - Brace Expansion II
https://leetcode.com/problems/brace-expansion-ii/

Description & Requirement:
    You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', 
    representing the color of the ith block. 
    The characters 'W' and 'B' denote the colors white and black, respectively.

    You are also given an integer k, which is the desired number of consecutive black blocks.

    In one operation, you can recolor a white block such that it becomes a black block.

    Return the minimum number of operations needed such that 
    there is at least one occurrence of k consecutive black blocks.

Example 1:
    Input: blocks = "WBBWWBBWBW", k = 7
    Output: 3
    Explanation:
        One way to achieve 7 consecutive black blocks is to recolor the 0th, 3rd, and 4th blocks
        so that blocks = "BBBBBBBWBW". 
        It can be shown that there is no way to achieve 7 consecutive black blocks in less than 3 operations.
        Therefore, we return 3.
Example 2:
    Input: blocks = "WBWBBBW", k = 2
    Output: 0
    Explanation:
        No changes need to be made, since 2 consecutive black blocks already exist.
        Therefore, we return 0.

Constraints:
    n == blocks.length
    1 <= n <= 100
    blocks[i] is either 'W' or 'B'.
    1 <= k <= n
"""


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # exception case
        assert isinstance(blocks, str) and len(blocks) >= 1
        assert isinstance(k, int) and 1 <= k <= (len(blocks))
        # main method: (sliding window)
        return self._minimumRecolors(blocks, k)

    def _minimumRecolors(self, blocks: str, k: int) -> int:
        assert isinstance(blocks, str) and len(blocks) >= 1
        assert isinstance(k, int) and 1 <= k <= (len(blocks))

        res = int(1e9+7)
        cnt = 0
        for idx, block in enumerate(blocks):
            if block == "W":
                cnt += 1
            if idx >= k and blocks[idx - k] == "W":
                cnt -= 1
            if idx >= k - 1:
                res = min(res, cnt)

        return res


def main():
    # Example 1: Output: 3
    # blocks = "WBWBBBW"
    # k = 2

    # Example 2: Output: 0
    blocks = "WBWBBBW"
    k = 2

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.minimumRecolors(blocks, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
