# Algorithm - Graph Theory - Bellman Ford

By [YuweiYin](https://yuweiyin.github.io/)

## 简介

单源最短路径 Single Source Shortest Path

含负权值加权图的最短路径 - Bellman-Ford 算法

## Bellman-Ford 算法设计

Bellman-Ford 算法解决的是一般情况下的单元最短路径问题，边的权重值可以为负值。

给定带(边)权重的有向图 G = (V, E) 和权重函数 w: E -> R，Bellman-Ford 算法**返回一个布尔值**，以表明**是否存在**一个从源结点 s 可以到达的 权重为负值的环路（**负权环**）。如果不存在负权环，则 BF 算法会给出最短路径和它们的权重。

Bellman-Ford 算法通过对边进行松弛操作 来渐近地降低源结点 s 到每个结点 v 的最短路径的估计值 v.d，直到该估计值 减小到实际的最短路径权重 d(s, v) 为止。该算法 True 布尔值当且仅当 输入图不包含从源结点 s 可达的负权环。

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

执行 Bellman-Ford 算法求单源最短路径：

```
BELLMAN_FORD(G, w, s)
1  INITIALIZE_SINGLE_SOURCE(G, s)
2  for i = 1 to |G.V|-1
3      for each edge(u, v) \in G.E
4          RELAX(u, v, w)
5  for each edge(u, v) \in G.E
6      if u.d + w(u, v) < v.d
7          return False
8  return True
```

算法流程描述：

1. 在 1 行，对所有结点的 d 值和 p 值进行初始化。
2. 在 2～4 行，对图的每条边进行 `|V| - 1` 次松弛操作，完成各结点的 d、p 值计算。
3. 在 5～7 行的 for 循环中，检查图中是否存在负权环，如果有则返回 False。
4. 在 8 行，前面已经检测不到负权环了，所以返回 True 表示没有负权环

`BELLMAN_FORD(G, w, s)` 第 1 行的初始化操作所需时间为 `\Theta(|V|)`，第 2～4 行循环的运行时间为 `\Theta(|E|)`，且一共要进行 `|V| - 1` 次循环，第 5～7 行的 for 循环所需时间为 `O(|E|)`。因此，Bellman-Ford 算法的总运行时间为 `O(|V|·|E|)`。

![bellman-ford-1](/img/info-technology/algorithm/graph-theory/shortest-path/bellman-ford-1.png)

要证明 Bellman-Ford 算法的正确性，首先证明在没有负权环的情况下，该算法能够正确计算出从源结点 s 可达的所有结点之间的最短路径权重。

《CLRS》**引理 24.2**：设 G = (V, E) 为一个带(边)权重的源结点为 s 的有向图，其权重函数为 w: E -> R。假定图 G 不包含从源结点 s 可以到达的权重为负值的环路（负权环）。那么在 Bellman-Ford 算法的第 2～4 行的 for 循环执行了 `|V| - 1` 次之后，对于所有从源结点 s 可以到达的结点 v，有 v.d = d(s, v)。

《CLRS》**推论 24.3**：设 G = (V, E) 为一个带(边)权重的源结点为 s 的有向图，其权重函数为 w: E -> R。假定图 G 不包含从源结点 s 可以到达的权重为负值的环路（负权环）。则对于所有结点 v \in V，存在一条从源结点 s 到结点 v 的路径 当且仅当 Bellman-Ford 算法终止时有 v.d < inf 无穷。

《CLRS》**定理 24.4**（Bellman-Ford 算法的正确性）：设 Bellman-Ford 算法运行在一带(边)权重的源结点为 s 的有向图 G = (V, E) 上，该图的权重函数为 w: E -> R。如果图 G 不包含从源结点 s 可以到达的权重为负值的环路（负权环），则算法将返回 True 值。且对于所有结点 v \in V，前驱子图 Gp 是一棵根结点为 s 的最短路径树。如果图 G 包含一条从源结点 s 可以到达的负权环，则算法将返回 False 值。

![bellman-ford-2](/img/info-technology/algorithm/graph-theory/shortest-path/bellman-ford-2.png)

![bellman-ford-3](/img/info-technology/algorithm/graph-theory/shortest-path/bellman-ford-3.png)

## 线性规划 & 差分约束系统

**线性规划**问题，是希望在满足**一组线性不等式的约束条件**下**优化一个线性函数**。在线性规划中存在一种**特例**，可以被**规约到单源最短路径问题**，并用 Bellman-Ford 算法求解。

### 线性规划

在通用的线性规划问题中，通常给定一个 m x n 的矩阵 A、一个 m 维的向量 b 和一个 n 维向量 c。目标是找到一个 n 维向量 x，使得在由不等式组 Ax <= b 所给定的 m 个约束条件下 优化目标函数 $ \sum_{i=1}^{n} c_{i} x_{i} $ 的值。这里的优化往往是求目标函数的最大值。

常用于解决通用线性规划问题的**单纯形算法**并不总是能够在多项式时间内完成，但却存在其它的多项式运行时间的线性规划算法。线性规划问题的设置具有许多实际价值，包括但不限于如下两点：

- 首先，如果知道可以将某个给定问题 看作一个多项式规模的线性规划问题，则可以立即获得一个多项式时间的算法解。
- 其次，对于线性规划的许多特殊问题，存在着更快的算法。
    - 例如，单源单目的地最短路径问题 和 最大流问题 都是线性规划问题的特例。

有时候并不关注最优化目标函数，而仅仅是希望找到一个**可行解**，即找到任何满足不等式组 Ax <= b 的向量 x，或者判断不存在可行解。下文关注这样一个**可行性问题**。

### 差分约束系统

在一个**差分约束系统** (System of Difference Constraints) 中，**线性规划矩阵** A 的每一行包括一个 1 和一个 -1，其它所有项皆为 0。因此，由不等式组 Ax <= b 所给出的约束条件 变为 m 个涉及 n 个变量的**差额限制条件**，其中的每个约束条件是如下所示的简单线性不等式：xj - xi <= bk。这里 1 <= i, j <= n, i != j, 并且 1 <= k <= m。

![difference-constraints-1](/img/info-technology/algorithm/graph-theory/shortest-path/difference-constraints-1.png)

这个问题的一个可能答案是 x = (-5, -3, 0, -1, -4)，可以对每个不等式进行验证，确认该向量确实是一个满足约束条件的可行解。事实上 这个问题的答案有多个，比如另一个可行解是 x' = (0, 2, 5, 4, 1)。这两个答案 x 和 x' 之间存在着关联关系：向量 x' 中每个元素比向量 x 中的对应元素的取值大 5。这种关系并不是巧合。

《CLRS》**引理 24.8**：设向量 x = (x1, x2, ..., xn) 为差分约束系统 Ax <= b 的一个解，设 d 为任意常数，则 x' = x + d = (x1+d, x2+d, ..., xn+d) 也是该差分约束系统的一个解。

证明：对于每个 xj 和 xi，有 (xj + d) - (xi + d) = xj - xi。因此，若向量 x 满足不等式组 Ax <= b，那么向量 x + d 也满足这个条件。

差分约束系统在许多不同的应用中都会出现。例如，未知变量 xi 可能代表的是事件发生的时间。每个约束条件给出的是 在两个事件之间必须间隔的 最短时间或最长时间。也许，这些事件代表的是产品装配过程中必须执行的任务。如果在时刻 x1 使用一种需要两个小时才能风干的粘贴剂材料，则需要等到该粘贴剂干了之后才能在时刻 x2 安装部件，这样，就有约束条件 x2 >= x1 + 2，也即 x1 - x2 <= -2。

### 约束图

可以从图论的观点来理解差分约束系统。在一个 Ax <= b 的差分约束系统中，将 m x n 的线性规划矩阵 A 看作是一张由 n 个结点和 m 条边构成的图的**邻接矩阵的转置**。对于 i = 1, 2, ..., n，图中的每个结点 vi 对应 n 个未知变量 xi 中的一个，图中的每条有向边则对应 m 个不等式中的一个。

形式化地说，给定差分约束系统 Ax <= b，其对应的**约束图**是一个带权重的有向图 G = (V, E)，其中：

- V = {v0, v1, ..., vn}
- E = {(vi, vj): xj - xi <= bk 是一个约束条件} \cup {(v0, v1), (v0, v2), (v0, v3), ..., (v0, vn)}

约束图包含一个**额外的结点** v0，从它出发到 vi (1 <= i <= n) 均单向可达，且 vi 均不能到达 v0，可将 v0 视作**源点**。

在图中，对 1 <= i <= n，如果 xj - xi <= bk 是一个差分约束条件，则边 (vi, vj) 的权重为 w(vi, vj) = bk。另外，所有与源点 v0 关联的边的权重均为 0。

![difference-constraints-2](/img/info-technology/algorithm/graph-theory/shortest-path/difference-constraints-2.png)

### 求解差分约束系统

定理 24.9 表明，将差分约束系统转化为约束图后，可以使用 Bellman-Ford 算法求解从源结点 v0 出发、到其它所有结点的单源最短路径。

- 如果 Bellman-Ford 算法返回 True 值，则最短路径权重给出的是该系统的一个可行解 x。
    - 另外，根据引理 24.8，对于任意常数 d 而言，x + d 也是一个可行解。
- 如果 Bellman-Ford 算法返回 False 值，则此差分约束系统没有可行解。

对于一个有 n 个未知变量 xi 和 m 个约束条件的差分约束系统，其生成的约束图有 n+1 个结点和 n+m 条边。因此，使用 Bellman-Ford 算法，可以在 O((n+1)(n+m))，即 O(n^2 + nm) 时间内求解该系统。

另外，可以对 Bellman-Ford 算法稍作修改，使该算法能够在 O(nm) 时间内解决 n 个未知变量和 m 个约束条件所构成的差分约束系统问题。修改的关键在于：第一个循环中，不对与源结点 v0 关联的那 n 条边进行松弛操作。原因：源结点 v0 的 d 值为 0，从 v0 出发的边权均为 0，且没有以 v0 为终点的边，因此与源结点 v0 关联的那 n 条边的权重值始终为 0 不会变化，所以无需进行松弛操作。

## Python 代码范例

Python 环境：Python 3.7

### Bellman-Ford

[GitHub Code Link](https://github.com/YuweiYin/Code_Play/blob/master/Algorithm-Essence/graph-theory/shortest-path/bellman-ford.py)

## 参考资料

- Introduction to Algorithm (aka CLRS) Third Edition - Chapter 24
