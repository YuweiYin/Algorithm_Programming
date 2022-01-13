# Algorithm - Divide and Conquer - Strassen

By [YuweiYin](https://yuweiyin.github.io/)

## 简介

矩阵乘法的 Strassen 算法

问题描述：若 A = (a\_{ij}) 和 B = (b_{ij}) 是 n 行 n 列的方阵（其实只要二者相容就行），对 i, j = 1, 2, ..., n 定义矩阵乘积 C = A · B 中的元素 `c_{ij} = \sum_{k=1}^{n} a_{ik} b_{kj}`。

## 解决方案及分析

### 朴素的矩阵乘积运算

为了执行此运算，需要计算 n^2 个矩阵元素，每个元素是 n 个值的和，因此总的时间复杂度为 O(n^3)。朴素解法如下：

```python
# 朴素的矩阵乘积运算
# 时间复杂度 \Theta(n^3)
def _naive_mm(self):
    n = len(self.matrix_a)
    res_matrix = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res_matrix[i][j] += self.matrix_a[i][k] * self.matrix_b[k][j]
    return res_matrix
```

### 普通的分治法

为了简单起见，当使用 Strassen 分治法计算矩阵乘积 C = A · B 时，假定三个矩阵均为 nxn 矩阵，且 n 为 2 的正整数次幂。此假设使得在每个分解步骤中，nxn 矩阵都被均等地划分为 4 个 n/2 x n/2 的子矩阵。

假定将 A、B 和 C 均等地分解为如下 4 个 n/2 x n/2 的子矩阵：

- `A = [[A11, A12], [A21, A22]]`
- `B = [[B11, B12], [B21, B22]]`
- `C = [[C11, C12], [C21, C22]]`

因此可以将式子 C = A · B 改写为：

`[[C11, C12], [C21, C22]] = [[A11, A12], [A21, A22]] · [[B11, B12], [B21, B22]]`

这等价于如下四个式子：

- `C11 = A11 · B11 + A12 · B21`
- `C12 = A11 · B12 + A12 · B22`
- `C21 = A21 · B11 + A22 · B21`
- `C22 = A21 · B12 + A22 · B22`

这四个式子各自对应了 n/2 x n/2 子矩阵的两个乘法、一个加法。如果用这四个式子设计一个直接的递归分治算法，伪代码如下：

```python
# 普通的分治法
# T(n) = 8T(n/2) + \Theta(n^2)
# 时间复杂度 \Theta(n^3)
def _divide_mm(self, matrix_a, matrix_b):
    n = len(matrix_a)
    res_matrix = [[0 for i in range(n)] for i in range(n)]
    if n == 1:
        res_matrix[0][0] = matrix_a[0][0] * matrix_b[0][0]
    else:
        # 矩阵拆分：从中间划分成四份
        a_11, a_12, a_21, a_22, b_11, b_12, b_21, b_22 = self._matrix_split(matrix_a, matrix_b)

        # 递归进行乘法后相加
        res_11 = self._matrix_addition(self._divide_mm(a_11, b_11), self._divide_mm(a_12, b_21))
        res_12 = self._matrix_addition(self._divide_mm(a_11, b_12), self._divide_mm(a_12, b_22))
        res_21 = self._matrix_addition(self._divide_mm(a_21, b_11), self._divide_mm(a_22, b_21))
        res_22 = self._matrix_addition(self._divide_mm(a_21, b_12), self._divide_mm(a_22, b_22))

        # 结果合并到 res_11 中
        res_11.extend(res_21)
        res_12.extend(res_22)
        assert len(res_11) == len(res_12)
        for i in range(len(res_11)):
            res_11[i].extend(res_12[i])
        res_matrix = res_11
    # 返回最终结果
    return res_matrix

# 辅助函数：矩阵拆分
# 从中间划分成四份
# 时间复杂度 O(n)
@staticmethod
def _matrix_split(m_a, m_b):
    assert len(m_a) == len(m_b)
    mid = len(m_a) >> 1

    a_1 = m_a[:mid]  # 前半 mid 行
    a_2 = m_a[mid:]  # 后半 mid 行
    a_11 = [row[:mid] for row in a_1]
    a_12 = [row[mid:] for row in a_1]
    a_21 = [row[:mid] for row in a_2]
    a_22 = [row[mid:] for row in a_2]

    b_1 = m_b[:mid]  # 前半 mid 行
    b_2 = m_b[mid:]  # 后半 mid 行
    b_11 = [row[:mid] for row in b_1]
    b_12 = [row[mid:] for row in b_1]
    b_21 = [row[:mid] for row in b_2]
    b_22 = [row[mid:] for row in b_2]

    return a_11, a_12, a_21, a_22, b_11, b_12, b_21, b_22

# 辅助函数：矩阵加法
# 对应位置相加，需约束两矩阵形状相同
# 时间复杂度 O(n^2)
@staticmethod
def _matrix_addition(m_a, m_b):
    assert len(m_a) == len(m_b)
    # 也可以直接把矩阵 m_b 的各值加到 m_a 中，不额外建立矩阵
    res_matrix = [[0 for j in range(len(m_a[i]))] for i in range(len(m_a))]
    for i in range(len(m_a)):
        assert len(m_a[i]) == len(m_b[i])
        for j in range(len(m_a[i])):
            res_matrix[i][j] = m_a[i][j] + m_b[i][j]
    return res_matrix
```

### Strassen 算法

1. 矩阵拆分：从中间划分成四份 `a_11, a_12, a_21, a_22, b_11, b_12, b_21, b_22`
2. 计算前述 8 个子矩阵的和或差，得到 10 个新的矩阵 s1..s10
3. 利用前述所有子矩阵，进行 7 次递归的矩阵乘法，得到 p1..p7
4. 对 p1..p7 进行加减运算得到最终结果的四个部分 `res_11, res_12, res_21, res_22`
5. 结果合并整理成 `res_matrix`

```python
# 辅助函数：矩阵减法
# 对应位置相减，需约束两矩阵形状相同
# 时间复杂度 O(n^2)
@staticmethod
def _matrix_subtraction(m_a, m_b):
    assert len(m_a) == len(m_b)
    # 也可以直接用矩阵 m_a 的各值减去 m_b 相应各值，不额外建立矩阵
    res_matrix = [[0 for j in range(len(m_a[i]))] for i in range(len(m_a))]
    for i in range(len(m_a)):
        assert len(m_a[i]) == len(m_b[i])
        for j in range(len(m_a[i])):
            res_matrix[i][j] = m_a[i][j] - m_b[i][j]
    return res_matrix

# 矩阵乘法的 Strassen 算法
# 这里假定待乘方阵的大小 n 是 2 的正整数次幂
# 核心思想是：将普通分治法的 8 次乘法降为 7 次
# T(n) = 7T(n/2) + \Theta(n^2)
# 时间复杂度 \Theta(n^{log 7}) = O(n^2.81) = \Omega(n^2.80)
def _strassen_mm(self, matrix_a, matrix_b):
    n = len(matrix_a)
    res_matrix = [[0 for i in range(n)] for i in range(n)]
    if n == 1:
        res_matrix[0][0] = matrix_a[0][0] * matrix_b[0][0]
    else:
        # 矩阵拆分：从中间划分成四份
        a_11, a_12, a_21, a_22, b_11, b_12, b_21, b_22 = self._matrix_split(matrix_a, matrix_b)

        # 计算前述 8 个子矩阵的和或差，得到 10 个新的矩阵 s1..s10
        s_1 = self._matrix_subtraction(b_12, b_22)
        s_2 = self._matrix_addition(a_11, a_12)
        s_3 = self._matrix_addition(a_21, a_22)
        s_4 = self._matrix_subtraction(b_21, b_11)
        s_5 = self._matrix_addition(a_11, a_22)
        s_6 = self._matrix_addition(b_11, b_22)
        s_7 = self._matrix_subtraction(a_12, a_22)
        s_8 = self._matrix_addition(b_21, b_22)
        s_9 = self._matrix_subtraction(a_11, a_21)
        s_10 = self._matrix_addition(b_11, b_12)

        # 利用前述所有子矩阵，进行 7 次递归的矩阵乘法，得到 p1..p7
        p_1 = self._strassen_mm(a_11, s_1)
        p_2 = self._strassen_mm(s_2, b_22)
        p_3 = self._strassen_mm(s_3, b_11)
        p_4 = self._strassen_mm(a_22, s_4)
        p_5 = self._strassen_mm(s_5, s_6)
        p_6 = self._strassen_mm(s_7, s_8)
        p_7 = self._strassen_mm(s_9, s_10)

        # 对 p1..p7 进行加减运算得到最终结果的四个部分
        # res_11 = p_5 + p_4 - p_2 + p_6
        # res_22 = p_5 + p_1 - p_3 - p_7
        res_11 = self._matrix_addition(self._matrix_subtraction(self._matrix_addition(p_5, p_4), p_2), p_6)
        res_12 = self._matrix_addition(p_1, p_2)
        res_21 = self._matrix_addition(p_3, p_4)
        res_22 = self._matrix_subtraction(self._matrix_subtraction(self._matrix_addition(p_5, p_1), p_3), p_7)

        # 结果合并到 res_11 中
        res_11.extend(res_21)
        res_12.extend(res_22)
        assert len(res_11) == len(res_12)
        for i in range(len(res_11)):
            res_11[i].extend(res_12[i])
        res_matrix = res_11
    # 返回最终结果
    return res_matrix
```

## 代码范例

### Python

Python 环境：Python 3.7

[GitHub Code Link](https://github.com/YuweiYin/Code_Play/blob/master/Algorithm-Essence/divide-conquer/matrix-strassen.py)

## 参考资料

- Introduction to Algorithm (aka CLRS) Third Edition - Chapter 4
