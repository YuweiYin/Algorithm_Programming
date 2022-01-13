# Algorithm - Dynamic Programming - Activity Select

By [YuweiYin](https://yuweiyin.github.io/)

## 简介

活动选择问题 Activity Select

### 活动选择问题引入

问题简述：在一些调度**竞争共享资源**的多个活动中，选出一个**最大**的**互相兼容**（资源上不冲突）的活动集合。

假定有一个 n 个活动 (activity) 的集合 S = {a1, a2, ..., an}，这些活动使用同一个资源（例如某一个教室，也例如操作系统的资源临界区），而这个资源在某个时刻只能供一个活动使用。每个活动 ai 都有一个开始时间 si 和一个结束时间 fi，其中 0 <= si < fi < inf。

如果某活动 ai 被选中，那么它在半开半闭的时间区间 `[si, fi)` 期间占用资源。如果两个活动 ai 和 aj 满足 `[si, fi)` 和 `[sj, fj)` 不重叠，则称这两个活动是**兼容**的。也即：若 `si >= fj` 或 `sj >= fi`，则活动 ai 和 aj 兼容。在**活动选择问题**中，目标是选出一个**最大的兼容活动集**。

假定活动已按结束时间的单调递增顺序排序：`f1 <= f2 <= ... <= fn`，例如如下的活动集合 S：

i | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11
:-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-:
s | 1 | 3 | 0 | 5 | 3 | 5 | 6 | 8 | 8 | 2 | 12
fi | 4 | 5 | 6 | 7 | 9 | 9 | 10 | 11 | 12 | 14 | 16

对此例而言，子集 {a3, a9, a11} 由互相兼容的活动组成，但它并不是一个最大集。最大兼容活动子集是 {a1, a4, a8, a11} 和 {a2, a4, a9, a11}。可见此任务的“最大”实则为“极大”之意，只要某个子集的兼容活动数量 无出其右，则它就是**一个**“最大”兼容活动子集。

## 解决方案

### 动态规划解决方案

这里先按照[动态规划](../dynamic-programming)的解题思路来处理，以对比动态规划与贪心算法的异同。

活动选择问题具有**最优子结构性质**。令 Sij 表示在活动 ai 结束之后开始、且在活动 aj 开始之前结束的那些活动的集合。假定 Aij 是 Sij 的一个最大兼容活动子集，且 Aij 中包含活动 ak。那么求 Sij 最优解的问题 就可以分解为两个子问题：求 Sik 和 Skj 的最优解。假定子问题的最优解为 Aik 和 Akj，易知 Aij = Aik 并 {ak} 并 Akj。

可以用“剪切-粘贴法”证明 Sij 的最优解 Aij 必然包含两个子问题 Sik 和 Skj 的最优解。否则，如果可以找到 Skj 的一个兼容活动子集 Akj' 满足 `|Akj'| > |Akj|`，那么可以将 Akj' 而不是 Akj 作为 Sij 的最优解的一部分，从而构造出的新最优解 Aij' 比假设中的最优解 Aij 更大，矛盾。（对子问题 Sik 证明类似）

刻画出活动选择问题的最优子结构，意味着可以考虑用动态规划的方法求解活动选择问题。当然，对于应用动态规划而言，还要注意是否有**重叠子问题性质**，这里的重叠子问题是很明显的：前述叙述里的 k 是无法提前预知的，所以要从 i 到 j 考虑每个 ak 活动的划分，不同的划分的子划分(子子问题)就会出现相同的问题。

如果用 c[i, j] 表示集合 Sij 的最优值（最大兼容活动子集的秩），则有如下递归式（用）：

- 若 Sij == $ \emptyset $，则 `c[i, j] = 0`
- 若 Sij != $ \emptyset $，则 `c[i, j] = max{ c[j, k] + c[k, j] + 1 }` $ for ak \in Sij $

接下来便可以设计一个带备忘机制的自顶向下递归算法，或者自底向上的循环算法。但活动选择问题本身还有一个重要的性质没被用到，此性质使得下文的贪心算法得以获得最优解。

### 贪心选择

加入无需求解所有子问题就能选择出一个活动加入到最优解，那么动态规划考察所有子问题就显得多余了。实际上，对于活动选择问题，只需考虑当前最优的选择——贪心选择 即可。

对于活动选择问题，贪心选择是当前可选的活动中，既能与当前最优解兼容、又最早结束的活动。如果某活动时最早结束的，那么选取它之后，剩下的资源量就是最多的，就更有可能选出更多兼容的活动。

- 对同一个问题，可能有不同的、但是都能获得最优解的贪心策略。比如此问题中可以按开始时间降序排列，然后贪心选择最晚开始的活动。
- 但是对于活动选择问题，贪心策略不一定都能获得最优解。例如，对于此问题，贪心选择活动持续时间最短、或者选择最早开始的活动 这些贪心策略均不能获得最优解。

前面已假定活动已按结束时间的单调递增顺序排序：`f1 <= f2 <= ... <= fn`，因此首次的贪心选择就是 a1。令集合 $ Sk = {ai \in S: si >= fk} $ 为在 ak 结束后才开始的活动集合。当做出贪心选择，选择了 a1 后，剩下的 S1 是唯一需要求解的子问题。

由最优子结构性质知，如果 a1 在最优解中，那么原问题的最优解由活动 a1 及子问题 S1 中的最优解组成。

活动选择问题 贪心选择的正确性(能得到最优解)：《CLRS》**定理 16.1**：考虑任意非空子问题 Sk，令 am 是 Sk 中结束时间最早的活动，则 am 在 Sk 的某个最大兼容活动子集中。

可以用“剪切-粘贴法”证明。因此，可以反复选择最早结束的活动，保留与此活动兼容的活动 并重复这一过程，直至不再有剩余活动。而且，因为总是选择最早结束的活动，所以选择的活动的结束时间必然是严格递增的。因此只需按结束时间单调递增顺序处理所有活动，每个活动只需考虑一次即可。

贪心算法通常都是**自顶向下**的设计：做出一个选择，然后求解剩下的那个子问题。而不是自底向上地求解出很多子问题，然后再做出选择。

### 递归的贪心算法

**活动结构体**：

```python
# 活动结构体
class Activity:
    def __init__(self, start, finish, info=None):
        self.start = start    # 活动开始时间
        self.finish = finish  # 活动结束时间
        self.info = info      # 关于此活动的其它信息
```

**类构造函数、按结束时间排序**：

```python
class ActivitySelect:
    def __init__(self, activity_list):
        assert isinstance(activity_list, list) and len(activity_list) > 0

        # 确保 activity_list 中每个元素都是 Activity 结构体
        # \Theta(n)
        for activity in activity_list:
            assert isinstance(activity, Activity)
        # 按结束时间 finish 升序排列 TODO 使用优先队列来维护 activity_list
        # O(n log n)
        activity_list = sorted(activity_list, key=lambda x: x.finish, reverse=False)

        self.activity_list = activity_list  # 活动列表 Activity 结构体数组
        self.optimal_set = []  # 最优解：最大兼容活动子集(仅存储下标)
        self.optimal_val = 0   # 最优值：最大兼容活动子集的秩
```

**递归算法**：

```python
# 活动选择问题 Activity Select
# 返回：最优值表、最优解表
def activity_select(self):
    assert isinstance(self.activity_list, list) and len(self.activity_list) > 0

    # 记活动总数量为 n
    n = len(self.activity_list)

    # 重置最优值和最优解
    self.optimal_val = 1
    self.optimal_set = [0]  # 最先结束的活动必然要选

    # 自顶向下递归实现 (贪心算法) \Theta(n)
    # self._activity_select_recursive(0, n)
    # 循环实现 (贪心算法) \Theta(n)
    self._activity_select_iteration()
    return self.optimal_val, self.optimal_set

# 自顶向下递归实现 (贪心算法)
# 输入：k 为前一个贪心选择的活动 ak 的下标。n 为总活动数目
# 时间复杂度 \Theta(n)
# 空间复杂度 \Theta(1)
def _activity_select_recursive(self, k, n):
    assert isinstance(self.activity_list, list) and len(self.activity_list) > 0

    # 从活动 ak 的后一个活动开始考虑
    m = k + 1
    # 如果 m 未至最末，从左至右(结束时间的升序)逐个考察每个任务。如果不与 ak 兼容，则检查下一个，直至兼容
    # 活动兼容：区间无重合(这里默认每个活动的时间为 左闭右开的区间)
    while m < n and self.activity_list[m].start < self.activity_list[k].finish:
        m += 1
    # 如果未扫描至末端，则表示活动 am 即为当前可行的贪心选择
    if m < n:
        self.optimal_val += 1        # 将最优值(子集的秩)加一
        self.optimal_set.append(m)   # 将 am 加入最优解(仅存储下标)
        self._activity_select_recursive(m, n)  # 继续递归 (尾递归，可改为循环)
```

**将尾递归改为循环算法**：

```python
# 循环实现 (贪心算法)
# 时间复杂度 \Theta(n)
# 空间复杂度 \Theta(1)
def _activity_select_iteration(self):
    assert isinstance(self.activity_list, list) and len(self.activity_list) > 0

    # 从活动 ak 的后一个活动开始考虑
    n = len(self.activity_list)
    k = 0

    # 如果 m 未至最末，从左至右(结束时间的升序)逐个考察每个任务。如果不与 ak 兼容，则检查下一个，直至兼容
    for m in range(1, n):
        # 活动兼容：区间无重合(这里默认每个活动的时间为 左闭右开的区间)
        if self.activity_list[m].start >= self.activity_list[k].finish:
            self.optimal_val += 1       # 将最优值(子集的秩)加一
            self.optimal_set.append(m)  # 将 am 加入最优解(仅存储下标)
            k = m  # 修改 k 值，表示当前的贪心选择为活动 ak，并且下个迭代开始时 m = k + 1
```

## 代码范例

### Python

Python 环境：Python 3.7

[GitHub Code Link](https://github.com/YuweiYin/Code_Play/blob/master/Algorithm-Essence/greedy-algorithm/activity-select.py)

### 引申

《CLRS》练习 16.1-4：**区间着色问题** (interval-graph color problem)。

假定有一组活动，需要将它们安排到一些教室，任意活动都可以在任意教室进行。希望使用最少的教室完成所有活动。可以设计一个高效的贪心算法求每个活动应该在哪个教室进行。

问题转换：可以构造一个区间图，顶点表示给定的活动，边链接**不兼容**的活动。要求用最少的颜色对顶点进行着色，使得多有相邻顶点的颜色均不相同（意味着不兼容的活动需要被安排到不同的教室里进行）。

## 参考资料

- Introduction to Algorithm (aka CLRS) Third Edition - Chapter 16
