# Algorithm - Dynamic Programming - Task Scheduling

By [YuweiYin](https://yuweiyin.github.io/)

## 简介

任务调度问题 Task Scheduling

### 任务调度问题描述

单处理器上的**单位时间任务**最优调度问题是一个可以用 **拟阵** (Matroid) 来求解的问题。在该问题中，每个任务都有一个**截止时间**以及错过截止时间后的**惩罚值**。可以将此问题转换为一个矩阵，并用贪心算法求解。

**单位时间任务** 是严格需要一个时间单位来完成的作业，如运行于计算机上的一个程序。给定一个单位时间任务的有限集合 S，对 S 的一个**调度**是指 S 的一个排列 (permutation)，它指明了任务执行的顺序。第一个被调度的任务开始于时刻 0，终止于时刻 1，第二个任务开始于时刻 1，终止于时刻 2，依此类推。

单处理器上带**截止时间**和**惩罚**的**单位时间任务**调度问题有如下输入：

- n 个单位时间任务的集合 S = {a1, a2, ..., an}
- n 个整数 d1, d2, ..., dn 表示任务**截止时间**。每个 di 满足 1 <= di <= n，期望任务 ai 在时间 di 之前完成。
- n 个非负权重或**惩罚** w1, w2, ..., wn。若任务 ai 在时间 di 之前没有完成，就会受到 wi 的惩罚，如果任务在截止时间前完成，则不会受到惩罚。（这里惩罚为定值，不随时间变化）

目标是找到 S 的一个调度方案，能**最小化总惩罚值**。

考虑一个给定的调度方案。如果方案中一个任务在截止时间后完成，那么称它是**延迟的** (late)，否则 称它是**提前的** (early)。对于任意调度方案，总是可以将其转换为**提前优先模式** (early-first form)，即：将提前的任务都置于延迟的任务之前。因为如果某个提前任务 ai 位于某个延迟任务 aj 之后，那么可以交换两者的位置，此时 ai 仍然是提前的，而 aj 仍然是延迟的。（实际上，能这样做主要是依赖于题目里的惩罚值为定值，延迟的任务不会因为延迟时间变长而增大惩罚值，所以可以让 late 的任务更加 later）

而且，总是可以将一个任意的调度方案转换为**规范模式** (canonical form) —— 提前任务都在延迟任务之前，且提前任务按截止时间单调递增的顺序排序。

这样，寻找最优调度方案的问题 就归结为寻找**提前任务子集** A 的问题。确定 A 之后，可以将 A 中元素按截止时间题赠的顺序排列，然后将延迟任务（差集 S-A）以任意顺序排列在其后，就得到了最优调度方案的规范形式。

对于一个任务集合 A，如果存在一个调度方案，使 A 中所有任务都不延迟，则称 A 是**独立的**。显然，一个调度方案的提前任务集合构成一个独立任务集。令 T 表示所有独立任务集 构成的集类。

下面考虑如何确定一个给定集合 A 是否独立的问题。对 t = 0, 1, 2, ..., n，令 Nt(A) 表示 A 中截止时间小于等于 t 的任务数。注意，对任意集合 A 均有 N0(A) = 0。

《CLRS》**引理 16.12**：对任意任务集合 A，如下 3 条性质是等价的：

1. A 是独立的
2. 对 t = 0, 1, 2, ..., n，均有 Nt(A) <= t
3. 如果 A 中任务按截止时间单调递增的顺序调度，那么不会有任务延迟

利用性质 2，可以设计出一个算法过程，在 O(|A|) 时间内确定一个给定任务集合 A 是否为独立的。

最小化延迟任务的惩罚之和问题 与 最大化提前任务的惩罚之和 是等价的。下面的定理 16.13 可以确保可以用贪心算法求出总惩罚最大的独立任务集 A。

《CLRS》**定理 16.13**：如果 S 是一个给定了**截止时间**的**单位时间任务**集合，T 是所有**独立任务集合**的**集类**，则对应的系统 (S, T) 是一个**拟阵**。

由定理 16.13，可以用贪心算法求出一个最大权重的独立任务集 A，然后可以创建一个最优调度方案，以 A 中任务为提前任务。这个算法是求解单处理器上带截止时间和惩罚的单位时间任务调度问题的一种高效算法。使用贪心算法的运行时间为 O(n^2)，因为算法共进行了 O(n) 次**独立性检查**，每次检查花费 O(n) 时间。

![task-scheduling-1](/img/info-technology/algorithm/greedy-algorithm/task-scheduling-1.png)

### 解决方案

```python
# 循环实现 (贪心算法)
# 时间复杂度 O(n^2)
# 空间复杂度 \Theta(n)
def _task_scheduling_iteration(self):
    n = len(self.task_list)  # 任务总数
    self.optimal_punish = 0  # 最优总惩罚因子

    # 设置 n 个时间槽
    neg_inf = -0x3f3f3f3f
    time_slot = [neg_inf] * n

    # 依次处理 n 个任务，各任务已经按惩罚因子降序排列了
    for i in range(n):
        task = self.task_list[i]
        assert isinstance(task, Task)
        is_slot_founded = False
        # 当处理任务 aj 时，如果存在不晚于 aj 的截止时间 dj 的空余时间槽，则将 aj 分配到其中最晚的那个槽
        for j in reversed(range(task.deadline)):
            if time_slot[j] == neg_inf:
                is_slot_founded = True
                time_slot[j] = task.task_id  # 时间槽占位
                break
        # 如果不存在这样的时间槽，则将 aj 分配到所有空余时间槽最晚的一格中
        if not is_slot_founded:
            self.optimal_punish += task.punish  # 此任务必然延迟
            for j in reversed(range(n)):
                if time_slot[j] == neg_inf:
                    time_slot[j] = task.task_id
                    break
    # 最优任务调度顺序
    self.optimal_order = time_slot
```

### 其它

《CLRS》思考题 16-4（调度问题的变形）提出了一个高效实现的方案。初始时令 n 个时间槽为空，时间槽 i 为单位时间长度，结束于时刻 i。按惩罚值单调递减的顺序处理所有任务。当处理任务 aj 时，如果存在**不晚于** aj 的截止时间 dj 的**空余时间槽**，则将 aj 分配到**其中最晚**的那个。如果不存在这样的时间槽，则将 aj 分配到所有空余时间槽最晚的一格中。另外，可以结合使用[快速不相交集合森林](../data_structure/union-find)来高效实现此算法。

## 代码范例

### Python

Python 环境：Python 3.7

[GitHub Code Link](https://github.com/YuweiYin/Code_Play/blob/master/Algorithm-Essence/greedy-algorithm/task-scheduling.py)

## 参考资料

- Introduction to Algorithm (aka CLRS) Third Edition - Chapter 16
