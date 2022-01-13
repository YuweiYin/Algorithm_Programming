# Algorithm - Graph Theory - MST Kruskal

By [YuweiYin](https://yuweiyin.github.io/)

## 简介

最小生成树 (Minimum Spanning Tree, MST) - Kruskal 算法

如下伪代码是生成 MST 的一个通用模式：

```
GENERIC_MST(G, w)
1  A = \emptyset
2  while A does not form a spanning tree
3      find an edge(u, v) that is safe for A
4      A = A \cup {(u, v)}
5  return A
```

## Kruskal

在 Kruskal 算法中，集合 A 是一个森林，其结点就是给定图的结点。每个加入到集合 A 中的安全边 永远是**权重最小**的**连接两个不同分量的边**。

Kruskal 算法找到安全边的策略是：在所有连接森林中两棵不同树的边里面，找到权重最小的边 (u, v)。设 C1 和 C2 为边 (u, v) 所连接的两棵树，由于此边一定是连接 C1 和其它某棵树的一条轻量级边，(u, v) 是 C1 的一条安全边。很显然，Kruskal 算法属于贪心算法。

Kruskal 算法的实现与计算连通分量的算法类似，需要使用一个不相交集合数据结构（如[并查集](../../data-structure/union-find)）来维护几个互不相交的顶点集合，每个集合代表当前森林中的一棵树。`FIND_SET(u)` 操作用于返回包含元素 u 的集合的代表元素。可以通过测试 `FIND_SET(u)` 是否等于 `FIND_SET(v)` 来判断顶点 u 和顶点 v 是否属于同一个集合(同一棵树)。`UNION(u, v)` 过程用于将两个集合合并。

```
MST_KRUSKAL(G, w)
1  A = \emptyset
2  for each vertex v \in G.V
3      MAKE_SET(v)
4  sort the edges of G.E into nondecreasing order by weight
5  for each edge (u, v) \in G.E, taken in nondecreasing order by weight
6      if FIND_SET(u) != FIND_SET(v)
7          A = A \cup {(u, v)}
8          UNION(u, v)
9  return A
```

算法流程描述：

1. 在 1～3 行，将集合 A 初始化为一个空集合，并创建 `|V|` 棵树（不相交集合），每棵树仅包含一个结点。
2. 在 4 行，把边集合 E 中的所有边都按照权重的**非降序**排序。
3. 在 5～8 行的 for 循环中，按权重非降序地选取边 (u, v)
    1. 在 6 行，检查边 (u, v) 的两个端点 u 和 v 是否属于同一个集合(同一棵树)，如果不属于同一集合，则 (u, v) 是安全边；如果二者属于同一个集合，则不能加入此边，否则会形成环路，不符合树的定义。
    2. 在 7 行，将安全边 (u, v) 加入集合 A
    3. 在 8 行，把安全边的两个端点合并到同一个集合(同一棵树)中
4. 在 9 行，返回集合(树) A

对于图 G = (V, E)，Kruskal 算法的运行时间依赖于不相交集合数据结构的实现方式。如果使用增加了按秩合并和路径压缩功能的 [并查集](../../data-structure/union-find)，则可以达到渐近最快。在此实现模式下，算法第 1 行初始化时间为 O(1)，第 2～3 行进行 `|V|` 次 `MAKE_SET` 操作创建不相交集合，第 4 行对边进行排序的时间为 `O(|E| log |E|)`，而算法第 5～8 行的 for 循环执行 `O(|E|)` 个 `FIND_SET` 和 `UNION` 操作，记不相交集合的运行时间为 `a(|V|)`，则整个算法的总运行时间为 `O((|V|+|E|) a(|V|))`。这里 a 是增长速度极慢的 Ackermann 函数。

由于假定图 G 是连通的，因此有 `|E| >= |V| - 1`，所以不相交集合操作的时间代价为 `O(|E| a(|V|))`。而且，由于 `a(|V|) = O(log |V|) = O(log |E|)`，所以 Kruskal 算法的总运行时间可以表达为 `O(|E| log |E|)`。另外，又由于 `|E| < |V|^2`，则有 `log |E| = O(log |V|)`，因此可以将 Kruskal 算法的总运行时间表达为 `O(|E| log |V|)`。

![mst-kruskal-1](/img/info-technology/algorithm/graph-theory/minimum-spanning-tree/mst-kruskal-1.png)

![mst-kruskal-2](/img/info-technology/algorithm/graph-theory/minimum-spanning-tree/mst-kruskal-2.png)

## Python 代码范例

Python 环境：Python 3.7

### MST Kruskal

[GitHub Code Link](https://github.com/YuweiYin/Code_Play/blob/master/Algorithm-Essence/graph-theory/minimum-spanning-tree/mst-kruskal.py)

## 参考资料

- Introduction to Algorithm (aka CLRS) Third Edition - Chapter 23
