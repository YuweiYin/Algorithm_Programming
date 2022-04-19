#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0821-Shortest-Distance-to-a-Character.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-19
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0821 - (Easy) - Shortest Distance to a Character
https://leetcode.com/problems/shortest-distance-to-a-character/

Description & Requirement:
    Given a string s and a character c that occurs in s, return an array of integers answer 
    where answer.length == s.length and answer[i] is the distance 
    from index i to the closest occurrence of character c in s.

    The distance between two indices i and j is abs(i - j), where abs is the absolute value function.

Example 1:
    Input: s = "loveleetcode", c = "e"
    Output: [3,2,1,0,1,0,0,1,2,2,1,0]
    Explanation: The character 'e' appears at indices 3, 5, 6, and 11 (0-indexed).
        The closest occurrence of 'e' for index 0 is at index 3, so the distance is abs(0 - 3) = 3.
        The closest occurrence of 'e' for index 1 is at index 3, so the distance is abs(1 - 3) = 2.
        For index 4, there is a tie between the 'e' at index 3 and the 'e' at index 5, 
            but the distance is still the same: abs(4 - 3) == abs(4 - 5) = 1.
        The closest occurrence of 'e' for index 8 is at index 6, so the distance is abs(8 - 6) = 2.
Example 2:
    Input: s = "aaab", c = "b"
    Output: [3,2,1,0]

Constraints:
    1 <= s.length <= 10^4
    s[i] and c are lowercase English letters.
    It is guaranteed that c occurs at least once in s.
"""


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        # exception case
        assert isinstance(s, str) and len(s) >= 1 and s.islower()
        assert isinstance(c, str) and len(c) == 1 and c.islower()
        # main method: (record the index of all target c in s, then scan twice)
        #     left to right, get the min distance from the current char to the closest c on its left
        #     right to left, get the min distance from the current chat to the closest c on its right
        return self._shortestToChar(s, c)

    def _shortestToChar(self, s: str, c: str) -> List[int]:
        """
        Runtime: 39 ms, faster than 95.83% of Python3 online submissions for Shortest Distance to a Character.
        Memory Usage: 14 MB, less than 57.93% of Python3 online submissions for Shortest Distance to a Character.
        """
        len_s = len(s)
        assert len_s >= 1
        assert len(c) == 1

        if len_s == 1:
            return [0]

        res = [int(1e9+7) for _ in range(len_s)]  # int(1e9+7) is INF, since 1 <= s.length <= 10^4
        closest_left_c = -1
        for idx, ch in enumerate(s):
            if ch == c:
                res[idx] = 0
                closest_left_c = idx
            else:
                if closest_left_c != -1:
                    # the min distance from the current char to the closest c on its left
                    res[idx] = idx - closest_left_c
                # else: there's no left c

        # right to left, get the min distance from the current chat to the closest c on its right
        idx = len_s - 1
        closest_right_c = -1
        while idx >= 0:
            ch = s[idx]
            if ch == c:
                res[idx] = 0
                closest_right_c = idx
            else:
                if closest_right_c != -1:
                    # the min distance from the current chat to the closest c on its right
                    res[idx] = min(res[idx], closest_right_c - idx)
                # else: there's no right c

            idx -= 1

        return res


def main():
    # Example 1: Output: [3,2,1,0,1,0,0,1,2,2,1,0]
    s = "loveleetcode"
    c = "e"

    # Example 2: Output: [3,2,1,0]
    # s = "aaab"
    # c = "b"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.shortestToChar(s, c)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
