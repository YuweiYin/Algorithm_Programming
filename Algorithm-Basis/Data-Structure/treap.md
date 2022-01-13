# Algorithm - Data Structure - Treap

By [YuweiYin](https://yuweiyin.github.io/)

## 简介

堆树/树堆 Treap 是由 Seidel 和 Aragon 提出的。它是 LEDA 内字典的默认实现，LEDA 是一组精心实现的数据结构和算法。

如果讲一个含 n 个元素的集合插入到一棵[二叉搜索树](./binary-search-tree) (Binary Sort/Search Tree, BST) 中，所得到的树可能会相当不平衡，从而导致操作时间变为线性时间复杂度 O(n)。**随机构造**二叉搜索树是**趋向于平衡的**。因此，一般来说，要为一组固定的元素建立一棵平衡树，可以采用一种策略就是**先随机排列**这些元素，然后按照排列的顺序将它们插入到树中。

但是，如果没法同时得到所有的元素，应该如何处理？如果一次收到一个元素，是否仍然能用它们来随机建立一棵二叉搜索树？

一棵 Treap 树是一棵更改了结点排列方式的二叉搜索树。通常，树内的每个结点 x 都有一个关键字值 x.key，用于 BST 排序。另外，还要为每个结点指定 x.priority，它是一个独立选取的随机数。假设所有的优先级都是不同的，而且所有的关键字也是不同的。Treap 树的结点被排列成让关键字遵循二叉搜索树的性质，且优先级遵循最小堆顺序性质：

- 如果 v 是 u 的左孩子，则 v.key < u.key
- 如果 v 是 u 的右孩子，则 v.key > u.key
- 如果 v 是 u 的孩子，则 v.priority > u.priority

这两个性质的结合就是这种树被称为 Treap 树的原因：它同时具有二叉搜索树和堆的特征。

![treap-1](/img/info-technology/algorithm/data-structure/treap-1.png)

假设将已有相应关键字 key 的结点 x1, x2, ..., xn 插入到一棵 Treap 树内，得到的 Treap 树是通过将这些结点及其优先级（**随机**选取的值）顺序插入一棵正常的二叉搜索树形成的，即 xi.priority < xj.priority 表示 xi 在 xj 之前被插入。

可以证明：

- 给定一个已有的相应关键字 key 和优先级 priority（互异）的结点 x1, x2, ..., xn 组成的集合，存在唯一的一棵 Treap 树与这些结点相关联。
- Treap 树的期望高度是 O(log n)，因此在 Treap 内查找一个值所花的时间为 O(log n)。

要将一个新的结点插入到一个已存在的 Treap 树中，要做的第一件事就是将一个随机的优先级赋予这个新结点。然后调用 treap-insert 插入算法，其操作如图所示。

![treap-2](/img/info-technology/algorithm/data-structure/treap-2.png)

![treap-3](/img/info-technology/algorithm/data-structure/treap-3.png)

可以证明：treap-insert 插入算法的期望运行时间是 O(log n)。当在一棵 Treap 树中插入一个结点时，执行旋转的期望次数小于 2。

定义一棵 BST 的**左脊柱**（left spine）是从根结点到有最小关键字 key 的结点的简单路径。换句话说，左脊柱是从根结点开始只包含左边缘的简单路径。对称地，BST 的**右脊柱**（right spine）是从根结点开始只包含右边缘的简单路径。一条脊柱的长度是它包含的结点数目。

![treap-4](/img/info-technology/algorithm/data-structure/treap-4.png)

## 设计 & 细节


### 建立 Treap 树

以 kv_array 中的每个元素为 [key, value] 数组，构建树结点。树结点设计如下：

```python
class TreeNode:
    def __init__(self, key=0, val=0, priority=0):
        self.key = key       # 键，按键构造 BST 树，并进行搜索/增添/删除
        self.val = val       # 值，树结点存储的值，可以为任意对象
        self.priority = priority   # 结点的优先级，用于构建最小堆
        self.left = None     # 左孩子指针
        self.right = None    # 右孩子指针
        self.parent = None   # 父结点指针
        self.is_left = True  # True 则表示自己是父结点的左孩子(默认)，否则为右孩子
```

Treap 类成员属性如下（这里利用的是最小堆，但最大堆也可以）：

```python
class Treap:
    # 构造 Treap
    def __init__(self, kv_array):
        self.bst = None             # 二叉搜索树结构，树根
        self.inf = 0x3f3f3f3f       # 0..inf 是优先级的随机选择范围
        self.used_priority = set()  # 集合，存储当前已经使用过的优先级
        self.sorted_key_list = []   # 已排好序的 key 列表
```

与 [AVL](avl-tree)、[RBT](./red-black-tree) 树的建立方式相同，Treap 也是循环调用插入函数，逐步建立 Treap 树。时间复杂度 O(n log n)

### 搜索

```python
def treap_search(self, search_key)
```

### 辅助操作：左旋

```python
def left_rotate(self, node_x)
```

- 与 RBT 的左旋操作完全相同。只有 AVL 树在旋转时要维护结点的高度属性
- 对 node 结点 x 而言，将 x 左旋，意味着：
    - 让 x 的右孩子 y (x.right) 成为 x 的父结点，且 x 等于 y.left。
    - 而 y 结点原本的左孩子变为新 x 的右孩子
    - 注意：如果将 BST 树根旋下来了，则需要更换树根

### 辅助操作：右旋

```python
def right_rotate(self, node_x)
```

- 与 RBT 的右旋操作完全相同。只有 AVL 树在旋转时要维护结点的高度属性
- 对 node 结点 x 而言，将 x 右旋，意味着：
    - 让 x 的左孩子 y (x.left) 成为 x 的父结点，且 x 等于 y.right。
    - 而 y 结点原本的右孩子变为新 x 的左孩子
    - 注意：如果将 BST 树根旋下来了，则需要更换树根

### 辅助操作：新建并返回具有随机优先级的结点

```python
def create_new_node(self, new_key, new_val)
```

### 辅助操作：插入结点后维护最小堆性质

```python
def _treap_priority_fixup(self, node)
```

- 时间复杂度 O(log n) 与树高有关

### 插入

- 时间复杂度 O(log n) 与树高有关

```python
def treap_insert(self, insert_key, insert_val)
```

### 删除

- 时间复杂度 O(log n) 与树高有关

```python
def treap_delete(self, delete_key)
```

实际执行的删除函数，可能递归

```python
def _treap_delete(self, root, delete_key)
```

### 最小值 min_bst(root)

- 找到一棵以 root 为根的 BST/Treap 中的最小值结点（一路向左）
- 时间复杂度 O(log n) 与树高有关

### 最大值 max_bst(root)

- 找到一棵以 root 为根的 BST/Treap 中的最大值结点（一路向右）
- 时间复杂度 O(log n) 与树高有关

### 前驱 predecessor(node)

- 找到在 BST 中 node 结点的前驱结点，即：其左子树中的最大值
- 时间复杂度 O(log n) 与树高有关

### 后继 successor(node)

- 找到在 BST 中 node 结点的后继结点，即：其右子树中的最小值
- 时间复杂度 O(log n) 与树高有关

### 检测是否为 BST check_bst(root)

- 检查一棵以 root 为根的二叉树是否为 BST
- 时间复杂度 O(n)

## 代码范例

### Python

Python 环境：Python 3.7

[GitHub Code Link](https://github.com/YuweiYin/Code_Play/blob/master/Algorithm-Essence/data-structure/treap.py)

## 参考资料

- Introduction to Algorithm (aka CLRS) Third Edition - Chapter 13 思考题 13-4
