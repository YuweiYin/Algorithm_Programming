#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1419-Minimum-Number-of-Frogs-Croaking.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-05-06
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 1419 - (Medium) - Minimum Number of Frogs Croaking
https://leetcode.com/problems/minimum-number-of-frogs-croaking/

Description & Requirement:
    You are given the string croakOfFrogs, which represents a combination of the string "croak" 
    from different frogs, that is, multiple frogs can croak at the same time, so multiple "croak" are mixed.

    Return the minimum number of different frogs to finish all the croaks in the given string.

    A valid "croak" means a frog is printing five letters 'c', 'r', 'o', 'a', and 'k' sequentially. 
    The frogs have to print all five letters to finish a croak. 
    If the given string is not a combination of a valid "croak" return -1.

Example 1:
    Input: croakOfFrogs = "croakcroak"
    Output: 1 
    Explanation: One frog yelling "croak" twice.
Example 2:
    Input: croakOfFrogs = "crcoakroak"
    Output: 2 
    Explanation: The minimum number of frogs is two. 
        The first frog could yell "crcoakroak".
        The second frog could yell later "crcoakroak".
Example 3:
    Input: croakOfFrogs = "croakcrook"
    Output: -1
    Explanation: The given string is an invalid combination of "croak" from different frogs.

Constraints:
    1 <= croakOfFrogs.length <= 10^5
    croakOfFrogs is either 'c', 'r', 'o', 'a', or 'k'.
"""


class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        # exception case
        assert isinstance(croakOfFrogs, str) and len(croakOfFrogs) >= 1
        # main method: (simulate the process)
        return self._minNumberOfFrogs(croakOfFrogs)

    def _minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        assert isinstance(croakOfFrogs, str) and len(croakOfFrogs) >= 1

        if len(croakOfFrogs) % 5:
            return -1

        res, frog_num = 0, 0
        cnt = [0] * 4
        ch2digit = {'c': 0, 'r': 1, 'o': 2, 'a': 3, 'k': 4}

        for ch in croakOfFrogs:
            digit = ch2digit[ch]
            if digit == 0:
                cnt[digit] += 1
                frog_num += 1
                if frog_num > res:
                    res = frog_num
            else:
                if cnt[digit - 1] == 0:
                    return -1
                cnt[digit - 1] -= 1
                if digit == 4:
                    frog_num -= 1
                else:
                    cnt[digit] += 1

        if frog_num > 0:
            return -1

        return res


def main():
    # Example 1: Output: 1
    croakOfFrogs = "croakcroak"

    # Example 2: Output: 2
    # croakOfFrogs = "crcoakroak"

    # Example 3: Output: -1
    # croakOfFrogs = "croakcrook"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minNumberOfFrogs(croakOfFrogs)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
