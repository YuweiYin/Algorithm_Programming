# Algorithm - Graph Theory - Johnson

By [YuweiYin](https://yuweiyin.github.io/)

## 简介

全源最短路径 All Pairs Shortest Path

用于稀疏图的 Johnson 算法

基于 [Dijkstra](./dijkstra) 和 [Bellman-Ford](./bellman-ford) 算法

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

## Johnson 算法

Johnson 算法可以在 `O(|V|^2 log |V| + |V|·|E|)` 的时间内找到所有结点对之间的最短路径。对于稀疏图来说，Johnson 算法的渐进性能优于 [重复平方法](./all-pairs-sp-mm) 和 [Floyd-Warshall](./floyd-warshall) 算法。

Johnson 算法会将 [Dijkstra](./dijkstra) 和 [Bellman-Ford](./bellman-ford) 这两个单源最短路径算法作为子过程。Johnson 算法要么返回一个包含所有结点对的最短路径权重的矩阵，要么报告图中包含一个负权环。

Johnson 算法使用的技术被称为 **重新赋予权重**，此技术的工作原理如下：

如果图 G = (V, E) 中所有的边权重 w 皆为非负值，那么可以对每个结点运行一次 Dijkstra 算法来找到所有结点对的最短路径，另外如果在 Dijkstra 算法中用 [斐波那契堆](../../data-structure/fibonacci-heap) 实现最小优先队列 Q，则总运行时间为 `O(|V|^2 log |V| + |V|·|E|)`，这在稀疏图的情况下优于 Floyd-Warshall 算法的 `\Theta(|V|^3)`。

如果图 G = (V, E) 中包含权重为负值的边，但没有负权环，那么只要先对图 G 使用 **重新赋予权重**技术进行预处理，并在 `O(|V|·|E|)`的时间内 计算出一组新的非负权重值，然后调用 `|V|` 次 Dijkstra 算法即可。

新赋予的权重 w' 必须满足如下两个重要的性质：

1. 对于所有结点对 u, v \in V，一条路径 p 是在使用权重函数 w 时从结点 u 到结点 v 的一条最短路径，当且仅当 p 是在使用权重函数 w' 时从 u 到 v 的一条最短路径。
2. 对于所有的边 (u, v)，新权重 w'(u, v) 为非负值。

### 重新赋予权重-维持最短路径

下面的引理描述的是 可以很容易地对边的权重进行重新赋值，来满足新权重函数 w' 需要的两个性质。使用 d 表示从权重函数 w 所导出的最短路径权重，而用 d' 表示从权重函数 w' 所导出的最短路径权重。

《CLRS》**引理 25.1**（重新赋予权重并不改变最短路径）：给定带(边)权重的有向图 G = (V, E)，其权重函数为 w: E -> R，设 h: V -> R 为任意函数，该函数将结点映射到实数上。对于每条边 (u, v) \in E，定义 w'(u, v) = w(u, v) + h(u) - h(v)。

设 `p = <v0, v1, ..., vk>` 为从结点 v0 到结点 vk 的任意一条路径，那么 p 是在使用权重函数 w 时 v0->vk 的一条最短路径，当且仅当 p 是在使用新权重函数 w' 时 v0->vk 的一条最短路径。即 w(p) = d(v0, vk) iff. w'(p) = d'(v0, vk)。而且，图 G 在使用权重函数 w 时不包负权环，当且仅当 p 在使用新权重函数 w' 也不包括权重为负值的环路。

### 重新赋予权重-生成非负权重

接下来确保第二个性质保持成立，即对于所有的边 (u, v) \in E，w'(u, v) 为非负值。给定带权重的有向图 G = (V, E)，其权重函数为 w: E -> R。构造一个新图 G' = (V', E')，这里 V' = V \cup {s}，s \notin V，E' = E \cup {(s, v): v \in V}。

即 s 是一个**新增的源结点**，它到其它所有结点均**单向可达**（且**边权均为 0**），其它结点均不到达 s。这类似于使用 Bellman-Ford 算法求解**差分约束系统**的做法。

![johnson-1](/img/info-technology/algorithm/graph-theory/shortest-path/johnson-1.png)

假定图 G 和图 G' 都不包含负权环。定义 对于所有的 v \in V'，h(v) = d(s, v)。根据三角不等式，对于所有的边 (u, v) \in E'，有 h(v) <= h(u) + w(u, v)。因此，依据引理 25.1 的式子来定义新的权重函数 w'，则有 w'(u, v) = w(u, v) + h(u) - h(v) >= 0，于是满足了第二条性质。图 25-6(b) 描述的是对图 25-6(a) 进行权重重新赋值后的图 G'。

![johnson-2](/img/info-technology/algorithm/graph-theory/shortest-path/johnson-2.png)

### 使用 Johnson 算法计算全源最短路径

```
JOHNSON(G, w)
1  compute G', where G'.V = G.V \cup {s}
       G'.E = G.E \cup {(s, v): v \in G.V}, and
       w(s, v) = 0 for all v \in G.V
2  if Bellman-Ford(G', w, s) == False
3      print "The input graph contains a negative-weight cycle!"
4  else
5      for each vertex v \in G'.V
6          set h(v) to the value of d(s, v)
               computed by the Bellman-Ford algorithm
7      for each edge(u, v) \in G'.E
8          w'(u, v) = w(u, v) + h(u) - h(v)
9      let D = (d_uv) be a new n x n matrix
10     for each vertex u \in G.V
11         run Dijkstra(G, w', u) to compute d'(u, v) for all v \in G.V
12         for each vertex v \in G.V
13             d_uv = d'(u, v) + h(v) - h(u)
14     return D
```

算法流程描述：

1. 在 1 行，新增源结点 s，生成图 G'。
2. 在 2 行，在图 G' 上运行 Bellman-Ford 算法，使用原始权重函数 w，计算从源结点 s 出发的单源最短路径。
3. 在 3 行，如果 Bellman-Ford 算法返回 False，表示图 G 含负权环。
4. 在 5～6 行，对 V 中每个结点 v，将 h(v) 的值设置为由 Bellman-Ford 算法所计算出来的最短路径权重 d(s, v)。
5. 在 7～8 行，对 E 中每条边 (u, v)，重新计算新的权重值 w'(u, v)
6. 在 9 行，设置权重矩阵 D
7. 在 10～13 行，对 V 中每个结点 u
    - 以 u 为起点、w' 为新的权重函数来运行 Dijkstra 算法。
    - 每次 Dijkstra 算法结束后，对 V 中每个结点 v，**还原**出最优路径值，并保存在 `d_uv` 表项中。
8. 在 14 行，返回最终计算好的全源最短路径权重矩阵。

## Python 代码范例

Python 环境：Python 3.7

### Johnson 全源最短路径算法

[GitHub Code Link](https://github.com/YuweiYin/Code_Play/blob/master/Algorithm-Essence/graph-theory/shortest-path/johnson.py)

## 参考资料

- Introduction to Algorithm (aka CLRS) Third Edition - Chapter 25
