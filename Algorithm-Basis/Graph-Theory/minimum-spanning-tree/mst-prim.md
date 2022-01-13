# Algorithm - Graph Theory - MST Prim

By [YuweiYin](https://yuweiyin.github.io/)

## 简介

最小生成树 (Minimum Spanning Tree, MST) - Prim 算法

如下伪代码是生成 MST 的一个通用模式：

```
GENERIC_MST(G, w)
1  A = \emptyset
2  while A does not form a spanning tree
3      find an edge(u, v) that is safe for A
4      A = A \cup {(u, v)}
5  return A
```

## Prim

在 Prim 算法中，集合 A 则是一棵树。每次加入到 A 中的安全边永远是**连接 A 和 A 之外某个结点**的边中 **权重最小的边**。

Prim 算法的工作原理与 Dijkstra 的最短路径算法相似。Prim 算法具有的一个性质是集合 A 中的**边总是构成一棵树**。这棵树从一个**任意的根结点** r 开始，一直长大到覆盖 V 中的所有结点时为止。算法每一步在连接集合 A 和 A 之外的结点的所有边中，选择一条**轻量级边**加入到 A 中。这条规则所加入的边都是对 A 安全的边（即：过程中始终保持 A 为某个最小生成树的子集）。当算法终止时，A 中的边形成一棵最小生成树。

本策略也属于贪心策略，因为每一步所加入的边都必须是使树的总权重增加量最小的边。

为了有效地实现 Prim 算法，需要**一种快速的方法来选择一条新的边**，以便加入到 由集合 A 中的边所构成的树中。在下面的伪代码中，无向连通图 G 和最小生成树的根结点 r 将作为算法的输入。在算法的执行过程中，所有不在树 A 中的结点都存放在一个基于 min_w 属性的**最小优先队列** Q 中。对于每个结点 v，属性 v.min_w 保存的是：连接 v 和树中结点的所有边中 最小边的权重。如果不存在这样的边，则设置 min_w 值为 inf 无穷。属性 v.p 表示结点 v 在树中的父结点，初始值为 nil 空。Prim 算法将 `GENERIC_MST` 中的集合 A 维持在 `A = {(v, v.p): v \in V - {r} - Q}` 的状态下。

当 Prim 算法终止时，最小优先队列 Q 将为空，而 G 的最小生成树 A 则是 `A = {(v, v.p): v \in V - {r}}`

```
MST_PRIM(G, w, r)
1  for each vertex u \in G.V
2      u.min_w = inf
3      u.p = nil
4  r.min_w = 0
5  Q = G.V
6  while Q is not empty
7      u = ExtractMin(Q)
8      for each v \in G.Adj[u]
9          if v \in Q and w(u, v) < v.min_w
10             v.p = u
11             v.min_w = w(u, v)
```

算法流程描述：

1. 在 1～4 行，将顶点集 V 中的每个结点的 min_w 值设置为 inf 无穷，父结点设置为 nil 空。而根结点 r 的 min_w 值设置为 0。
2. 在 5 行，创建最小优先队列 Q 并将 V 中全部结点入队。
3. 在 6～11 行的 while 循环中，只要最小优先队列 Q 不空，就继续处理
    1. 在 7 行，先取出 Q 中最小结点 u
    2. 在 8～11 行的 for 循环中，逐个考察结点 u 的邻接结点 v
    	- 在 9 行，判断此邻接结点 v 是否仍在 Q 中（不在 Q 中表示该结点已被加入到 MST 树中），并且边权 w(u, v) 更小
        - 在 10～11 行，如果第 9 行判断为真，则将 v 的父结点置为 u，并且更新 v 到 u 的最小边权（最小优先队列 Q 进行 `decrease_key` 操作）

![mst-prim-1](/img/info-technology/algorithm/graph-theory/minimum-spanning-tree/mst-prim-1.png)

![mst-prim-2](/img/info-technology/algorithm/graph-theory/minimum-spanning-tree/mst-prim-2.png)

Prim 算法的运行时间取决于最小优先队列 Q 的实现方式。如果用 [二叉堆](../../data_structure/heap-priority-queue) 实现 Q，则建堆的时间成本为 `O(|V|)`。while 循环总共执行 `|V|` 次，而每个 `ExtractMin` 操作需要 `O(log |V|)` 时间，因此 `ExtractMin` 操作的总时间为 `O(|V| log |V|)`。另外，由于所有邻接表的长度之和为 `2|E|`，所以算法第 8～11 行的 for 循环的总执行次数为 `O(|E|)`，如果在每个结点中维护一个标志位 标明自己是否在 Q 中，就可以让判断 `if v \in Q` 的时间降至 O(1)。算法第 11 行隐含了 `decrease_key` 操作，该操作在最小二叉堆上的执行时间成本为 `O(log |V|)`。

因此，如果用最小二叉堆实现 Q，那么 Prim 算法的总运行时间为 `O(|V| log |V| + |E| log |V|)`，这等于 `O(|E| log |V|)`。从渐近意义来说，它与 Kruskal 算法的运行时间相同。

如果用 [斐波那契堆](../../data-structure/fibonacci-heap) 来实现最小优先队列 Q，可以进一步改善 Prim 算法的渐近时间复杂度。如果斐波那契堆有 `|V|` 个元素，则 `ExtractMin` 操作的摊还时间为 `O(log |V|)`，而 `decrease_key` 操作的摊还时间仅为 O(1)。

因此，如果用斐波那契堆实现 Q，则 Prim 算法的运行时间将被改善到 `O(|E| + |V| log |V)`，更适合于稠密图。

## Python 代码范例

Python 环境：Python 3.7

### MST Prim

[GitHub Code Link](https://github.com/YuweiYin/Code_Play/blob/master/Algorithm-Essence/graph-theory/minimum-spanning-tree/mst-prim.py)

## 参考资料

- Introduction to Algorithm (aka CLRS) Third Edition - Chapter 23
