# Algorithm - Data Structure - Interval Tree

By [YuweiYin](https://yuweiyin.github.io/)

## 简介

区间树 (Interval Tree)

与 [顺序统计树](./order-statistic-tree) (Order Statistic Tree, OST) 相似，区间树也是基于 [红黑树](./red-black-tree) (Red Black Tree, RBT) 数据结构的扩张，用于支持由区间构成的动态集合上的一些操作。

实数域 R 上的 **闭区间** (closed interval) 是一个实数的有序对 [t1, t2]，其中 t1 <= t2。区间 [t1, t2] 表示了集合 $ {t \in R: t1 <= t <= t2} $。**开**(open)区间 和 **半开**(half-open)区间 分别略去了集合的两个和一个端点。在此后的讨论中，均假设区间都是闭的。

区间便于表示占用一个连续时间段的一些事件。例如：查询一个由时间区间数据（左右断点 pair）构成的数据库，找出给定时间区间内发生了什么事件。

## 设计

把闭区间 [t1, t2] 表示成一个对象 inter，其中属性 inter.low = t1 为**低端点**(low endpoint)，属性 inter.high = t2 为**高端点**(high endpoint)。如果两个对象 inter1 和 inter2 的区间**交集不为空**，则称这两个**区间重叠**(overlap)。对对象属性而言，重叠意味着 inter1.low <= inter2.high 并且 inter2.low <= inter1.high。

任何两个区间 inter1 和 inter2 满足**区间三分律** (interval trichotomy)，即下述三条性质有且仅有其一成立：

1. inter1 和 inter2 重叠。
    - 即：inter1.low <= inter2.high 并且 inter2.low <= inter1.high
2. inter1 在 inter2 左边。
    - 即：inter1.high < inter2.low
3. inter1 在 inter2 右边。
    - 即：inert1.low > inter2.high

![interval-tree-1](/img/info-technology/algorithm/data-structure/interval-tree-1.png)

区间查询 Range Query 任务中，与区间树类似的比如 [线段树](./segment-tree) (Segment Tree, ST)。但线段树一般是针对静态的数据，一旦数据量变化，就需要花费 O(n) 的时间重建。而区间树是一种基于红黑树的动态集合数据结构。

区间树中每个树结点 x 都包含一个区间属性 inter，此属性可以设置为一个元组对象 tuple 或者一种新的结构体对象，视具体需求而定。

区间树主要支持如下操作：

- `interval_insert(T, x)`
    - 将包含区间属性 inter 的元素 x 插入到区间树 T 中
- `interval_delete(T, x)`
    - 从区间树 T 中删除元素 x
- `interval_search(T, target_inter)`
    - 返回一个指向区间树 T 中元素 x 的指针，使 x.inter 与 target\_inter 重叠
    - 若此元素不存在，则返回 None

![interval-tree-2](/img/info-technology/algorithm/data-structure/interval-tree-2.png)

### 扩张步骤

1. 基础数据结构：
    - 选择红黑树作为基础数据结构，其每个结点 x 包含一个区间属性 x.inter，且 x 的关键字 key 为区间的低端点 x.inter.low。
    - 因此，该数据结构按中序遍历列出的就是按低端点的次序排列的各区间。
2. 附加信息：
    - 每个结点 x 中除了自身的区间信息 以及红黑树本身的信息外，还包含一个数值 x.max，表示以 x 为根的子树中所有区间端点的最大值。
3. 对信息的维护：
    - 通过给定区间的 x.inter 和结点 x 的子结点的 max 值，可以确定 x.max 值
    - x.max = max(x.inter.high, x.left.max, x.right.max)
    - 由于更新 x 的附加信息仅依赖于本结点及其孩子结点 这 3 个结点的信息，所以可以保证插入和删除时对附加信息的维护也是 O(log n) 时间的。
4. 设计新的操作：
    - 对于插入和删除，只需维护 max 信息即可
    - 利用附加信息 max，可以设计的新操作是 `interval_search(T, target_inter)` 找出区间树 T 中与区间 target\_inter 重叠的那个结点。若此元素不存在，则返回 None


### 建立区间树

以 kv_array 中的每个元素为 [key, value] 数组，构建树结点。树结点设计如下：

```python
class TreeNode:
    def __init__(self, inter_low, inter_high, val=0, color=True):
        self.key = inter_low  # 键，区间树的关键字 key 即为区间的低端点
        self.val = val        # 值，树结点存储的值，可以为任意对象
        self.color = color    # 结点的颜色，True 代表红色(默认)，False 代表黑色
        self.left = None      # 左孩子指针
        self.right = None     # 右孩子指针
        self.parent = None    # 父结点指针
        '''上面是红黑树原本的所需的树结点属性'''
        '''下面是顺序统计树扩张红黑树功能所需的属性'''
        self.inter = (inter_low, inter_high)  # interval 区间属性 (这里默认为闭区间)
        self.max_end = inter_high             # 以本结点为根的子树的 所有区间端点的最大值
```

### 区间查询

```python
# 查询区间树中是否存在与闭区间 target_interval 有重叠的区间
def interval_search(self, target_interval):
    if isinstance(self.bst, TreeNode) and \
            isinstance(target_interval, tuple) and len(target_interval) == 2:
        ptr = self.bst
        while isinstance(ptr, TreeNode) and ptr != self.nil:
            # 如果 ptr 结点的区间与目标区间 target_interval 有重叠，则返回 ptr
            # 有重叠：inter1.low <= inter2.high 并且 inter2.low <= inter1.high
            if ptr.inter[0] <= target_interval[1] and target_interval[0] <= ptr.inter[1]:
                return ptr
            # 如果无重叠，则往左或往右 继续搜索
            else:
                assert isinstance(ptr.left, TreeNode)
                # 如果左孩子存在 (不是哨兵)，且左子树的区间端点最大值超过 目标区间的低端点，
                # 表示左侧有与目标区间重合的区间结点，则往左继续搜索
                # 注意到：由于区间是连续的，所以此时不可能与右子树中的任何区间重叠了
                if ptr.left != self.nil and ptr.left.max_end >= target_interval[0]:
                    ptr = ptr.left
                # 否则，左孩子不存在 (是哨兵)，或者左子树的区间端点最大值不及 目标区间的低端点，
                # 表示左侧的结点已经不可能与目标区间有重合了，则往右继续搜索
                else:
                    ptr = ptr.right
        # 如果出了循环、到了这一步，表示找不到
        return None
    else:
        # BST 树为空树，找不到目标结点
        return None
```

### 左旋/右旋

在左旋和右旋操作中，返回新父亲 node\_y 之前，加上相同的语句，维护 max\_end 属性：

```python
# 维护区间树的属性 max_end (注意先更新此时的子结点 node_x, 后更新 node_y)
# 对某一个结点进行 max_end 维护的总时间复杂度为 O(log n)，不增加渐近量级
assert isinstance(node_x.left, TreeNode) and isinstance(node_x.right, TreeNode)
assert isinstance(node_y.left, TreeNode) and isinstance(node_y.right, TreeNode)
node_x.max_end = max(max(node_x.left.max_end, node_x.right.max_end), node_x.inter[1])
node_y.max_end = max(max(node_y.left.max_end, node_y.right.max_end), node_y.inter[1])
```

例如完整的左旋操作：

```python
# 辅助操作：左旋。返回替代了 node 的新结点
# 时间复杂度 O(1)
def _left_rotate(self, node_x):
    # 对 x 进行左旋，即让 x 的右孩子 y (x.right) 成为 x 的父结点，且 x 等于 y.left。
    # 而 y 结点原本的左孩子变为新 x 的右孩子
    if isinstance(node_x, TreeNode) and isinstance(node_x.right, TreeNode):
        # 如果 x 是 BST 树根，那么树根要更换
        if node_x == self.bst:
            self.bst = node_x.right

        # 调整树结构
        node_y = node_x.right
        node_y.parent = node_x.parent  # 设置 node_y 的父结点（互相关联）
        if isinstance(node_x.parent, TreeNode):
            if node_x == node_x.parent.left:
                node_x.parent.left = node_y
            else:
                node_x.parent.right = node_y

        node_x.right = node_y.left  # y 结点原本的左孩子变为新 x 的右孩子
        if isinstance(node_y.left, TreeNode):
            node_y.left.parent = node_x

        node_y.left = node_x
        node_x.parent = node_y

        # 维护区间树的属性 max_end (注意先更新此时的子结点 node_x, 后更新 node_y)
        # 对某一个结点进行 max_end 维护的总时间复杂度为 O(log n)，不增加渐近量级
        assert isinstance(node_x.left, TreeNode) and isinstance(node_x.right, TreeNode)
        assert isinstance(node_y.left, TreeNode) and isinstance(node_y.right, TreeNode)
        node_x.max_end = max(max(node_x.left.max_end, node_x.right.max_end), node_x.inter[1])
        node_y.max_end = max(max(node_y.left.max_end, node_y.right.max_end), node_y.inter[1])

        # 返回替代了 node 的结点 node_y
        return node_y
    else:
        return None
```

### 插入

```python
# 根据 TreeNode 对象增加结点
# 增加后（每次都增加叶结点），调用 rb_insert_fixup 维护红黑性质
# 时间复杂度 O(log n) 与树高有关
def interval_insert(self, insert_node):
    assert isinstance(insert_node, TreeNode)
    insert_interval = insert_node.inter
    assert isinstance(insert_interval, tuple) and len(insert_interval) == 2
    assert insert_interval[0] <= insert_interval[1]
    insert_node.left = self.nil
    insert_node.right = self.nil
    insert_node.color = True
    if self.is_bst_empty:
        # 如果当前 BST 为空，则直接设置 self.bst 结点，完成插入
        insert_node.parent = self.nil
        insert_node.color = False
        self.bst = insert_node
        self.is_bst_empty = False
    else:
        ptr = self.bst  # 用 ptr 指针从 root 结点（一般设为 self.bst）开始向下搜索插入位置
        ptr_p = self.bst.parent  # ptr_p 记录 ptr 的父亲
        # 插入过程中维护区间树的 max_end 属性
        while isinstance(ptr, TreeNode) and ptr != self.nil:
            ptr_p = ptr
            # ptr 会是新结点的祖先结点，所以根据高端点 决定是否需要更新本结点的 max_end
            if insert_interval[1] > ptr.max_end:
                ptr.max_end = insert_interval[1]
            # 根据低端点 (即 key) 来决定往左还是往右插入
            if insert_interval[0] <= ptr.key:
                ptr = ptr.left
            else:
                ptr = ptr.right

        # 根据 key 决定该插入到左边还是右边
        if insert_node.key <= ptr_p.key:
            ptr_p.left = insert_node
        else:
            ptr_p.right = insert_node
        insert_node.parent = ptr_p

        self._rb_insert_fixup(insert_node)  # 插入后维护红黑性质
```

原本的 `_rb_insert_fixup` 函数无需改动。

### 删除

按结点 TreeNode 对象删除结点，先判断某结点是否存在：

```python
# 根据 TreeNode 精确匹配结点，用于删除结点时检查某结点是否存在于树中
# 如果搜索到了，则返回 True，如果搜索不到，则返回 False
def exact_search(self, target_node):
    if isinstance(self.bst, TreeNode) and isinstance(target_node, TreeNode):
        ptr = self.bst
        while isinstance(ptr, TreeNode) and ptr != self.nil:
            if target_node == ptr:
                # 找到了目标结点，返回此 TreeNode
                return True
            elif target_node.key < ptr.key:
                # 如果新结点 key 值小于当前结点，则应该往左走
                ptr = ptr.left
            else:
                # 如果新结点 key 值大于当前结点，则应该往右走
                ptr = ptr.right
        # 如果出了循环、到了这一步，表示找不到
        return False
    else:
        # 找不到目标结点
        return False
```

删除某结点后，逐级向上维护 max\_end 属性：

```python
# 删除某结点后，逐级向上维护 max_end 属性
# 时间复杂度 O(log n) 与树高有关
def _interval_delete_fix_max(self, node):
    ptr = node
    while isinstance(ptr, TreeNode) and ptr != self.nil:
        assert isinstance(ptr.left, TreeNode) and isinstance(ptr.right, TreeNode)
        ptr.max_end = max(max(ptr.left.max_end, ptr.right.max_end), ptr.inter[1])
        ptr = ptr.parent
```

原本的 `_rb_delete_fixup` 函数无需改动。

## 代码范例

### Python

Python 环境：Python 3.7

[GitHub Code Link](https://github.com/YuweiYin/Code_Play/blob/master/Algorithm-Essence/data-structure/interval-tree.py)

## 参考资料

- Introduction to Algorithm (aka CLRS) Third Edition - Chapter 14
