# Algorithm - Data Structure - Adelson-Velsky-Landis Tree

By [YuweiYin](https://yuweiyin.github.io/)

## 简介

AVL 树 (Adelson-Velsky-Landis Tree)，是最早发明的自平衡二叉查找树 (Self-Balanced Binary Search Tree)，它于 1962 年被发表于论文《An algorithm for the organization of information》。此数据结构名称为其三位发明者的名字缩写。

[二叉搜索树](./binary-search-tree) (Binary Sort/Search Tree, BST) 在处理 search、insert 和 delete 操作时，遍历的路径长度至多为树高，因此如果树的**平衡性**得到保证，则树高为 O(log n)，从而使得这三种操作的时间复杂度均为 O(log n)。

最坏情况是 BST 树极度不平衡，退化成了一条链。在这种情况下，前述三个操作的时间复杂度为 O(n)。

但原始的 BST 本身不具备保证平衡性的操作，树是否平衡完全看增删结点的顺序，AVL 树即为 BST 的改进，**保证了树的平衡性**，从而保证不会出现 BST 的最坏情况。

- AVL 保证树平衡性的核心思想如下：
    - 维持每个结点的左右子树高度差距不超过 1。（因此每个树结点需要维护自己的**树高属性**）
    - 在增删树结点、改动树结构时，检测**平衡因子**。如果破坏了树平衡性，那就“纵向”调整树结构，直至平衡。
    - 这种“纵向”调整具体的实现是“**左旋**”和“**右旋**”操作，
    - 前述的调整路径长度至多为**树高**，所以增删结点操作的整体时间复杂度仍为 O(log n)，仅仅是增加了一些常数因子。

### AVL 树的应用

AVL 树由其稳定高效，被广泛使用。

它可以用于实现优先队列 Priority Queue。（另外，堆 Heap 也可以实现优先队列。）

Solaris 操作系统会使用 AVL 树结构来管理页表中已访问过的页面，即缓存机制，以便迅速地再次访问（搜索/查找）。另外，其它操作系统，如 Linux 和 Windows，也都使用类似 AVL 的数据结构完成此功能。

![avl-solaris-segment-data-structure](/img/info-technology/algorithm/data-structure/avl-solaris-segment-data-structure.png)

## 设计 & 细节

### 建立 AVL 树

以 kv_array 中的每个元素为 [key, value] 数组，构建树结点。树结点设计如下：

```python
class TreeNode:
    def __init__(self, key=0, val=0):
        self.key = key       # 键，按键构造 BST/AVL 树，并进行搜索/增添/删除
        self.val = val       # 值，树结点存储的值，可以为任意对象
        self.height = 1      # 初始时树高为 1
        self.left = None     # 左孩子指针
        self.right = None    # 右孩子指针
        self.parent = None   # 父结点指针
```

AVL 树的建立就是循环调用 insert(key) 插入，逐步建立 AVL 树。时间复杂度 O(n log n)

### 搜索 search(key)

- search 操作与 BST 的 search 没有区别：
    - 如果当前结点为空，则返回 None，表示查询不到目标结点
    - 如果当前结点的 key 值等于目标 key 值，则查询到，返回结点
    - 如果当前结点的 key 值小于目标 key 值，则进入左子树，递归搜索
    - 如果当前结点的 key 值大于目标 key 值，则进入右子树，递归搜索
- **查询不会影响树结构**，所以不会调用关于树平衡性的辅助操作。

### 辅助操作：平衡性检测 balanced\_factor(node)

判断 node 结点是否平衡，即计算其左右子树的平衡因子 (Balanced Factor) 差距。

如果差距不大于 1，则平衡，否则不平衡，需要通过旋转操作来调整至平衡。

这里返回 node 左子树高度减去 node 右子树高度的值，作为 node 的平衡因子。

### 辅助操作：左旋 `left_rotate(node)`

- 对 node 结点 x 而言，将 x 左旋，意味着：
    - 让 x 的右孩子 y (x.right) 成为 x 的父结点，且 x 等于 y.left。
    - 而 y 结点原本的左孩子变为新 x 的右孩子
    - 注意维护三个指针，以及 height 属性

![tree-rotate-1](/img/info-technology/algorithm/data-structure/tree-rotate-1.png)

### 辅助操作：右旋 right\_rotate(node)

- 对 node 结点 x 而言，将 x 右旋，意味着：
    - 让 x 的左孩子 y (x.left) 成为 x 的父结点，且 x 等于 y.right。
    - 而 y 结点原本的右孩子变为新 x 的左孩子
    - 注意维护三个指针，以及 height 属性

### 辅助操作：平衡性维护 maintain\_balance(node)

- 从 node 结点开始，逐级向上进行 height 修改，以及平衡性调整
- 两种情况下会调用：1. 插入结点后；2."确实地"删除结点后。
- 时间复杂度 O(log n) 与树高有关
- **逐层向上调整**，根据平衡因子 分四种情况，用旋转操作来调整平衡

不平衡出现时，有如下四种情况：

- case 1：**LL 左左结构** - node 的平衡因子 bf=2 且其左孩子的平衡因子 bf=1
    - 把 node 右旋一次即可
- case 2：**LR 左右结构** - node 的平衡因子 bf=2 且其左孩子的平衡因子 bf=-1
    - 先把 node 的左孩子左旋一次，整体成为左左结构，再把 node 右旋一次即可
- case 3：**RL 右左结构** - node 的平衡因子 bf=-2 且其左孩子的平衡因子 bf=1
    - 先把 node 的右孩子右旋一次，整体成为右右结构，再把 node 左旋一次即可
- case 4：**RR 右右结构** - node 的平衡因子 bf=-2 且其左孩子的平衡因子 bf=-1
    - 把 node 左旋一次即可

注意：如果旋转时影响了整个的 BST/AVL 树根，则需要更换树根

另外，还要维护每个结点的 height 属性。

### 插入 insert(key)

以 `kv_array = [[1, 100], [2, 200], [3, 300], [7, 700], [8, 800], [9, 900], [4, 400]]` 为例，对于 kv_array 中的每个列表元素，其中的首元素为 key，次元素为 value。key 必须要是具备全序关系，而 value 可以为任何对象。

**以插入方式逐步建立 AVL**，如下图所示：

![avl-1](/img/info-technology/algorithm/data-structure/avl-1.png)

插入新结点后，要调用 `maintain_balance` 辅助操作，逐步向上根据平衡性来调整树结构。

### 删除 delete(key)

AVL 树的删除 delete 操作与普通 BST 的删除操作类似，但是有区别：

- 在删除一个既有左孩子又有右孩子的中间结点时，需要考虑当前结点的平衡因子
    - 由于删除前的 AVL 树中，所有结点都是满足平衡性的，因此每个结点的平衡因子只可能是 0 或 1 或 -1。
    - 如果平衡因子为 0 或 -1，表示右孩子比左孩子更高，则与普通 BST 做法相同：
        - 先找出右孩子中的最小元素（右子树中一路向左），替换当前结点的值
        - 然后递归地在右子树中删除该结点
    - 如果平衡因子为 1，表示左孩子比右孩子更高，则从左子树中删除元素：
        - 先找出左孩子中的最大元素（左子树中一路向右），替换当前结点的值
        - 然后递归地在左子树中删除该结点
- 在“确实地”删除了结点后，调用 maintain_balance 辅助操作，检查被删除结点的**所有祖先结点**的平衡性。
    - 前述替换并不会影响当前结点的平衡性，故不用逐步往上检查平衡性。
    - 每次 delete 操作时，至多有一个被“确实”删除的结点。
    - 所谓的“确实地”删除有三种情况：
        - 当前结点仅有左孩子
        - 当前结点仅有右孩子
        - 当前结点没有孩子（为叶结点）

例如：在前述已经建立好的 AVL 树中，删除 key=9 的结点：

![avl-2](/img/info-technology/algorithm/data-structure/avl-2.png)

其它 BST 中的基本操作，如找 最大值、最小值、前驱、后继、判断一棵树是否为 BST 等，都不在此赘述。

## AVL 树高分析

以 `N_{h}` 表示高度为 h 的子树里的元素个数。

边界情况：当 h 为常数量级 O(1) 时：`N_{O(1)} = O(1)`

考虑高度为 h 的树的 root 结点及其左右子树，可拆分为：`N_{h} = 1 + N_{h-1} + N_{h-2}`

上式的计算方式与 Fibonacci 数的计算类似，有 `N_{h} > F_{h} = \Phi^{h} / \sqrt{5}`，其中 `\Phi` 为黄金比例，约为 1.618。

于是有 h 约等于 `1.440 log_{\Phi} n`，故 AVL 树高的量级保证为 O(log n)。

## 代码范例

### Python

Python 环境：Python 3.7

[GitHub Code Link](https://github.com/YuweiYin/Code_Play/blob/master/Algorithm-Essence/data-structure/avl-tree.py)

## 参考资料

- MIT 6.006 Introduction to Algorithms, Fall 2011
    - [Erik Demaine - AVL Trees, AVL Sort](https://www.youtube.com/watch?v=FNeL18KsWPc)
    - [Victor Costan - R6. AVL Trees](https://www.youtube.com/watch?v=IWzYoXKaRIc)
