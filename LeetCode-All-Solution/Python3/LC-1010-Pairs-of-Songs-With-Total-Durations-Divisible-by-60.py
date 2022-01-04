#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1010-Pairs-of-Songs-With-Total-Durations-Divisible-by-60.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-04
=================================================================="""

import sys
import time
from typing import List

"""
LeetCode - 1010 - (Medium) - Pairs of Songs With Total Durations Divisible by 60
https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

Description:
    You are given a list of songs where the i-th song has a duration of time[i] seconds.

Requirement:
    Return the number of pairs of songs for which their total duration in seconds is divisible by 60. 
    Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.

Example 1:
    Input: time = [30,20,150,100,40]
    Output: 3
    Explanation: Three pairs have a total duration divisible by 60:
        (time[0] = 30, time[2] = 150): total duration 180
        (time[1] = 20, time[3] = 100): total duration 120
        (time[1] = 20, time[4] = 40): total duration 60
Example 2:
    Input: time = [60,60,60]
    Output: 3
    Explanation: All three pairs have a total duration of 120, which is divisible by 60.

Constraints:
    1 <= time.length <= 6 * 10^4
    1 <= time[i] <= 500
"""


class Solution:
    def numPairsDivisibleBy60(self, _time: List[int]) -> int:
        # exception case
        if not isinstance(_time, list) or len(_time) <= 1:
            return 0
        # border case
        if len(_time) == 2:
            return 1 if (_time[0] + _time[1]) % 60 == 0 else 0
        # double loop O(n^2): test each pair or the list: for(i=0; i<max; ++i) { for(j=i+1; j<max; ++j) {...} }
        # main method: (hash dict O(n): similar to TwoSum problem)
        return self._numPairsDivisibleBy60(_time)

    def _numPairsDivisibleBy60(self, _time: List[int]) -> int:
        len_num = len(_time)
        target = 60
        res_counter = 0
        # diff_dict = dict({(target - _time[0]) % target: 1})  # key: diff from (pair_sum % 60 == 0); value: counter
        mod_num_dict = dict({_time[0] % target: 1})  # key: every number mod 60; value: counter
        # one loop, pair cur_num with the diff before
        cur_index = 1  # start from the second number (try to pair with the first number)
        while cur_index < len_num:
            cur_num = _time[cur_index] % target
            cur_diff = (target - cur_num) % target
            # if successfully paired, then update res_counter
            if cur_diff in mod_num_dict:  # this means: pair_sum % target == 0
                res_counter += mod_num_dict[cur_diff]
            # update the mod_num_dict (to be paired with later numbers)
            if cur_num in mod_num_dict:
                mod_num_dict[cur_num] += 1
            else:  # add cur_diff to diff_dict
                mod_num_dict[cur_num] = 1
            cur_index += 1

        return res_counter


def main():
    # Example 1: Output: 3
    _time = [30, 20, 150, 100, 40]

    # Example 2: Output: 3
    # _time = [60, 60, 60]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.numPairsDivisibleBy60(_time)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
