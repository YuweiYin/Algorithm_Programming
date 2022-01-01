#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================
@Project : algorithm/dynamic_programming
@File    : longest-common-subsequence.py
@Author  : YuweiYin
@Date    : 2020-05-27
=================================================="""

import sys
import time

"""
最长公共子序列 (Longest Common Subsequence, LCS)

参考资料：
Introduction to Algorithm (aka CLRS) Third Edition - Chapter 15
"""


class LongestCommonSubsequence:
    def __init__(self, seq_x, seq_y):
        assert isinstance(seq_x, str) and isinstance(seq_y, str)
        self.seq_x = seq_x       # 序列(字符串) X
        self.seq_y = seq_y       # 序列(字符串) Y
        self.optimal_lcs = ''    # 最优 LCS (字符串) LCS 可以有多个，这里仅求出一个 LCS
        self.neg_inf = -0x3f3f3f3f    # 目标是求公共子序列的最大值 LCS，所以备忘录各个位置初始化为 -inf

    # 最长公共子序列
    # case 1: 若 i == 0 或 j == 0，则 c[i, j] = 0
    # case 2: 若 i, j > 0 且 xi == yi，则 c[i, j] = c[i-1, j-1] + 1
    # case 3: 若 i, j > 0 且 xi != yi，则 c[i, j] = max(c[i-1, j], c[i, j-1])
    # 返回：LCS 最优值表、LCS 最优解表
    # 如果原序列 X 或 Y 长度为 0，则返回 [], []
    def lcs(self):
        assert isinstance(self.seq_x, str) and isinstance(self.seq_y, str)
        if len(self.seq_x) == 0 or len(self.seq_y) == 0:
            return [], []
        # 记序列 X 长度为 m、序列 X 长度为 n
        m = len(self.seq_x)
        n = len(self.seq_y)
        # c[i, j] 表格（二维数组 c[0..m, 0..n]）保存前缀 Xi 和前缀 Yj 的 LCS 长度(最优值)
        # 因此 c[m, n] 就是原序列 X 和 Y 的 LCS 的长度(原问题最优值)
        # b[i, j] 表格（二维数组 c[1..m, 1..n]）保存计算 c[i, j] 时所选择的子问题最优解，方便构造原问题的最优解
        # b[i, j] 等于 0 仅作占位、等于 1 表示当前最优解是 c[i, j] = c[i-1, j-1] + 1
        # 等于 2 表示当前最优解是 c[i, j] = c[i-1, j]、等于 3 则表示 c[i, j] =  c[i, j-1]
        c_table = [[self.neg_inf for _ in range(n + 1)] for _ in range(m + 1)]
        b_table = [[0 for _ in range(n)] for _ in range(m)]
        # c_table 首行与首列的值均置为 0
        for i in range(m + 1):
            c_table[i][0] = 0
        for i in range(n + 1):
            c_table[0][i] = 0

        # 自底向上循环实现 (动态规划) \Theta(mn)
        c_table, b_table = self._lcs(c_table, b_table, m, n)
        return c_table, b_table

    # 自底向上循环实现 (动态规划)
    # 时间复杂度 \Theta(mn)
    # 空间复杂度 \Theta(mn)
    def _lcs(self, c_table, b_table, m, n):
        assert isinstance(self.seq_x, str) and isinstance(self.seq_y, str)

        # 对于序列 X 和 Y 各种长度的前缀(子问题)求最优解/值，自底向上分别计算
        # case 1: 若 i == 0 或 j == 0，则 c[i, j] = 0
        # case 2: 若 i, j > 0 且 xi == yi，则 c[i, j] = c[i-1, j-1] + 1
        # case 3: 若 i, j > 0 且 xi != yi，则 c[i, j] = max(c[i-1, j], c[i, j-1])
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # b[i, j] 等于 0 仅作占位
                # 等于 1 表示遇到了公共字符，当前最优解是 c[i, j] = c[i-1, j-1] + 1
                if self.seq_x[i - 1] == self.seq_y[j - 1]:  # case 2
                    c_table[i][j] = c_table[i - 1][j - 1] + 1
                    b_table[i - 1][j - 1] = 1
                # 等于 2 表示当前最优解是 c[i, j] = c[i-1, j] 该查看前缀 X_{i-1}
                elif c_table[i - 1][j] >= c_table[i][j - 1]:  # case 3.1
                    c_table[i][j] = c_table[i - 1][j]
                    b_table[i - 1][j - 1] = 2
                # 等于 3 表示当前最优解是 c[i, j] =  c[i, j-1] 该查看前缀 Y_{j-1}
                else:  # case 3.2
                    c_table[i][j] = c_table[i][j - 1]
                    b_table[i - 1][j - 1] = 3
        # 返回备忘录 c 和 b
        return c_table, b_table

    # 根据 b_table 获取最优解 LCS (字符串)
    # 时间复杂度 \Theta(m+n)
    def get_optimal_lcs(self, b_table):
        self.optimal_lcs = ''
        self._get_optimal_lcs(b_table, len(self.seq_x) - 1, len(self.seq_y) - 1)
        return self.optimal_lcs

    def _get_optimal_lcs(self, b_table, m, n):
        # 边界情况
        if m == 0 or n == 0:
            # 遇到边界，如果边界处的 b_table 值是 1，则表示该字符也是公共字符，属于 lcs
            if b_table[m][n] == 1:
                self.optimal_lcs += self.seq_x[m]
            return
        # b[i, j] 等于 0 仅作占位
        # 等于 1 表示遇到了公共字符，当前最优解是 c[i, j] = c[i-1, j-1] + 1
        if b_table[m][n] == 1:
            self._get_optimal_lcs(b_table, m - 1, n - 1)
            self.optimal_lcs += self.seq_x[m]
        # 等于 2 表示当前最优解是 c[i, j] = c[i-1, j] 该查看前缀 X_{i-1}
        elif b_table[m][n] == 2:
            self._get_optimal_lcs(b_table, m - 1, n)
        # 等于 3 表示当前最优解是 c[i, j] =  c[i, j-1] 该查看前缀 Y_{j-1}
        else:
            self._get_optimal_lcs(b_table, m, n - 1)


def main():
    # 这里仅为了确定计算的最优顺序，而不是为了计算矩阵乘积值
    # 所以链乘的矩阵序列是 相邻两两相容的，因此这里用 p 数组给出各矩阵的规模
    # 假设有 A_0..A_{n-1} 这 n 个矩阵，那么 A_i 矩阵的规模为 p[i] * p[i-1]
    # 因此若有 n 个矩阵，则 p 数组的长度就为 n+1
    seq_x = 'ABCBDAB'
    seq_y = 'BDCABA'

    lcs = LongestCommonSubsequence(seq_x, seq_y)

    start = time.process_time()
    c_table, b_table = lcs.lcs()
    end = time.process_time()

    print('\noptimal_lcs:')
    print(lcs.get_optimal_lcs(b_table))  # BCBA

    print('\nc_table:')
    for row in c_table:
        print(row)
    print('\nb_table:')
    for row in b_table:
        print(row)

    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
