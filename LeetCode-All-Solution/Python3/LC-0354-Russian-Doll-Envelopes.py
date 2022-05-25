#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0354-Russian-Doll-Envelopes.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-05-25
=================================================================="""

import sys
import time
from typing import List
import bisect
# import functools

"""
LeetCode - 0354 - (Hard) - Russian Doll Envelopes
https://leetcode.com/problems/russian-doll-envelopes/

Description & Requirement:
    You are given a 2D array of integers envelopes where envelopes[i] = [w_i, h_i] 
    represents the width and the height of an envelope.

    One envelope can fit into another if and only if both the width and height of one envelope are greater than 
    the other envelope's width and height.

    Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).

    Note: You cannot rotate an envelope.

Example 1:
    Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
    Output: 3
    Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
Example 2:
    Input: envelopes = [[1,1],[1,1],[1,1]]
    Output: 1

Constraints:
    1 <= envelopes.length <= 10^5
    envelopes[i].length == 2
    1 <= w_i, h_i <= 10^5
"""


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # exception case
        assert isinstance(envelopes, list) and len(envelopes) >= 1
        # main method: (sort and find the longest monotonous 2D-array)
        return self._maxEnvelopes(envelopes)

    def _maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        assert isinstance(envelopes, list) and len(envelopes) >= 1
        len_env = len(envelopes)
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        dp_h = [envelopes[0][1]]
        for idx in range(1, len_env):
            # after sorting, envelopes[idx][0] <= envelopes[idx][0]
            cur_h = envelopes[idx][1]
            if cur_h > dp_h[-1]:
                dp_h.append(cur_h)
            else:
                bi_idx = bisect.bisect_left(dp_h, cur_h)
                dp_h[bi_idx] = cur_h

        return len(dp_h)


def main():
    # Example 1: Output: 3
    envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]

    # Example 2: Output: 1
    # envelopes = [[1, 1], [1, 1], [1, 1]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maxEnvelopes(envelopes)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
