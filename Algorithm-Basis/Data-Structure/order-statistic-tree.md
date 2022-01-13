# Algorithm - Data Structure - Order Statistic Tree

By [YuweiYin](https://yuweiyin.github.io/)

## 简介

顺序统计树 (Order Statistic Tree, OST)

[顺序统计](../sort/median-order-statistic)：n 个元素集合中的第 i ($ i \in {1, 2, ..., n} $) 个顺序统计量就是简单地规定为集合中的具有第 i 小关键字的元素。对于一个无序的集合，能够在 $ \Theta(n) $ 的时间内确定任何的顺序统计量。可以通过修改、扩张 [红黑树](./red-black-tree) (Red Black Tree, RBT) 数据结构，构建顺序统计树，在 $ O(log n) $ 时间内确定任何的顺序统计量。此外，还可以在 $ O(log n) $ 时间内计算一个元素的**秩**，即它在集合线性序中的位置。

顺序统计树只是简单地在每个结点上存储附加信息的一棵红黑树。在红黑树的结点 x 中，除了通常属性 x.key、x.val、x.color、x.left、x.right、x.parent 之外，还包括另一个属性 x.size。这个属性包含了以 x 为根的子树 (包括 x 本身) 的 (内)结点数，即这棵子树的大小。如果定义哨兵的大小为 0，也就是设置 T.nil.size 为 0，则有等式：x.size = x.left.size + s.right.size + 1

顺序统计树的示意图如下：

![ost-1](/img/info-technology/algorithm/data-structure/ost-1.png)

在一棵顺序统计树中，并不要求关键字各不相同。（例如，上图中的树就包含了两个值为 14 的关键字和两个值为 21 的关键字。）在有相等关键字的情况下，前面秩的定义便不再适合。为此，可以通过定义一个元素的秩为在中序遍历树时输出的位置，来消除原顺序统计树定义的不确定性。如上图所示，存储在黑色结点的关键字 14 的秩为 5，存储在红色结点的关键字 14 的秩为 6。

### 建立顺序统计树

以 kv_array 中的每个元素为 [key, value] 数组，构建树结点。树结点设计如下：

```python
class TreeNode:
    def __init__(self, key=0, val=0, color=True):
        self.key = key       # 键，按键构造 BST/RBT 树，并进行搜索/增添/删除
        self.val = val       # 值，树结点存储的值，可以为任意对象
        self.color = color   # 结点的颜色，True 代表红色(默认)，False 代表黑色
        self.left = None     # 左孩子指针
        self.right = None    # 右孩子指针
        self.parent = None   # 父结点指针
        '''上面是红黑树原本的所需的树结点属性'''
        '''下面是顺序统计树扩张红黑树功能所需的属性'''
        self.size = 1        # 以本结点为根的子树 (包括本结点) 的 (内)结点数，即这棵子树的大小/总结点数
        # rank = x.left.size + 1 就是本结点的秩 (第 rank 小顺序统计量)
        # 红黑树/顺序统计树的哨兵 self.nil 的 size 设置为 0
```

### 查找具有给定秩的元素

在说明插入和删除过程中如何维护 size 信息之前，先来讨论利用这个附加信息来实现的两个顺序统计查询。首先一个操作是对具有给定秩的元素的检索。过程 os\_select(node, target\_rank) 返回一个指针，其指向以 node 为根的子树中包含第 target\_rank 小关键字的结点。为找出顺序统计树 T 中的第 target\_rank 小关键字，调用 os\_select(T.root, target\_rank)。

```python
# 查找具有给定秩 target_rank 的元素 (target_rank >= 1)
# 时间复杂度 O(log n)
def os_select(self, target_rank):
    if isinstance(target_rank, int) and target_rank >= 1 and isinstance(self.bst, TreeNode):
        return self._os_select(self.bst, target_rank)
    else:
        # target_rank 取值范围不合法，或者树为空树，找不到目标结点
        return None

# 从以结点 root 为根的子树中 查找具有给定秩 target_rank 的元素
def _os_select(self, root, target_rank):
    # 断言当前结点 root 及其两个孩子都是树结点 (根据红黑树性质)
    assert isinstance(root, TreeNode) and isinstance(root.left, TreeNode) and isinstance(root.right, TreeNode)
    # 如果当前 root 已经移动到了哨兵结点，则找不到目标秩的结点
    if root == self.nil:
        return None
    # 计算以 root 为根的子树中结点 root 的秩 cur_rank
    # root.left.size 是对以 root 为根的子树进行中序遍历后排在 root 之前的结点个数
    cur_rank = root.left.size + 1
    # 如果目标顺序统计量序号 target_rank 等于 cur_rank，
    # 则结点 root 就是第 target_rank 小的元素，返回 root
    if target_rank == cur_rank:
        return root
    # 如果 target_rank < cur_rank，
    # 那么第 target_rank 小元素在 root 的左子树中，因此对 root.left 进行递归调用
    elif target_rank < cur_rank:
        return self._os_select(root.left, target_rank)
    # 如果 target_rank > cur_rank，
    # 那么第 target_rank 小元素在 root 的右子树中，因此对 root.right 进行递归调用
    else:
        # 注意 root 的秩为 cur_rank，表示已经有 cur_rank 个元素比 root.right 小了，
        # 所以在右子树中找第 target_rank - cur_rank 小的元素
        return self._os_select(root.right, target_rank - cur_rank)
```

因为每次递归调用都在顺序统计树中下降一层，os\_select 的总时间最差与树的高度成正比。又因为该树是一棵红黑树，其高度为 $ O(log n) $，其中 n 为树的结点数。所以，对于 n 个元素的动态集合，os\_select 的运行时间为 $ O(log n) $。

### 确定一个元素的秩

给定指向顺序统计树 T 中结点 node 的指针，过程 os\_rank 返回对 T 中序遍历对应的线性序中 node 的位置。

```python
# 根据输入的 node 确定此元素的秩
# 给定指向顺序统计树 OST 中结点 node 的指针
# 返回对 OST 中序遍历对应的线性序中 node 的位置
# 时间复杂度 O(log n)
def os_rank_by_node(self, node):
    if isinstance(node, TreeNode):
        # node 的秩是中序遍历次序排在 node 之前的结点数再加上 1 (代表 node 自身)
        # rank 为以结点 y 为根的子树中 node.key 的秩
        rank = node.left.size + 1
        # 如果还未到 OST 树根，则继续往上搜索
        ptr = node
        while ptr != self.bst:
            assert isinstance(ptr.parent, TreeNode)
            # 如果 ptr 所指结点是其父结点的右孩子，
            # 那么它的父结点和 以左兄弟为根的子树的所有结点都排在 ptr 前
            # 所以它的秩需要加上左兄弟的秩 + 1 (代表父结点)
            if ptr == ptr.parent.right:
                assert isinstance(ptr.parent.left, TreeNode)
                rank += ptr.parent.left.size + 1  # 加上左兄弟的秩 + 1 (代表父结点)
                ptr = ptr.parent  # 指针上移
        return rank
    else:
        # 异常输入，返回 -1 秩
        return -1
```

### 左旋/右旋时维护 size

![ost-2](/img/info-technology/algorithm/data-structure/ost-2.png)

在左旋/右旋操作结束后，执行如下命令：

```python
# 维护顺序统计树的属性 size
# 对某一个结点进行 size 维护的总时间复杂度为 O(log n)，不增加渐近量级
node_y.size = node_x.size
node_x.size = node_x.left.size + node_x.right.size + 1
```

完整的左旋操作：

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

        # 维护顺序统计树的属性 size
        # 对某一个结点进行 size 维护的总时间复杂度为 O(log n)，不增加渐近量级
        node_y.size = node_x.size
        node_x.size = node_x.left.size + node_x.right.size + 1

        # 返回替代了 node 的结点 node_y
        return node_y
    else:
        return None
```

右旋时在相同的位置插入相同的两行代码即可。

### 插入时维护 size

寻找插入位置的路径中的所有结点 size += 1

```python
ptr = self.bst           # 用 ptr 指针从 root 结点（一般设为 self.bst）开始向下搜索插入位置
ptr_p = self.bst.parent  # ptr_p 记录 ptr 的父亲
# 插入过程中维护顺序统计树的 size 属性
while isinstance(ptr, TreeNode) and ptr != self.nil:
    ptr_p = ptr
    ptr.size += 1  # 插入路径中的结点 size 均加 1
    if insert_key <= ptr.key:
        ptr = ptr.left
    else:
        ptr = ptr.right
```

`_rb_insert_fixup` 过程无需修改。

### 删除时维护 size

寻找插入位置的路径中的所有结点 size -= 1

```python
# 插入过程中维护顺序统计树的 size 属性
ptr = root               # 用 ptr 指针从 root 结点（一般设为 self.bst）开始向下搜索删除位置
ptr_p = root.parent      # ptr_p 记录 ptr 的父亲
# 删除过程中维护顺序统计树的 size 属性
while isinstance(ptr, TreeNode) and ptr != self.nil:
    ptr_p = ptr          # 跟踪父结点
    ptr.size -= 1        # 删除路径中的结点 size 均减 1
    if delete_key == ptr.key:
        break            # 定位到了目标删除结点
    elif delete_key < ptr.key:
        ptr = ptr.left   # 小则往左
    else:
        ptr = ptr.right  # 大则往右
```

若没有搜索到目标结点，则需要恢复之前被 -1 结点 size

```python
# 若搜索到叶，表示没找到目标结点
if ptr == self.nil:
    # 此时需要把删除路径中的结点 size 均加 1 (恢复成原本的 size)
    ptr = ptr_p
    while isinstance(ptr, TreeNode) and ptr != self.nil:
        ptr.size += 1
        ptr = ptr.parent
    print('提示：删除时，找不到 key 为', delete_key, '的元素')
```

欲删除结点 ptr 的左右孩子均不为空，则将 ptr 替换为其后继。把 ptr 替换为其后继结点 y，修改链接关系和 color（不修改 key、value），最后还要**更新 y 的 size**。

```python
# 现在把 ptr 替换为其后继结点 y，并修改链接关系和 color（不修改 key、value）
self._rb_transplant(ptr, y)
assert isinstance(y, TreeNode)
assert isinstance(y.left, TreeNode) and isinstance(y.right, TreeNode)
y.left = ptr.left
y.left.parent = y
y.color = ptr.color  # y 继承 ptr 的颜色
y.size = y.left.size + y.right.size + 1  # 更新 y 的 size
```

`_rb_delete_fixup` 过程无需修改。

## 代码范例

### Python

Python 环境：Python 3.7

[GitHub Code Link](https://github.com/YuweiYin/Code_Play/blob/master/Algorithm-Essence/data-structure/order-statistic-tree.py)

## 参考资料

- Introduction to Algorithm (aka CLRS) Third Edition - Chapter 14
