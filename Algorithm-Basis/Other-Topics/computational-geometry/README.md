# Algorithm - Computational Geometry

Algorithm - [YuweiYin](https://github.com/YuweiYin)

## 目录

- 计算几何学 Computational Geometry
    - (欧几里得空间)点和线段的构造
    - 基本几何运算: 对位四则运算、内积、叉积、距离、夹角
    - 判断线段相交
        - 给定两条线段，判断二者是否相交
        - 给定线段集合，判断其中是否存在相交线段
    - 凸包问题: 给定点集，寻找该点集的凸包 (convex hull)
        - Graham 扫描法
        - Jarvis 步进法
    - 最远/最近点对问题
        - 给定凸多边形的顶点集合，求出该点集的最远点对: 旋转卡壳算法 (Rotating Calipers)
        - 给定点集，求出该点集的最近点对

## 0. 计算几何学

计算几何学是计算机科学的一个分支，专门研究那些用来解决**几何问题**的算法。在现代工程与数学界，计算几何学在不同的领域里有着广泛的应用，包括计算机图形学、机器人学、VLSI 电路设计、计算机辅助设计、分子建模、冶金学、制造业、纺织品设计学、林学和统计学等。计算几何学问题的**输入**通常是**对几何对象集合的描述**，如点集、线段集，或者一个多边形中按顺/逆时针顺序排列的顶点集合。而问题的**输出**通常是回答**关于这些几何对象的查询**，例如，**直线是否相交**；或者是否为一个新的几何对象，例如，点集的**凸包问题** (convex hull，即最小封闭凸多边形)。

这里将研究**欧式二维空间**内(即平面上)的若干个计算几何算法。用点集 {p1, p2, p3, ...} 来表示每一个数输入对象，其中每个 pi = {xi, yi}, 且 $ xi, yi \in R $。例如，以顶点序列 `<p_0, p_1, p_2, ..., p_{n-1}>` 来表示一个含有 n 个顶点的多边形 P (polygon)，这些点以在 P 的边界上出现的顺序来排列。

计算几何学也可以应用到三维，甚至更高维度的空间上，不过这样的问题及其解决方案较难可视化。而且 即便是在二维空间上，也能够充分展现计算几何学的精妙之处。

## 1. 线段的性质

![computational-geometry-1](/img/info-technology/algorithm/other-topics/computational-geometry/computational-geometry-1.png)

![computational-geometry-2](/img/info-technology/algorithm/other-topics/computational-geometry/computational-geometry-2.png)

### 1.1. 叉积

![computational-geometry-3](/img/info-technology/algorithm/other-topics/computational-geometry/computational-geometry-3.png)

事实上，二维向量的**叉积**是一个三维的概念。根据“右手法则”，它是一个与 p1 和 p2 都垂直的向量，其量值为 `| x1 y2 - x2 y1 |`。在这里，不考虑叉积作为一个向量的方向性，而仅考虑其模长。

### 1.2. 确定连续线段是向左转还是向右转

![computational-geometry-4](/img/info-technology/algorithm/other-topics/computational-geometry/computational-geometry-4.png)

![computational-geometry-5](/img/info-technology/algorithm/other-topics/computational-geometry/computational-geometry-5.png)

### 1.3. 判定两条线段是否相交

为判定两条线段是否相交，需要检查每条线段是否**跨越**了包含另一条线段的直线。如果点 p1 位于某条直线的一边，而点 p2 位于该直线的另一边，则称线段 p1p2 跨越了这条直线。若 p1 或 p2 恰好落在直线上，则出现边界情况。两条线段相交当且仅当下面两个条件**至少成立一个**：

1. 对于这两条线段，其中的每条线段都**跨越**了包含另一条线段的直线。
2. 一条线段的某个端点落在另一条线段上。（边界情况）

下面的过程实现了上述思想。如果线段 p1p2 和 p3p4 相交，那么 `SEGMENTS_INTERSECT` 返回 True，否则返回 False。它调用了子过程 `DIRECTION`，利用上述的叉积方法计算出线段的相应方向；另外还调用了子过程 `ON_SEGMENT` 来判断一个与线段共线的点 是否位于这条线段上（包含线段的端点）。

```
SEGMENTS_INTERSECT(p1, p2, p3, p4)
1  d_1 = DIRECTION(p3, p4, p1)
2  d_2 = DIRECTION(p3, p4, p2)
3  d_3 = DIRECTION(p1, p2, p3)
4  d_4 = DIRECTION(p1, p2, p4)
5  if ((d_1 > 0 and d_2 < 0) or (d_1 < 0 and d_2 > 0) and
       (d_3 > 0 and d_4 < 0) or (d_3 < 0 and d_4 > 0))
6      return True
7  elif d_1 == 0 and ON_SEGMENT(p3, p4, p1)
8      return True
9  elif d_2 == 0 and ON_SEGMENT(p3, p4, p2)
10     return True
11 elif d_3 == 0 and ON_SEGMENT(p1, p2, p3)
12     return True
13 elif d_4 == 0 and ON_SEGMENT(p1, p2, p4)
14     return True
15 else
16     return False
```

```
DIRECTION(pi, pj, pk)
1  return (pk - pi) * (pj - pi)
```

```
ON_SEGMENT(pi, pj, pk)
1  if min(xi, xj) <= xk <= max(xi, xj) and
       min(yi, yj) <= yk <= max(yi, yj)
2      return True
3  else
4      return False
```

![computational-geometry-6](/img/info-technology/algorithm/other-topics/computational-geometry/computational-geometry-6.png)

![computational-geometry-7](/img/info-technology/algorithm/other-topics/computational-geometry/computational-geometry-7.png)

![computational-geometry-8](/img/info-technology/algorithm/other-topics/computational-geometry/computational-geometry-8.png)

### 1.4. 叉积的其它应用

当需要根据相对于给定原点的极角大小 对给定的点集进行排序时，可以使用叉积进行排序过程中的比较。另外，可以用红黑树来维护一个线段集合的垂直顺序。并不是显式地记录红黑树关键字值，而是通过计算叉积来确定 与同一个给定的垂直线相交的两条线段的相对位置。

![computational-geometry-9](/img/info-technology/algorithm/other-topics/computational-geometry/computational-geometry-9.png)

![computational-geometry-10](/img/info-technology/algorithm/other-topics/computational-geometry/computational-geometry-10.png)

## 2. 确定任意一对线段是否相交

![segment-intersect-1](/img/info-technology/algorithm/other-topics/computational-geometry/segment-intersect-1.png)

![segment-intersect-2](/img/info-technology/algorithm/other-topics/computational-geometry/segment-intersect-2.png)

### 2.1. 线段排序

![segment-intersect-3](/img/info-technology/algorithm/other-topics/computational-geometry/segment-intersect-3.png)

![segment-intersect-4](/img/info-technology/algorithm/other-topics/computational-geometry/segment-intersect-4.png)

### 2.2. 移动扫除线

典型的扫除 Sweeping 算法需要维护如下两组数据：

1. **扫除线状态** (sweep-line status) 给出了与扫除线相交的物体之间的关系。
2. **事件点调度** (event-point schedule) 是一个按 x 坐标从左到右排列的事件点序列。随着扫除线从左到右行进，每当遇到事件点的 x 坐标时，扫除都会暂停 并处理该事件点，然后重新开始扫除。扫除线状态仅在事件点处改变。

![segment-intersect-5](/img/info-technology/algorithm/other-topics/computational-geometry/segment-intersect-5.png)

### 2.3. 求线段交点的伪代码

下面的算法将一个由 n 条线段组成的集合 S 作为输入，如果 S 中存在一对线段相交，则返回 True，否则返回 False。完全前序 T 由一棵[红黑树](../../data-structure/red-black-tree)来维护。

```
ANY_SEGMENTS_INTERSECT(S)
1  T = \emptyset
2  sort the endpoints of the segments in S from left to right,
       breaking ties by putting left endpoints before right endpoints
       and breaking further ties by putting points with lower y-coordinates first
3  for each point p in the sorted list of endpoints
4      if p is the left endpoint of a segment s
5          INSERT(T, s)
6          if (ABOVE(T, s) exists and intersects s)
               or (BELOW(T, s) exists and intersects s)
7              return True
8      if p is the right endpoint of a segment s
9          if both ABOVE(T, s) and BELOW(T, s) exist
               and ABOVE(T, s) intersects BELOW(T, s)
10             return True
11         DELETE(T, s)
12 return False
```

下图 33-5 说明了此算法的执行过程。

1. 第 1 行，初始化完全前序(扩展红黑树的动态集合) T 为空
2. 第 2 行，将 2n 个线段端点 由左到右排序，并按照前述方法处理多个点 x 坐标值相同的情况，从而确定事件点的调度次序。
	- 执行第 2 行的一种方式是，在 (x, e, y) 上对端点按照字典序排序，其中 x 和 y 为通常对坐标，而 e = 0 表示左端点、e = 1 表示右端点。
3. 在第 3～11 行的 for 循环中，每一次迭代都处理一个事件点 p。
	- 如果事件点 p 是某线段 s 的左端点，那么第 5 行将 s 添加到完全前序 T 中。
		- 如果 s 与(由经过 p 的扫除线所定义的)完全前序中的(与之连续的)两条连续线段 中的任一条相交，则第 6～7 行返回 True，表示存在相交的线段。
		- 如果 p 位于另一条线段 s' 上，则出现边界情况。此时，仅需要将 s 和 s' 连续地放入 T 中。
	- 如果事件点 p 是某线段 s 的右端点，那么第 11 行会将 s 从完全前序 T 中删除。
		- 考虑经过 p 的扫除线所定义的完全前序，如果 s 旁边(ABOVE 或者 BELOW)的线段有相交，那么第 9～10 行返回 True。
		- 如果这些线段不相交，则第 11 行就将 s 从完全前序 T 中删除。
		- 只要第 10 行的 return 语句没有阻碍第 11 行的执行，那么当 s 被删除后，s 旁边的线段就会在完全前序中变为连续。
4. 最后，如果在处理完全部 2n 个事件点后没发现存在线段相交，第 12 行就返回 False。

![segment-intersect-6](/img/info-technology/algorithm/other-topics/computational-geometry/segment-intersect-6.png)

### 2.4. 求线段交点算法的正确性

![segment-intersect-7](/img/info-technology/algorithm/other-topics/computational-geometry/segment-intersect-7.png)

![segment-intersect-8](/img/info-technology/algorithm/other-topics/computational-geometry/segment-intersect-8.png)

![segment-intersect-9](/img/info-technology/algorithm/other-topics/computational-geometry/segment-intersect-9.png)

### 2.5. 求线段交点算法的运行时间

![segment-intersect-10](/img/info-technology/algorithm/other-topics/computational-geometry/segment-intersect-10.png)

### 2.6. 其它线段相交相关问题与性质

![segment-intersect-11](/img/info-technology/algorithm/other-topics/computational-geometry/segment-intersect-11.png)

![segment-intersect-12](/img/info-technology/algorithm/other-topics/computational-geometry/segment-intersect-12.png)

## 3. 寻找凸包

![convex-hull-1](/img/info-technology/algorithm/other-topics/computational-geometry/convex-hull-1.png)

![convex-hull-2](/img/info-technology/algorithm/other-topics/computational-geometry/convex-hull-2.png)

因此，通过在 O(n log n) 时间内计算出 n 个输入点的凸包，然后再找出得到的凸多边形中的最远顶点对，就可以在 O(n log n) 时间内 找出任意 n 个点组成的集合中**距离最远的点对**。

**旋转卡壳** (Rotating Calipers) 算法可以在 O(n) 时间内计算出给定凸多边形(或者凸包的顶点集)的最远点对。

```
begin
     p0:=pn;
     q:=NEXT[p];
     while (Area(p,NEXT[p],NEXT[q]) > Area(p,NEXT[p],q)) do
          q:=NEXT[q];
          q0:=q;
          while (q != p0) do
               begin
                    p:=NEXT[p];
                    Print(p,q);
                    while (Area(p,NEXT[p],NEXT[q]) > Area(p,NEXT[p],q) do
                         begin
                              q:=NEXT[q];
                              if ((p,q) != (q0,p0)) then Print(p,q)
                              else return
                         end;
                    if (Area(p,NEXT[p],NEXT[q]) = Area(p,NEXT[p],q)) then
                      if ((p,q) != (q0,p0)) then Print(p,NEXT[q])
                      else Print(NEXT[p],q)
               end
end
```

### 3.1. Graham 扫描法

![convex-hull-3](/img/info-technology/algorithm/other-topics/computational-geometry/convex-hull-3.png)

```
GRAHAM_SCAN(Q)
1  let p_0 be the point in Q with the minimum y-coordinate,
       or the leftmost such point in case of a tie
2  let <p_1, p_2, ..., p_m> be the remaining points in Q,
       sorted by polar angle in counterclockwise order around p_0
       (if more than one point has the same angle, remove all but
       	the one that is farthest from p_0)
3  if m < 2
4      return "convex hull is empty"
5  else
6      let S be an empty stack
7      PUSH(p_0, S)
8      PUSH(p_1, S)
9      PUSH(p_2, S)
10     for i = 3 to m
11         while the angle formed by points NEXT_TO_TOP(S), TOP(S), 
               and p_i makes a nonleft turn
12             POP(S)
13         PUSH(p_i, S)
14 return S
```

![convex-hull-4](/img/info-technology/algorithm/other-topics/computational-geometry/convex-hull-4.png)

![convex-hull-5](/img/info-technology/algorithm/other-topics/computational-geometry/convex-hull-5.png)

![convex-hull-6](/img/info-technology/algorithm/other-topics/computational-geometry/convex-hull-6.png)

![convex-hull-7](/img/info-technology/algorithm/other-topics/computational-geometry/convex-hull-7.png)

![convex-hull-8](/img/info-technology/algorithm/other-topics/computational-geometry/convex-hull-8.png)

### 3.2. Jarvis 步进法

![convex-hull-9](/img/info-technology/algorithm/other-topics/computational-geometry/convex-hull-9.png)

![convex-hull-10](/img/info-technology/algorithm/other-topics/computational-geometry/convex-hull-10.png)

![convex-hull-11](/img/info-technology/algorithm/other-topics/computational-geometry/convex-hull-11.png)

### 3.3. 其它点集凸包相关问题与性质

![convex-hull-12](/img/info-technology/algorithm/other-topics/computational-geometry/convex-hull-12.png)

## 4. 寻找最近点对

![nearest-pair-1](/img/info-technology/algorithm/other-topics/computational-geometry/nearest-pair-1.png)

![nearest-pair-2](/img/info-technology/algorithm/other-topics/computational-geometry/nearest-pair-2.png)

### 4.1. 分治算法

![nearest-pair-3](/img/info-technology/algorithm/other-topics/computational-geometry/nearest-pair-3.png)

![nearest-pair-4](/img/info-technology/algorithm/other-topics/computational-geometry/nearest-pair-4.png)

### 4.2. 算法的正确性

![nearest-pair-5](/img/info-technology/algorithm/other-topics/computational-geometry/nearest-pair-5.png)

![nearest-pair-6](/img/info-technology/algorithm/other-topics/computational-geometry/nearest-pair-6.png)

![nearest-pair-7](/img/info-technology/algorithm/other-topics/computational-geometry/nearest-pair-7.png)

### 4.3. 算法的实现与运行时间分析

![nearest-pair-8](/img/info-technology/algorithm/other-topics/computational-geometry/nearest-pair-8.png)

```
1  let Y_L[1..Y.length] and Y_R[1..Y.length] be new arrays
2  Y_L.length = Y_R.length = 0
3  for i = 1 to Y.length
4      if Y[i] \in P_L
5          Y_L.length = Y_L.length + 1
6          Y_L[Y_L.length] = Y[i]
7      else
8          Y_R.length = Y_R.length + 1
9          Y_R[Y_R.length] = Y[i]
```

![nearest-pair-9](/img/info-technology/algorithm/other-topics/computational-geometry/nearest-pair-9.png)

### 4.4. 其它最近点对相关问题与性质

![nearest-pair-10](/img/info-technology/algorithm/other-topics/computational-geometry/nearest-pair-10.png)

## 5. 其它计算几何学相关问题

### 5.1. 凸层

![cg-other-questions-1](/img/info-technology/algorithm/other-topics/computational-geometry/cg-other-questions-1.png)

### 5.2. 最大层

![cg-other-questions-2](/img/info-technology/algorithm/other-topics/computational-geometry/cg-other-questions-2.png)

### 5.3. 巨人和鬼问题

![cg-other-questions-3](/img/info-technology/algorithm/other-topics/computational-geometry/cg-other-questions-3.png)

### 5.4. 拾取棍子问题

![cg-other-questions-4](/img/info-technology/algorithm/other-topics/computational-geometry/cg-other-questions-4.png)

### 5.5. 稀疏包分布

![cg-other-questions-5](/img/info-technology/algorithm/other-topics/computational-geometry/cg-other-questions-5.png)

![cg-other-questions-6](/img/info-technology/algorithm/other-topics/computational-geometry/cg-other-questions-6.png)

## 代码范例

### Python

Python 环境：Python 3.7

[GitHub Code Link](https://github.com/YuweiYin/Code_Play/blob/master/Algorithm-Essence/other-topics/computational-geometry/computational-geometry.py)

## 参考资料

- Introduction to Algorithm (aka CLRS) Third Edition - Chapter 33
