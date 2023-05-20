#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1079-Letter-Tile-Possibilities.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-05-19
=================================================================="""

import sys
import time
# from typing import List
import collections
# import functools

"""
LeetCode - 1079 - (Medium) - Letter Tile Possibilities
https://leetcode.com/problems/letter-tile-possibilities/

Description & Requirement:
    You have n  tiles, where each tile has one letter tiles[i] printed on it.

    Return the number of possible non-empty sequences of letters 
    you can make using the letters printed on those tiles.

Example 1:
    Input: tiles = "AAB"
    Output: 8
    Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
Example 2:
    Input: tiles = "AAABBC"
    Output: 188
Example 3:
    Input: tiles = "V"
    Output: 1

Constraints:
    1 <= tiles.length <= 7
    tiles consists of uppercase English letters.
"""


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        # exception case
        assert isinstance(tiles, str) and len(tiles) >= 1
        # main method: (backtrace)
        return self._numTilePossibilities(tiles)

    def _numTilePossibilities(self, tiles: str) -> int:
        assert isinstance(tiles, str) and len(tiles) >= 1

        count = collections.Counter(tiles)
        tile = set(tiles)

        def __dfs(i):
            if i == 0:
                return 1
            res = 1
            for t in tile:
                if count[t] > 0:
                    count[t] -= 1
                    res += __dfs(i - 1)
                    count[t] += 1
            return res

        return __dfs(len(tiles)) - 1


def main():
    # Example 1: Output: 8
    tiles = "AAB"

    # Example 2: Output: 188
    # tiles = "AAABBC"

    # Example 3: Output: 1
    # tiles = "V"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.numTilePossibilities(tiles)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
