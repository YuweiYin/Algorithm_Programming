# Algorithm - Dynamic Programming - Longest Common Subsequence

By [YuweiYin](https://yuweiyin.github.io/)

## 简介

最长公共子序列 (Longest Common Subsequence, LCS)

### LCS 问题引入

在生物应用中，经常需要比较两个（或多个）不同生物体的 DNA。一个 DNA 序列由一串称为 **碱基** (base) 的分子组成。碱基有腺嘌呤、鸟嘌呤、胞嘧啶、胸腺嘧啶 4 种类型。用英文单词首字母表示这 4 种碱基，这样就可以将一个 DNA 序列表示为离散有限集合 {A, C, G, T} 上的一个字符串。

比较两个 DNA 序列的原因是希望确定它们的“相似度”，作为度量两种生物相近程度的指标。如果两个序列的最长公共子序列 LCS 的长度比较长，那么可以认为二者相近程度较高。

除了 LCS 外，还有编辑距离 (Edit Distance) 等衡量字符串相似度/相近程度的指标。

### LCS 问题描述

给定一个有序序列(一般是字符串或数组) `X = <x1, x2, ..., xm>`。那么另一个序列 `Z = <z1, z2, ..., zk>` 满足如下条件时称 Z 为 X 的**子序列** (subsequence)：存在一个严格递增的 X 的下标序列 `<i1, i2, ..., ik>`，对所有的 j = 1, 2, ..., k，满足 `x_{i_{j}} = z_j`。

例如，`Z = <B, C, D, B>` 是 `X = <A, B, C, B, D, A, B>` 的子序列，对应的下标序列为 `<2, 3, 5, 7>`。另外，同一个子序列 Z，可能对应 X 中不同的下标序列。

**注意**：“子序列”与“子串”概念不同，后者需要是原序列的**连续的一段**，而前者只需保证在原序列中**下标序严格递增**就行。

给定两个序列 X 和 Y，如果 Z 既是 X 的子序列，也是 Y 的子序列，那么称 Z 是 X 和 Y 的**公共子序列** (common subsequence)。所有公共子序列中，极长的公共子序列（可能不止一个）被称为“最长公共子序列”。

**LCS 问题**：给定两个序列 `X = <x1, x2, ..., xm>` 和 `Y = <y1, y2, ..., yn>`，求 X 和 Y 的长度最长的公共子序列。

## 动态规划解决方案

先考察暴力穷举搜索方法的时间复杂度量级，然后考虑是否满足动态规划的适用条件：最优子结构性质、重叠子问题性质。

### 1. 刻画 LCS 的结构特征

如果要用暴力搜索方法求解 LCS 问题，就要穷举 X 的左右自学咧，对每个子序列检查它是否也是 Y 的子序列，过程中记录找到过的最长子序列。X 的每个子序列对应 X 的下标集合 {1, 2, ..., m} 的一个子集，所以 X 有 2^m 个子序列，因此暴力搜索方法的运行时间为指数阶，所以对较长的序列是不实用的。

现分析 LCS 问题具有最优子结构性质。子问题的自然分类对应两个输入序列的“前缀”对。**前缀**定义：给定一个序列 `X = <x1, x2, ..., xm>`，对 i = 0, 1, ..., m，定义 X 的第 i 前缀为 `Xi = <x1, x2, ..., xi>`。而 X0 是空串 `<>`。

《CLRS》**定理 15.1 (LCS 的最优子结构)**：令 `X = <x1, x2, ..., xm>` 和 `Y = <y1, y2, ..., yn>` 为两个序列，`Z = <z1, z2, ..., zk>` 为 X 和 Y 的任意 LCS。

1. 如果 xm == yn，则 zk == xm == yn，且前缀 Z_{k-1} 是前缀 X_{m-1} 和前缀 Y_{n-1} 的一个 LCS。
    - 因为可以把 xm 和 yn 加到公共子序列 Z 的末尾
2. 如果 xm != yn
    1. 如果此时 zk != xm，那么意味着序列 Z 是前缀 X_{m-1} 和序列 Y 的一个 LCS。
    2. 如果此时 zk != yn，那么意味着序列 Z 是序列 X 和前缀 Y_{n-1} 的一个 LCS。

从上述定理可以看出，两个序列的 LCS 包含两个序列的前缀的 LCS。因此 LCS 问题具有最优子结构性质。后面考察相应的递归算法是否具有重叠子问题性质。

### 2. 设计递归求解方案

根据步骤 1 中阐述的定理 15.1，可以设计出 LCS 问题的递归解法。而且容易看出，LCS 问题具有重叠子问题性质。为了求解 X 和 Y 的一个 LCS，可能需要求 X 和 Y_{n-1} 的一个 LCS，以及 X_{m-1} 和 Y 的一个 LCS。但是这几个子问题都包含求解 X_{m-1} 和 Y_{n-1} 的 LCS 这样一个公共子子问题。

定义 c[i, j] 表示前缀 Xi 和前缀 Yj 的 LCS 长度(最优值)。如果 i=0 或 j=0，即此序列/前缀长度为 0，则其 LCS 为 0。最优解的递归式如下：

- 若 i == 0 或 j == 0，则 c[i, j] = 0
- 若 i, j > 0 且 xi == yi，则 c[i, j] = c[i-1, j-1] + 1
- 若 i, j > 0 且 xi != yi，则 c[i, j] = max(c[i-1, j], c[i, j-1])

### 3. 计算 LCS 的长度(最优值)

根据步骤 2 中的递归式，可以很容易地写出一个暴力搜索 DFS 解法，其耗时为指数时间。

但是，由于 LCS 问题只有 $ \Theta(mn) $ 个不同的子问题，因此可以利用动态规划思想 设计一个以 m、n 为变量的多项式时间复杂度算法。

函数 `lcs` 设计了 c[i, j] 表格（二维数组 c[0..m, 0..n]）保存前缀 Xi 和前缀 Yj 的 LCS 长度(最优值)。因此 c[m, n] 就是原序列 X 和 Y 的 LCS 的长度(原问题最优值)。

另外，还维护了另一个 b[i, j] 表格（二维数组 c[1..m, 1..n]）保存计算 c[i, j] 时所选择的子问题最优解，方便构造原问题的最优解。

类构造函数：

```python
class LongestCommonSubsequence:
    def __init__(self, seq_x, seq_y):
        assert isinstance(seq_x, str) and isinstance(seq_y, str)
        self.seq_x = seq_x       # 序列(字符串) X
        self.seq_y = seq_y       # 序列(字符串) Y
        self.optimal_lcs = ''    # 最优 LCS (字符串) LCS 可以有多个，这里仅求出一个 LCS
        self.neg_inf = -0x3f3f3f3f    # 目标是求公共子序列的最大值 LCS，所以备忘录各个位置初始化为 -inf
```

计算 LCS 的长度(最优值)，表格初始化、初始调用

```python
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
    c_table = [[self.neg_inf for j in range(n + 1)] for i in range(m + 1)]
    b_table = [[0 for j in range(n)] for i in range(m)]
    # c_table 首行与首列的值均置为 0
    for i in range(m + 1):
        c_table[i][0] = 0
    for i in range(n + 1):
        c_table[0][i] = 0

    # 自底向上循环实现 (动态规划) \Theta(mn)
    c_table, b_table = self._lcs(c_table, b_table, m, n)
    return c_table, b_table
```

```python
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
```

### 4. 构造 LCS(最优解)

```python
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
```

对于本 LCS 算法，完全可以去掉 b 表格。每个 c[i, j] 只依赖于 c 表格中的临近三项：c[i-1, j]、c[i, j-1]、c[i-1, j-1]。给定某个 c[i, j] 的值，可以在 O(1) 时间内判断出在计算 c[i, j] 时使用了前述三项中的哪一项。

另外，如果无需还原构造出最优解，c 表格仅为一维数组也足够了：

- 若 i == 0，则 c[i] = 0
- 若 i > 0 且 xi == yi，则 c[i] = c[i-1] + 1
- 若 i > 0 且 xi != yi，则 c[i] = max(c[i-1], c[i]) 此处覆盖掉原 c[i]

## 代码范例

### Python

Python 环境：Python 3.7

[GitHub Code Link](https://github.com/YuweiYin/Code_Play/blob/master/Algorithm-Essence/dynamic-programming/longest-common-subsequence.py)

## 参考资料

- Introduction to Algorithm (aka CLRS) Third Edition - Chapter 15
