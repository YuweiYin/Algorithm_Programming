# Algorithm - Graph Theory - All Pairs Shortest Path

By [YuweiYin](https://yuweiyin.github.io/)

## 简介

全源最短路径 All Pairs Shortest Path

最短路径和矩阵乘法

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

## 全源最短路径和矩阵乘法

本节介绍有向图 G = (V, E) 上所有结点对的最短路径问题的一种动态规划算法。在动态规划的每个大循环里，将调用一个与矩阵乘法非常相似的操作，因此该算法看上去就像是重复的矩阵乘法。下面先给出一个 `\Theat(|V|^4)` 的算法，然后再将该算法改进到 `\Theat(|V|^3 log |V|)`。

- 动态规划算法的通常设计步骤：
    1. 分析最优解的结构（最优子结构性质、重叠子问题性质）
    2. 设计递归解决方案
    3. 计算最优值（自底向上的循环解法 or 带备忘的自顶向下递归解法）
    4. 根据第 3 步的表格信息 构造最优解

### 1. 最短路径的结构

在单源最短路径中，已证明一条最短路径的所有子路径都是最短路径，即具有最优子结构性质。假定用邻接矩阵来表示输入图，即 W = (wij)。考虑从结点 i 到结点 j 到一条最短路径 p，假定 p 至多包含 m 条边，并假定图中没有负权环，且 m 为有限值。

如果 i == j，则路径 p 的权重为 0 且不包含任何边。如果结点 i 和结点 j 不是同一个结点，则将路径 p 分解为 `i ~> k->j`，其中 i 到 k 的路径 p' 至多包含 m-1 条边。由 **引理 24.1**（最短路径的子路径也是最短路径）可知，p' 是从结点 i 到 k 的一条最短路径，因此 d(i, j) = d(i, k) + wkj。

### 2. 设计递归解决方案

设 lij^{m} 为从结点 i 到结点 j 的至多包含 m 条边的任意路径中的最小权重。当 m == 0 时，从结点 i 到结点 j 之间存在一条没有变得最短路径 当且仅当 i == j。因此有：

- 如果 i == j，则 lij^{0} = 0
- 如果 i != j，则 lij^{0} = inf 无穷

对于 m >= 1，需要计算的 lij^{m} 是 lij^{m-1} 的最小值 和 从 i 到 j 最多由 m 条边组成的任意路径的最小权重。通过对 j 的所有可能的前驱结点 k 进行检查来获得该值。因此递归式定义如下：

$$ lij^{m} = min( lij^{m-1}, min( lik^{m-1} + w(k, j) ) ) $$

因为对于所有的 j 有 w(j, j) = 0，所以上式简化为：对所有 1 <= k <= n，计算 $ lij^{m} = min( lik^{m-1} + w(k, j) ) $

如果图 G 不包含负权环，则对于每一对结点 i 和 j，如果 d(i, j) < inf，表示从 i 到 j 之间存在一条最短路径。由于该路径是简单路径，其包含的边最多为 n-1 条。从结点 i 到结点 j 的、由多于 n-1 条边构成的路径的权重 不可能比从 i 到 j 的最短路径权重更小。因此，真正的最短路径权重可以由此公式给出：$ d(i, j) = lij^{n-1} = lij^{n} = lij^{n+1} = ... $

### 3. 自底向上的循环解法

根据输入矩阵 W = (wij)，可以计算出矩阵序列 L^{1}, L^{2}, ..., L^{n-1}，其中对于 m = 1, 2, ..., n-1，有 L^{m} = (lij^{m})。最后的矩阵 L^{n-1} 包含的是最短路径的实际权重。注意，对于所有的结点 i 和 j，L^{1} = (wij)，因此 L^{1} = W。

该算法的核心如下面的伪代码所示。该伪代码程序可以在给定 W 和 L^{m-1} 的情况下，计算出 L^{m}。也就是说，该伪代码将最近计算出的最短路径扩展了一条边。

```
EXTEND_SHORTEST_PATHS(L, W)
1  n = L.rows
2  let L' = (l_ij') be a new n x n matrix
3  for i = 1 to n
4      for j = 1 to n 
5          l_ij' = inf
6          for k = 1 to n
7              l_ij' = min(l_ij', l_ik + w_kj)
8  return L'
```

该过程计算在算法结束时返回的矩阵 L' = (lij')。计算该矩阵的方式是对于所有的 i 和 j 来计算第 2 步给出的递归公式。使用 L 作为 L^{m-1}，而 L' 作为 L^{m}。该算法的运行时间为 `\Theta(n^3)`。

