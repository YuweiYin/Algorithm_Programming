# Algorithm - Data Structure - Binary Indexed Tree

By [YuweiYin](https://yuweiyin.github.io/)

## 简介

树状数组 Fenwick Tree (Binary Indexed Tree, BIT)

## 场景

场景与 [线段树](./segment-tree) (Segment Tree, ST) 相似，BIT 常用作于区间求和。

- array：依下标 index 连续存储的**数值**数组/列表
- add(index, value)：把 array 中下标为 index 的元素值 增长 value
- sum(num)：计算前缀和（前 num 个元素值的和）
- range_sum(from, to)：求闭区间 \[ from, to \] 中元素值的和

注意：

1. array 中存储的也可以不是数值，而是某种结构体，但是该结构体一定要两两可以比较序关系（**全序**关系）
2. add 和 sum 操作可以有**很多次**。

## 场景分析

### 数组/列表结构

如果直接用 array 数组进行操作，那么 add 操作的时间复杂度为 O(1)，sum 操作的时间复杂度为 O(n)，其中 n 为 array 的长度。

设有 a 次 add、s 次 sum，则整体时间复杂度为 O(a + sn)

### 前缀和数组

如果使用一个与 array 等长的数组 pre_array 来存储前缀和，那么构造 pre_array 的时间复杂度为 O(n)。

在 pre_array 上操作并对其进行维护，add 操作的时间复杂度为 O(n)，sum 操作的时间复杂度为 O(1)。

比如：如果修改了第一个元素的值，那么整个 pre_array 的值都要改变。

设有 a 次 add、s 次 sum，则整体时间复杂度为 O(an + s)

### 树状数组

对前述两种方式进行折中：要存储并维护前缀和数组，但要换成层级树状结构，树高为 O(log n)。

进行 add 和 sum 操作时，只要操作/维护路径长度不超过树高，那么整体的时间复杂度就会降低，均为 O(log n)。

设有 a 次 add、s 次 sum，则整体时间复杂度为 O(a log n + s log n) = O((a + s) log n)

但是，与线段树类似，一旦 array 长度变化，线状数组 BIT 就需要重建了，每次重建的时间复杂度为 O(n log n)，也可以优化为 O(n)。

因此，在 n 值较大（数组较长）、且数组长度不频繁变动的情况下，线状数组对区间求和 sum 操作效率的提升效果显著。

## 设计 & 细节

### BIT 建立

以 array = [1, 7, 3, 0, 5, 8, 3, 2, 6, 2, 1, 1, 4, 5] 为例。分析时假定数组首位 index 为 1。

![bit-1](/img/info-technology/algorithm/data-structure/bit-1.png)

BIT 建立过程：

- 设置一个与 array 等长的前缀和数组 pre_array，其值均为空。
- 第一轮扫描（tree layer 1），从 index=1 首元素开始：
    - index = 1 - 1 + 2^0 = 1 的位置，记录闭区间 \[ 1, 1 \] 的前缀和 1
    - index = 1 - 1 + 2^1 = 2 的位置，记录闭区间 \[ 1, 2 \] 的前缀和 8
    - index = 1 - 1 + 2^2 = 4 的位置，记录闭区间 \[ 1, 4 \] 的前缀和 11
    - index = 1 - 1 + 2^3 = 8 的位置，记录闭区间 \[ 1, 8 \] 的前缀和 29
    - index = 1 - 1 + 2^4 = 16 大于数组长度 14，跳到下一轮扫描
- 第二轮扫描（tree layer 2），从 pre_array 中非空的第一个元素 index=3 开始：
    - index = 3 - 1 + 2^0 = 3 的位置，记录闭区间 \[ 3, 3 \] 的前缀和 3
    - index = 3 - 1 + 2^1 = 4 的位置，pre_array 在该位置已经有值了，找往后找首个非空元素 index=5
    - index = 5 - 1 + 2^0 = 5 的位置，记录闭区间 \[ 5, 5 \] 的前缀和 5
    - index = 5 - 1 + 2^1 = 6 的位置，记录闭区间 \[ 5, 6 \] 的前缀和 13
    - index = 5 - 1 + 2^2 = 8 的位置，pre_array 在该位置已经有值了，找往后找首个非空元素 index=9
    - index = 9 - 1 + 2^0 = 9 的位置，记录闭区间 \[ 9, 9 \] 的前缀和 6
    - index = 9 - 1 + 2^1 = 10 的位置，记录闭区间 \[ 9, 10 \] 的前缀和 8
    - index = 9 - 1 + 2^2 = 12 的位置，记录闭区间 \[ 9, 12 \] 的前缀和 10
    - index = 9 - 1 + 2^3 = 16 大于数组长度 14，跳到下一轮扫描
- 第三轮扫描（tree layer 3），从 pre_array 中非空的第一个元素 index=7 开始：
    - index = 7 - 1 + 2^0 = 7 的位置，记录闭区间 \[ 7, 7 \] 的前缀和 3
    - index = 7 - 1 + 2^1 = 8 的位置，pre_array 在该位置已经有值了，找往后找首个非空元素 index=11
    - index = 11 - 1 + 2^0 = 11 的位置，记录闭区间 \[ 11, 11 \] 的前缀和 1
    - index = 11 - 1 + 2^1 = 12 的位置，pre_array 在该位置已经有值了，找往后找首个非空元素 index=13
    - index = 13 - 1 + 2^0 = 13 的位置，记录闭区间 \[ 13, 13 \] 的前缀和 4
    - index = 13 - 1 + 2^1 = 14 的位置，记录闭区间 \[ 13, 14 \] 的前缀和 9
    - index = 13 - 1 + 2^2 = 16 大于数组长度 14，跳到下一轮扫描
- 第四轮扫描，发现 pre_array 已经写满了，pre_array（即 BIT）构造结束。

但是多轮扫描的比较复杂，因此通常设置一个值全为 0 的 pre_array，从左至右地使用 add 操作来完成 BIT 的建立。

建立 BIT 的时间复杂度为 O(n log n)。

### 元素增值 add

以 array = [1, 7, 3, 0, 5, 8, 3, 2, 6, 2, 1, 1, 4, 5] 为例。将 index=5 的元素值增加 2：add(5, 2)。

需要将 pre_array 中所有包含了 index=5 元素的前缀和结点均增加 2。

![bit-2](/img/info-technology/algorithm/data-structure/bit-2.png)

下标改为二进制值：

![bit-3](/img/info-technology/algorithm/data-structure/bit-3.png)

- 观察：0x0101 +2^0 = 0x0110, 0x0110 +2^1 = 0x1000
- 发现：每次将最末的 1 进位。
- 实现：`index += index & (-index)`
    - 注：`index & (-index)` 又常被称为 **lowbit**(index) 函数

**注意**：如果 add(index, value) 的 value 参数为**负数**，则可实现**减值**操作。

### 区间求和 sum

以 array = \[ 1, 7, 3, 0, 5, 8, 3, 2, 6, 2, 1, 1, 4, 5 \] 为例。求前 13 个元素值的和 sum(13)。

拆分 sum(13) = range_sum(1, 8) + range_sum(9, 12) + range_sum(13, 13) = 29 + 10 + 4 = 43

根据 BIT 的构造，闭区间 \[ 1, 8 \]、\[ 9, 12 \]、\[ 13, 13 \] 是一定可以直接索引到的，其索引下标在 pre_array 中分别为 8、12、13。

![bit-4](/img/info-technology/algorithm/data-structure/bit-4.png)

- 如何快速获得这几个索引下标呢？观察二进制表示：
    - 13 = 2^3 + 2^2 + 2^0 = 0x1101 为输入 sum 的参数值
    - 12 = 2^3 + 2^2 = 0x1100 为 0x1101 最末的 1 清零
    - 8 = 2^3 = 0x1000 为 0x1100 最末的 1 清零
    - 结束标志 0 = 0x1000 为 0x1000 最末的 1 清零
    - 实现：`index -= index & (-index)`

![bit-5](/img/info-technology/algorithm/data-structure/bit-5.png)

- 时间复杂度分析：
    - 角度一：代表这三个闭区间的结点分别位于“树”的第 1、2、3 层，操作路径长度不超过树高。
    - 角度二：拆解 13 为二进制表示，检验次数即为二进制位数 (int)(log 13)。
    - 因此 sum 操作的时间复杂度为 O(log n)。

BIT 与快速幂算法有异曲同工之妙。

### 其它实现细节

- 使用**长度为 n+1** 的 pre_array 作为 BIT
    - 首位为 0 仅作占位，不影响求和结果
    - 方便 sum 操作的循环结束判断：num 减到 0 就停止
- 建立 BIT：
    - O(n log n)：以全 0 数组开始，用 add 操作建立 BIT
- 求任意区间和 `range_sum(from, to) = sum(to) - sum(from - 1)` 时间复杂度仍然为 O(log n)

## 代码范例

### Python

Python 环境：Python 3.7

[GitHub Code Link](https://github.com/YuweiYin/Code_Play/blob/master/Algorithm-Essence/data-structure/binary-indexed-tree.py)

## 参考资料

[Youtube - Tutorial: Binary Indexed Tree (Fenwick Tree)](https://www.youtube.com/watch?v=v_wj_mOAlig)
