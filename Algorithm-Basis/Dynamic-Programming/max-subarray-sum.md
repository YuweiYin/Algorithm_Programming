# Algorithm - Dynamic Programming - Max Subarray Sum

By [YuweiYin](https://yuweiyin.github.io/)

## 简介

连续子数组的最大和 Max Subarray Sum

问题描述：从一个包含数值（有的为正数、有的为负数）数组中找出一个下标连续的子数组，使得该连续子数组内的各数值之和最大。

## 代码范例

### Python

Python 环境：Python 3.7

[GitHub Code Link](https://github.com/YuweiYin/Code_Play/blob/master/Algorithm-Essence/dynamic-programming/max-subarray-sum.py)

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================
@Project : algorithm/dynamic_programming
@File    : max-subarray-sum.py
@Author  : YuweiYin
=================================================="""

import sys
import time

"""
连续子数组的最大和 Max Subarray Sum
"""


class MaxSubarraySum:
    def __init__(self, array):
        assert isinstance(array, list) and len(array) > 0
        self.array = array
        self.start = 0
        self.end = len(array) - 1
        self.is_all_neg = False  # True 表示数组全为负数，否则不全是负数

        # 预处理：确定实际的起始终止下标，无需考虑数组首尾的负数值
        # 时间复杂度 O(n)
        arr_len = len(self.array)
        lo = 0
        while lo < arr_len and self.array[lo] < 0:
            lo += 1
        self.start = lo
        # 如果扫描完整个数组发现全是负数，则无需确定 self.end
        if lo == arr_len:
            self.is_all_neg = True
        else:
            hi = arr_len - 1
            while self.array[hi] < 0 <= hi:
                hi -= 1
            self.end = hi

    # 寻找连续子数组的最大和
    # 返回：最大和, 起始下标, 终止下标（这里是闭区间，且包含子数组首尾的 0）
    # 如果起始或终止下标为 -1，则为异常、无最大和
    def find_max_subarray_sum(self):
        # 如果整个数组全是负数，则只需挑出其中最大的一个数
        if self.is_all_neg:
            max_num = -0x3f3f3f3f
            max_index = -1
            for index, num in enumerate(self.array):
                if num > max_num:
                    max_num = num
                    max_index = index
            return max_num, max_index, max_index
        else:
            # return self._find_max_subarray_sum_1()  # 暴力计算 O(n^2)
            # return self._find_max_subarray_sum_2()  # 分治法 O(n log n)
            return self._find_max_subarray_sum_3()  # 线性动态规划 O(n)

    # 暴力计算
    # 已确保数组中存在非负数
    # 时间复杂度 O(n^2)
    def _find_max_subarray_sum_1(self):
        max_sum = -0x3f3f3f3f
        max_start = -1
        max_end = -1
        for i in range(self.start, self.end + 1):  # i 为当前区间起始位置
            cur_sum = 0
            for j in range(i, self.end + 1):  # j 为当前区间终止位置
                cur_sum += self.array[j]  # 累加 cur_sum
                if cur_sum >= max_sum:  # 如果超越了 max_sum，则更新最大和、起始下标、终止下标
                    max_sum = cur_sum
                    max_start = i
                    max_end = j
        return max_sum, max_start, max_end

    # 分治法
    # T(k) = 2T(k/2) + O(k)
    # 时间复杂度 O(n log n)
    def _find_max_subarray_sum_2(self):
        return self._find_mss_2_recursion(self.start, self.end)

    # 分治法的实际工作过程，可能递归
    def _find_mss_2_recursion(self, lo, hi):
        if lo == hi:
            return self.array[lo], lo, lo
        else:
            mid = int((lo + hi) >> 1)
            # 完全位于左侧的子数组最大和
            left_sum, left_lo, left_hi = self._find_mss_2_recursion(lo, mid)
            # 完全位于右侧的子数组最大和
            right_sum, right_lo, right_hi = self._find_mss_2_recursion(mid + 1, hi)
            # 跨越"中轴"的子数组最大和
            cross_sum, cross_lo, cross_hi = self._find_mss_2_cross(lo, mid, hi)

            # 取前述三者的最大和作为返回值
            if left_sum >= right_sum and left_sum >= cross_sum:
                return left_sum, left_lo, left_hi
            elif right_sum >= left_sum and right_sum >= cross_sum:
                return right_sum, right_lo, right_hi
            else:
                return cross_sum, cross_lo, cross_hi

    # 寻找跨越"中轴"的区间最值
    def _find_mss_2_cross(self, lo, mid, hi):
        left_sum = -0x3f3f3f3f  # 从 mid 往左的子数组和（包含 mid）
        left_start = mid  # 从 mid 往左的子数组的起始位置
        cur_sum = 0
        for i in reversed(range(lo, mid + 1)):
            cur_sum += self.array[i]
            if cur_sum >= left_sum:  # 如果超越了 left_sum，则更新最大和、起始下标
                left_sum = cur_sum
                left_start = i

        right_sum = -0x3f3f3f3f  # 从 mid 往右的子数组和（不包含 mid）
        right_end = mid + 1  # 从 mid 往右的子数组的终止位置
        cur_sum = 0
        for i in range(mid + 1, hi + 1):
            cur_sum += self.array[i]
            if cur_sum >= right_sum:  # 如果超越了 right_sum，则更新最大和、终止下标
                right_sum = cur_sum
                right_end = i

        return left_sum + right_sum, left_start, right_end

    # 线性动态规划
    # 时间复杂度 O(n)
    def _find_max_subarray_sum_3(self):
        max_sum = -0x3f3f3f3f
        max_start = -1
        max_end = -1
        cur_sum = 0
        cur_start = 0
        for i in range(self.start, self.end + 1):  # i 为当前区间起始位置
            cur_sum += self.array[i]  # 累加 cur_sum
            # 如果超越了 max_sum，则更新最大和、起始下标、终止下标
            if cur_sum >= max_sum:
                max_sum = cur_sum
                max_start = cur_start
                max_end = i
            # 如果 cur_sum 小于零，则此"前缀和"是不需要的，重置 cur_sum 为零
            if cur_sum < 0:
                cur_sum = 0
                cur_start = i + 1  # 重置 cur_start 为后一个下标

        return max_sum, max_start, max_end


def main():
    array = [-1, 13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7, -2]

    mss = MaxSubarraySum(array)

    start = time.process_time()
    ans_sum, ans_start, ans_end = mss.find_max_subarray_sum()
    end = time.process_time()

    print('ans_sum:', ans_sum)      # 43
    print('ans_start:', ans_start)  # 8
    print('ans_end:', ans_end)      # 11

    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())

```

## 参考资料

- Introduction to Algorithm (aka CLRS) Third Edition - Chapter 4
