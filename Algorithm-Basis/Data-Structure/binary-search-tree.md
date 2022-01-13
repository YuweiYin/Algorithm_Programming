# Algorithm - Data Structure - Binary Sort/Search Tree

By [YuweiYin](https://yuweiyin.github.io/)

## 简介

二叉排序/搜索树 (Binary Sort/Search Tree, BST)

- BST 是一棵二叉树
    - 对于 BST 中的**任一**结点 node，其左右子树也均为 BST。
    - 其**左子树** node->left 中的**所有**结点 key 值都**小于等于** node 结点的值 node->key；
    - 其**右子树** node->right 中的**所有**结点 key 值都**大于** node 结点的值 node->key。
    - BST 的**中序遍历**结果即为所有数据的**升序排列**。

## 场景

BST 主要用于组织数据的存储结构，以高效实现如下三种功能：

- search(key)：按 key 查找/搜索元素
- insert(key)：按 key 插入元素
- delete(key)：按 key 删除元素

使用 BST 数据结构，最关心的操作一般是 search，但 insert 和 delete 操作也有可能较为频繁，BST 能够同时权衡三者。

## 场景分析

### 无序的数组/列表结构

- 无序数组建立，时间复杂度为 O(n)，空间复杂度为 O(n)
- search 操作，需要扫描数组、逐个比较，时间复杂度为 O(n)
- insert 操作，只要数组空间有剩余，那么可以直接插入尾部，时间复杂度为 O(1)
- delete 操作，需要扫描数组、逐个比较，找到目标元素 x 后，再把 x 之后的元素逐个向左挪动，时间复杂度为 O(n)

### 单链表结构

- 单链表建立，时间复杂度为 O(n)，空间复杂度为 O(n)
- search 操作，需要扫描链表、逐个比较，时间复杂度为 O(n)
- insert 操作，可以直接在首部（头指针）处插入，时间复杂度为 O(1)
- delete 操作，需要扫描数组、逐个比较，找到目标元素 x 后，再把 x 前一个元素的 next 指针改动，时间复杂度为 O(n)

### 无序的数组/列表结构

如果用前述无序数组或链表处理，其搜索的时间复杂度为 O(n)，假设一次比较的耗时为 10^(-6) 秒，且数据量级达到了 10^7，即千万级别，那么一次搜索操作可能就要耗费近 10 秒，这一般是难以忍受的。

如果提前把数组排序：

- 有序数组建立（[排序](../sort/)），时间复杂度为 O(n log n)，空间复杂度为 O(n)
- search 操作，执行二分查找 Binary Search，时间复杂度为 O(log n)
- insert 操作，执行二分查找定位插入的位置 index，但其后需要把 index 之后的元素全部往右挪动，因此总时间复杂度为 O(n)
- delete 操作，类似于 insert 操作，执行二分查找定位元素的位置 index，但其后需要把 index 之后的元素全部往左挪动，总时间复杂度为 O(n)

### BST

而 BST 能同时权衡这三种操作，将其（平均）时间复杂度均降到 O(log n)，大幅提升了总体性能。

- 建立 BST 时间复杂度为 O(n log n)，空间复杂度为 O(n)，可动态增删结点
- search 操作：
    - 如果当前结点值 *等于/小于/大于* 目标值则 *返回结果/向左搜索/向右搜索*
    - 如果最终为空则表示找不到
    - 时间复杂度为 O(log n)
- insert 操作：
    - 搜索方式同 search 操作，找到插入位置（叶结点 x）
    - 进行插入：如果新结点 new_node 的值小于等于 x 的值，则插入为 x 的左孩子（即 `new_node = x->left`）；否则插入为 x 的右孩子。
    - BST 一般不考虑增添结点之后，树的平衡操作。
    - 时间复杂度为 O(log n)
- delete 操作：
    - 搜索方式同 search 操作，找到欲删除的结点
    - 如果找不到，则返回空；如果找到了，则删除它，并**调整树结构**。
    - 时间复杂度为 O(log n)

注意：BST 在处理 search、insert 和 delete 操作时，遍历的路径长度至多为树高，因此如果树的**平衡性**得到保证，则树高为 O(log n)，从而使得这三种操作的时间复杂度均为 O(log n)。

但原始的 BST 本身不具备保证平衡性的操作，树是否平衡完全看增删结点的顺序，[AVL 树](./avl-tree) 即为 BST 的改进，保证了树的平衡性，从而保证不会出现 BST 的最坏情况。

最坏情况是 BST 树极度不平衡，退化成了一条链。在这种情况下，前述三个操作的时间复杂度为 O(n)。

## 设计 & 细节

以计算区间最小值为例，展开下文叙述。

### 建立 BST

以 array 中的每个元素为 key，调用 insert(key) 插入，逐步建立 BST。时间复杂度 O(n log n)

以 `array = [15, 10, 20, 8, 12, 17, 25]` 为例，建立 BST 如下：

![bst-1](/img/info-technology/algorithm/data-structure/bst-1.png)

图中结点内部的值即为 key，左侧的数字即为中序遍历（升序排列）数组的下标。

以 kv_array 中的每个元素为 [key, value] 数组，构建树结点。树结点设计如下：

```python
class TreeNode:
    def __init__(self, key=0, val=0):
        self.key = key      # 键，按键构造 BST 树，并进行搜索/增添/删除
        self.val = val      # 值，树结点存储的值，可以为任意对象
        self.left = None    # 左孩子
        self.right = None   # 右孩子
        self.parent = None  # 父结点。便于删除、以及其它逐层向上的调整操作
```

### 搜索 search(key)

根据前面构造好的 BST，讨论搜索 search 操作。

以查找 key=17 为例，即 search(17)：

- 从根结点出发，比较 17 和 15，发现 17 > 15，故进入 15 的右孩子 20；
- 比较 17 和 20，发现 17 < 20，故进入 20 的左孩子 17；
- 比较 17 和 17，发现 17 == 17，匹配成功，返回 key=17 的 TreeNode 结点。

以查找 key=11 为例（查找失败），即 search(11)：

- 从根结点出发，比较 11 和 15，发现 11 < 15，故进入 15 的左孩子 10；
- 比较 11 和 10，发现 11 > 10，故进入 10 的右孩子 12；
- 比较 11 和 12，发现 11 < 12，故进入 12 的左孩子 None；
- 发现当前结点为 None，结束搜索，目标结点不存在。


### 插入 insert(key)

根据前面构造好的 BST，讨论插入 insert 操作。

以插入 key=17 为例，即 insert(17)：

- 从根结点出发，比较 17 和 15，发现 17 > 15，故进入 15 的右孩子 20；
- 比较 17 和 20，发现 17 <= 20，故进入 20 的左孩子 17；
- 比较 17 和 17，发现 17 <= 17，故进入 17 的左孩子 None；
- 发现当前结点为 None，找到了应插入的位置，于是构造 key=17 的 TreeNode 结点作为新结点。

以插入 key=11 为例（查找失败），即 insert(11)：

- 从根结点出发，比较 11 和 15，发现 11 <= 15，故进入 15 的左孩子 10；
- 比较 11 和 10，发现 11 > 10，故进入 10 的右孩子 12；
- 比较 11 和 12，发现 11 <= 12，故进入 12 的左孩子 None；
- 发现当前结点为 None，找到了应插入的位置，于是构造 key=11 的 TreeNode 结点作为新结点。

### 删除 delete(key)

删除 delete 操作的过程：

- 一开始的过程类似于 search 操作，如果找不到目标结点，则不执行删除操作。
- 如果匹配成功，找到了应该删除的 TreeNode 目标结点，那么根据目标结点的左右孩子数量来进行不同的处理
    - 如果目标结点没有孩子，直接删除目标结点
    - 如果目标结点仅有右孩子，则删除目标结点，并把其父结点与其右孩子结点链接起来
    - 如果目标结点仅有左孩子，则删除目标结点，并把其父结点与其左孩子结点链接起来
    - 如果目标结点左右孩子均有：
        - 先把目标结点的值改为 **其右孩子子树中的最小值（一路向左）**，
        - 然后**递归**，在目标结点的右孩子子树中，删除前述最小值结点
        - 处理的深度至多为树高，每次处理为常数时间复杂度，因此总时间复杂度仍为 O(log n)，如果树比较**平衡**。

### 检查一棵二叉树是否为 BST

- 从根至叶，递归地对每个结点判断四个条件是否同时满足：
    - 当前结点的左孩子 (如果有) 的值小于等于当前结点的值
    - 当前结点的右孩子 (如果有) 的值大于当前结点的值
    - （递归）当前结点的左孩子 (如果有) 满足 BST 性质
    - （递归）当前结点的右孩子 (如果有) 满足 BST 性质

注意：当搜索到 None 空结点时，应该返回 True。详细见下文代码的 check_bst(root) 方法。

检查一棵二叉树是否为 BST 的时间复杂度为 O(n)。

### 最大值/最小值/前驱/后继

- max_bst(root)
    - 找到一棵以 root 为根的 BST 中的最大值结点（一路向右）。
- min_bst(root)
    - 找到一棵以 root 为根的 BST 中的最小值结点（一路向左）。
- predecessor(node)
    - 找到在 BST 中 node 结点的前驱结点，即：其左子树中的最大值。
- successor(node)
    - 找到在 BST 中 node 结点的后继结点，即：其右子树中的最小值。

上述四个操作的时间复杂度均为 O(log n)，与树高有关。

### 实现细节

为了便于修改、调整树结构，树结点的指针域除了左右孩子外，还有父结点。

## 代码范例

### Python

Python 环境：Python 3.7

[GitHub Code Link](https://github.com/YuweiYin/Code_Play/blob/master/Algorithm-Essence/data-structure/binary-search-tree.py)

## 参考资料

- [Youtube - Data structures: Binary Search Tree](https://www.youtube.com/watch?v=pYT9F8_LFTM)
- [Youtube - Binary search tree - Implementation in C/C++](https://www.youtube.com/watch?v=COZK7NATh4k)
- [Youtube - Delete a node from Binary Search Tree](https://www.youtube.com/watch?v=gcULXE7ViZw)
- [Youtube - Check if a binary tree is binary search tree or not](https://www.youtube.com/watch?v=yEwSGhSsT0U)
