# Algorithm - Data Structure - Lowest Common Ancestor

By [YuweiYin](https://yuweiyin.github.io/)

## 简介

最近公共祖先 (Lowest Common Ancestor, LCA)

## 场景

LCA(T, u, v) 问题的目标是求一棵树 T 上两结点 u 和 v 的最近公共祖先 a。

- “**最近**”意味着结点 a 在树 T 中的深度尽量大。
- 结点 x 的“**祖先**”包括了 x 结点自身，以及 x 的父结点、x 的父结点的父结点、...、树根结点。

LCA 查询的重要应用：一旦找到了树中两结点 u, v 的最近公共祖先 a，那么 u->v 的**最短路径**便是 u->a->v 路径。

## 场景分析

### 朴素 LCA 算法

1. 先求出树上每个结点的深度。
2. 对于查询 LCA(u, v)，用两个指针 p1、p2 指向 u、v。
3. 将 p1、p2 中深度较大的结点不断指向其父结点，直到 p1、p2 所指结点的深度相同。
4. 之后 p1、p2 同步向上移动，直到 p1==p2，即二者指向同一结点，该结点就是目标 LCA(u, v)。

### LCA 向 RMQ 转化

LCA 问题可以转化为 [RMQ 区间最值查询](./range-min-max-query) 问题。利用 RMQ 中的 Sparse Table 处理 Euler Tour（后文会详述），通过时间复杂度 O(n log n) 的预处理，LCA 查询可以达到 O(1) 的时间复杂度。

### LCA 的 Tarjan 算法

LCA 的 Tarjan 算法是一种利用 [Union Find 并查集](./union-find) 的离线算法，能够在一次 DFS 过程中完成所有 query。

时间复杂度为 O(n + q) ，q 为 query 的次数。

## 设计 & 细节

以下图的树为例，结点内部的数字为结点值/结点 key，结点左边的数字为结点的前序遍历序号：

![lca-1](/img/info-technology/algorithm/data-structure/lca-1.png)

### 遍历构造工具数组

先对树 T 进行深度优先遍历 DFS（前序遍历），同时记录此遍历路径。如果**不记录重复的结点**，那么就是普通的前序遍历序列 Preorder Traversal（**下文简称 PT**）。
```python
PT = [ 0, 5, 7, 2, 1, 3, 6, 8, 9, 4 ]
```

PT 有个特性：树中任意两结点 u, v，如果 u 是 v 的祖先，那么 u 的 key 在序列 PT 中的下标索引一定小于 v。（反之则不一定）

PT 是从 index 到结点 key 的映射，PT 数组的长度为树结点总数目，可以得出其逆映射（**记为 PTR**）为：
```python
PTR = [ 0, 4, 3, 5, 9, 1, 6, 2, 7, 8 ]
```

注意：如果以上述列表形式表达 PTR，那么其总长度应该为树结点 key 的最大值，如果处理的 key 并不连续，那么将会有很多空值、浪费空间。因此考虑用如下字典方式表达 PTR 映射：
```python
PTR = dict({
	0: 0, 1: 4, 2: 3, 3: 5, 4: 9,
	5: 1, 6: 6, 7: 2, 8: 7, 9: 8
})
```

如果**要记录重复的结点**，则序列称为称为 Euler Tour（**下文简称 ET**）。这里的 ET 只记录结点对应于 PT 序列中的下标（即图中结点左侧的数字）。
```python
ET = [ 0, 1, 2, 3, 2, 1, 4, 5, 4, 6, 4, 1, 7, 1, 0, 8, 9, 8, 0 ]
```

另外还需要一个与 PT 等长的**数组 First** 用于映射，记录 ET 中 `range(len(PT))` 这些下标数字 在 ET 中首次出现的位置：
```python
First = [ 0, 1, 2, 3, 6, 7, 9, 12, 15, 16 ]
```

前述列表的构造，时间复杂度均为 O(n)，n 为树结点总数目。

最后，对 ET 数组构建 Sparse Table，方便进行 RMQ 查询任意子区间的最小值。时间复杂度 O(n log n)。

### 查询 LCA

利用前述数组/列表 即可在常数时间计算任两个结点 u, v 的 LCA(u, v)，以 LCA(3, 8) 为例。

注意：输入给 LCA 算法的参数代表了结点的 key（即图中结点内部的数字），可通过 PTR 转换为 PT 中的下标。

1. 先利用 PTR 字典，将结点 key 为 3 和 8 **映射**为 PT 对应的下标。
	- 即 PTR[3] = 5 和 PTR[8] = 7
2. 随后利用 First 数组，在 ET 中找到**第一次出现** 5 和第一次出现 7 的位置。
	- 即 First[5] = 7 和 First[7] = 12
3. 利用 RMQ 算法求 ET 中 index=7 到 index=12 的**闭区间中的最小值**。
	- 此闭区间为 \[ 5, 4, 6, 4, 1, 7 \]，其最小值即为目标 LCA 结点在 PT 中的下标 1
4. 最后利用 PT 数组，将前序遍历序列的下标映射为结点 key
	- 即 PT[1] = 5

这四个步骤的时间复杂度均为 O(1)，因此查询 LCA 的总时间复杂度为 O(1)。

### LCA & RMQ 效率分析

由于 LCA 查询利用了 RMQ 算法，因此也继承了一些 RMQ 算法的缺点。

RMQ 算法的主要缺点在于构造 Sparse Table 的处理时间较长，为 O(n log n) 时间复杂度，因此如果用于构造 Sparse Table 的原数组经常变化（每次变化都需要重建 ST），则 RMQ 算法效率不高。

因此，这里我们需要观察 LCA 查询中，什么情况会导致重建 Sparse Table。

Sparse Table 只依赖于 ET 数组，而只要树结构不变（没有结点/边的增删），ET 数组就不会变。因此：将某结点 x 替换为另一个结点 y 不会改变 ET，也不会使得 ST 重建。（会使得 PT 和 PTR 改变，而 ET 和 First 不变。）

因此，只要**树结构不频繁变动**，利用 RMQ 算法的 LCA 查询就会很高效 O(1)。

## 代码范例

### Python

Python 环境：Python 3.7

- 注：
	- 采用邻接表来存储，因为多叉树是一种较为稀疏的图结构。Vertex 类为顶点结构体，AdjacencyList 为图结构体。
	- 其中 SparseTableRMQ 类的写法与 [RMQ 区间最值查询](./range-min-max-query) 文章中的代码相同。

[GitHub Code Link](https://github.com/YuweiYin/Code_Play/blob/master/Algorithm-Essence/data-structure/lowest-common-ancestor.py)

## 参考资料

[Youtube - Lowest Common Ancestor Tutorial](https://www.youtube.com/watch?v=HeeyUZmaZg0)
