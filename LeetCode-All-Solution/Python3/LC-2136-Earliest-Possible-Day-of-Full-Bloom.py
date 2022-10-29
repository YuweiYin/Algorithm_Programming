#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2136-Earliest-Possible-Day-of-Full-Bloom.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-10-29
=================================================================="""

import sys
import time
from typing import List
from functools import cmp_to_key
# import collections

"""
LeetCode - 2136 - (Hard) - Earliest Possible Day of Full Bloom
https://leetcode.com/problems/earliest-possible-day-of-full-bloom/

Description & Requirement:
    You have n flower seeds. Every seed must be planted first before it can begin to grow, then bloom. 
    Planting a seed takes time and so does the growth of a seed. 
    You are given two 0-indexed integer arrays plantTime and growTime, of length n each:

        plantTime[i] is the number of full days it takes you to plant the ith seed. 
            Every day, you can work on planting exactly one seed. 
            You do not have to work on planting the same seed on consecutive days, 
            but the planting of a seed is not complete until you have worked plantTime[i] days on planting it in total.
        growTime[i] is the number of full days it takes the ith seed to grow after being completely planted. 
            After the last day of its growth, the flower blooms and stays bloomed forever.

    From the beginning of day 0, you can plant the seeds in any order.

    Return the earliest possible day where all seeds are blooming.

Example 1:
    Input: plantTime = [1,4,3], growTime = [2,3,1]
    Output: 9
    Explanation: The grayed out pots represent planting days, colored pots represent growing days, 
        and the flower represents the day it blooms.
        One optimal way is:
        On day 0, plant the 0th seed. The seed grows for 2 full days and blooms on day 3.
        On days 1, 2, 3, and 4, plant the 1st seed. The seed grows for 3 full days and blooms on day 8.
        On days 5, 6, and 7, plant the 2nd seed. The seed grows for 1 full day and blooms on day 9.
        Thus, on day 9, all the seeds are blooming.
Example 2:
    Input: plantTime = [1,2,3,2], growTime = [2,1,2,1]
    Output: 9
    Explanation: The grayed out pots represent planting days, colored pots represent growing days, 
        and the flower represents the day it blooms.
        One optimal way is:
        On day 1, plant the 0th seed. The seed grows for 2 full days and blooms on day 4.
        On days 0 and 3, plant the 1st seed. The seed grows for 1 full day and blooms on day 5.
        On days 2, 4, and 5, plant the 2nd seed. The seed grows for 2 full days and blooms on day 8.
        On days 6 and 7, plant the 3rd seed. The seed grows for 1 full day and blooms on day 9.
        Thus, on day 9, all the seeds are blooming.
Example 3:
    Input: plantTime = [1], growTime = [1]
    Output: 2
    Explanation: On day 0, plant the 0th seed. The seed grows for 1 full day and blooms on day 2.
        Thus, on day 2, all the seeds are blooming.

Constraints:
    n == plantTime.length == growTime.length
    1 <= n <= 10^5
    1 <= plantTime[i], growTime[i] <= 10^4
"""


class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        # exception case
        assert isinstance(plantTime, list) and len(plantTime) >= 1
        assert isinstance(growTime, list) and len(plantTime) == len(growTime)
        for t in plantTime + growTime:
            assert isinstance(t, int) and t >= 1
        # main method: (sorting)
        return self._earliestFullBloom(plantTime, growTime)

    def _earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        """
        Runtime: 2198 ms, faster than 82.58% of Python3 online submissions for Earliest Possible Day of Full Bloom.
        Memory Usage: 33.3 MB, less than 43.55% of Python3 online submissions for Earliest Possible Day of Full Bloom.
        """
        assert isinstance(plantTime, list) and len(plantTime) >= 1
        assert isinstance(growTime, list) and len(plantTime) == len(growTime)

        def compare_fn(i: int, j: int) -> int:
            if growTime[i] > growTime[j]:
                return -1
            if growTime[i] < growTime[j]:
                return 1
            return 0

        n = len(plantTime)
        idx = list(range(n))
        idx.sort(key=cmp_to_key(compare_fn))

        prev = res = 0
        for i in idx:
            res = max(res, prev + plantTime[i] + growTime[i])
            prev += plantTime[i]

        return res


def main():
    # Example 1: Output: 9
    plantTime = [1, 4, 3]
    growTime = [2, 3, 1]

    # Example 2: Output: 9
    # plantTime = [1, 2, 3, 2]
    # growTime = [2, 1, 2, 1]

    # Example 3: Output: 2
    # plantTime = [1]
    # growTime = [1]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.earliestFullBloom(plantTime, growTime)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
