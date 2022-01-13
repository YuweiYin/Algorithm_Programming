# Algorithm - Graph Theory - DAG Shortest Path

By [YuweiYin](https://yuweiyin.github.io/)

## 简介

单源最短路径 Single Source Shortest Path

有向无环图 (Directed Acyclic Graph, DAG) 的单源最短路径

### 有向无环图 DAG 的单源最短路径

根据结点的**拓扑排序**次序来对带(边)权重的有向无环图 G = (V, E) 进行边的松弛操作，可以在 `\Theta(|V| + |E|)` 时间内计算出从单个源结点 s 到所有结点之间的最短路径。在有向无环图中，即便存在权重为负值的边，但由于没有权重为负值的环路（负权环），所以最短路径都是存在的。

算法先对有向无环图进行拓扑排序，下面的伪代码展示了如何对一个有向无环图进行拓扑排序：

```
TOPOLOGICAL_SORT(G)
1  call DFS(G) to compute finishing times v.f for each vertex v
2  as each vertex is finished, insert it into the front of a linked list
3  return the linked list of vertices
```

可以在 `\Theta(|V| + |E|)` 的时间内完成拓扑排序。因为 DFS 需要 `\Theta(|V| + |E|)` 的运行时间。将结点插入到链表最前端所需的时间为 O(1)，而一共只有 `|V|` 个结点需要插入。

拓扑排序之后，可以确定结点之间的一个线性次序。如果 DAG 包含从结点 u 到结点 v 的一条路径，则 u 在拓扑排序的次序中位于 v 的前面。只需按照拓扑排序的次序对结点进行一遍处理即可。每次对一个结点进行处理时，从该结点发出的所有边进行松弛操作。

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

执行 `DAG_SHORTEST_PATHS` 过程求单源最短路径：

```
DAG_SHORTEST_PATHS(G, w, s)
1  topologically sort the vertices of G
2  INITIALIZE_SINGLE_SOURCE(G, s)
3  for each vertex u, taken in topologically sorted order
4      for each vertex v \in G.Adj[u]
5          RELAX(u, v, w)
```

算法流程描述：

1. 在 1 行，进行拓扑排序（一次 DFS）。
2. 在 2 行，对所有结点的 d 值和 p 值进行初始化。
3. 在 3～5 行，外层循环对每个结点 u，内层循环对 u 的每个邻接结点 v 进行松弛操作。

---

第 1 行 拓扑排序的时间为 `\Theta(|V| + |E|)`，第 2 行初始化过程的时间为 `\Theta(|V|)`。3～5 行的外循环执行了 `|V|` 次，内外循环合起来 恰好对每条边进行了一次松弛操作，（利用聚合分析）内循环每次对运行时间为 `\Theta(1)`。因此本算法的总运行时间为 `\Theta(|V| + |E|)`。对于以邻接表表示的图来说，这个时间为线性级。

![dag-shortest-path-1](/img/info-technology/algorithm/graph-theory/shortest-path/dag-shortest-path-1.png)

下面的定理将证明 `DAG_SHORTEST_PATHS` 过程能够正确计算出 从源结点 s 出发的所有的最短路径。

《CLRS》**定理 24.5**：如果带(边)权重的有向无环图 G = (V, E) 有一个源结点 s，则在算法 `DAG_SHORTEST_PATHS` 终止时，对于所有的结点 v \in V，有 v.d == d(s, v)，且前驱子图 Gp 是一棵最短路径树。

![dag-shortest-path-2](/img/info-technology/algorithm/graph-theory/shortest-path/dag-shortest-path-2.png)

---

算法 `DAG_SHORTEST_PATHS` 的一个有趣的应用是在 **PERT (Program Evaluation and Review Technique) 图** 的分析中进行关键路径的判断。PERT 图是一个有向无环图，在这种图中，每条边代表需要进行的工作，边上的权重代表执行该工作所需要的时间。如果边 (u, v) 进入结点 v，边 (v, x) 离开结点 v（从结点 v 发出），则工作 (u, v) 必须在工作 (v, x) 前完成。PERT 图中的一条路径代表的是一个工作执行序列。

**关键路径**则是该有向无环图中一条(加权)**最长**的路径，该条路径代表执行任何工作序列所需要的最长时间。因此，关键路径上的权重提供的是执行所有工作所需时间的下界。可以使用如下两种办法中的任意一种来找到 PERT 图中的关键路径：

- 将所有权重变为负数，然后运行 `DAG_SHORTEST_PATHS`。
- 运行 `DAG_SHORTEST_PATHS`，但进行如下修改：
    - 在 `INITIALIZE_SINGLE_SOURCE` 的第 2 行将 inf 替换为 -inf
    - 在 `RELAX` 过程中将 `<` 替换为 `>`

## Python 代码范例

Python 环境：Python 3.7

### DAG Shortest Path

[GitHub Code Link](https://github.com/YuweiYin/Code_Play/blob/master/Algorithm-Essence/graph-theory/shortest-path/dag-shortest-path.py)

## 参考资料

- Introduction to Algorithm (aka CLRS) Third Edition - Chapter 24
