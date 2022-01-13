# Algorithm - Mathematics - Probability Statistics

By [YuweiYin](https://yuweiyin.github.io/)

## 简介

雇用问题 Hiring Problem

- 问题描述：
    - 现在要雇用一名办公助理，最多可能会面试 n 位应聘者。
    - 每次面试一个应聘者，就要**立刻决定**是否雇用他。
    - 并且假定**不能够重新雇用**已经被辞掉的办公助理。
    - 希望雇用到“更好”的办公助理，但是在**面试之前没法知道**应聘者是否“够好”。因此这是一个 Online **在线问题**。
    - 如果要面试一位应聘者，需要支付给雇用代理一小笔费用。
    - 如果要雇用一位应聘者，则需要向他支付一定的费用（这里）。
- 目标：
    - 在耗费的金钱 与 能够雇用到的“更好”的助理 之间进行权衡。

## 分析 & 设计

### 简单方法

设计应聘者结构体如下：

```python
# 应聘者结构体
class Candidate:
    def __init__(self, c_id, ability=0, salary=1, interview=0):
        self.c_id = c_id            # 该应聘者的编号
        self.ability = ability      # 该应聘者的能力, 据此来决定是否雇用 (默认设置为自然数, 良序集)
        self.salary = salary        # 雇用此应聘者需要花费的总金额 (默认值为 1, 便于分析)
        self.interview = interview  # 与此应聘者进行面试需要花费的总金额 (默认值为 0, 相比于 salary 可忽略, 便于分析)
```

设计 Hiring 类，构造函数如下：
```python
class Hiring:
    def __init__(self, candidate_array):
        for candidate in candidate_array:
            assert isinstance(candidate, Candidate)

        self.candidate_array = candidate_array  # 应聘者列表 (面试前不可知)
        self.total_num = len(candidate_array)   # 应聘者总数 (此处假定已知)
        self.cur_hire = Candidate(-0x3f3f3f3f, ability=-0x3f3f3f3f)  # 当前雇用在位的应聘者, 此信息面试官可知
        self.total_cost = 0                     # 整个应聘过程中的总花费 (雇用过程结束后才可知)
```

如果是简单的策略，只在乎最终雇用到最好的助理，那么可以对每个应聘者都面试。如果当前面试的应聘者优于当前在位的办公助理，则替换之。伪代码如下：

```python
# 执行雇用过程
# 面试前既不知道有多少应聘者、也更不知道其 id 或 ability
# 返回面试与雇用的总花费
def _do_hire_1(self):
    # 设置初始值
    self.total_cost = 0
    self.cur_hire = Candidate(-0x3f3f3f3f, ability=-0x3f3f3f3f)
    # 循环处理每位应聘者
    for candidate in self.candidate_array:
        assert isinstance(candidate, Candidate)
        # 一旦当前应聘者分数更高，就雇用
        if candidate.ability > self.cur_hire.ability:
            self.total_cost += candidate.interview + candidate.salary
            self.cur_hire = candidate
    # 返回面试与雇用的总花费
    return self.total_cost
```

举办面试的费用较低，记为 c\_i，而雇用的费用较高，设为 c\_h。假设每次举办面试的费用 c\_i 是相等的，每次雇用的总花费 c\_h 也是均等的。假设整个过程中选择雇用了 m 人（0 <= m <= n），因此该算法的总费用就是 O(n c\_i + m c\_h)。由于 c\_i 相对于 c\_h 是很小的，而且如果总是需要面试全部 n 个应聘者，则面试的总花费是个定值，因此这里只关注于分析 m c\_k，即雇用的费用。

在**最坏情况**下，应聘者的 ability 是严格增序，那么每次面试都需要进行雇用，总的费用是 O(n c\_k)。

对于这个在线算法而言，既无法提前知道应聘者的 ability 的次序或分布，也不能控制这个次序。

### 随机算法 & 概率分析

在雇用问题中，可以假设应聘者以随机顺序出现。由于应聘者的 ability 具备全序关系、两两可比，所以这 n 个应聘者能够确定一个排名次序（应聘者 id 号的一个 permutation 排列）。前述随机的假设意味着排名次序 是在所有 n! 种可能的排列中 **等概率** 出现的。

如果雇用问题事先有一份应聘者名单（即：面试前已知各个应聘者的 c_id，但不知其 ability）。此时，不像之前那样只能去猜测、假定应聘者以随机次序出现，而是能够主动地随机打乱次序，获得了对流程的控制，并且加强了随机次序。但是，此时该雇用问题**不再完全是在线的了**。

设 X 是一个随机变量，其值等于雇用一个新办公助理的次数。则根据期望的定义，则 X 的期望如下：

$$ E[X] = \sum_{x=1}^{n} (x Pr{X = x}) $$

但上述计算会比较麻烦。此时使用**指示器随机变量**分析雇用问题，定义 n 个变量。与每个应聘者是否被雇用对应。特别地，假设 Xi 对应于第 i 个应聘者被雇用 这个事件的指示器随机变量。因而：Xi = I{应聘者 i 被雇用}

- 如果应聘者 i 被雇用，则 Xi = 1
- 如果应聘者 i 不被雇用，则 Xi = 0

以及 X = X1 + X2 + ...  + Xn，故有 E[Xi] = Pr{应聘者 i 被雇用}

```python
# 执行随机化的雇用过程
# 面试前有应聘者的名单，因此知道应聘者数目，也知道其 id，但不知道各位应聘者的 ability
# 很显然，如果面试前就已经知道了各位应聘者的确切 ability，那么一般只需要找到最大值就完成雇用了
# 返回面试与雇用的总花费
def _do_hire_2(self):
    # 先随机打乱数组，再执行与 _do_hire_1 相同的算法
    shuffler = ShuffleArray(self.candidate_array)
    shuffler.do_shuffle()
    # 设置初始值
    self.total_cost = 0
    self.cur_hire = Candidate(-0x3f3f3f3f, ability=-0x3f3f3f3f)
    # 循环处理每位应聘者
    for candidate in shuffler.array:
        assert isinstance(candidate, Candidate)
        # 一旦当前应聘者分数更高，就雇用
        if candidate.ability > self.cur_hire.ability:
            self.total_cost += candidate.interview + candidate.salary
            self.cur_hire = candidate
    # 返回面试与雇用的总花费
    return self.total_cost
```

对应于程序中，如果某个应聘者 i（从 1 开始计算）被雇用，意味着他的 ability 比前面 i - 1 个应聘者都更高。由于已经控制应聘者以随机顺序出现，所以前面 i - 1 个应聘者也以随机次序出现。这些前 i 个应聘者中的任意一个都等可能地是目前最有资格的。应聘者 i 比应聘者 1 到 i - 1 更有资格的概率是 1/i，因而也以 1/i 的概率被雇用。所以有：E[Xi] = 1/i

根据期望的线性性质，可以计算得：

$$ E[X] = E[\sum_{i=1}^{n} Xi] = \sum_{i=1}^{n} E[Xi] = \sum_{i=1}^{n} (1/i) = ln n + O(1) $$

尽管面试了 n 个人，但平均起来，实际上大约只会雇用他们之中的 ln n 个人。总结起来为如下的引理：

《CLRS》**引理 5.2**：假设应聘者以随机次序出现，雇用问题算法 总的雇用费用平均情形下为 O(c\_h \* ln n)。

《CLRS》**引理 5.3**：经随机化处理后的雇用问题算法 总的雇用费用平均情形下为 O(c\_h \* ln n)。

这种经随机化处理后的平均情形下的雇用费用 比最坏情况下的雇用费用 O(c\_h \* n) 有了很大的改进。

### 在线雇用问题

**问题描述**：假设现在**不希望面试所有**的应聘者，也**不希望**一旦有了更好（ability 值更大）的申请者就**立即解雇**当前的在职者。取而代之的，是希望雇用**接近最好**（一种预估）的应聘者，且整个过程**只雇用一名**应聘者。

- 注意：
    - 仍然需要保证：每次面试后，要么立即雇用次应聘者，要么立即拒绝此应聘者。而不是等到考察了多位应聘者之后做出综合决策（离线算法）。
    - 不过应聘者的总数目是可以提前知晓的。（这也是此在线雇用问题不够“在线”的一个部分。）

**目标**：在 **最小化面试次数** 和 **最大化雇用者的质量** 两方面取得平衡。

通过如下方式来对问题建模：面试完每一位应聘者，都能知晓其能力值分数（ability）。在已看过 j 位应聘者后，可以知道这 j 个人中哪一位的分数最高，但是不知道在剩余的 n - j 位应聘者中会不会有更高分数的应聘者。

可以采取这样的策略：选择一个正整数 k < n，面试这 k 位应聘者并拒绝他们，不过会取他们中的最高分数值 s 作为参考。在面试剩余的 n - k 位应聘者时，一旦有比 s 分数更高的应聘者 就雇用他，剩下的应聘者就都不面试了。

如果最好的应聘者在前 k 个里面（被拒绝掉了），那么之后的 n - k 位面试者的分数都不及 s，所以将雇用最后一位（第 n 个）应聘者，即便此应聘者的分数可能较低。

```python
# 执行在线雇用过程
# 面试前知道有多少应聘者，但不知道其 id 名单 (所以不能进行随机化) 以及能力值分数 ability
# 返回面试的次数
def _do_online_hire(self):
    n = len(self.candidate_array)
    k = int(n / math.e)  # 经证明，k = n/e 可以使得选到最佳应聘者的概率下界最大化，成功概率至少为 1/e
    self.cur_hire = Candidate(-0x3f3f3f3f, ability=-0x3f3f3f3f)
    if n == 1:
        # 仅一名待面试的应聘者，直接雇用
        assert isinstance(self.candidate_array[0], Candidate)
        self.cur_hire = self.candidate_array[0]
        return 1
    elif n > 1 and isinstance(k, int) and 0 < k < n:
        # 待面试的应聘者超过 1 人，取前 k 人淘汰，并记录这 k 人中的最高分 best_ability
        best_ability = -0x3f3f3f3f
        for i in range(k):
            assert isinstance(self.candidate_array[i], Candidate)
            if self.candidate_array[i].ability > best_ability:
                best_ability = self.candidate_array[i].ability

        # 随后面试的 n - k 人中，一旦有比 best_ability 更高分的人出现，则直接雇用，不面试剩下的人了
        for i in range(k, n):
            assert isinstance(self.candidate_array[i], Candidate)
            # 如果面试到最后一个人，直接雇用
            if i == n - 1:
                self.cur_hire = self.candidate_array[i]
                return n
            else:
                if self.candidate_array[i].ability > best_ability:
                    self.cur_hire = self.candidate_array[i]
                    return i + 1
        # 不应运行到此处
        return 0
    else:
        # 表示参数类型/范围错误，或者 n == 0 没有应聘者
        return 0
```

现在关键是分析什么样的 k 值才有最佳的权衡效果。记事件 S 为：成功选择最好的应聘者。记事件 Si 表示最好的应聘者时第 i 位（序号从 1 开始）应聘者。故有 $ Pr{S} = \sum_{i=1}^{n} Pr{Si} $。

根据此算法的性质，当最好的应聘者是前 k 个应聘者中的一个时，不会成功（事件 S 不会发生），即 对 i = 1, 2, ..., k 有 Pr{Si} = 0。从而有 $ Pr{S} = \sum_{i = k+1}^{n} Pr{Si} $。

可以证明（详见《CLRS》），Pr{S} 的界如下：

$$ (ln n - ln k) k/n <= Pr{S} <= (ln (n-1) - ln (k-1)) k/n $$

这是 Pr{S} 的一个相当紧确的界。由于希望最大化成功的概率，所以关注如何选取 k 值使得 Pr{S} 的下界最大化。以 k 为自变量对表达式 (ln n - ln k) k/n 求导，得到 (ln n - ln k - 1) / n。令此导数为 0，得 k = n/e 时，概率下界最大化。

因此，如果**选用 k = n/e** 来实现上述算法，那么将以**至少 1/e 的概率成功**雇用到最好的应聘者。

e \~= 2.71828182845904 所以 1/e \~= 0.3678794411714423

## 代码范例

### Python

Python 环境：Python 3.7

[GitHub Code Link](https://github.com/YuweiYin/Code_Play/blob/master/Algorithm-Essence/mathematics/probability_statistics/hiring.py)

## 参考资料

- Introduction to Algorithm (aka CLRS) Third Edition - Chapter 5
