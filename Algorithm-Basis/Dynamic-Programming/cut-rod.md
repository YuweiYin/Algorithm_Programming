# Algorithm - Dynamic Programming - Cut Rod

By [YuweiYin](https://yuweiyin.github.io/)

## 简介

钢条切割 Cut Rod

**问题描述**：给定一段长度为正整数 n 的钢条和一个价格表(数组) p (下标 i = 1, 2, ..., n)，pi 表示长度为 i 的短钢条的售价。求一个切割钢条方案(最优解)，使得销售收益(最优值) rn 最大。（可以不进行切割）

注意：原钢条总长度 n 为正整数，切割出的短钢条长度也是正整数。（可以把长度为 0 的钢条价格视作为 0，因此可忽略之）

例如，价格表如下：

长度 i | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10
:-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-:
价格 pi | 1 | 5 | 8 | 9 | 10 | 17 | 17 | 20 | 24 | 30

考虑钢条原长为 n = 4 的情况，有如下切割方案：

![cut-rod-1](/img/info-technology/algorithm/dynamic-programming/cut-rod-1.png)

长度为 n 的钢条共有 2^{n-1} 种不同的切割方案。（因为长度为 n 的钢条中间有 n-1 个位置可以选择 切割 xor 不切割）

注意到，如果按长度非递减的顺序切割小段钢条，可能的切割方案会减少许多。切割方案的数量可由 **划分函数** (Partition Function) 给出，此函数近似等于 $ e^{\pi \sqrt(2n/3)} / (4n \sqrt(3)) $，此值小于 2^{n-1}，但仍远远大于任何 n 的多项式。

### 子问题划分

如果用加法来表达切割方案，如果切成 k 个短钢条 (1 <= k <= n)，那么 n = i1 + i2 + ... ik，对应的收益 $ rn = p_{i1} + ... + p_{ik} $

对于最优切割收益 rn，其值应等于 $ rn = max{pn, r_1 + r_{n-1}, r_2 + r_{n-2}, ..., r_{n-1} + r_1} $

这里的 pn 对应于不切割的收益，$ r_i + r_{n-i} $ 对应于将钢条切分为长度为 i 和 n-i 的两段情况下的最佳收益。由于无法预知哪种切割方案会获得最佳收益，因此必须考察所有可能的 i，选取其中的最大值。

为了求解规模为 n 的原问题，先求解形式完全一样(递归)，但规模更小的子问题。当完成首次切割后，将切出的两段钢条看成两个独立的钢条切割问题。递归切分的基础情况就是当前 n=0 或 n=1 时，仅一种方案。

之后通过**组合**两个相关子问题的最优解，并在**所有可能**的两段切割方案中**选取组合收益最大者**，构成原问题的最优解。称钢条切割问题满足 **最优子结构** (Optimal Substructure) 性质：问题的最优解由相关子问题的最优解组合而成，而这些子问题可以独立求解。

除了上述求解方案外，还有一种更简单的递归求解方案：将钢条从左边切割下长度为 i 的一段，**只对右边**剩下长度为 n-i 的那段进行递归切割，左边的一段就不再继续切割了，简化方案的公式如下：

$$ rn = max_{1<=i<=n} (p_i + r_{n-i}) $$

### 自顶向下递归实现 (暴力搜索-回溯法)

```python
class CutRod:
    def __init__(self, price_list, rod_len):
        assert isinstance(price_list, list) and 0 <= rod_len < len(price_list)
        self.price_list = price_list
        self.rod_len = rod_len
```

```python
# 钢条切割
# 返回：最佳收益(最优值)、最佳切割方案列表(最优解)
# 如果返回最佳收益为 -1，则为异常
def cut_rod(self):
    if self.rod_len == 0:
        return 0
    # return self._cut_rod_1(self.rod_len)  # 自顶向下递归实现 (DFS 暴力搜索) O(2^n)
    # return self._cut_rod_2(self.rod_len)  # 自顶向下递归实现 (带备忘录的动态规划) O(n^2)
    return self._cut_rod_3(self.rod_len)  # 自底向上循环实现 (动态规划) O(n^2)
```

```python
# 自顶向下递归实现 (DFS 暴力搜索)
# rn = max_{1<=i<=n} (p_i + r_{n-i})
# 输入：rest_len 为当前待切割的钢条长度
# 时间复杂度 O(2^n)
def _cut_rod_1(self, rest_len):
    assert rest_len >= 0
    # 长度为 0 的钢条收益为 0
    if rest_len == 0:
        return 0, [0]
    # 递归树全遍历的方式查找所有可行解
    best_reward = 0
    best_solution = [-1] * (self.rod_len + 1)  # TODO 最优解
    for i in range(1, rest_len + 1):
        # 取可行解中的最值
        best_reward = max(best_reward, self.price_list[i] + self._cut_rod_1(rest_len - i)[0])
    # 返回最优值
    return best_reward, best_solution
```


### 自顶向下递归实现 (带备忘录的动态规划)

```python
# 自顶向下递归实现 (带备忘录的动态规划)
# 输入：rob_len 为待切割的总钢条长度
# 时间复杂度 O(n^2)
def _cut_rod_2(self, rob_len):
    assert rob_len >= 0
    # 初始化备忘录
    neg_inf = -0x3f3f3f3f
    reward_memo = [neg_inf] * (self.rod_len+ 1)
    # 递归求解
    best_solution = [-1] * (self.rod_len + 1)  # TODO 最优解
    return self._memoized_cut_rob(rob_len, reward_memo), best_solution

def _memoized_cut_rob(self, rest_len, reward_memo):
    assert rest_len >= 0
    # 一旦目标 rest_len 存在于 reward_memo 表中，则直接查值返回即可
    if reward_memo[rest_len] >= 0:
        return reward_memo[rest_len]
    # 否则与普通回溯法类似处理
    if rest_len == 0:
        best_reward = 0
    else:
        best_reward = 0
        for i in range(1, rest_len + 1):
            best_reward = max(best_reward, self.price_list[i] + self._memoized_cut_rob(rest_len - i, reward_memo))
    # 注意在求得当前 rest_len 的最优值后，需记录于备忘录中
    reward_memo[rest_len] = best_reward
    return best_reward
```

### 自底向上循环实现 (动态规划)

```python
# 自底向上循环实现 (动态规划)
# 输入：rob_len 为待切割的总钢条长度
# 时间复杂度 O(n^2)
def _cut_rod_3(self, rob_len):
    assert rob_len >= 0
    # 初始化备忘录
    neg_inf = -0x3f3f3f3f
    reward_memo = [neg_inf] * (self.rod_len + 1)
    reward_memo[0] = 0  # 长度为 0 的钢条收益为 0
    # 切割，每次切割的左段(之后不会再切割的部分)长度从 rob_len - 1 到 0 变动
    # 因此当前切割后的剩余长度 rest_len 从 1 到 rob_len 变动，这样可以表达所有切分方案
    for rest_len in range(1, rob_len + 1):
        best_reward = 0
        # 在当前切割后的 rest_len 基础上继续切分，最短为 1、初次循环的 rest_len 也为 1
        # 循环结束后就能得到 以此 rest_len 作为"可变切割部分" 能获得的最大收益了
        for i in range(1, rest_len + 1):
            best_reward = max(best_reward, self.price_list[i] + reward_memo[rest_len - i])
        # 记录此收益到备忘录中，之后查表即可得值
        reward_memo[rest_len] = best_reward
    # 返回 reward_memo[rob_len] 意味着让整个 rob_len 长度都作为"可变切割部分" 能获得的最大收益，即为目标最优值
    return reward_memo[rob_len]
```

### 重构最优解

```python
# 自底向上循环实现 (动态规划)
# 输入：rob_len 为待切割的总钢条长度
# 时间复杂度 O(n^2)
def _cut_rod_3(self, rob_len):
    assert rob_len >= 0
    # 初始化备忘录
    neg_inf = -0x3f3f3f3f
    reward_memo = [neg_inf] * (self.rod_len + 1)
    reward_memo[0] = 0  # 长度为 0 的钢条收益为 0
    # 用于还原构造最优解的数组
    solutions = [neg_inf] * (self.rod_len + 1)
    # 切割，每次切割的左段(之后不会再切割的部分)长度从 rob_len - 1 到 0 变动
    # 因此当前切割后的剩余长度 rest_len 从 1 到 rob_len 变动，这样可以表达所有切分方案
    for rest_len in range(1, rob_len + 1):
        best_reward = 0
        # 在当前切割后的 rest_len 基础上继续切分，最短为 1、初次循环的 rest_len 也为 1
        # 循环结束后就能得到 以此 rest_len 作为"可变切割部分" 能获得的最大收益了
        for i in range(1, rest_len + 1):
            cur_reward = self.price_list[i] + reward_memo[rest_len - i]
            if best_reward < cur_reward:
                best_reward = cur_reward
                # solutions[rest_len] 表示剩余长度为 rest_len 时的最佳切割长度
                solutions[rest_len] = i
        # 记录此收益到备忘录中，之后查表即可得值
        reward_memo[rest_len] = best_reward
    # 通过 solutions 数组构造最优解
    # solutions[rest_len] 表示剩余长度为 rest_len 时的最佳切割长度
    # 初始的"剩余长度"为总钢条长度 rob_len，每次切割之后 rest_len 减小
    best_solution = []
    _rob_len = rob_len
    while _rob_len > 0:
        best_solution.append(solutions[_rob_len])
        _rob_len -= solutions[_rob_len]
    # 返回 reward_memo[rob_len] 意味着让整个 rob_len 长度都作为"可变切割部分" 能获得的最大收益，即为目标最优值
    return reward_memo[rob_len], best_solution
```

## 代码范例

### Python

Python 环境：Python 3.7

[GitHub Code Link](https://github.com/YuweiYin/Code_Play/blob/master/Algorithm-Essence/dynamic-programming/cut-rod.py)

## 参考资料

- Introduction to Algorithm (aka CLRS) Third Edition - Chapter 15
