# Algorithm - Graph Theory - Floyd-Warshall

By [YuweiYin](https://yuweiyin.github.io/)

## 简介

全源最短路径 All Pairs Shortest Path

Floyd-Warshall 算法 & 计算有向图的传递闭包 Transitive Closure

## 全源最短路径

全源最短路径是考虑如何找到一个图中所有结点之间的(加权)最短路径。

给定一个带(边)权重的有向图 G = (V, E)，其权重函数为 w: E -> R，该函数将边映射到实数值权重上。目标是找到对于所有的结点对 u, v \in V，一条从结点 u 到结点 v 的加权最短路径。

计算结果通常以表格(二维数组)形式输出：第 u 行第 v 列给出的是结点 u 到结点 v 的最短路径权重值。

可以对每个结点单独运行**单源最短路径算法**，例如 Dijkstra 算法或 Bellman-Ford 算法。

- 对于 Dijkstra 算法
    - 如果使用**线性数组**来实现**最小优先队列** Q，则 `|V|` 次运行的总时间是 `O(|V|^3 + |V|·|E|)`，即 `O(|V|^3)`。
    - 如果使用**二叉堆**实现 Q，则 `|V|` 次运行的总时间是 `O(|V|·|E| log |V|)`，这在**稀疏图**的情况下是个较大的改进。
    - 如果使用**斐波那契堆**实现 Q，则 `|V|` 次运行的总时间是 `O(|V|·|E| + |V|^2 log |V|)`。这对大型稀疏图来说是个很好的算法。

但是如果图中含有权重为负值的边，就不能使用 Dijkstra 算法。此时如果运行 Bellman-Ford 算法，`|V|` 次运行的总时间是 `O(|V|^2·|E|)`，在稠密图（`|E|` 接近 `|V|^2`）的情况下，此运行时间为 `O(|V|^4)`。

假定用邻接矩阵来表达图结构，将结点编号为 1, 2, ..., `|V|`，则算法的输入是一个 n x n 的矩阵 W，该矩阵代表的是一个有 n 个结点的有向图 G = (V, E) 的边的权重。即 W = (wij)，其中：

- 若 i == j，则 wij = 0
- 若 i != j 且 (i, j) \in E，则 wij 等于有向边 (i, j) 的权重值 w(i, j)
- 若 i != j 且 (i, j) \notin E，则 wij = inf 无穷

算法输出的表格是一个 n x n 的矩阵 D = (dij)，其中 dij 代表的是从结点 i 到结点 j 的一条最短路径的权重值。若用 d(i, j) 来代表从结点 i 到结点 j 的最短路径权重，则在算法结束时有 dij = d(i, j)。

为了获取最优解，还需要计算出**前驱结点矩阵** P = (pij)，其中 pij 在 i == j 或 从 i 到 j 不存在路径时为 nil 空，在其他情况下给出的是从结点 i 到结点 j 的某条最短路径上 结点 j 的前驱结点。有矩阵 P 的第 i 行所诱导的**前驱子图** 是一棵根结点为 i 的**最短路径树**。

如果 Gpi 是一棵以结点 i 为根结点的最短路径树，则下面的过程将打印出从结点 i 到结点 j 的一条最短路径。

```
PRINT_ALL_PAIRS_SHORTEST_PATH(P, i, j)
1  if i == j
2      print i
3  elseif pij == nil
4      print "no path from" i "to" j "exists"
5  else
6      PRINT_ALL_PAIRS_SHORTEST_PATH(P, i, pij)
7      print j
```

## Floyd-Warshall 算法

本节介绍与[“矩阵乘法”解法](./all-pairs-sp-mm) 不同的动态规划公式 来解决全源最短路径问题。Floyd-Warshall 算法的运行时间为 `\Theta(|V|^3)`。假定带(边)权有向图 G = (V, E) **可以存在负权重的边**，但**不能存在负权环**。此算法的可以延伸求解有向图的**传递闭包**。

- 动态规划算法的通常设计步骤：
    1. 分析最优解的结构（最优子结构性质、重叠子问题性质）
    2. 设计递归解决方案
    3. 计算最优值（自底向上的循环解法 or 带备忘的自顶向下递归解法）
    4. 根据第 3 步的表格信息 构造最优解

### 1. 最短路径的结构

在 Floyd-Warshall 算法中，考虑对一条最短路径上的各个**中间结点**进行处理。简单路径 `p = <v1, v2, ..., vl>` 上的中间结点是指 路径 p 上除了起点 v1 和终点 vl 之外的任意结点。

Floyd-Warshall 算法依赖于如下观察。假定图 G 的所有结点为 V = {1, 2, ..., n}，考虑其中的一个子集 {1, 2, ..., k}，这里 k 是某个小于 n 的正整数。对于任意结点对 i, j \in V，考虑从结点 i 到结点 j 的**所有中间结点均取自集合** {1, 2, ..., k} 的路径，并且设 p 为这些路径中权重最小的一条路径（显然路径 p 是简单路径）。Floyd-Warshall 算法利用了路径 p 和 从 i 到 j 之间的中间结点均取自集合 {1, 2, ..., k-1} 的最短路径 这两种路径之间的关系。该关系依赖于结点 k 是否是路径 p 上的一个中间结点。

![floyd-warshall-1](/img/info-technology/algorithm/graph-theory/shortest-path/floyd-warshall-1.png)

### 2. 设计递归解决方案

基于上述观察，可以定义一个最短路径估计的递归公式。设 dij^{k} 为从结点 i 到结点 j 的所有中间结点全部取自集合 {1, 2, ..., k} 的一条最短路径的权重。当 k == 0 时，dij^{0} 代表的路径没有任何中间结点，这样的路径最多只有一条边 (i, j)，因此 dij^{0} = w(i, j)。据此有如下的递归定义式：

- 若 k == 0，则 dij^{k} = w(i, j)
- 若 k >= 1，则 dij^{k} = min( dij^{k-1}, dik^{k-1} + dkj^{k-1} )

因为对任何路径来说，所有中间结点都属于集合 {1, 2, ..., n}，故矩阵 D^{n} = (dij^{n}) 给出的就是最终答案：对于所有的 i, j \in V，有 dij^{n} = d(i, j) 最优值。

### 3. 自底向上的循环解法

根据前述递归式，可以使用如下的算法，以递增次序来计算 dij^{k} 的值。该算法的输入为一个 n x n 的矩阵 W，即邻接矩阵表示法的权重矩阵。算法返回的是最短路径权重矩阵 D^{n}。

```
FLOYD_WARSHALL(W)
1  n = W.rows
2  D^{0} = W
3  for k = 1 to n
4      let D^{k} = (d_ij^{k}) be a new n x n matrix
5      for i = 1 to n
6          for j = 1 to n
7              d_ij^{k} = min( d_ij^{k-1}, d_ik^{k-1} + d_kj^{k-1} )
8  return D^{n}
```

Floyd-Warshall 算法的运行时间由算法第 3～7 行的三层 for 循环嵌套所决定。因为算法第 7 行的每次执行时间为 O(1)，因此该算法的总运行时间为 `\Theta(n^3)`。而且此代码非常紧凑，也没有包含任何精巧的数据结构，因此隐藏在渐近符号中的常数因子较小，且算法实现难度很小。即便对于输入规模中等的图，Floyd-Warshall 算法的效率也相当好。

![floyd-warshall-2](/img/info-technology/algorithm/graph-theory/shortest-path/floyd-warshall-2.png)

![floyd-warshall-3](/img/info-technology/algorithm/graph-theory/shortest-path/floyd-warshall-3.png)

### 构造一条最短路径

在 Floyd-Warshall 算法中，可以有多种不同的方法来构建最短路径。一种办法是先计算最短路径权重矩阵 D，然后利用 D 矩阵去构造**前驱矩阵** P（即前面图 25-4 右侧的 $ \Pi $ 矩阵），构造时间为 O(n^3)。一旦给定了前驱矩阵，`PRINT_ALL_PAIRS_SHORTEST_PATH(P, i, j)` 将打印出给定起点 i 和终点 j 的一条最短路径上的所有结点。

另外，可以在计算矩阵 D^{k} 的同时计算前驱矩阵 P。具体来说，将计算一个矩阵序列 P^{1}, P^{2}, ..., P^{n}，最终的前驱矩阵 P = P^{n}。定义 pij^{k} 为从结点 i 到结点 j 的一条 所有中间结点都取自集合 {1, 2, ..., k} 的最短路径上 j 的前驱结点。

可以给出 pij^{k} 的一个递归公式如下。当 k == 0 时，从 i 到 j 的一条最短路径没有中间结点。

- 若 i == j 或 wij == inf，则 pij^{0} = inf
- 若 i != j 或 wij < inf，则 pij^{0} = i

对于 k >= 1，如果考虑路径 `i ~> k ~> j`，这里 k != j，则所选择的 j 的前驱等价于：选择从结点 **k** 到 j 的一条 中间结点全部取自集合 {1, 2, ..., k-1} 的最短路径上的前驱。否则等等价于：选择从结点 **i** 到 j 的一条 中间结点全部取自集合 {1, 2, ..., k-1} 的最短路径上的前驱。即，对于 k >= 1，有如下式子：

- 若 dij^{k-1} <= dik^{k-1} + dkj^{k-1}，则 pij^{k} = pij^{k-1}
- 若 dij^{k-1} > dik^{k-1} + dkj^{k-1}，则 pij^{k} = pkj^{k-1}

因此可以在计算 D^{k} 的同时计算出 P^{k}，最终需要的**前驱矩阵 P**为 P^{n}。另外，**前驱子图** Gp\_{i} 是前驱矩阵的第 i 行，且此前驱子图为一棵根结点为 i 的最短路径树。

## 有向图的传递闭包

给定有向图 G = (V, E)，结点集合为 V = {1, 2, ..., n}，目标是判断对于所有的结点对 i, j，图 G **是否包含一条**从结点 i 到 j 的路径（即**可达性**的判别）。定义图 G 的**传递闭包** 为图 G^\* = (V, E^\*)，其中 E^\* = {(i, j): 如果图 G 中包含一条从结点 i 到 j 的路径}。

一种时间复杂度为 `\Theta(n^3)` 的计算图 G 的传递闭包的办法是给 E 中的每条边赋予权重 1，不存在的边则在邻接矩阵中赋值为 inf 无穷，然后运行 Floyd-Warshall 算法。如果存在一条从结点 i 到结点 j 的路径，则在最终的矩阵 D^{n} 中，有 dij < n，否则 dij = inf。

还有一种类似的方法，其时间复杂度仍为 `\Theta(n^3)`，但在实际场景中能节省时间和空间。该办法以**逻辑或**操作 $ \lor $ 和 **逻辑与**操作 $ \land $ 来替换 Floyd-Warshall 算法中的算术操作 min 和 +。对于 i, j, k = 1, 2, ..., n，定义：如果图 G 中存在一条从结点 i 到结点 j 的所有中间结点都取自集合 {1, 2, ..., k} 的路径，则 tij^{k} = 1，否则 tij^{k} = 0。

构建传递闭包 G^\* = (V, E^\*) 的方法为：将边 (i, j) 置于集合 E^\* 当且仅当 tij^{n} = 1。

- 在 k 为 0 时，有：
    - 若 i != j 且 (i, j) \notin E，则 tij^{0} = 0
    - 若 i == j 或 (i, j) \in E，则 tij^{0} = 1
- 对于 k >= 1，有：
    - tij^{k} = tij^{k-1} \lor ( tik^{k-1} \land tkj^{k-1} )

同 Floyd-Warshall 算法一样，以 k 递增的次序来计算矩阵 T^{k} = (tij^{k})：

```
TRANSITIVE_CLOSURE(G)
1  n = |G.V|
2  let T^{0} = (t_ij^{0}) be a new n x n matrix
3  for i = 1 to n
4      for j = 1 to n
5          if i == j or (i, j) \in G.E
6              t_ij^{0} = 1
7          else
8              t_ij^{0} = 0
9  for k = 1 to n
10     let T^{k} = (t_ij^{k}) be a new n x n matrix
11     for i = 1 to n
12         for j = 1 to n
13             t_ij^{k} = t_ij^{k-1} \lor ( t_ik^{k-1} \land t_kj^{k-1} )
14 return T^{n}
```

由于在某些计算机上，对单个位值进行的逻辑运算 比 对数据整数字的算术操作要快，所以此方法隐含在渐近符号中的常数因子相对更小，因此更快。

另外，因为上述传递闭包算法 使用到的矩阵的各元素仅存储布尔值，而不是整数值，其空间需求也比常规的 Floyd-Warshall 算法小一个数量级，这个数量级就是当前计算机存储里的一个字的规模。

![transitive-closure-1](/img/info-technology/algorithm/graph-theory/shortest-path/transitive-closure-1.png)

## Python 代码范例

Python 环境：Python 3.7

### Floyd-Warshall 全源最短路径算法

[GitHub Code Link](https://github.com/YuweiYin/Code_Play/blob/master/Algorithm-Essence/graph-theory/shortest-path/floyd-warshall.py)

## 参考资料

- Introduction to Algorithm (aka CLRS) Third Edition - Chapter 25