这与矩阵乘法的过程很类似，$ cij = \sum_{k=1}^{n} aik · bkj $

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

回到全源最短路径问题，通过对最短路径一条边一条边地扩展来计算最短路径权重，设 A·B 表示由算法 `EXTEND_SHORTEST_PATHS(A, B)` 所返回的矩阵“乘积”，可以计算出下面由 n-1 个矩阵所构成的矩阵序列：

- L^{1} = L^{0} · W = W
- L^{2} = L^{1} · W = W^2
- L^{3} = L^{2} · W = W^3
- ...
- L^{n-1} = L^{n-2} · W = W^{n-1}

前面已经阐述了，矩阵 L^{n-1} = W^{n-1} 包含的是最短路径权重，下面的伪代码程序可以在 `\Theta(n^4)` 运行时间内计算出该矩阵序列。

```
SLOW_ALL_PAIRS_SHORTEST_PATHS(W)
1  n = W.rows
2  L^{1} = W
3  for m = 2 to n-1
4      let L^{m} be a new n x n matrix
5      L^{m} = EXTEND_SHORTEST_PATHS(L^{m-1}, W)
6  return L^{n-1}
```

![all-pairs-sp-mm-1](/img/info-technology/algorithm/graph-theory/shortest-path/all-pairs-sp-mm-1.png)

### 改进算法的运行时间

注意到，目标并不是要计算出所有的 L^{m} 矩阵，感兴趣的仅仅是 L^{n-1}。而且根据前面的分析，在没有负权环的情况下，对所有的 m >= n-1，均有 L^{m} = L^{n-1}。正如传统的矩阵乘法是相关的，由 `EXTEND_SHORTEST_PATHS` 过程所定义的矩阵乘法也是相关的，因此可以利用**矩阵快速幂**的思想，设计如下的**重复平方**计算方法，记 $ log_{2} (n-1) $ 的上取整值为 t：

- L^{1} = W
- L^{2} = W^2 = W · W
- L^{4} = W^4 = W^2 · W^2
- L^{8} = W^8 = W^4 · W^4
- ...
- L^{2^t} = W^{2^t} = W^{2^{t-1}} · W^{2^{t-1}}

由于 2^t >= n-1，所以最后的乘积 L^{2^t} 等于 L^{n-1}。下面的伪代码过程使用重复平方技术来计算上述矩阵序列

```
FASTER_ALL_PAIRS_SHORTEST_PATHS(W)
1  n = W.rows
2  L^{1} = W
3  m = 1
4  while m < n-1
5      let L^{2m} be a new n x n matrix
6      L^{2m} = EXTEND_SHORTEST_PATHS(L^{m}, L^{m})
7      m = 2m
8  return L^{m}
```

`FASTER_ALL_PAIRS_SHORTEST_PATHS` 过程的总运行时间为 `\Theta(n^3 log n)`。由于该代码非常紧凑，也没有包含任何精巧的数据结构，因此隐藏在渐近符号中的常数因子较小，且算法实现难度很小。


## Python 代码范例

Python 环境：Python 3.7

### 全源最短路径和矩阵乘法

[GitHub Code Link](https://github.com/YuweiYin/Code_Play/blob/master/Algorithm-Essence/graph-theory/shortest-path/all-pairs-sp-mm.py)

## 参考资料

- Introduction to Algorithm (aka CLRS) Third Edition - Chapter 25
