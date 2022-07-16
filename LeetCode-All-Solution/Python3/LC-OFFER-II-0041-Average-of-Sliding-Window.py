#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-OFFER-II-0041-Average-of-Sliding-Window.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-07-16
=================================================================="""

import sys
import time
import collections
# from typing import List
# import functools

"""
LeetCode - OFFER-II-0041 - (Easy) - Average of Sliding Window
https://leetcode.cn/problems/qIsx9U/
https://leetcode.com/problems/moving-average-from-data-stream/

Description & Requirement:
    给定一个整数数据流和一个窗口大小，根据该滑动窗口的大小，计算滑动窗口里所有数字的平均值。

    实现 MovingAverage 类：
        MovingAverage(int size) 用窗口大小 size 初始化对象。
        double next(int val) 成员函数 next 每次调用的时候都会往滑动窗口增加一个整数，
            请计算并返回数据流中最后 size 个值的移动平均值，即滑动窗口里所有数字的平均值。

Example 1:
    Input:
        inputs = ["MovingAverage", "next", "next", "next", "next"]
        inputs = [[3], [1], [10], [3], [5]]
    Output:
        [null, 1.0, 5.5, 4.66667, 6.0]
    Explanation:
        MovingAverage movingAverage = new MovingAverage(3);
        movingAverage.next(1); // 返回 1.0 = 1 / 1
        movingAverage.next(10); // 返回 5.5 = (1 + 10) / 2
        movingAverage.next(3); // 返回 4.66667 = (1 + 10 + 3) / 3
        movingAverage.next(5); // 返回 6.0 = (10 + 3 + 5) / 3

Constraints:
    1 <= size <= 1000
    -105 <= val <= 10^5
    最多调用 next 方法 10^4 次
"""


class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.sum = 0
        self.queue = collections.deque()

    def next(self, val: int) -> float:
        """
        Time: 56 ms, beat 97.80% (Python3)
        Memory: 17.9 MB, beat 91.60% (Python3)
        """
        if len(self.queue) == self.size:
            self.sum -= self.queue.popleft()
        self.sum += val
        self.queue.append(val)
        if len(self.queue) > 0:
            return self.sum / len(self.queue)
        else:
            return 0.


def main():
    # Example 1: Output: [null, 1.0, 5.5, 4.66667, 6.0]
    command_list = ["MovingAverage", "next", "next", "next", "next"]
    param_list = [[3], [1], [10], [3], [5]]

    # init instance
    # solution = Solution()
    size = param_list[0][0]
    obj = MovingAverage(size)
    ans = ["null"]

    # run & time
    start = time.process_time()
    assert len(command_list) == len(param_list)
    for idx in range(1, len(command_list)):
        command = command_list[idx]
        param = param_list[idx]
        if command == "next" and isinstance(param, list) and len(param) == 1:
            ans.append(obj.next(param[0]))
        else:
            ans.append("null")
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
