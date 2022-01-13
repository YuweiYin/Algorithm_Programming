# Algorithm - Graph Theory - Dijkstra

By [YuweiYin](https://yuweiyin.github.io/)

## 简介

单源最短路径 Single Source Shortest Path

非负权值加权图的最短路径 - Dijkstra 算法

## Dijkstra 算法设计

Dijkstra 算法解决的是**带(边)权重的有向图**上的**单源最短路径**问题，该算法要求**所有边的权重都为非负值**。在下文中，均假定对于所有的边 (u, v) \in E，都有 w(u, v) >= 0。如果所采用的实现方式合适，Dijkstra 算法的渐近运行时间低于 [Bellman-Ford 算法]((./bellman-ford))。

Dijkstra 算法属于贪心算法，在运行过程中 维持的关键信息是**一组结点集合 S**。从源结点 s 到该集合中的每个结点之间的最短路径已被找到。算法重复从结点集 V-S 中选择(当前)**最短路径估计最小**的结点 u 加入到集合 S 中，然后对所有**从 u 发出的边**进行**松弛**操作。在下面的伪代码中，使用一个最小优先队列 Q 来保存结点集合，每个结点在 Q 中的关键值 key 为其 d 值。d 意为 distance，v.d 是源结点 s 到结点 v 的最短路径估计值。

使用如下运行时间为 `\Theta(|V|)` 的算法来对 最短路径估计 和 前驱结点 进行初始化：

```
INITIALIZE_SINGLE_SOURCE(G, s)
1  for each vertex v \in G.V
2      v.d = inf
3      v.p = nil
4  s.d = 0
```

在初始化操作结束后，对于所有的结点 v \in V，有 v.p = nil 和 s.d = 0，以及除 s 外的所有结点 v 有 v.d = inf 无穷（表示不可达）。

对一条边 (u, v) 的松弛过程为：首先测试 是否可以对从 s 到 v 的最短路径进行改善。测试的方法是：将 s->u 的最短路径距离 加上 u->v 的边权重值，前述二者的和 与当前得到的 s->v 的最短路径估计 进行比较，如果前者更小，则更新估计值 v.d 并修改前驱结点 v.p。

```
RELAX(u, v, w)
1  if u.d + w(u, v) < v.d
2      v.d = u.d + w(u, v)
3      v.p = u
```

执行 Dijkstra 算法求单源最短路径：

```
DIJKSTRA(G, w, s)
1  INITIALIZE_SINGLE_SOURCE(G, s)
2  S = \emptyset
3  Q = G.V
4  while Q is not empty
5      u = ExtractMin(Q)
6      S = S \cup {u}
7      for each vertex v \in G.Adj[u]
8          RELAX(u, v, w)
```

算法流程描述：

1. 在 1 行，对所有结点的 d 值和 p 值进行初始化。
2. 在 2 行，将集合 S 初始化为一个空集
3. 在 3 行，对最小优先队列 Q 进行初始化，并将 V 中所有结点入队
4. 在 4～8 行，只要 Q 不空，则继续 while 循环
    1. 在 5 行，取出 Q 中最小 d 值的结点 u
    2. 在 6 行，把结点 u 加入集合 S 中
    3. 在 7～8 行的 for 循环中，对于 u 的每个邻接结点 v，松弛边 (u, v)，并隐含着执行 Q 中元素的降 key 操作。

![dijkstra-1](/img/info-technology/algorithm/graph-theory/shortest-path/dijkstra-1.png)

## Dijkstra 算法的正确性

因为 Dijkstra 算法总是选择集合 V-S 中“最轻”或“最近”的结点来加入到集合 S 中，该算法使用的是[贪心策略](../../greedy-algorithm/)。下面的定理和推论指出，使用贪心策略的 Dijkstra 算法能够计算出最短路径。证明的关键在于：该算法在每次选择结点 u 加入到集合 S 后，有 u.d == d(s, u)，即达到了与 s 的最短距离。

《CLRS》**定理 24.6**（Dijkstra 算法的正确性）：Dijkstra 算法运行在带权重的有向图 G = (V, E) 时，如果所有权重为非负值，则在算法终止时，对于所有结点 u \in V，有 u.d == d(s, u)。

**证明**：使用此循环不变式：在算法第 4～8 行的 while 语句的每次循环开始前，对每个结点 v \in S，有 v.d == d(s, v)。

只需证明对于每个结点 u \in V，当结点 u 被加入到集合 S 时，有 u.d == d(u, v)，一旦证明这点，就可以利用**上界性质**来证明该循环不变式 在后续的所有时间内保持成立。

![dijkstra-2](/img/info-technology/algorithm/graph-theory/shortest-path/dijkstra-2.png)

![dijkstra-3](/img/info-technology/algorithm/graph-theory/shortest-path/dijkstra-3.png)

《CLRS》**推论 24.7**：如果在带权重的有向图 G = (V, E) 上运行 Dijkstra 算法，其中的权重皆为非负值，源结点为 s，则在算法终止时，前驱子图 Gp 是一棵根结点为 s 的最短路径树。

## Dijkstra 算法分析

Dijkstra 算法的运行速度取决于最小优先队列 Q 的具体实现。算法中用到了 `|V|` 次 `insert` 操作、`extract_min` 操作，以及至多 `|E|` 次的 `decrease_key` 操作。

如果用**数组**来维护最小优先队列 Q，先对 `|V|` 个结点编号，然后将 v.d 的值存放在数组的第 v 个记录里。这样每次 `insert` 和 `decrease_key` 操作的执行时间为 O(1)，但每次 `extract_min` 操作需要搜索整个数组，耗时为 `O(|V|)`。因此算法的总运行时间为 `O(|V|^2 + |E|) = O(|V|^2)`。

如果是稀疏图，特别地，如果 `|E| = o(|V|^2 / log |V|)`，则可以使用二叉堆来实现最小优先队列，从而改善算法的运行时间。在这种模式下，构建最小二叉堆的成本为 `O(|V|)`。每次 `decrease_key` 操作的执行时间为 `O(log |V|)`，而至多有 `|E|` 次此操作。因此算法的总运行时间为 `O((|V| + |E|) log |V|)`。若所有结点都可以从源结点到达，则该时间为 `O(|E| log |V|)`。若稀疏图 `|E| = o(|V|^2 / log |V|)`，则该时间成本相对于前面数组实现的 `O(|V|^2)` 有所改善。

但如果使用 [斐波那契堆](../../data-structure/fibonacci-heap) 来实现最小优先队列 Q，则可以将 Dijkstra 算法的运行时间改善到 `O(|E| + |V| log |V|)`。因为如果斐波那契堆有 `|V|` 个元素，则 `extract_min` 操作的摊还时间为 `O(log |V|)`，而 `decrease_key` 操作的摊还时间仅为 O(1)。在后面的算法具体实现中，即是采用斐波那契堆 Fibonacci Heap 来实现最小优先队列 Q。

从历史的角度上看，斐波那契堆提出的动机就是因为人们观察到 Dijkstra 算法调用的 `decrease_key` 操作通常较多，比 `extract_min` 操作更多。因此，任何能够将 `decrease_key` 操作的摊还代价降低到 `o(log |V|)` 而又不增加 `extract_min` 操作的摊还代价的方法 都将产生比二叉堆的渐进性能更优的实现。

Dijkstra 算法既类似于 [广度优先搜索](../graph-basis/graph-basis)，也有些类似于计算最小生成树 MST 的 [Prim 算法](../minimum-spanning-tree/mst-prim)（而且二者均适用 Fibonacci Heap 实现最小优先队列）。它与广度优先搜索的类似点在于 集合 S 对应的是广度优先搜索中的黑色结点集合：正如集合 S 中的结点的最短路径权重 已经被计算出来一样，在广度优先搜索中，黑色结点的正确的广度优先距离 也已经被计算出来了。Dijkstra 算法与 Prim 算法的相似之处是，两个算法都使用最小优先队列来寻找给定集合（即 Dijkstra 算法中的 S 集合与 Prim 算法中逐步增长的树）之外的“最轻”结点，将该结点加入到集合里，并对位于集合外面的结点的权重进行调整。

## Python 代码范例

Python 环境：Python 3.7

### Dijkstra (Fibonacci Heap)

[GitHub Code Link](https://github.com/YuweiYin/Code_Play/blob/master/Algorithm-Essence/graph-theory/shortest-path/dijkstra.py)

## 参考资料

- Introduction to Algorithm (aka CLRS) Third Edition - Chapter 24
