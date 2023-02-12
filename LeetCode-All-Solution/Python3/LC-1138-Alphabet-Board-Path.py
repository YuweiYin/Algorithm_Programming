#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1138-Alphabet-Board-Path.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-02-12
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 1138 - (Medium) - Alphabet Board Path
https://leetcode.com/problems/alphabet-board-path/

Description & Requirement:
    On an alphabet board, we start at position (0, 0), corresponding to character board[0][0].

    Here, board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"], as shown in the diagram below.

    We may make the following moves:
        'U' moves our position up one row, if the position exists on the board;
        'D' moves our position down one row, if the position exists on the board;
        'L' moves our position left one column, if the position exists on the board;
        'R' moves our position right one column, if the position exists on the board;
        '!' adds the character board[r][c] at our current position (r, c) to the answer.

    (Here, the only positions that exist on the board are positions with letters on them.)

    Return a sequence of moves that makes our answer equal to target in the minimum number of moves. 
    You may return any path that does so.

Example 1:
    Input: target = "leet"
    Output: "DDR!UURRR!!DDD!"
Example 2:
    Input: target = "code"
    Output: "RR!DDRR!UUL!R!"

Constraints:
    1 <= target.length <= 100
    target consists only of English lowercase letters.
"""


class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        # exception case
        assert isinstance(target, str) and len(target) >= 1
        # main method: (simulate the process)
        return self._alphabetBoardPath(target)

    def _alphabetBoardPath(self, target: str) -> str:
        assert isinstance(target, str) and len(target) >= 1

        res = []
        i = j = 0
        ord_a = ord("a")

        for ch in target:
            diff = ord(ch) - ord_a
            div, mod = diff // 5, diff % 5

            while j > mod:
                j -= 1
                res.append("L")
            while i > div:
                i -= 1
                res.append("U")
            while j < mod:
                j += 1
                res.append("R")
            while i < div:
                i += 1
                res.append("D")

            res.append("!")

        return "".join(res)


def main():
    # Example 1: Output: "DDR!UURRR!!DDD!"
    target = "leet"

    # Example 2: Output: "RR!DDRR!UUL!R!"
    # target = "code"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.alphabetBoardPath(target)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
