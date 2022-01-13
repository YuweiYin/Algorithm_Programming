# Algorithm - Dynamic Programming - Optimal Binary Search Tree

By [YuweiYin](https://yuweiyin.github.io/)

## 简介

最优二叉搜索树 (Optimal Binary Search Tree)

### 最优二叉搜索树引入

假设生在实现一个英语文本到法语文本的翻译程序，对英语文本中出现的每个单词，需要查找对应的法语单词。（不考虑句型变化等因素）

为了实现这些查找操作，可以创建一棵[二叉搜索树 BST](../data-structure/binary-search-tree)，将 n 个英语单词（n 为英语词表大小）作为关键字 key，而对应的法语单词作为其关键数据/卫星数据 val。由于词表中的每个单词都有可能被搜索到，所以可以通过使用[红黑树](../data-structure/red-black-tree) 或其它平衡搜索树结构，从而使得每次搜索时间平均为 O(log n)。

但是在此实际应用中，单词出现的频率是不同的。如果按照词表顺序，以插入方式逐步构造 BST，位于词表靠前位置的单词往往处于靠近根结点的位子哈。在这种情下，可能像“the”这种频繁使用的单词会位于搜索树中远离根的位置，而像“machicolation”这种很少使用的单词会位于靠近根的位置。这样往往会增加翻译文本时的总搜索深度/比较次数。

因此，需要让**在当前任务中**频繁出现、检索次数可能很多的单词**置于靠近根的位置**。使得所有搜索操作预期访问的结点总数最少。（假定已经知道当前任务中 每个词语出现的词频）

这个问题称为**最优二叉搜索树** (Optimal Binary Search Tree) 问题。

### 最优二叉搜索树问题描述

形式化定义如下：

给定一个含有 n 个不同关键字的已(按**严格升序**)排序的序列 `K = <k1, k2, ..., kn>`，利用这 n 个值作为关键字 key 构建一棵二叉搜索树 BST。对每个关键字 ki，都有一个概率 pi 表示其**搜索频率**。

另外，有些要搜索的值可能不在 K 中，因此还有 n+1 个**伪关键字** d0, d1, d2, ..., dn 表示不在 K 中的值。例如，d0 表示所有小于 k1 的值，dn 表示所有大于 kn 的值，而 di 表示所有在 ki 和 k_{i+1} 的值。每个伪关键字 di 也都有一个相应的 pi 表示其搜索频率。

下图显示 对一个 n=5 个关键字的集合构造的两棵二叉搜索树。每个关键字 ki 是一个内部结点，而每个伪关键字 di 是一个叶结点。每次搜索要么成功（在内部结点找到某个关键字 ki）、要么失败（在叶结点找到某个伪关键字 di），有如下公式：

![optimal-bst-1](/img/info-technology/algorithm/dynamic-programming/optimal-bst-1.png)

由于假定已知每个关键字和伪关键字的搜索频率，因此可以确定在一棵给定的 BST 中进行一次搜索的期望代价。假定一次搜索的代价等于访问的结点数，即找到的结点的深度加一。那么在一棵 BST 中进行一次搜索的期望代价为：

![optimal-bst-2](/img/info-technology/algorithm/dynamic-programming/optimal-bst-2.png)

对于一个给定的概率集合，希望构造出一棵期望搜索代价最小的 BST，称为**最优二叉搜索树**。前面给出的 图 15-9 (b) 就是在给定概率集合下的最优二叉搜索树，其期望代价为 2.75。

此例显示：最优二叉搜索树不一定是高低最矮的。而且概率最高的关键字也不一定出现在 BST 的根结点。这是因为：伪关键字 di 必须要是叶结点，而在建立树的时候还要同时考虑 ki 和 di 中的概率值 pi。

## 动态规划解决方案

先考察暴力穷举搜索方法的时间复杂度量级，然后考虑是否满足动态规划的适用条件：最优子结构性质、重叠子问题性质。

对于最优 BST 问题，穷举并检查所有可能的 BST 并不是一个高效的算法。对任意一棵 n 个结点的二叉树，都可以通过对结点标记关键字 k1, k2, ..., kn 构造出一棵二叉搜索树，然后向其中添加伪关键字作为叶结点。可以证明，含有 n 个结点的二叉树的数量为 $ \Omega(4^n / n^{3/2}) $，因此暴力搜索穷举法需要指数时间。因此考虑本问题是否适合使用动态规划方法。

### 1. 刻画最优二叉搜索树的结构特征

考虑一棵二叉搜索树的任意子树，它必包含连续关键字 ki, ..., kj (1 <= i <= j <= n)，而且其叶结点必然是伪关键字 d_{i-1}, ..., dj。本问题是具有**最优子结构性质**的，下面予以说明。

因此该问题的最优子结构是：如果一棵最优二叉树 T 有一棵包含关键字 ki, ..., kj 的子树 T'，那么 T' 必然是包含关键字 ki, ..., kj 和伪关键字 d_{i-1}, ..., dj 的子问题的最优解。

用“剪切-粘贴法”可以证明这一点。如果存在子树 T''，其期望搜索代价比 T' 低，那么将 T' 从 T 中删除，然后将 T'' 粘贴到相应位置，就可以得到一棵期望搜索代价低于 T 的二叉搜索树，这与 T 原本是最优 BST 假设相矛盾。

可以用子问题的最优解构造原问题的最优解。给定关键字序列 ki, ..., kj，假设其中某个关键字 kr (i <= r <= j) 是这些关键字所在的最优子树的根结点。那么 kr 结点的左子树就包含了关键字 ki, ..., k_{r-1}（以及伪关键字 d_{i-1}, ..., d_{r-1}），而右子树包含了关键字 k_{r+1}, ..., kj（以及伪关键字 dr, ..., dj）。因此只要检查所有可能的根结点 kr，并对每种情况分别求解左最优 BST 子树 和 右最优 BST 子树，即可保证找到原问题的最优解。

另外，还有一个值得注意的细节——“空子树”。假定在关键字序列 ki, ..., kj 中选 ki 作为最优子树的根结点，那么其左孩子是仅含伪关键字 d_{i-1} 的叶结点。同样地，如果选 kj 作为最优子树的根结点，那么其左孩子是仅含伪关键字 dj 的叶结点。

### 2. 设计递归求解方案

选取子问题域：求解包含关键字 ki, ..., kj 的最优二叉搜索树，其中 1 <= i < j <= n。定义最优值表格(二维数组) e[i, j] 为：在包含关键字 ki, ..., kj 的最优二叉搜索树中进行一次搜索的期望代价。最终，原问题的最优值为 e[1, n]。

pi 为关键字 ki 的概率权重；qi 为伪关键字 di 的概率权重。

当 j = i - 1 时是基本情况，此时子树仅包含伪关键字 d_{i-1}，期望搜索代价为 e[i, i-1] = q_{i-1}。

当 j >= i 时，需要从 ki, ..., kj 中选择一个根结点 kr，然后构造最优左右子树。当一棵子树成为一个结点的子树时，由于每个结点的深度都增加了 1，所有概率之和为：

$$ w(i, j) = \sum_{l=i}^{j} p_l + \sum_{l=i-1}^{j} p_l $$

因此有公式：`e[i, j] = pr + (e[i, r-1] + w(i, r-1)) + (e[r+1, j] + w(r+1, j))`

由于有 `w(i, j) = w(i, r-1) + pr + w(r+1, j)`

所以 e[i, j] 可重写为 `e[i, j] = e[i, r-1] + e[r+1, j] + w(i, j)`

故有如下递归公式：

- 若 j == i-1，则 e[i, j] = q_{i-1}
- 若 i <= j，则 e[i, j] = min{ e[i, r-1] + e[r+1, j] + w(i,j) }

另外，为了记录最优二叉树的结构，定义表格(二维数组) root[i, j] 保存根结点 kr 的下标 r。利用 root 表格可以构建出最优解。

### 3. 计算最优 BST 的期望搜索代价(最优值)

用表格 e[1..n+1, 0..n] 来保存 e[i, j] 值。第一维下标上界为 n+1 而不是 n，是因为对于只包含伪关键字 dn 的子树，需要计算并保存 e[n+1, n]。第二维下标下界为 0，是因为对于只包含伪关键字 d0 的子树，需要计算并保存 e[1, 0]。只是用表中满足 i < j 的表项 e[i, j]。

而表格 root[i, j] 记录 包含了关键字 k1, ..., kj 的子树 的根。只使用此表中满足 1 <= i <= j <= n 的表项 root[i, j]。

此外，还需要另一个表格 w[1..n+1, 0..n] 来提高计算效率。为了避免每次计算 e[i, j] 都要重新计算 w(i, j)，可以将此值保存在表格 w 中，这样每次可以节省 $ \Theta(j-i) $ 次加法运算。对基本情况，令 `w[i, i-1] = q_{i-1}` (1 <= i <= n+1)。而对 i <= j 的情况，可这样计算： `w[i, j] = w[i, j-1] + pj + qj`。

这样，对 $ \Theta(n^2) $ 个 w[i, j]，每个的计算时间为 $ \Theta(1) $。

**类构造函数**：

```python
class OptimalBinarySearchTree:
    def __init__(self, p_arr, q_arr, float_acc):
        assert isinstance(p_arr, list) and len(p_arr) > 0
        assert isinstance(q_arr, list) and len(q_arr) == len(p_arr) + 1
        self.p_arr = p_arr     # 各个关键字 k_i 对应的概率权重 p_i
        self.q_arr = q_arr     # 各个伪关键字 d_i 对应的概率权重 q_i
        self.float_acc = float_acc      # p_arr 和 q_arr 中概率值(浮点数)保留小数点后的位数
        self.optimal_cost = 0x3f3f3f3f  # 最优的期望搜索代价
        self.inf = 0x3f3f3f3f  # 目标是求期望搜索代价的最小值，所以在计算前让代价初始化为 inf
```

**对象初始化**：

```python
# p_arr[i] 是各个关键字 k_i 对应的概率权重 p_i
# q_arr[i] 是各个伪关键字 d_i 对应的概率权重 q_i
p_arr = [0.15, 0.10, 0.05, 0.10, 0.20]
q_arr = [0.05, 0.10, 0.05, 0.05, 0.05, 0.10]
float_acc = 2  # p_arr 和 q_arr 中概率值(浮点数)保留小数点后的位数

o_bst = OptimalBinarySearchTree(p_arr, q_arr, float_acc)
```

**表格初始化、初始调用**：

```python
# 最优二叉搜索树
# - 若 j == i-1，则 e[i, j] = q_{i-1}
# - 若 i <= j，则 e[i, j] = min{ e[i, r-1] + e[r+1, j] + w(i,j) }
# - w[i, j] = w[i, j-1] + pj + qj
# 返回：o_bst 最优值表、o_bst 最优解表
def optimal_bst(self):
    assert isinstance(self.p_arr, list) and len(self.p_arr) > 0
    assert isinstance(self.q_arr, list) and len(self.q_arr) == len(self.p_arr) + 1

    # 记关键字数量为 n
    n = len(self.p_arr)

    # 表格 e[1..n+1, 0..n] 来保存 e[i, j] 值
    # 第一维下标上界为 n+1 而不是 n，是因为对于只包含伪关键字 dn 的子树，需要计算并保存 e[n+1, n]
    # 第二维下标下界为 0，是因为对于只包含伪关键字 d0 的子树，需要计算并保存 e[1, 0]。只是用表中满足 i < j 的表项 e[i, j]
    e_table = [[0 for j in range(n + 1)] for i in range(n + 2)]

    # 为了避免每次计算 e[i, j] 都要重新计算 w(i, j)，可以将此值保存在表格 w 中
    # 这样每次可以节省 $ \Theta(j-i) $ 次加法运算。
    w_table = [[0 for j in range(n + 1)] for i in range(n + 2)]

    # 表格 root[i, j] 记录 包含了关键字 k1, ..., kj 的子树 的根
    # 利用 root 表格可以构建出最优解。只使用此表中满足 1 <= i <= j <= n 的表项 root[i, j]
    # r_table = [[0 for j in range(n)] for i in range(n)]
    r_table = [[0 for j in range(n + 1)] for i in range(n + 2)]

    # e[i, i-1] 和 w[i, i-1] 均置为 q_{i-1}
    for i in range(1, n + 2):
        e_table[i][i - 1] = self.q_arr[i - 1]
        w_table[i][i - 1] = self.q_arr[i - 1]

    # 自底向上循环实现 (动态规划) \Theta(n^3)
    e_table, w_table, r_table = self._optimal_bst(e_table, w_table, r_table, n)
    return e_table, w_table, r_table
```

**求最优值/解的表格**：

```python
# 自底向上循环实现 (动态规划)
# 时间复杂度 \Theta(n^3)
# 空间复杂度 \Theta(n^2)
def _optimal_bst(self, e_table, w_table, r_table, n):
    assert isinstance(self.p_arr, list) and len(self.p_arr) > 0
    assert isinstance(self.q_arr, list) and len(self.q_arr) == len(self.p_arr) + 1

    # 对于各个长度(length) 和各个起点(i) 的子关键字序列(子问题)求最优解/值，自底向上分别计算
    # - 若 j == i-1，则 e[i, j] = q_{i-1}
    # - 若 i <= j，则 e[i, j] = min{ e[i, r-1] + e[r+1, j] + w(i,j) }
    # - w[i, j] = w[i, j-1] + pj + qj
    for length in range(1, n + 1):          # 子关键字序列的长度取值范围为 1 ~ n
        # 第一个循环
        for i in range(1, n - length + 2):  # 子关键字序列起点 i 取值范围为 0 ~ n-1
            j = i + length - 1              # 子关键字序列终点 j
            e_table[i][j] = self.inf
            w_table[i][j] = round(w_table[i][j - 1] + self.p_arr[j - 1] + self.q_arr[j], self.float_acc)
            for r in range(i, j + 1):
                cost = e_table[i][r - 1] + e_table[r + 1][j] + w_table[i][j]
                if cost < e_table[i][j]:
                    e_table[i][j] = round(cost, self.float_acc)
                    r_table[i][j] = r

    # 此时最优值为 e[1, n]
    self.optimal_cost = e_table[1][n]
    # 返回备忘录 e、w 和 r
    return e_table, w_table, r_table

# 获取最优值(最优的期望搜索代价) e[1, n]
def get_optimal_cost(self):
    return self.optimal_cost
```

![optimal-bst-3](/img/info-technology/algorithm/dynamic-programming/optimal-bst-3.png)

### 4. 构造最优 BST (最优解)

```python
# 根据 r_table 打印最优解
# 时间复杂度 \Theta(n)
def print_optimal_bst(self, r_table):
    n = len(self.p_arr)
    # 首先打印树根
    cur_root = r_table[1][n]
    print('k', cur_root, '为根')
    # 然后调用递归算法处理其左右子树
    self._print_optimal_bst(r_table, cur_root, True, 1, cur_root - 1)
    self._print_optimal_bst(r_table, cur_root, False, cur_root + 1, n)

# 参数 parent_key 是当前子树的父结点序号，is_left 为 True 表示当前子树是其父结点的左孩子，否则反之
def _print_optimal_bst(self, r_table, parent_key, is_left, i, j):
    # 特殊情况：伪关键字数量比关键字数量多 1，所以仅在如下情况会让 k_j 有右孩子 d_j
    if i > j:
        if i == j + 1 and (not is_left):
            print('叶结点 d', j, '为 k', j, '的右孩子')
        return
    # 基本情况：i == j 表示到了关键字 k 的"叶"结点
    if i == j:
        # 根据当前子树是其父结点的左孩子还是右孩子，分别处理
        if is_left:
            print('k', i, '为 k', parent_key, '的左孩子')
        else:
            print('k', i, '为 k', parent_key, '的右孩子')
        # 处理真正的叶结点：伪关键字 d_{i-1} 和 d_{i}
        print('叶结点 d', i - 1, '为 k', i, '的左孩子')
        print('叶结点 d', i, '为 k', i, '的右孩子')
    # 否则需要检查关键字区间 ki, ..., kj 中的树结构
    else:
        # 通过查看 r_table[i][j] 得到此关键字序列该选择的树根
        cur_root = r_table[i][j]
        # 根据当前子树是其父结点的左孩子还是右孩子，分别处理
        if is_left:
            print('k', cur_root, '为 k', parent_key, '的左孩子')
        else:
            print('k', cur_root, '为 k', parent_key, '的右孩子')
        # 递归处理当前根的左右子树
        self._print_optimal_bst(r_table, cur_root, True, i, cur_root - 1)
        self._print_optimal_bst(r_table, cur_root, False, cur_root + 1, j)
```

## 代码范例

### Python

Python 环境：Python 3.7

[GitHub Code Link](https://github.com/YuweiYin/Code_Play/blob/master/Algorithm-Essence/dynamic-programming/optimal-binary-search-tree.py)

## 参考资料

- Introduction to Algorithm (aka CLRS) Third Edition - Chapter 15
