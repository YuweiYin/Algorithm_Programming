# Algorithm - Data Structure - Range Minimum/Maximum Query

By [YuweiYin](https://yuweiyin.github.io/)

## 简介

区间最值查询 Sparse Table (Range Minimum/Maximum Query, RMQ)

## 场景

RMQ 主要用作于求 array 中区间最大值/最小值，在 O(n log n) 时间复杂度的预处理（运用动态规划思想）后，求区间最值的操作能达到 O(1) 的时间复杂度！不过代价是修改或者增删 array 数组时，需要重新用 O(n log n) 的时间复杂度进行预处理。

预处理（构建 Sparse Table）的空间复杂度为 O(n log n)，而非 O(n^2)。因为只存储长度为 2 的自然数幂次（1、2、4、8...）的区间最值。

- array：依下标 index 连续存储的**数值**数组/列表
- update：修改 array 中某个下标 index 对应的数值
- query(from, to)：查询 array 中某一个下标区间 \[from, to\) 中的**区间最值**

注意：

1. array 中存储的也可以不是数值，而是某种结构体，但是该结构体一定要两两可以比较序关系（**全序**关系）
2. update 和 query 可以有**很多次**。

## 场景分析

### 数组/列表结构

- 建数组的时间复杂度为 O(n)，array 长度变化的数组修改时间为 O(1)
- update 时间复杂度为 O(1)
- query 查询区间最值/区间和 的时间复杂度为 O(n)

### [线段树结构](./segment-tree)

- 建树时间复杂度为 O(n)，一旦 array 长度变化，需要重新建树
- update 时间复杂度为 O(log n)
- query 查询区间最值/区间和 的时间复杂度为 O(log n)

### Sparse Table RMQ

- 建表时间复杂度为 O(n log n)，空间复杂度为 O(n log n)，一旦 array 长度变化，需要重新建表
- update 操作后也需要重新建表，时间复杂度为 O(n log n)
- query 查询区间最值 的时间复杂度为 O(1)

从以上对比很明显可以看出，Sparse Table RMQ 适合于这样的场景：array 很长、且几乎不改变，并且需要处理大量的区间最值 query 操作。

## 设计 & 细节

以计算区间最小值为例，展开下文叙述。

### 建表

Sparse Table 只预先计算并存储长度为 2 的自然数幂次（1、2、4、8...）的区间最值。

以 array = [5, 2, 4, 7, 6, 3, 1, 2] 为例，处理过程如下：

1. 计算长度为 2^0 = 1 的区间最值：以步长为 1、窗口大小为 1 的滑动窗口扫过 array，结果即为原 array
	- 结果：res\_0 = [5, 2, 4, 7, 6, 3, 1, 2]
2. 计算长度为 2^1 = 2 的区间最值：以步长为 1、窗口大小为 2 的滑动窗口扫过 array。**注意尾部为空，记为 -。**
	- 结果：res\_1 = [2, 2, 4, 6, 3, 1, 1, -] （在求区间最小值的场景下，可以将 - 预设为 inf 无穷大）
3. 计算长度为 2^2 = 4 的区间最值：以步长为 1、窗口大小为 4 的滑动窗口扫过 array。
	- 结果：res\_2 = [2, 2, 3, 1, 1, -, -, -]
4. 计算长度为 2^3 = 8 的区间最值：以步长为 1、窗口大小为 8 的滑动窗口扫过 array。
	- 结果：res\_3 = [1, -, -, -, -, -, -, -]
5. 长度 2^4 = 16 > 8，结束扫描，前述结果的整体（二维数组 / 矩阵）即为 Sparse Table。

**Sparse Table 的含义**：res\_i[j] 表示从 array 的下标 j 开始、长度为 2^i 的区间的最值。

- 求窗口最值的优化策略：
	- 按前述的滑动窗口描述，每次都以步长为 1 扫过原始 array，但窗口会逐渐变大。
	- 如果计算窗口的最值时都是线性扫描，则会导致复杂度很高，额外做了很多重复的加法。
	- 因此可以用动态规划的思想、利用之前的输出值，来优化求区间最值的过程。

![rmq-0](/img/info-technology/algorithm/data-structure/rmq-0.png)

1. 计算长度为 2^0 = 1 的区间最值：以步长为 1、窗口大小为 1 的滑动窗口扫过 array，结果即为原 array
	- 结果：res\_0 = [5, 2, 4, 7, 6, 3, 1, 2]
2. 计算长度为 2^1 = 2 的区间最值：以步长为 1、窗口大小为 2 的滑动窗口扫过 array。窗口大小仅为 2，所以正常调用 min/max 函数即可。
	- 结果：res\_1 = [2, 2, 4, 6, 3, 1, 1, -]
3. 计算长度为 2^2 = 4 的区间最值：以步长为 1、窗口大小为 4 的滑动窗口扫过 array。计算窗口最值时，要利用 res\_1 的结果。
	- 比如：计算 res\_2[3] 时，即需要计算从 index=3 开始、长度为 2^2 的区间的最值，也就等于 res\_1[3] + res\_1[3 + 2^1]
	- 即：**状态转移方程**为 res\_i[j] = min( res\_{i-1}[j], res\_{i-1}[j + 2^{i-1}] )
	- 注意：计算到 res\_2[5] 时，发现 res\_1[7] 为 -，便停止计算、进行下一轮。
	- 结果：res\_2 = [2, 2, 3, 1, 1, -, -, -]
4. 计算长度为 2^3 = 8 的区间最值：以步长为 1、窗口大小为 8 的滑动窗口扫过 array。计算窗口最值时，要利用 res\_2 的结果。
	- res\_3[0] = min( res\_2[0], res\_2[0 + 2^2] ) = min(2, 1) = 1
	- 结果：res\_3 = [1, -, -, -, -, -, -, -]
5. 长度 2^4 = 16 > 8，结束扫描，前述结果的整体（二维数组 / 矩阵）即为 Sparse Table。

### 查询 query(left, right)

以 array = [5, 2, 4, 7, 6, 3, 1, 2] 为例，查询闭区间 \[ 1, 6 \] 的区间最小值 query(1, 6)：

- 先将 query 闭区间拆为两个子区间 sub1 和 sub2
	- 希望这两个子区间有如下两个性质：
        1. 两个子区间等长，其长度为 2 的自然数幂次；
        2. 两区间的并集恰好覆盖整个 query 区间。
	- 计算 query 区间的长度的 log\_2  对数值（下取整）为 (int) log\_2 (6 - 1) = 2
	- 则子区间长度 len(sub1) = len(sub2) = 2^2 = 4
	- 现在需确定这两个区间的起始位置：
		- sub1 从 left（即 index=1）开始
		- sub1 从 right - 2^2 + 1（即 index=3）开始
	- 两个子区间的区间最小值可以直接通过索引 Sparse Table 得到：
		- range_min(sub1) = SparseTable\[2\]\[1\]
		- range_min(sub1) = SparseTable\[2\]\[3\]
	- 用 min 函数计算这两个“最小值”的较小者，即可得到整个 query 区间的最小值

### 更新 update(index, value)

由于更新 array 中的一个值，或者增删一个元素，其影响往往都不止一条路径。

因此 Sparse Table 不像线段树、树状数组那样，更新操作的时间复杂度只是树高量级，即 O(log n)。

每次更新都需要重新建 Sparse Table，时间复杂度为 O(n log n)。

## 代码范例

### Python

Python 环境：Python 3.7

[GitHub Code Link](https://github.com/YuweiYin/Code_Play/blob/master/Algorithm-Essence/data-structure/range-min-max-query.py)

## 参考资料

[Youtube - Sparse Table Tutorial / RMQ](https://www.youtube.com/watch?v=9FLPwDn6L08)
