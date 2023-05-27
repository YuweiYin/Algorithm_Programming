#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1093-Statistics-from-a-Large-Sample.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-05-27
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1093 - (Medium) - Statistics from a Large Sample
https://leetcode.com/problems/statistics-from-a-large-sample/

Description & Requirement:
    You are given a large sample of integers in the range [0, 255]. 
    Since the sample is so large, it is represented by an array count where 
    count[k] is the number of times that k appears in the sample.

    Calculate the following statistics:
        - minimum: The minimum element in the sample.
        - maximum: The maximum element in the sample.
        - mean: The average of the sample, calculated as the total sum of 
            all elements divided by the total number of elements.
        - median:
            - If the sample has an odd number of elements, 
                then the median is the middle element once the sample is sorted.
            - If the sample has an even number of elements, 
                then the median is the average of the two middle elements once the sample is sorted.
        - mode: The number that appears the most in the sample. It is guaranteed to be unique.

    Return the statistics of the sample as an array of floating-point numbers [minimum, maximum, mean, median, mode]. 
    Answers within 10-5 of the actual answer will be accepted.

Example 1:
    Input: count = [0,1,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    Output: [1.00000,3.00000,2.37500,2.50000,3.00000]
    Explanation: The sample represented by count is [1,2,2,2,3,3,3,3].
        The minimum and maximum are 1 and 3 respectively.
        The mean is (1+2+2+2+3+3+3+3) / 8 = 19 / 8 = 2.375.
        Since the size of the sample is even, the median is the average of the two middle elements 2 and 3, which is 2.5.
        The mode is 3 as it appears the most in the sample.
Example 2:
    Input: count = [0,4,3,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,0,0,0]
    Output: [1.00000,4.00000,2.18182,2.00000,1.00000]
    Explanation: The sample represented by count is [1,1,1,1,2,2,2,3,3,4,4].
        The minimum and maximum are 1 and 4 respectively.
        The mean is (1+1+1+1+2+2+2+3+3+4+4) / 11 = 24 / 11 = 2.18181818... 
            (for display purposes, the output shows the rounded number 2.18182).
        Since the size of the sample is odd, the median is the middle element 2.
        The mode is 1 as it appears the most in the sample.

Constraints:
    count.length == 256
    0 <= count[i] <= 10^9
    1 <= sum(count) <= 10^9
    The mode of the sample that count represents is unique.
"""


class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        # exception case
        assert isinstance(count, list) and len(count) == 256
        # main method: (process simulation)
        return self._sampleStats(count)

    def _sampleStats(self, count: List[int]) -> List[float]:
        assert isinstance(count, list) and len(count) == 256

        total = sum(count)

        # mean = 0.0
        median = 0.0
        min_num = 256
        max_num = 0
        mode = 0

        left = (total + 1) >> 1
        right = (total + 2) >> 1
        cnt = 0
        max_freq = 0
        sum_ = 0
        for i in range(len(count)):
            sum_ += count[i] * i
            if count[i] > max_freq:
                max_freq = count[i]
                mode = i
            if count[i] > 0:
                if min_num == 256:
                    min_num = i
                max_num = i
            if cnt < right <= cnt + count[i]:
                median += i
            if cnt < left <= cnt + count[i]:
                median += i
            cnt += count[i]
        mean = sum_ / total
        median = median / 2.0

        res = [min_num, max_num, mean, median, mode]
        res = [float(num) for num in res]

        return res


def main():
    # Example 1: Output: [1.00000,3.00000,2.37500,2.50000,3.00000]
    count = [
        0, 1, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    ]

    # Example 2: Output: [1.00000,4.00000,2.18182,2.00000,1.00000]
    # count = [
    #     0, 4, 3, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    # ]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.sampleStats(count)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
