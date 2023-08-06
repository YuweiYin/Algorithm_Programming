#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0920-Number-of-Music-Playlists.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-08-06
=================================================================="""

import sys
import time
# from typing import List
import functools
# import itertools

"""
LeetCode - 0920 - (Hard) - Number of Music Playlists
https://leetcode.com/problems/number-of-music-playlists/

Description & Requirement:
    Your music player contains n different songs. You want to listen to goal songs 
    (not necessarily different) during your trip. To avoid boredom, you will create a playlist so that:

        Every song is played at least once.
        A song can only be played again only if k other songs have been played.

    Given n, goal, and k, return the number of possible playlists that you can create. 
    Since the answer can be very large, return it modulo 109 + 7.

Example 1:
    Input: n = 3, goal = 3, k = 1
    Output: 6
    Explanation: There are 6 possible playlists: 
        [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], and [3, 2, 1].
Example 2:
    Input: n = 2, goal = 3, k = 0
    Output: 6
    Explanation: There are 6 possible playlists: 
        [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2, 1], [2, 1, 2], and [1, 2, 2].
Example 3:
    Input: n = 2, goal = 3, k = 1
    Output: 2
    Explanation: There are 2 possible playlists: [1, 2, 1] and [2, 1, 2].

Constraints:
    0 <= k < n <= goal <= 100
"""


class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        # exception case
        assert isinstance(n, int) and isinstance(goal, int) and isinstance(k, int) and 0 <= k < n <= goal
        # main method: (dynamic programming)
        return self._numMusicPlaylists(n, goal, k)

    def _numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        assert isinstance(n, int) and isinstance(goal, int) and isinstance(k, int) and 0 <= k < n <= goal

        MOD = int(1e9+7)

        @functools.lru_cache(maxsize=None)
        def __dp(i, j):
            if i == 0:
                return j == 0

            ans = (__dp(i - 1, j - 1) * (n - j + 1)) % MOD
            ans += (__dp(i - 1, j) * max(j - k, 0)) % MOD

            return ans % MOD

        return __dp(goal, n) % MOD


def main():
    # Example 1: Output: 6
    # n = 3
    # goal = 3
    # k = 1

    # Example 2: Output: 6
    # n = 2
    # goal = 3
    # k = 0

    # Example 3: Output: 2
    n = 2
    goal = 3
    k = 1

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.numMusicPlaylists(n, goal, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
