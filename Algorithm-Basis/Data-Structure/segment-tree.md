# Algorithm - Data Structure - Segment Tree

By [YuweiYin](https://yuweiyin.github.io/)

## 简介

线段树 (Segment Tree, ST)

## 场景

线段树常用作于求 array 中区间最大值/最小值、区间的和，这类区间的**某种特性值**。

- array：依下标 index 连续存储的**数值**数组/列表
- update：修改 array 中某个下标 index 对应的数值
- query：查询 array 中某一个下标区间 \[left, right\) 中的**某种特性值**（比如：区间最值、区间的和）

注意：

1. array 中存储的也可以不是数值，而是某种结构体，但是该结构体一定要两两可以比较序关系（**全序**关系）
2. update 和 query 可以有**很多次**。

## 场景分析

### 数组/列表结构

如果采用普通的数组/列表结构进行处理，那么 update 操作的时间复杂度为 O(1)，query 操作的时间复杂度为 O(n)，其中 n 为 array 的长度。

设有 u 次 update、q 次 query，则整体时间复杂度为 O(u + qn)

在 query 较多较频繁的场景下，该结构的整体时间复杂度较高。

### 线段树结构

而线段树通过维护不同粒度的区间特性值，其形状是完全二叉树（树高为 O(log n)），以二分查找的思路来加速 query 操作，使其时间复杂度降低到了 O(log n)。

为了维护不同粒度的区间特性值，线段树在 update 操作时是从叶向上逐级更新，时间复杂度增加到了 O(log n)。

设有 u 次 update、q 次 query，则整体时间复杂度为 O(u log n + q log n) = O((u + q) log n)

但是，一旦 array 长度变化，线段树就需要重建了，每次重建的时间复杂度为 O(n)。

因此，在 n 值较大（数组较长）、且数组长度不频繁变动的情况下，线段树对 query 操作效率的提升效果显著。

## 设计 & 细节

### 求区间特性值 merge

merge(left, right) 函数用于计算下标为 \[ left, right \] 的闭区间的“区间特性值”，比如最小值。

- 注意：
    - 通常来说，merge 操作需要做到常数时间复杂度，即 O(1)。
    - 下文均以求区间最小值为例展开论述。
    - array 的长度 n 目前暂假定为 2 的自然数幂次，之后会讨论其他情况。

### ST 建立

- 建树思路：
    - 线段树的叶结点均为 array 数组中的各个值。
    - 从叶结点开始，相邻两两结点 merge 出父结点的值，直至根结点。

- 可以看出：
    - 最终结点数目为 n + n/2 + n/4 + ... + 1 = 2n-1。
    - 建树需对 array 扫描一遍，时间复杂度为 O(n)

我们用一个长度为 2n 的大数组来存储所有结点值，其中下标较大的最末 n 个位置存放原 array 的值，作为叶结点值。

随后从后往前扫描，对叶结点两两分组，进行 merge 操作，计算出的值为其父结点的值，保存于下标为 (int)(left / 2) 的位置。

- 以 array = [1, 5, 3, 7] 为例：
    - 构造大数组 st = [inf, inf, inf, inf, 1, 5, 3, 7]。其中 inf 为预设的数字最大值，因为目前假定 merge 是求区间最小值。
    - 从后往前扫描，两两 merge：
        - [3, 7] -> 3: st = [inf, inf, inf, 3, 1, 5, 3, 7]
        - [1, 5] -> 1: st = [inf, inf, 1, 3, 1, 5, 3, 7]
        - [1, 3] -> 1: st = [inf, 1, 1, 3, 1, 5, 3, 7]
    - 最终得到线段树（大数组）为 [inf, 1, 1, 3, 1, 5, 3, 7]，建树完毕。

以 array = [1, 5, 3, 7, 3, 2, 5, 7] 为例：

1. 初始 st 大数组：

![segment-tree-0](/img/info-technology/algorithm/data-structure/segment-tree-0.png)

2. 构造完毕的 st：

![segment-tree-1](/img/info-technology/algorithm/data-structure/segment-tree-1.png)

3. st 各结点存储的区间信息如下：

![segment-tree-2](/img/info-technology/algorithm/data-structure/segment-tree-2.png)

### 更新 update

更新 array 的值时，修改叶结点的值，并逐级向上 merge。

因为树高为 O(log n)，因此 update 操作的时间复杂度为 O(log n)。

以 array = [1, 5, 3, 7, 3, 2, 5, 7] 为例，更新其 index=5 的值为 6，即操作 update(5, 6)：

1. 先修改叶结点：

![segment-tree-3](/img/info-technology/algorithm/data-structure/segment-tree-3.png)

2. 再逐级向上更新：

![segment-tree-4](/img/info-technology/algorithm/data-structure/segment-tree-4.png)

3. 直至树根，更新完毕：

![segment-tree-5](/img/info-technology/algorithm/data-structure/segment-tree-5.png)

### 查询 query

查询某一区间 \[ left, right \] 的“区间特性值”（比如最小值），执行操作 query(left, right)。

这里 \[ left, right \] 为闭区间，变量取值范围为 0 <= left <= right <= n-1

- 从叶结点开始查询。查询时，有三种情况：
    - case 1. 当前结点所代表的区间完全位于 query 区间 \[ left, right \] 之外（与闭区间无交集），则不应考虑当前结点。
    - case 2. 当前结点所代表的区间完全位于 query 区间 \[ left, right \] 之内（含边界值）
        - case 2.1. 当前结点的父结点所代表的区间也完全位于 query 区间 \[ left, right \] 之内（含边界值），则可以直接查询其父结点值，减少查询量。
        - case 2.2. 当前结点的父结点所代表的区间部分位于 query 区间 \[ left, right \] 之内、部分在外，则分段考虑：先处理位于 query 区间外的部分；后处理位于 query 区间内的部分。

以 array = [1, 5, 3, 7, 3, 2, 5, 7] 为例，查询区间 \[ 1, 6 \] 的最小值 query(1, 6)：

![segment-tree-6](/img/info-technology/algorithm/data-structure/segment-tree-6.png)

- 分析：
    - 从叶结点开始查询，下标为 0 和下标为 7 的叶结点都与 query 区间 \[ 1, 6 \] 无交集，属于情况 1，排除之。
    - 下标为 1 和下标为 6 的结点完全位于 query 区间 \[ left, right \] 之内，属于情况 2。但是其父结点所代表的区间不完全位于 query 区间内，所以属于情况 2.2。
    - 下标为 2 至下标为 5 的结点属于情况 2.1，因此只需观察其父结点即可。

实现时，为了避免重复处理那些 query 区间外的、已被排除的值，可采用对撞指针、区间夹逼的思想。query 时间复杂度 O(log n)。

更多例子：以 update 后的 array = [1, 5, 3, 7, 3, 6, 5, 7] 为例，查询区间 \[ 1, 6 \] 的最小值 query(1, 6)：

![segment-tree-7](/img/info-technology/algorithm/data-structure/segment-tree-7.png)

![segment-tree-8](/img/info-technology/algorithm/data-structure/segment-tree-8.png)

### n != power of 2

若 array 长度 n 不为 2 的自然数幂次，树的结构看似比较乱，当前算法看似无法正常运行。

一个简单的考虑是将 array 填充 inf 直至某个 2 的自然数幂次，但这可能会带来很大的存储负担，增加了时空复杂度。

实际上，本算法能够处理**任意正整数** n 长度的 array，即便是奇数也没问题。

以 array = [4, 3, 9, 1, 6, 7] 为例：

![segment-tree-9](/img/info-technology/algorithm/data-structure/segment-tree-9.png)

## 代码范例

### Python

Python 环境：Python 3.7

[GitHub Code Link](https://github.com/YuweiYin/Code_Play/blob/master/Algorithm-Essence/data-structure/segment-tree.py)

## 参考资料

- [Youtube - Efficient Segment Tree Tutorial](https://www.youtube.com/watch?v=Oq2E2yGadnU)
- [CF Blog](http://codeforces.com/blog/entry/18051)
