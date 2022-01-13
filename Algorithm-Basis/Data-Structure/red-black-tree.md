# Algorithm - Data Structure - Red-Black Tree

By [YuweiYin](https://yuweiyin.github.io/)

## 简介

红黑树 (Red-Black Tree, RBT)，是一个著名的、被广泛应用的树形数据结构。它是在 1972 年由鲁道夫·贝尔发明的，起初被称之为"对称二叉 B 树"，它的“红黑树”之名是 Leo J. Guibas 和 Robert Sedgewick 于 1978 年发表的一篇论文中得来的。红黑树的操作时间复杂度（平均/最坏）均较低，并且在实践中高效：它可以在 O(log n) 的时间内做查找、插入和删除操作，其中 n 是树中元素的数目。[参考自 Wiki](https://zh.wikipedia.org/wiki/%E7%BA%A2%E9%BB%91%E6%A0%91)

红黑树是对 [二叉搜索树](./binary-search-tree) (Binary Sort/Search Tree, BST) 的改进，它与 [AVL 树](./avl-tree) (Adelson-Velsky-Landis Tree)都属于自平衡二叉查找树 (Self-Balanced Binary Search Tree)，但二者有所区别。

红黑树作为一棵自平衡的二叉搜索树，自然也要满足 BST 的基本性质。

但在平衡性方面，它不像 AVL 树那样维护每个结点的平衡因子，而是改为维护如下五条**红黑性质**：

1. 每个结点要么是红色的，要么是黑色的。
2. 根结点是黑色的。
3. 每个叶结点都是黑色的空结点（NIL 结点）。
4. 每个红色结点的子结点都只能是黑色的。（即：任意两个红色结点不能是直接父子关系。）
5. 从任一结点出发（以该结点为子树的根），到其每个叶结点的所有简单路径 都包含相同数目的黑色结点。

红黑树示例：

![rbt-1](/img/info-technology/algorithm/data-structure/rbt-1.png)

- 在查找/搜索操作上
    - 红黑树与 AVL 树性能几乎没有差别。
- 在插入和删除操作上
    - AVL 树会进行大量的平衡性检测、自叶到根维护平衡因子和树高属性；
    - 而红黑树牺牲了树结构的高度平衡性，只要求一定程度的平衡性约束，从而只用进行较少的维护操作，任何不平衡都能在三次旋转之内解决。
- 由于红黑树维护的五条性质，它保证了树的深度不超过最短路径长度的两倍
- 从而有此结论：一棵有 n 个内部结点的红黑树的高度至多为 `2 log (n+1)`
- 理论分析可知其搜索、插入、删除操作的平均、最坏时间复杂度均为 O(log n)
- 从渐进时间复杂度的角度看，红黑树和 AVL 树的性能是相同的，但红黑树的统计性能比 AVL 树更高。二者均有许多实际应用

实际上插入 AVL 树和红黑树的速度取决于所插入数据的分布

- 如果数据分布较好（有规律），则比较宜于采用 AVL树
- 如果数据比较杂乱，那么往往红黑树效率更优

红黑树典型的用途是实现**关联数组**，它是 Java 中 TreeMap、TreeSet 以及 jdk1.8 后 HashMap 的底层存储结构。另外，Linux 内核的调度系统中，进程运行队列的调度也是使用 RBT 实现的。

## 设计 & 细节

由于红黑树 T 的叶结点均为黑色的 NIL 结点，为了便于处理边界条件，专门设置一个“哨兵” T.nil 结点来代表叶结点 NIL。所有本该指向 NIL 的指针都指向 T.nil，这样还能节省大量存储空间。

该哨兵 T.nil 的 color 属性为 BLACK，其它属性 key、value、is_left 均可设置为 任意值/默认值，而其 parent、left、right 指针均指向自己。

将前面的红黑树 (a) 的叶结点均改为哨兵 T.nil 后，（另外，RBT 树根结点的父结点也指向 T.nil）如下图所示：

![rbt-2](/img/info-technology/algorithm/data-structure/rbt-2.png)

由于关注的是存储了关键字 key 的结点，故在此后的作图描述中，均忽略哨兵，如下图所示：

![rbt-3](/img/info-technology/algorithm/data-structure/rbt-3.png)

### 建立红黑树

以 `kv_array` 中的每个元素为 [key, value] 数组，构建树结点。树结点设计如下：

```python
class TreeNode:
    def __init__(self, key=0, val=0, color=True):
        self.key = key       # 键，按键构造 BST/RBT 树，并进行搜索/增添/删除
        self.val = val       # 值，树结点存储的值，可以为任意对象
        self.color = color   # 结点的颜色，True 代表红色(默认)，False 代表黑色
        self.left = None     # 左孩子指针
        self.right = None    # 右孩子指针
        self.parent = None   # 父结点指针
```

与 AVL 树的建立方式相同，RBT 也是循环调用插入函数，逐步建立 RBT 树。时间复杂度 O(n log n)

### 搜索 search(key)

```python
# 根据 key 值搜索结点
# 如果搜索到了，则返回结点 TreeNode，如果搜索不到，则返回 None
def search(self, search_key):
    if isinstance(self.bst, TreeNode):
        ptr = self.bst
        while isinstance(ptr, TreeNode) and ptr != self.nil:
            if search_key == ptr.key:
                # 找到了目标结点，返回此 TreeNode
                return ptr
            elif search_key < ptr.key:
                # 如果新结点 key 值小于当前结点，则应该往左走
                ptr = ptr.left
            else:
                # 如果新结点 key 值大于当前结点，则应该往右走
                ptr = ptr.right
        # 如果出了循环、到了这一步，表示找不到
        return None
    else:
        # BST 树为空树，找不到目标结点
        return None
```

### 辅助操作：左旋 left\_rotate(node)

- 对 node 结点 x 而言，将 x 左旋，意味着：
    - 让 x 的右孩子 y (x.right) 成为 x 的父结点，且 x 等于 y.left。
    - 而 y 结点原本的左孩子变为新 x 的右孩子
    - 注意：如果将 BST 树根旋下来了，则需要更换树根

![tree-rotate-1](/img/info-technology/algorithm/data-structure/tree-rotate-1.png)

### 辅助操作：右旋 right\_rotate(node)

- 对 node 结点 x 而言，将 x 右旋，意味着：
    - 让 x 的左孩子 y (x.left) 成为 x 的父结点，且 x 等于 y.right。
    - 而 y 结点原本的右孩子变为新 x 的左孩子
    - 注意：如果将 BST 树根旋下来了，则需要更换树根

### 插入 rb\_insert(key)

- 时间复杂度 O(log n) 与树高有关
- 插入方式同普通的 BST 树，在成功插入后，从新插入的红色结点开始，调用 rb_insert_fixup 逐级向上调整平衡性

### 辅助操作：插入后维护红黑性质 rb_insert_fixup(node)

- 时间复杂度 O(log n) 与树高有关

case 1、case 2、case 3：

![rbt-insert](/img/info-technology/algorithm/data-structure/rbt-insert.png)

case 1'、case 2'、case 3' 是前述的镜像情况，不再赘述。

```python
# 辅助操作：插入之后，逐级向上进行红黑性质维护
# 时间复杂度 O(log n) 与树高有关
# 根据当前结点的父结点、爷爷结点、叔叔结点的颜色，分 3 种情况，用旋转操作来调整平衡
def _rb_insert_fixup(self, node):
    if isinstance(node, TreeNode) and node != self.nil:
        # 当前结点 node 为新插入的结点，是红色的
        while isinstance(node.parent, TreeNode) and node.parent.color:
            # node 的爷爷结点必为树结点 (红黑树性质)
            assert isinstance(node.parent.parent, TreeNode)
            if node.parent.parent == self.nil:
                # node 的爷爷结点为 nil 结点，而且父结点存在
                # 这表示父结点为树根，且根是红色。只需要把根改为黑色即可
                assert node.parent == self.bst
                self.bst.color = False
            else:
                # node 的爷爷结点为树结点，且非 nil
                if node.parent == node.parent.parent.left:
                    # 如果 node 的父结点是 node 爷爷结点的左孩子
                    uncle = node.parent.parent.right
                    if isinstance(uncle, TreeNode) and uncle.color:
                        # case 1: 父结点为红色、父结点是爷爷结点的左孩子、叔叔结点也为红色
                        # 这种情况可以直接处理掉
                        node.parent.color = False  # 置父结点的颜色为黑色
                        uncle.color = False  # 置叔叔结点的颜色为黑色
                        node.parent.parent.color = True  # 置爷爷结点颜色为红色
                        node = node.parent.parent  # node 上移至其爷爷结点
                    else:
                        # 此时：父结点为红色、父结点是爷爷结点的左孩子、叔叔结点不存在或者为黑色
                        if node == node.parent.right:
                            # case 2: 父结点为红色、父结点是爷爷结点的左孩子、
                            # 叔叔结点不存在或者为黑色、当前结点是父结点的右孩子
                            # 这种情况先转换成 case 3，然后再处理掉
                            node = node.parent  # node 上移至其父（旋转后会降下来）
                            self._left_rotate(node)  # 左旋，"拉直" 呈 LL 型
                        # case 3: 父结点为红色、父结点是爷爷结点的左孩子、
                        # 叔叔结点不存在或者为黑色、当前结点是父结点的左孩子
                        node.parent.color = False  # 修改父结点为黑色
                        node.parent.parent.color = True  # 修改爷爷结点为红色
                        self._right_rotate(node.parent.parent)  # 右旋爷爷结点
                else:
                    # 如果 node 的父结点是 node 爷爷结点的右孩子（与前述操作呈镜像处理，减少注释）
                    uncle = node.parent.parent.left
                    if isinstance(uncle, TreeNode) and uncle.color:
                        # case 1': 父结点为红色、父结点是爷爷结点的右孩子、叔叔结点也为红色
                        # 这种情况可以直接处理掉
                        node.parent.color = False  # 置父结点的颜色为黑色
                        uncle.color = False  # 置叔叔结点的颜色为黑色
                        node.parent.parent.color = True  # 置爷爷结点颜色为红色
                        node = node.parent.parent  # node 上移至其爷爷结点
                    else:
                        # 此时：父结点为红色、父结点是爷爷结点的右孩子、叔叔结点不存在或者为黑色
                        if node == node.parent.left:
                            # case 2': 父结点为红色、父结点是爷爷结点的右孩子、
                            # 叔叔结点不存在或者为黑色、当前结点是父结点的左孩子
                            # 这种情况先转换成 case 3，然后再处理掉
                            node = node.parent  # node 上移至其父（旋转后会降下来）
                            self._right_rotate(node)  # 右旋，"拉直" 呈 RR 型
                        # case 3': 父结点为红色、父结点是爷爷结点的右孩子、
                        # 叔叔结点不存在或者为黑色、当前结点是父结点的右孩子
                        node.parent.color = False  # 修改父结点为黑色
                        node.parent.parent.color = True  # 修改爷爷结点为红色
                        self._left_rotate(node.parent.parent)  # 左旋爷爷结点

        # while 循环结束、处理完毕，如果此时树根存在，则置为黑色
        if isinstance(self.bst, TreeNode) and self.bst != self.nil:
            self.bst.color = False
```

### 删除 rb\_delete(key)

- 时间复杂度 O(log n) 与树高有关

### 辅助操作：结点替换 rb_transplant(u, v)

- 将结点 u 替换为结点 v（用于删除时的红黑性质保持）
- 时间复杂度 O(log n) 与树高有关

```python
# 辅助操作：将结点 u 替换为结点 v（用于删除时的红黑性质保持）
# 时间复杂度 O(log n) 与树高有关
def _rb_transplant(self, u, v):
    if isinstance(u, TreeNode) and isinstance(v, TreeNode):
        if u == self.bst or u.parent == self.nil:
            self.bst = v
        else:
            # u 的父结点必为树结点 (红黑树性质)
            assert isinstance(u.parent, TreeNode)
            # 根据 u 是其父结点的左孩子还是右孩子，更换指针
            if u == u.parent.left:
                u.parent.left = v
            else:
                u.parent.right = v
    else:
        pass
    # 无条件执行：让 v 的 parent 指针指向 u 的父结点
    v.parent = u.parent
```

### 辅助操作：删除后维护红黑性质 rb\_delete\_fixup(node)

- 时间复杂度 O(log n) 与树高有关

case 1、case 2、case 3、case 4：

![rbt-delete](/img/info-technology/algorithm/data-structure/rbt-delete.png)

case 1'、case 2'、case 3'、case 4' 是前述的镜像情况，不再赘述。

```python
# 辅助操作：删除之后，逐级向上进行红黑性质维护
# 时间复杂度 O(log n) 与树高有关
# 当删除结点 node 时，让其后继 s 替换 node。在结点被移除或者在树中移动之前，必须先记录 s 的颜色
# 根据当前结点的父结点、兄弟结点、兄弟结点的孩子结点的颜色，分 4 种情况，用旋转操作来调整平衡
def _rb_delete_fixup(self, node):
    # if isinstance(node, TreeNode) and node != self.nil:
    if isinstance(node, TreeNode) and node != self.bst:
        # 当前结点 node 为真正需要被删除的结点，其祖先中有黑色结点被删除(替换)了
        while node != self.bst and not node.color:
            # node 的父结点必为树结点 (红黑树性质)
            assert isinstance(node.parent, TreeNode)
            if node.parent == self.nil:
                # 父结点是 nil，表示当前 node 为树根，只需要把根改为黑色即可
                assert node == self.bst
                self.bst.color = False
            elif node == node.parent.left:
                # 如果 node 是其父结点的左孩子
                # node 的父结点必为树结点 (红黑树性质)
                assert isinstance(node.parent, TreeNode)
                # 记录 bro 为 node 父结点的右孩子，即 node 的兄弟结点
                bro = node.parent.right
                # node 的兄弟结点必为树结点 (红黑树性质)
                assert isinstance(bro, TreeNode)
                if bro.color:
                    # case 1: node 是其父结点的左孩子、其兄弟结点 bro 为红色
                    bro.color = False  # 让 bro 的颜色改为黑色
                    node.parent.color = True
                    self._left_rotate(node.parent)
                    bro = node.parent.right  # 确保 bro 还是 node 的兄弟结点
                # bro 结点的孩子必为树结点 (红黑树性质)
                assert isinstance(bro.left, TreeNode) and isinstance(bro.right, TreeNode)
                if not bro.left.color and not bro.right.color:
                    # case 2: 此时兄弟结点 bro 一定为黑色，如果原本不是黑色，会经过 case 1 变为黑色
                    # 此时 bro 孩子均为黑色，让 bro 变为 红色
                    bro.color = True
                    node = node.parent  # node 上移
                else:
                    # 此时 bro 的孩子不全为黑色
                    if not bro.right.color:
                        # case 3: 此时 node 是其父结点的左孩子，且兄弟结点 bro 一定为黑色
                        # bro 的左孩子为红色，右孩子为黑色
                        bro.left.color = False  # 修改 bro 左孩子为黑色
                        bro.color = True  # 修改 bro 为红色（一红挂两黑）
                        self._right_rotate(bro)  # 右旋 bro
                        bro = node.parent.right  # 确保 bro 还是 node 的兄弟结点
                        # case 3 之后，保证 bro 为黑色、bro 的右孩子为红色
                    # case 4: 此时 node 是其父结点的左孩子，且兄弟结点 bro 一定为黑色
                    # bro 的右孩子为红色，左孩子颜色为黑色
                    bro.color = node.parent.color
                    node.parent.color = False
                    bro.right.color = False
                    self._left_rotate(node.parent)
                    node = self.bst

            else:
                # 如果 node 是其父结点的右孩子
                # node 的父结点必为树结点 (红黑树性质)
                assert isinstance(node.parent, TreeNode)
                # 记录 bro 为 node 父结点的左孩子，即 node 的兄弟结点
                bro = node.parent.left
                # node 的兄弟结点必为树结点 (红黑树性质)
                assert isinstance(bro, TreeNode)
                if bro.color:
                    # case 1': node 是其父结点的右孩子、其兄弟结点 bro 为红色
                    bro.color = False  # 让 bro 的颜色改为黑色
                    node.parent.color = True
                    self._right_rotate(node.parent)
                    bro = node.parent.left  # 确保 bro 还是 node 的兄弟结点
                # bro 结点的孩子必为树结点 (红黑树性质)
                assert isinstance(bro.left, TreeNode) and isinstance(bro.right, TreeNode)
                if not bro.left.color and not bro.right.color:
                    # case 2': 此时兄弟结点 bro 一定为黑色，如果原本不是黑色，会经过 case 1' 变为黑色
                    # 此时 bro 孩子均为黑色，让 bro 变为 红色
                    bro.color = True
                    node = node.parent  # node 上移
                else:
                    # 此时 bro 的孩子不全为黑色
                    if not bro.left.color:
                        # case 3': 此时 node 是其父结点的右孩子，且兄弟结点 bro 一定为黑色
                        # bro 的左孩子为黑色，右孩子为红色
                        bro.right.color = False  # 修改 bro 右孩子为黑色
                        bro.color = True  # 修改 bro 为红色（一红挂两黑）
                        self._left_rotate(bro)  # 左旋 bro
                        bro = node.parent.left  # 确保 bro 还是 node 的兄弟结点
                        # case 3' 之后，保证 bro 为黑色、bro 的左孩子为红色
                    # case 4': 此时 node 是其父结点的右孩子，且兄弟结点 bro 一定为黑色
                    # bro 的左孩子为红色，右孩子颜色为黑色
                    bro.color = node.parent.color
                    node.parent.color = False
                    bro.left.color = False
                    self._right_rotate(node.parent)
                    node = self.bst

        # 最终将 node 的颜色置为黑色
        node.color = False
```

### 最小值 min_bst(root)

- 找到一棵以 root 为根的 BST/RBT 中的最小值结点（一路向左）
- 时间复杂度 O(log n) 与树高有关

### 最大值 max_bst(root)

- 找到一棵以 root 为根的 BST/RBT 中的最大值结点（一路向右）
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


### 实现细节


## 红黑树树高分析

## 代码范例

### Python

Python 环境：Python 3.7

[GitHub Code Link](https://github.com/YuweiYin/Code_Play/blob/master/Algorithm-Essence/data-structure/red-black-tree.py)

## 参考资料

- Introduction to Algorithm (aka CLRS) Third Edition - Chapter 13 Red-Black Tree
