# Algorithm - Data Structure - B Tree

By [YuweiYin](https://yuweiyin.github.io/)

## 简介

B Tree 是为**磁盘**或其它直接存取的**辅助存储设备**而设计的一种**平衡搜索树**。B 树类似于 [红黑树](./red-black-tree)，但 B 树在**降低磁盘 I/O 操作数**方面要更好一些。许多**数据库系统**使用 B 树或者 B 树的变种（B+ 树、B\* 树等）来存储信息。

B 树与红黑树的不同之处在于 B 树的结点可以有很多孩子，从数个到数千个。即，一棵 B 树的“**分支因子**”（结点度数）可以相当大，尽管它通常依赖于所使用的磁盘单元的特性。B 树类似于红黑树，就是每棵含有 n 个结点的 B 树的高度为 O(log n)。

然而，一棵 B 树的严格高度可能比一棵红黑树的高度要小许多，这是因为它的分支因子，也就是表示高度的对数的底数可以非常大。因此，我们也可以使用 B 树在时间 O(log n) 内完成一些动态集合的操作。

B 树以一种自然的方式推广了 [二叉搜索树](./binary-search-tree)，下图给出了一棵简单的 B 树。

![b-tree-1](/img/info-technology/algorithm/data-structure/b-tree-1.png)

### 辅存上的数据结构

计算机系统利用各种技术来提供存储能力。一个计算机系统的**主存** (Primary Memory 或者 Main Memory) 通常由**硅存储芯片**组成。这种技术每位的存储**代价**一般要比磁存储技术（如磁带或磁盘）高不止一个数量级。许多计算机系统还有基于磁盘的 **辅存** (Secondary Memory)，这种辅存的**容量**通常要比主存的容量高出至少两个数量级。

![b-tree-2](/img/info-technology/algorithm/data-structure/b-tree-2.png)

上图是一个典型的**磁盘驱动器**。驱动器由一个或多个 platter **盘片**组成，它们以一个固定的速度绕着一个共同的 spindle **主轴**旋转。每个盘的表面覆盖着一层可磁化的物质。驱动器通过 arm **磁臂**末端的 head **磁头**来读/写盘片。磁臂可以将磁头向主轴移近或者移远。当一个给定的磁头处于静止时，它下面经过的磁盘表面（一段圆弧）称为一个 track **磁道**。越往主轴靠近，磁道越密集。多个盘片增加的仅仅是磁盘驱动器的容量，而不影响性能。

尽管磁盘比主存便宜并且具有更多的容量，但是它的读写速度比主存慢很多，因为它有机械运动的部分。磁盘有两个机械运动的部分：**盘片旋转**和**磁臂运动**。商用磁盘的旋转速度一般是 5400～15,000 转/分钟 (RPM)。通常 15,000 RPM 的速度是用于服务器级的驱动器上，7200 RPM 的速度常用于台式机的驱动器上，而 5400 RPM 的速度用于笔记本电脑的驱动器上。

碍于材料、**物理硬件的极限**能力，转速上的提升已经不大实际了。尽管 7200 RPM 看上去很快，但是旋转一圈需要 8.33 ms，这比硅存储的常见存取时间 50 ns 要高出 5 个数量级。换句话说，如果等待一个磁盘旋转完整的一圈，让一个特定的项到达读/写磁头下方，这段时间内，存取主存的次数可能超过了 100,000 次。虽然平均来讲，只需等待半圈就行了，但是磁盘存储和硅存储的存取时间差距仍然是巨大的。而且移动磁臂也要耗费时间，商用磁盘的平均存取时间往往是 8～11 ms。

为了摊还机械移动所花费的等待时间，磁盘会一次存取多个数据项而不仅是一个。基于“二八法则”和**程序/数据的局部性原理**，这种**一次性加载多个相邻数据项的操作是很合理的**。信息被分为一些列相等大小的、在柱面内连续出现的位 page **页面**，并且每个磁盘读/写一个或多个完整的页面。对于一个典型的磁盘而言，一页的长度可能为 2^11 ～ 2^14 字节。一旦读/写磁头正确定位，并且盘片已经旋转到所要页面的开头位置，对磁盘的读/写操作就完全电子化了（除了磁盘的旋转外），此时磁盘能够快速（近乎光速）读/写大量的数据。

通常，定位到一页信息并将其从磁盘里读出的时间要比对读出信息进行检查的时间长得多，因此在考虑与外存有交互的应用/算法/数据结构/操作时，运行时间的分析往往分为两大部分：

- **磁盘存取次数**
- CPU (计算) 时间

可以使用需要读出或写入磁盘的信息的**页数**来衡量磁盘存取次数。具体磁盘存取时间不是常量，它依赖于当前磁道和所需磁道之间的距离以及磁盘的初始旋转状态。但是仍然可以使用读或写的页数作为磁盘存取总时间的主要近似值。

### Introduction to B Tree

在一个典型的 B 树应用（比如数据库系统）中，所要**处理的数据量非常大**，以至于所有数据**无法一次性装入主存**，处理时需要**分批**地从外存加载进主存。B 树算法将所需页面从磁盘复制到主存，然后将修改过的页面写回磁盘。在任何时刻，B 树算法都只需在主存中保持一定数量的页面。因此，主存的大小并不限制被处理的 B 树的大小。

用以下的伪代码来对磁盘操作进行建模，一个对象操作的典型模式如下：

```
x = a pointer to some object
DISK-READ(x)
operations that access and/or modify the attributes of x
DISK-WRITE(x)  // omitted if no attributes of x were changed
other operations that access but do not modify attributes of x
```

设 x 为指向一个对象的指针。如果该对象正在主存中，那么可以不用访问外存 就能引用该对象的各个成员属性、成员方法，如 x.key。然而，如果 x 所指向的对象现在并不在主存（这里不考虑各级 cache 缓存机制）中，而是驻留在外存（这里假设为磁盘）里，那么在引用它的属性之前，必须先调用执行 DISK-READ(x)，**将该对象读入主存中**。另外，这里假设 如果 x 已经在主存中了，则 DISK-READ(x) 不需要磁盘存取、视作空操作。类似地，调用执行 DISK-WRITE(x) 用来将对对象 x 的属性**所做的修改存储于外存**。

在任何时刻，系统可以在**主存中只保持有限的数据页数**。假定系统不再将被使用的页从主存中换出，后文的 B 树算法分析会忽略淘汰页面（包括淘汰算法/策略）的耗时。

由于在大多数系统中，一个 B 树算法的运行时间主要由它所执行的 DISK-READ 和 DISK-WRITE 操作的次数所决定的，所以我们希望这些操作能够读/写尽可能多的有效信息，从而减少访问外存的次数。因此，一个 B 树结点**通常和一个完整磁盘页一样大**，并且当前系统磁盘页的大小限制了一个 B 树结点可以含有的孩子个数。

如果 B 树的一个内部结点 x 包含 x.n 个关键字，那么结点 x 就有 x.n + 1 个孩子。结点 x 中的关键字就是**分隔点**，它们把结点 x 中所处理的关键字的属性分隔为 x.n + 1 个子域，每个子域都由 x 的一个孩子处理。

当在一棵 B 树中查找一个关键字时，基于对存储在 x 中的 x.n 个关键字的比较，做出一个 (x.n + 1) 路的选择。叶结点的结构与内部结点的结构不同，后文将会继续探讨。

记 Branching Factor 分支因子为 bf，则 B 树中每个结点的关键字数目以及孩子数量范围如下：

- bf - 1 <= # of keys <= 2 \* bf - 1
- bf <= # of children <= 2 \* bf

每个结点的孩子数量等于其含有的关键字数目加一。另外，根结点的 keys 或 children 数量没有上述下界限制，但有上界限制。

而 2-3 树就是分支因子 bf=2 的简化版 B 树，2-3 树中每个结点的关键字至少为 1 个、至多为 3 个；孩子数至少为 2 个、至多为 4 个。

B 树是很平衡的，其**所有叶结点都在同一层**（深度 depth 相同）。

对存储在磁盘上的一棵大的 B 树，通常分支因子 bf 在 50～2000 之间，具体值取决于一个关键字相对于一页的大小。一个大的分支因子可以大大地降低 B 树的高度，从而减少查找关键字时所需的磁盘存取次数。

![b-tree-3](/img/info-technology/algorithm/data-structure/b-tree-3.png)

上图展示了一棵分支因子为 1001、高度为 2 的 B 树，它可以存储超过 10 亿个关键字。而且，由于根结点可以持久地保存在主存中，所以在这棵树中查找某个关键字至多只需 2 次磁盘存取。

### B 树定义

为简单起见，我们假定，就像二叉搜索树 BST 和红黑树 RBT 中一样，任何和关键字相联系的 **卫星数据** (Satellite Information) 将与关键字一样存放在同一个结点中。一个常见的 B 树变种，被称为 B+ 树 (B+ -Tree)，它把所有的卫星数据都存储在叶结点中，内部结点只存放关键字和孩子指针，因此最大化了内部结点的分支因子。

一棵 B 树 T 是具有以下性质的有根树（根为 T.root）：

1. 每个结点 x 有下面属性：
    1. 自然数 x.n\_keys，当前存储在结点 x 中的关键字个数。
    2. 列表 x.keys，存放 x.n\_keys 个关键字，以非降序存放。
    3. 列表 x.vals，存放 x.n\_keys 个值元素，可为任意对象。
    4. 布尔值 x.is\_leaf，如果 x 是叶结点，则为 True；如果 x 为内部结点，则为 False。
2. 每个内部结点 x 还包含列表 x.kids，存放 x.n\_keys + 1 个孩子结点。
    1. 叶结点没有孩子，所以其 x.kids 列表为空。
    2. 除了叶结点外，每个结点（即内部结点）如果有 m 个关键字，则有 m + 1 个孩子结点。
3. 关键字 x.keys 对存储在各子树中的关键字范围加以分割：如果记 k\_i 为任意一个存储在以 x.kids[i] 为根的子树中的关键字，那么有如下不等式（简记 n = x.n_keys）：
    - k\_0 <= x.keys[0] <= k\_1 <= x.keys[1] <= ... <= k\_{n - 1} <= x.keys[n - 1] <= k\_{n}
4. 每个结点所包含的关键字个数有上界和下界，用一个被称为 B 树的**最小度数** (minimum degree) 的固定整数 (即**分支因子**) bf >= 2 来表示这些界。
    1. 除了根结点以外的每个结点必须**至少**有 (bf - 1) 个关键字。因此，除了根结点以外的每个内部结点都**至少**有 bf 个孩子。如果树非空，根结点至少有一个关键字。
    2. 每个结点**至多**可包含 (2 \* bf - 1) 个关键字。因此，一个内部结点至多可有 (2 \* bf) 个孩子结点
    3. 当一个结点恰好有 (2 \* bf - 1) 个关键字时，称该结点是 **满的** (full)。
    4. 另一个常见的 B 树变种称为 **B\*树**，它要求每个内部结点至少是 2/3 满的，而 B 树仅要求至少半满（即有 bf - 1 个关键字）。
5. 每个叶结点具有相同的深度，即树的高度 h = O(log\_{bf} n)。

分支因子 bf = 2 时的 B 树是最简单的。每个内部结点有 2 个、3 个或 4 个孩子，即一棵 2-3-4 树。然而，为了减少外存访问次数，在实际中会将 bf 开设得比较大，比如物理页面的字节数。

### B 树的高度

B 树上大部分的操作所需的磁盘存取次数与 B 树的高度时成正比的。如下是 B 树最坏情况下的高度分析：

《CLRS》定理 18.1：如果 n_keys >= 1，那么对任意一棵包含 n 个关键字、高度为 h、最小度数 bf >= 2 的 B 树 T，有：`h <= log_{bf} ((n + 1) / 2)`

与红黑树对比，尽管二者的高度都以 O(log n) 的速度增长（bf 相比于 n 还只是个常数），但对 B 树来说，log 对数的底数可以比红黑树大很多倍（红黑树为 log\_{2}）。因此，对大多数的树操作而言，要检查的结点数载 B 树中要比在红黑树中少大约 log\_{bf} 的因子。由于在一棵树中检查任意一个结点都需要一次磁盘访问，所以 B 树**避免了大量的磁盘访问**。

## 设计 & 细节

约定：

- B 树的**根结点始终在主存中**，这样无需对根做 DISK-READ 操作；然而，当根结点被改变后，需要对根结点做一次 DISK-WRITE 操作，把改变写回到外存。
- 任何被当做参数的结点在被传递之前，都要对它们先做一次 DISK-READ 操作，将之调入主存。
- 在实现时的 DISK-READ 和 DISK-WRITE 操作都只是待完善的空操作，仅作示意。

```python
# 从外存读取结点 node 的第 kid_index 个孩子结点
@staticmethod
def disk_read(node, kid_index):
    # TODO 从外存读取对象（这里代码假设整个 B 树已在主存）
    if isinstance(node, TreeNode) and kid_index < len(node.kids) and \
            isinstance(node.kids[kid_index], TreeNode):
        return True
    return False
```

```python
# 将结点 node 写到外存
@staticmethod
def disk_write(node):
    # TODO 将结点 node 写到外存（这里代码假设整个 B 树已在主存）
    if isinstance(node, TreeNode):
        return True
    else:
        return False
```

### 建立 B 树

以 kv_array 中的每个元素为 [key, value] 数组，构建树结点。树结点设计如下：

```python
class TreeNode:
    def __init__(self, key=0, val=0):
        # keys 和 vals 列表之间必须逐下标一一对应
        # 即 val_i 对象是 key_i 关键字的卫星数据
        self.keys = [key]    # 当前存储在结点中的关键字列表，关键字升序排列
        self.vals = [val]    # 当前存储在结点中的值元素列表，卫星数据，可以为任意对象
        self.kids = []       # 孩子结点指针列表
        self.parent = None   # 父结点指针
        self.is_leaf = True  # 如果此结点是叶结点，则为 True，否则为 False
```

B 树的建立就是循环调用 insert(key, val) 插入操作，逐步建立 B 树。时间复杂度 O(n log n)

### 辅助操作：二分查找

由于 B-Tree 结点的 keys 列表是非降序排列的，所以在定位目标 key 时可以进行二分搜索，加速检索定位。返回 k 在 keys 列表中的索引，如果不存在返回当前下标（便于 B-Tree 索引其孩子结点）。

```python
# 辅助操作：B-Tree 结点 keys (非降序排列) 的二分搜索
# 返回 k 在 keys 列表中的索引，如果不存在返回当前下标
def _binary_search(self, keys, lo, hi, k):
    assert isinstance(keys, list) and isinstance(lo, int) and isinstance(hi, int)
    n_keys = len(keys)
    if n_keys == 0:
        return n_keys
    # 越界情况
    if lo < 0:
        lo = 0
    if hi >= n_keys:
        hi = n_keys - 1
    # 根据下标大小分情况处理
    if lo == hi:
        return lo if k <= keys[lo] else lo + 1
    elif lo < hi:
        mid = int((lo + hi) >> 1)
        # 目标 k 匹配 mid 位置的值，返回 mid
        if k == keys[mid]:
            return mid
        # 目标 k 小于 mid 位置的值，往左看
        elif k < keys[mid]:
            return self._binary_search(keys, lo, mid - 1, k)
        # 目标 k 大于 mid 位置的值，往右看
        else:
            return self._binary_search(keys, mid + 1, hi, k)
    else:
        # 不存在
        return lo
```

### 搜索 search(key)

搜索一棵 B 树和搜索一棵二叉树很相似，只是在每个结点所做的不是二叉或者“两路”分支选择，而是根据结点的孩子数量做多路分支选择。具体而言，对每个内部结点 x，做的是一个 (x.n\_keys + 1) 路的分支选择。

B 树 search 时定义在二叉搜索树 BST 的 search 操作的一个直接推广。它的输入是一个指向某子树根结点 x 的指针，以及要在该子树中搜索的一个关键字 k。因此，顶层调用的形式为 search(T.root, k)。如果 k 在 B 树中，那么 search 操作返回的是由结点 y 和使得 y.keys[i] == k 的下标 i 组成的有序对 (y, i)，否则返回 (None, -1)。

```python
# 根据 key 值搜索结点
# 如果搜索到了，则返回结点 TreeNode 及其孩子下标 kid_index
# 如果搜索不到，则返回 None, -1
def search(self, search_key):
    if isinstance(self.b_root, TreeNode):
        return self._search(self.b_root, search_key)
    else:
        # 当前树为空，找不到目标结点
        return None, -1

def _search(self, root, search_key):
    if isinstance(root, TreeNode):
        # key_index = 0  # 当前结点的关键字索引，如果找不到，就是孩子结点索引
        # 线性扫描当前结点的每个关键字，在当前结点中找出下标 kid_index，
        # 使得 search_key 搜索目标关键字 小于等于 root 的某个孩子的关键字
        # while key_index < len(root.keys) and search_key > root.keys[key_index]:
        #     key_index += 1
        key_index = self._binary_search(root.keys, 0, len(root.keys) - 1, search_key)
        # 检查是否已找到关键字
        if 0 <= key_index < len(root.keys) and search_key == root.keys[key_index]:
            return root, key_index
        # 如果找不到，判断当前结点 root 是否为叶子，如果是，则表示没有此元素
        elif root.is_leaf:
            return None, -1
        # 如果当前结点 root 是中间结点，从外存读取孩子结点
        else:
            if self.disk_read(root, key_index):
                return self._search(root.kids[key_index], search_key)
            else:
                # 读外存失败
                print('_search: Path 2')
                return None, -1
    else:
        # root 结点类型异常
        print('_search: Path 1')
        return None, -1
```

在递归过程 \_search 中所遇到的结点构成了一条从树根向下（不一定到叶结点）的简单路径。因此，由 search 过程访问的磁盘页面数为 O(h) = O(log\_{bf} n)，其中 h 为 B 树的高，n 为 B 树中所含关键字的个数。由于 x.n\_keys < 2 \* bf，所以在结点中的线性扫描 while 循环花费的时间为 O(bf)，因此总的 CPU 时间为 O(h \* bf) = O(bf \* log\_{bf} n)。

如果 B-Tree 结点在定位目标 key 时进行二分搜索，而不是 while 循环的线性扫描，则可以加速检索定位 O(log\_{2} bf)。因此总的 CPU 时间可以优化为 O(h \* bf) = O(log\_{bf} n \* log\_{2} bf)。

由于 B 树应用中**主要的耗时操作还是磁盘访问**，因此减少树高、减少磁盘访问次数是更重要的优化任务（这与二分查找的优化并不冲突）。

### 创建一个新的树结点

```python
# 辅助操作：新建树结点
def create_new_node(self, new_key=0, new_val=0):
    new_node = TreeNode(new_key, new_val)
    if self.disk_write(new_node):
        return new_node
    else:
        return None
```

### 插入 insert(key, val)

B-Tree 中插入一个关键字要比二叉搜索树 BST 中插入一个关键字复杂。先要查找插入新关键字的**叶结点**的位置，但此时不能像 BST 那样简单地创建一个新的叶结点，因为这样会违反 B 树的性质：所有叶结点都在同一层。相反，B 树中插入的做法是将新的关键字**插入一个已经存在的叶结点上**。

由于不能将关键字插入一个满的叶结点，故引入 **split 分裂**操作。在中间结点（此中间结点不是满的）搜索到新关键字应插入的下一级孩子时，先检查此孩子是否为满的。如果此孩子不满，则往下搜索；如果此孩子已满（有 2 \* bf - 1 个 keys 和 2 \* bf 个 kids），则先将此孩子从中间分裂开来：左 bf - 1 个关键字和左 bf 个孩子属于“新左孩子”，右 bf - 1 个关键字和右 bf 个孩子属于“新右孩子”，剩余的正中间的关键字被提升到当前中间结点（已经保证了此中间结点不是满的，所以可以容纳一个新的关键字）。

完成分裂操作后，判断待插入关键字该进入“新左孩子”还是“新右孩子”，往下继续搜索，直到插入某个非满的叶结点为止。

![b-tree-4](/img/info-technology/algorithm/data-structure/b-tree-4.png)

![b-tree-5](/img/info-technology/algorithm/data-structure/b-tree-5.png)

插入操作的初始调用（要对树根为满的情况特殊处理）：

### 删除 delete(key)

从 B 树上删除结点也较为复杂一点，主要是需要保证 B 树的这两大性质：1. 所有叶结点在同一层；2. 除根结点外的所有结点的关键字数目最少为分支因子 (bf - 1)，从而孩子数目最少为 bf。因此，如果某个删除操作**将要**违反性质，则会“向上回溯”调整。

并且，与插入操作只能插入到叶结点不同，删除时可以从任意一个结点中删除一个关键字。而且当从一个内部结点删除关键字后，还需重新安排这个结点的孩子（具体来说，是被删关键字两侧的孩子）。

delete 操作从以 x 为根的子树中删除关键字 k。本算法需保证无论任何时候，结点 x 递归调用自身时，x 中关键字个数至少为 bf。这个条件比 B 树规定的下界（x.n\_keys >= bf - 1）更严格一些，在此情况下，一趟下降的过程就足以将 k 从树中删除。

另外，如果当前根结点 x 成为一个不含任何关键字的内部结点（如下述 2c 和 3b 情况中可能会出现），那么 x 就要被删除。而 x 的唯一孩子 x.kids[0] 成为新根，从而树的高度降低 1，同时也维持非空 B 树的树根必须包含至少一个关键字的性质。

delete(x, k) 删除时的各种情况如下：

1. 如果关键字 k 在结点 x 中，并且 x 是叶结点，则从 x 中删除 k。
2. 如果关键字 k 在结点 x 中，并且 x 是内部结点，则分情况做如下处理：
    1. 关键字 k 左右的孩子结点分别称为 left 和 right。如果子结点 left 中至少包含 bf 个关键字（表示从 left 中删除一个关键字也不会影响其 B 树性质），则找出关键字 k 在以 left 为根的子树中的**前驱** k'。在 x 中用 k' 替代 k，并在 y 中递归删除 k'。（找到 k' 并删除它可以在沿树下降的单过程中完成）
    2. 对称地，如果子结点 left 中的关键字数目少于 bf（表示从 left 中删除一个关键字会影响其 B 树性质），则检查子结点 right。如果 right 中至少包含 bf 个关键字，则找出关键字 k 在以 right 为根的子树中的**后继** k''。在 x 中用 k'' 替代 k，并在 right 中递归删除 k''。（找到 k'' 并删除它可以在沿树下降的单过程中完成）
    3. 否则，如果 left 和 right 都只含有 (bf - 1) 个关键字，则将关键字 k 和子结点 right 中的所有关键字都合并进入子结点 left（此时 left 结点变为满结点）。然后释放子结点 right，并递归地在子结点 left 中删除关键字 k。
3. 如果关键字 k 当前不在内部结点 x 中，则确定该往哪个子结点中继续搜索，假设为 x.kids[i]。如果 x.kids[i] 只有 (bf - 1) 个关键字（表示从 x.kids[i] 中删除一个关键字会影响其 B 树性质），必须执行下述步骤 3.1 和 3.2 来调整树结构，随后再递归向下删除。
    1. 如果 x.kids[i] 只含有 (bf - 1) 个关键字，但是它的一个相邻的兄弟结点至少包含 bf 个关键字，则将 x 中的某个关键字下降至 x.kids[i] 中，再将 x.kids[i] 相邻的左兄弟或右兄弟结点 bro 的一个关键字提升到 x 中，而 bro 结点的相应孩子指针也移动到 x.kids[i] 中。（此乃移花接木、李代桃僵之术也。）
    2. 如果 x.kids[i] 和其所有相邻兄弟结点都只包含 (bf - 1) 个关键字（表示 x.kids[i] 没法从兄弟结点“借”关键字来维持 B 树性质），则将 x.kids[i] 与其某一个兄弟结点合并。
        - 当合并孩子结点时，记待合并的孩子为 l 和 r，将 x 中“夹在” l、r 中间的关键字记为 k\_mid，则合并操作即为：先把 k\_mid 下降、加入 l 的关键字，然后把 r 的所有关键字和孩子都加入 l，最后释放结点 r。
        - 注意，上述的 l 和 r 表示的是左右相对位置，而 x.kids[i] 即可能是 l 也可能是 r。如果 x.kids[i] 是 l，则执行上述合并操作；如果 x.kids[i] 是 r，则应反过来：先把 k\_mid 下降、加入 r 的关键字，然后把 l 的所有关键字和孩子都加入 r，最后释放结点 l。
        - 此后在 x.kids[i] 中递归地删除目标关键字 k。

![b-tree-delete-1](/img/info-technology/algorithm/data-structure/b-tree-delete-1.png)

![b-tree-delete-2](/img/info-technology/algorithm/data-structure/b-tree-delete-2.png)

![b-tree-delete-3](/img/info-technology/algorithm/data-structure/b-tree-delete-3.png)

![b-tree-delete-4](/img/info-technology/algorithm/data-structure/b-tree-delete-4.png)

## B-Tree 相关数据结构

- 二叉搜索树：二叉树，每个结点只存储一个关键字，等于则命中，小于走左结点，大于走右结点；
- B（B-）树：一种二叉搜索树的扩展，属于多路搜索树
    - 每个结点存储 (bf - 1) 到 (2 \* bf - 1) 个关键字
    - 内部结点和叶结点均存储 key/val，非叶结点也可以命中，同一个 key 只在一个结点中出现
    - 内部结点有 n\_keys + 1 个孩子结点，叶结点无孩子（kids 列表为空）。
- B+ 树：B+ 树是 B 树的变种
    - 在 B 树的基础上，将所有 val 移至叶结点，只能在叶结点命中，且同一个 key 可以在多个结点中出现
    - 内部结点仅作为索引，不命中目标。由于不存储 val，所以可以有更多的空间、更大的分支因子，从而降低树高、减少磁盘访问次数。
    - 内部结点的 keys 数量与 kids 数量相等
    - B+ 树常用于 File System 文件系统
- B\* 树：B\* 树是 B 树的进一步变种，也可以基于 B+ 树进行改变，核心变化如下：
    - 规定结点的关键字数目最少为 (2/3) \* 2 \* bf - 1，而不是 (1/2) \* 2 \* bf - 1 = bf - 1
    - 每个结点存在指向其兄弟结点的指针。即：每一层的结点形成了链表。
    - B\* 树的插入分裂方式有所不同：当一个结点满时，如果它的某个兄弟结点未满，那么将一部分数据移到兄弟结点中，再在原结点插入关键字。这种方式能够降低分裂结点、分配新结点的概率，从而提升空间利用率、有助于降低树高，从而减少磁盘访问次数。

## 代码范例

### Python

Python 环境：Python 3.7

[GitHub Code Link](https://github.com/YuweiYin/Code_Play/blob/master/Algorithm-Essence/data-structure/b-tree.py)

## 参考资料

- Introduction to Algorithm (aka CLRS) Third Edition - Chapter 18
- MIT 6.046J Design and Analysis of Algorithms, Spring 2015
    - Amartya Shankha Biswas - [R2. 2-3 Trees and B-Trees](https://www.youtube.com/watch?v=TOb1tuEZ2X4)
