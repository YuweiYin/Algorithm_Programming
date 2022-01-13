# Algorithm - Data Structure - Splay Tree

By [YuweiYin](https://yuweiyin.github.io/)

## 简介

伸展树 Splay Tree 是由 Sleator 和 Tarjan 提出的，也是一种 [二叉搜索树](./binary-search-tree) (Binary Sort/Search Tree, BST) 的变形。它可以“**自我调整**”，不需要明确的平衡条件（如 [AVL 树](./avl-tree)中的树高/平衡因子、[红黑树](./red-black-tree)中的结点颜色、[Treap 树](./treap)中的优先级）来维持平衡。取而代之的是，每次存取时在树内进行 splay 伸展操作（涉及左/右旋转）。在一棵有 n 个结点的树上，每个操作的**摊还代价**是 O(log n)。

伸展树 Splay Tree 的**核心思想是**：由于刚刚被访问的结点很可能**再次被访问**，因此搜索 search 操作定位目标结点后，需要把该结点**移至树根**。这种思想也符合著名的“**二八法则**”，它正是利用了 **数据访问的局部性** 这个重要的经验性结论。

另外，在插入新结点之后，对新结点要调用 splay 伸展操作；在删除结点之后，对被删结点的父结点要调用 splay 伸展操作。从而调整树的平衡性。

## 设计 & 细节


### 建立 Splay Tree 树

以 kv_array 中的每个元素为 [key, value] 数组，构建树结点。树结点设计如下：

```python
class TreeNode:
    def __init__(self, key=0, val=0):
        self.key = key       # 键，按键构造 BST 树，并进行搜索/增添/删除
        self.val = val       # 值，树结点存储的值，可以为任意对象
        self.left = None     # 左孩子指针
        self.right = None    # 右孩子指针
        self.parent = None   # 父结点指针
        self.is_left = True  # True 则表示自己是父结点的左孩子(默认)，否则为右孩子
```

Splay Tree 类成员属性如下：

```python
class SplayTree:
    # 构造 Splay Tree 即普通的二叉树
    # 时间复杂度 O(n)
    def __init__(self, kv_array):
        self.bst = None             # 二叉搜索树结构，树根
        self.sorted_key_list = []   # 已排好序的 key 列表
```

与 [AVL](avl-tree)、[RBT](./red-black-tree)、[Treap](./treap) 树的建立方式相同，Splay Tree 也是循环调用插入函数，逐步建立 Splay Tree 树。时间复杂度 O(n log n)

### 搜索

```python
def splay_search(self, search_key)
```

### 辅助操作：从结点开始伸展、移动到树根

1 型 展开操作：Splay Tree 搜索/插入/删除结点之后，仅考虑单层情况，逐级向上把该结点移至树根

```python
# 1 型 展开操作：Splay Tree 搜索/插入/删除结点之后，仅考虑单层情况，逐级向上把该结点移至树根
# 时间复杂度 O(log n) 与树高有关
# 根据当前结点是其父结点的左孩子还是右孩子，分 2 种情况，用旋转操作来调整平衡
def _splay_1(self, node):
    if isinstance(node, TreeNode):
        if isinstance(node.parent, TreeNode):
            # 当前结点的父结点存在
            if node.is_left:
                # 当前结点是其父结点的左孩子，则右旋其父
                node = self.right_rotate(node.parent)
            else:
                # 当前结点是其父结点的右孩子，则左旋其父
                node = self.left_rotate(node.parent)
            if node is not None and isinstance(node, TreeNode) and \
                    isinstance(node.parent, TreeNode):
                # 如果父结点仍然存在，则递归、继续往上调整
                self._splay_1(node)
            else:
                return
        else:
            # 当前结点的父结点为非树结点，可终止
            return
    else:
        # 当前结点为非树结点，可终止
        return
```

2 型 展开操作（**更优、树更平衡**）：Splay Tree 搜索/插入/删除结点之后，考虑两层情况，逐级向上把该结点移至树根

```python
# 2 型 展开操作：Splay Tree 搜索/插入/删除结点之后，考虑两层情况，逐级向上把该结点移至树根
# 时间复杂度 O(log n) 与树高有关
# 根据当前结点是其父结点的左孩子还是右孩子，以及父结点是爷爷结点的左孩子还是右孩子
# 分 4 种情况，用旋转操作来调整平衡
def _splay_2(self, node):
    if isinstance(node, TreeNode):
        if isinstance(node.parent, TreeNode):
            if isinstance(node.parent.parent, TreeNode):
                # 当前结点的父结点和爷爷结点均存在
                if node.is_left:
                    if node.parent.is_left:
                        # LL 左左型，先旋转爷爷结点，再旋转父结点
                        self.right_rotate(node.parent.parent)
                        node = self.right_rotate(node.parent)
                    else:
                        # RL 右左型，先旋转父结点，再旋转爷爷结点
                        node = self.right_rotate(node.parent)
                        node = self.left_rotate(node.parent)
                else:
                    if node.parent.is_left:
                        # LR 左右型，先旋转父结点，再旋转爷爷结点
                        node = self.left_rotate(node.parent)
                        node = self.right_rotate(node.parent)
                    else:
                        # RR 右右型，先旋转爷爷结点，再旋转父结点
                        self.left_rotate(node.parent.parent)
                        node = self.left_rotate(node.parent)
                if node is not None and isinstance(node, TreeNode) and \
                        isinstance(node.parent, TreeNode):
                    # 如果父结点仍然存在，则递归、继续往上调整
                    self._splay_2(node)
                else:
                    return
            else:
                # 当前结点的爷爷结点为非树结点，表示父结点为树根
                # 则将当前结点移至树根
                if node.is_left:
                    # 当前结点是其父结点的左孩子，则右旋其父
                    node = self.right_rotate(node.parent)
                else:
                    # 当前结点是其父结点的右孩子，则左旋其父
                    node = self.left_rotate(node.parent)
                if node != self.bst:
                    # 不应走此分支
                    print('_splay_after_search_2: Error Path')
                    return
        else:
            # 当前结点的父结点为非树结点，可终止
            return
    else:
        # 当前结点为非树结点，可终止
        return
```

- 时间复杂度 O(log n) 与树高有关

### 辅助操作：左旋

```python
def left_rotate(self, node_x)
```

- 与 RBT/Treap 的左旋操作完全相同。只有 AVL 树在旋转时要维护结点的高度属性
- 对 node 结点 x 而言，将 x 左旋，意味着：
    - 让 x 的右孩子 y (x.right) 成为 x 的父结点，且 x 等于 y.left。
    - 而 y 结点原本的左孩子变为新 x 的右孩子
    - 注意：如果将 BST 树根旋下来了，则需要更换树根

### 辅助操作：右旋

```python
def right_rotate(self, node_x)
```

- 与 RBT/Treap 的右旋操作完全相同。只有 AVL 树在旋转时要维护结点的高度属性
- 对 node 结点 x 而言，将 x 右旋，意味着：
    - 让 x 的左孩子 y (x.left) 成为 x 的父结点，且 x 等于 y.right。
    - 而 y 结点原本的右孩子变为新 x 的左孩子
    - 注意：如果将 BST 树根旋下来了，则需要更换树根

### 插入

- 时间复杂度 O(log n) 与树高有关

```python
def splay_insert(self, insert_key, insert_val)
```

### 删除

- 时间复杂度 O(log n) 与树高有关

```python
def splay_delete(self, delete_key)
```

实际执行的删除函数，可能递归

```python
def _splay_delete(self, root, delete_key)
```

### 最小值 min\_bst(root)

- 找到一棵以 root 为根的 BST/SplayTree 中的最小值结点（一路向左）
- 时间复杂度 O(log n) 与树高有关

### 最大值 max\_bst(root)

- 找到一棵以 root 为根的 BST/SplayTree 中的最大值结点（一路向右）
- 时间复杂度 O(log n) 与树高有关

### 前驱 predecessor(node)

- 找到在 BST 中 node 结点的前驱结点，即：其左子树中的最大值
- 时间复杂度 O(log n) 与树高有关

### 后继 successor(node)

- 找到在 BST 中 node 结点的后继结点，即：其右子树中的最小值
- 时间复杂度 O(log n) 与树高有关

### 检测是否为 BST check\_bst(root)

- 检查一棵以 root 为根的二叉树是否为 BST
- 时间复杂度 O(n)

## 代码范例

### Python

Python 环境：Python 3.7

[GitHub Code Link](https://github.com/YuweiYin/Code_Play/blob/master/Algorithm-Essence/data-structure/splay-tree.py)

## 参考资料

- MIT 6.854J Advanced Algorithms - [Lecture 04, 09/13: Splay Trees](https://www.youtube.com/watch?v=QnPl_Y6EqMo)
