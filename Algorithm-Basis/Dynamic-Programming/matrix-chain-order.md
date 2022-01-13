# Algorithm - Dynamic Programming - Matrix Chain Order

By [YuweiYin](https://yuweiyin.github.io/)

## 简介

矩阵链乘法 Matrix Chain Order

**问题描述**：给定一个含 n 个矩阵的序列（矩阵链）`<A1, A2, ..., An>`，其中相邻的矩阵两两**相容** (compatible)、矩阵乘法是合法的。需要确定一种计算的次序，使得计算矩阵乘积 A1·A2·...·An 总耗时最少。（所需的总标量乘法次数最少）

- 注意：
    - 只要相邻矩阵两两相容，计算的结果就不会因次序不同而改变。
    - 但是次序不同会造成实际的乘法、加法次数的不同。
    - 这里均假定使用如下朴素的矩阵乘法操作

抽象出的矩阵结构体：

```python
# 矩阵结构体
class Matrix:
    # 构造时确保矩阵非空且行列合法
    def __init__(self, arr_2d):
        assert isinstance(arr_2d, list) and len(arr_2d) > 0 and len(arr_2d[0]) > 0
        self.matrix = arr_2d
        self.row_num = len(arr_2d)
        self.col_num = len(arr_2d[0])
        # 确保每一行的元素个数都等于列数
        for row in range(len(arr_2d)):
            assert isinstance(row, list) and len(row) == self.col_num
```

朴素的矩阵乘法：

```python
# 矩阵乘积运算 计算 A * B 的结果
# 其中矩阵 A 的规模为 P*Q、矩阵 B 的规模为 Q*R
# 时间复杂度 \Theta(P*Q*R)
# 空间复杂度 \Theta(P*R)
@staticmethod
def matrix_multiply(matrix_a, matrix_b):
    assert isinstance(matrix_a, Matrix) and isinstance(matrix_b, Matrix)
    # 先确保输入的两矩阵是相容的
    if matrix_a.col_num != matrix_b.row_num:
        print('matrix_multiply: incompatible dimensions')
        return None
    res_matrix = [[0 for j in range(matrix_b.col_num)] for i in range(matrix_a.row_num)]
    for i in range(matrix_a.row_num):
        for j in range(matrix_b.col_num):
            for k in range(matrix_a.col_num):
                res_matrix[i][j] += matrix_a.matrix[i][k] * matrix_b.matrix[k][j]
    return res_matrix
```

如果 A 是 pxq 的矩阵，B 是 qxr 的矩阵，那么乘积 C 是 pxr 的矩阵。计算 C 所需的时间主要由标量乘法的总次数来决定，即 `p*q*r`。后文均以标量乘法的次数来表示计算代价。

以矩阵链 `<A1, A2, A3>` 相乘为例，假设三者的规模分别为 10x100、100x5、5x50。

- 如果按照 ((A1 A2) A3) 的顺序计算，那么为计算 (A1 A2) 乘法需要 `10*100*5` 即 5000 次标量乘法，此时规模为 10x5，再与 A3 相乘又需要做 `10*5*50` 即 2500 次标量乘法，因此总共需要执行 7500 次乘法。
- 如果按照 (A1 (A2 A3)) 的顺序计算，那么为计算 (A2 A3) 乘法需要 `100*5*50` 即 25000 次标量乘法，此时规模为 100x50，再与 A1 相乘又需要做 `10*100*50` 即 50000 次标量乘法，因此总共需要执行 75000 次乘法。

可以看出，以第一种方式计算，其标量乘法次数比第二种方式少了 10 倍，因此往往也能缩短运行时间至 1/10，这是很可观的。

而且矩阵乘法也是大数据处理、机器学习等技术中中非常常见运算，所以掌握如何优化矩阵链乘是很重要的技术方法。

注意：求解矩阵链乘问题并不是要真正进行矩阵相乘运算，而是确定代价最低的计算顺序。确定最优计算顺序所花费的时间 通常要比随后真正进行矩阵相乘所花的时间要少得多。

### 计算括号化方案的数量

所谓的**括号化方案**就是确定矩阵相乘顺序。((A1 A2) A3) 就是先进行 A1·A2，再乘 A3。而 (A1 (A2 A3)) 就是先进行 A2·A3，再被 A1 乘。

很明显，穷举所有可能的括号化方案是低效的算法，下面予以说明。

对于一个含有 n 个矩阵的链，令 P(n) 表示可供选择的括号化方案的数量。当 n = 1 时，由于只有一个矩阵，因此只有一种完全括号化方案。

当 n >= 2 时，拆解原任务：完全括号化的矩阵乘积可以描述为 两个完全括号化的部分积相乘的形式。而这两个部分积的划分点在第 k 个矩阵和第 k+1 个矩阵之间，k = 1, 2, ..., n-1。因此有如下递归公式：

- 如果 n == 1 则 P(n) = 1
- 如果 n >= 2 则 P(n) = $ \sum_{k=1}^{n-1} P(k) P(n-k) $

可以证明，此递归公式的增长速度为 $ \Omega(2^n) $。因此，括号化方案的数量与 n 呈指数关系，通过暴力搜索穷尽所有有可能的括号化方案来寻找最优方案 是一个糟糕的策略。

另外，一个与上述公式相似的著名递归公式 所产生的序列为 **卡塔兰数** (Catalan Numbers)，该序列的增长速度为 $ \Omega(4^n / n^{3/2}) $。

## 动态规划解决方案

使用动态规划算法的动机：

可以看出，原问题可以通过在矩阵链某个位置 k 划分左右两个部分 为子问题，从而分别递归计算子问题。但是一开始并不知道怎样的划分位置是好的，所以需要对每个位置进行划分尝试。

每次划分的两部分视作子问题，那么很显然多个子问题之间具有重叠部分 (公共子问题)。因此无法用“干净切分”的分治法，而前面也分析过了暴力搜索是不实际的，因此考虑动态规划算法。

### 1. 刻画最优括号化方案的结构特征

假设子问题 Ai...Aj 的最优括号化方案的分割点在矩阵 Ak 和 A_{k+1} 之间。那么，继续对“前缀”子链 Ai...Ak 进行括号化时，应该直接采用独立求解它时所的的最优方案，即具有 **最优子结构性质**：子问题取得最优解/值 是 原问题取得最优解/值 的必要条件。

另外，需要保证在确定当前分割点 k 前，已经考虑了当前子问题中所有可能的划分点，从而不会遗漏最优解/值。

### 2. 设计递归求解方案

用子问题的最优解来递归地定义原问题的最优解的代价。

对矩阵乘法问题，可以将 对所有 1 <= i <= j <= n 确定 Ai..Aj 的最优括号化方案 作为子问题。令备忘录表格 m[i, j] 表示计算矩阵 A_{i..j} 所需标量乘法次数的最小值。因此，原问题的最优解（计算 A_{1..n}）所需的最低代价就是 m[1, n] 的值。

将 m[i, j] 递归定义如下。对于 i == j 的基本情况，矩阵链只包含唯一的矩阵 A_{i..i} = A_i，因此不需要做任何标量乘法运算。所以，对所有的 i = 1, 2, ..., n 而言，m[i, i] = 0。

若 i < j，则进行划分。假设 Ai...Aj 的最优括号化方案的分割点在矩阵 Ak 和 A_{k+1} 之间，其中 i <= k < j。因此 m[i, j] 就等于计算子问题 A_{i..k} 和 A_{k+1..j} 的代价 再加上两者相乘的代价 的最小值。

记矩阵 Ai 的规模为 p_{i-1} x pi (1 <= i <= n)，所以 A_{i..k} 与 A_{k+1..j} 相乘的代价为 `p_{i-1} * p_k * pj` 次标量乘法，因此有递归计算式：`m[i, j] = m[i, k] + m[k+1, j] + p_{i-1} * p_k * pj`

k 有 j-i 种可能取值，即 k = i, i+1, ..., j-1。由于最优分割点比在其中，只需检查所有可能情况（同时利用备忘录），找出最优者即可。因此，链乘 Ai...Aj 最小代价括号化方案的递归求解公式如下：

- 如果 i = j 则 `m[i, j] = 0`
- 如果 i < j 则 `m[i, j] = min{m[i, k] + m[k+1, j] + p_{i-1} * p_k * pj}`
    - $ \forall k \in [i, j) $

m[i, j] 的值给出了子问题最优解的代价，但它并未提供足够的信息来构造最优解。为此，利用另一个备忘录 s[i, j] 保存链乘 Ai...Aj 最优括号化方案的各个分割点位置 k，即使得 `m[i, j] = m[i, k] + m[k+1, j] + p_{i-1} * p_k * pj` 成立的 k 值。

### 3. 计算最优代价(最优值)

如果不使用备忘录，那么计算的递归算法是指数时间的，并不比检查所有括号化方案的暴力搜索方法更好。

注意到，需要求解的不同子问题的数目是相对较少的：每对满足 1 <= i <= j <= n 的 i 和 j 对应一个唯一的子问题，共有 $ C_n^2 + n = \Theta(n^2) $ 个。递归算法会在递归调用树的不同分支中多次遇到同一个子问题。这种**重叠子问题性质**也正是应用动态规划方法的标志之一。（还有**最优子结构性质**）

为了避免重复计算公共子问题，常采用自底向上的表格法 代替基于前述公式的递归算法 来计算最优代价。（当然，也可以采用带备忘录的自顶向下递归方法）。

![matrix-chain-order-1](/img/info-technology/algorithm/dynamic-programming/matrix-chain-order-1.png)

类构造函数：

```python
class MatrixChainOrder:
    def __init__(self, p_arr):
        assert isinstance(p_arr, list) and len(p_arr) > 1
        self.p_arr = p_arr       # p 数组给出各矩阵的规模
        self.optimal_paren = ''  # 最优括号化方案 (字符串)
        self.inf = 0x3f3f3f3f    # 目标是求代价最小值，所以备忘录各个位置初始化为 inf
```

如下为初始调用函数，这里 `self.p_arr = [30, 35, 15, 5, 10, 20, 25]`

```python
# 矩阵链乘最佳计算顺序
# 返回：最佳收益(最优值)、最佳切割方案列表(最优解)
# 如果返回最佳收益为 -1，则为异常
def matrix_chain_order(self):
    assert isinstance(self.p_arr, list) and len(self.p_arr) > 1
    # 矩阵数量为 p 数组长度减一
    matrix_num = len(self.p_arr) - 1
    # 备忘录表格 m[i, j] 表示计算矩阵 A_{i..j} 所需标量乘法次数的最小值
    # 因此，原问题的最优解（计算 A_{1..n}）所需的最低代价就是 m[1, n] 的值
    # 备忘录 s[i, j] 保存链乘 Ai...Aj 最优括号化方案的各个分割点位置 k
    # 即：使得 m[i, j] = m[i, k] + m[k+1, j] + p_{i-1} * p_k * pj 成立的 k 值
    m_table = [[self.inf for j in range(matrix_num)] for i in range(matrix_num)]
    s_table = [[self.inf for j in range(matrix_num)] for i in range(matrix_num)]
    # m_table 主对角线的值均置为 0
    for i in range(matrix_num):
        m_table[i][i] = 0
    # s_table 主对角线 (i, i) 的值均置为 i
    for i in range(matrix_num):
        s_table[i][i] = i

    # 自顶向下递归实现 (DFS 暴力搜索) O(2^n)
    # m_table, s_table = self._matrix_chain_order_1(m_table, s_table, matrix_num)
    # 自顶向下递归实现 (带备忘录的动态规划) O(n^2)
    # self._matrix_chain_order_2(m_table, s_table, matrix_num)
    # 自底向上循环实现 (动态规划) O(n^2)
    m_table, s_table = self._matrix_chain_order_3(m_table, s_table, matrix_num)
    return m_table, s_table
```

如下为具体的实现：自底向上循环实现 (动态规划)

```python
# 自底向上循环实现 (动态规划)
# 时间复杂度 \Theta(n^3)
# 空间复杂度 \Theta(n^2)
def _matrix_chain_order_3(self, m_table, s_table, matrix_num):
    assert isinstance(self.p_arr, list) and len(self.p_arr) > 1

    # 对于每种 chain_len 链长(子问题)求最优解/值，自底向上分别计算
    for chain_len in range(2, matrix_num + 1):
        # i 为当前链的起始位置
        for i in range(matrix_num - chain_len + 1):
            # j 为当前链的终止位置
            j = i + chain_len - 1
            # 对于每个切分点 k 计算代价，i <= k < j
            for k in range(i, j):
                # 计算代价时仅依赖于已经求出的 m[i, k] 和 m[k+1, j]
                # 注意这里 i 从下标 0 开始，于是原公式里的 p_{i-1} * p_k * pj 需改为 p_i * p_{k+1} * p_{j+1}
                cost = m_table[i][k] + m_table[k + 1][j] + self.p_arr[i] * self.p_arr[k + 1] * self.p_arr[j + 1]
                if cost < m_table[i][j]:
                    m_table[i][j] = cost
                    s_table[i][j] = k
    # 返回备忘录 m 和 s
    return m_table, s_table
```

- 时间复杂度 $ \Theta(n^3) $
- 空间复杂度 $ \Theta(n^2) $

### 4. 构造最优解

`s_table` 的每个表项 s[i, j] 记录了在当前情况下的最佳划分 k 值，指出 Ai..Aj 的最优括号化方案的分割点应该在 Ak 和 A_{k+1} 之间。由于知道最后一次矩阵乘法运算是在 A_{1..s[1, n]} 乘 A_{1+s[1, n]..n}，可以据此递归回溯出更早的矩阵乘法的具体计算过程(分割点)。

```python
# 根据 s_table 获取最优解的括号化方案 (字符串)
def get_optimal_paren(self, s_table):
    self.optimal_paren = ''
    self._get_optimal_paren(s_table, 0, len(self.p_arr) - 2)
    return self.optimal_paren

def _get_optimal_paren(self, s_table, lo, hi):
    if lo == hi:
        self.optimal_paren += 'A' + str(lo + 1)
    else:
        self.optimal_paren += '('
        self._get_optimal_paren(s_table, lo, s_table[lo][hi])
        self._get_optimal_paren(s_table, s_table[lo][hi] + 1, hi)
        self.optimal_paren += ')'
```

### 备忘录机制

可以在自然但低效的递归算法基础上，增加备忘录机制，维护一个**公共表格**记录子问题的解，供每级递归过程(各个子问题)调用。一旦某子问题已经有最优解/值，则直接查表返回，不再重复计算。

```python
# 自顶向下递归实现 (带备忘录的动态规划)
# 时间复杂度 \Theta(n^3)
# 空间复杂度 \Theta(n^2)
def _matrix_chain_order_2(self, m_table, s_table, matrix_num):
    self._lookup_matrix_chain_order(m_table, s_table, 0, matrix_num - 1)
    return m_table, s_table

def _lookup_matrix_chain_order(self, m_table, s_table, i, j):
    # 先查表，如果当前子问题已有解，则直接返回之
    if m_table[i][j] < self.inf:
        return m_table[i][j]
    # 基本情况：i j 相等表示仅有一个矩阵，无需标量运算
    if i == j:
        return 0
    # 对于每个切分点 k 计算代价，i <= k < j
    for k in range(i, j):
        # 计算代价时仅依赖于已经求出的 m[i, k] 和 m[k+1, j]
        # 注意这里 i 从下标 0 开始，于是原公式里的 p_{i-1} * p_k * pj 需改为 p_i * p_{k+1} * p_{j+1}
        left_cost = self._lookup_matrix_chain_order(m_table, s_table, i, k)
        right_cost = self._lookup_matrix_chain_order(m_table, s_table, k + 1, j)
        merge_cost = self.p_arr[i] * self.p_arr[k + 1] * self.p_arr[j + 1]
        cost = left_cost + right_cost + merge_cost
        if cost < m_table[i][j]:
            m_table[i][j] = cost
            s_table[i][j] = k
    return m_table[i][j]
```

最后，可以输入真实的矩阵序列 A1..An，先以 `matrix_chain_order` 算法分析计算顺序，再按计算顺序调用 `matrix_multiply` 函数进行矩阵乘法运算。

## 代码范例

### Python

Python 环境：Python 3.7

[GitHub Code Link](https://github.com/YuweiYin/Code_Play/blob/master/Algorithm-Essence/dynamic-programming/matrix-chain-order.py)

## 参考资料

- Introduction to Algorithm (aka CLRS) Third Edition - Chapter 15
