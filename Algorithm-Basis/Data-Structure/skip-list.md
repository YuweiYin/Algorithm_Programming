# Algorithm - Data Structure - Skip List

By [YuweiYin](https://yuweiyin.github.io/)

## 简介

跳表 Skip List 是由 William Pugh 于 1990 年在其论文 《Skip lists: a probabilistic alternative to balanced trees》中提出。跳表实际就是一种可以进行二分查找的有序链表，即：**链表加多级索引**的结构。（如果数据是存储在有序数组里，那么可以进行二分查找。数组可以迅速定位下标元素，但链表不行，所以需要多级索引。）

跳表是一个随机化的数据结构，可以被看做二叉树的一个变种，它在性能上和红黑树，AVL 树不相上下，但是跳表的原理非常简单，

它采用随机技术决定链表中哪些节点应增加向前指针以及在该节点中应增加多少个指针。跳表结构的头节点需有足够的指针域，以满足可能构造最大级数的需要，而尾节点不需要指针域。

采用这种随机技术，跳表中的搜索、插入、删除操作的时间均为O(logn)，然而，最坏情况下时间复杂性却变成O(n)。相比之下，在一个有序数组或链表中进行插入/删除操作的时间为O(n)，最坏情况下为O(n)。

### 优点

1. 主要优点：可以跟红黑树、AVL 树等平衡 BST 一样，做到比较稳定地插入、查询与删除。其理论插入/查询/删除的算法时间复杂度均为 O(log n)。
2. 代码相对简单（相对于红黑树和 AVL 树）
3. 增删结点/区间时，相对更方便（相对于 Balanced BST）
4. 在并发环境下，更新数据时，红黑树或 AVL 树需要调整的结点可能太多，不利于并发。但 Skip List 在更新时需要调整的结点较少。

### 应用

SkipList 有许多应用，比如著名的 Redis 数据库、Google 的 Bigtable 数据库，同时它被广泛地运用到了各种缓存的实现当中。

## 设计 & 细节

### 建立 Skip List

以 `kv_array` 中的每个元素为 [key, value] 数组，构建链表结点。链表结点设计如下：

```python
# 非循环多域双向链表
class ListNode:
    def __init__(self, key=0, val=None, level=1):
        self.key = key      # 键，按键构造链表
        self.val = val      # 值，结点存储的值，可以为任意对象
        self.pre = []       # 指向前一个结点的指针数组，n 级结点有 n 个 pre。头尾结点最多
        self.next = []      # 指向下一个结点的指针数组，n 级结点有 n 个 next。头尾结点最多
        self.level = level  # 当前结点所在的层级，最低为 1
        # 搜索时先搜索高层级的索引结点，找不到再逐级下降。如果在最低层都找不到，就表示搜索不到
```

Skip List 类成员属性如下：

```python
class SkipList:
    # 构造 Skip List 即：具备多级索引结构的链表
    def __init__(self, kv_array):
        self.tail = ListNode(0x3f3f3f3f)   # 链表尾结点, key 为 inf。这里考虑升序排列链表
        self.head = ListNode(-0x3f3f3f3f)  # 链表头结点, key 为 -inf
        self.node_list = []                # 除头结点外，从首至尾的元素 ListNode 列表
        self.max_level = 0x3f3f3f3f        # 允许的最多层级数
        self.cur_max_level = 1             # 当前所有结点的最大层级数

        self.head.pre.append(None)
        self.head.next.append(self.tail)   # 链表头结点指向尾结点
        self.tail.pre.append(self.head)
        self.tail.next.append(None)  # 链表尾结点指向 None
```

循环调用插入函数，逐步建立 Skip List。

### 搜索

- Skip List 根据 key 值搜索结点
- 时间复杂度 O(log n) 与层数有关

```python
def skip_list_search(self, search_key)
```

### 辅助操作：新建并返回具有随机层数的结点

```python
# 辅助操作：新建并返回具有随机层数的结点
def create_new_node(self, new_key, new_val):
    new_node = ListNode(new_key, new_val)
    random.seed(id(new_node))  # 以新结点对象的唯一标识符 id 作为随机数种子
    new_level = 1
    while random.random() > 0.5:  # 50% 的几率增加一个 level
        new_level += 1
        # 检测是否更新当前最大层数
        if new_level > self.cur_max_level:
            if new_level > self.max_level:
                # 不能超过预设的最高层数 inf
                new_level = self.max_level
                break
            self.cur_max_level = new_level
            # 当前策略：为了避免层数过高，如果更新了最大层数，则不再提升新结点的层数
            # 并且把 Skip List 首尾结点的 level 提升
            self.head.level += 1
            self.tail.level += 1
            self.head.pre.append(None)
            self.head.next.append(self.tail)
            self.tail.pre.append(self.head)
            self.tail.next.append(None)
            # break  # 也可以不加此限制，去掉这个 break，让 level 仅因概率决定
    # 设置新结点的层级并返回新结点
    new_node.level = new_level
    new_node.pre = [None] * new_level
    new_node.next = [None] * new_level
    return new_node
```

### 插入

- Skip List 按 key 插入新结点，并给出 value
- 时间复杂度 O(log n) 与树高有关

```python
def skip_list_insert(self, insert_key, insert_val, insert_type=2)
```

插入策略 1：逐层插入 时间复杂度 O(n)，对新结点的每个 level 找到其应插入的位置

```python
def _skip_list_insert_1(self, insert_key, insert_val)
```

插入策略 2（较优）：利用跳表的 search 策略快速定位每层的插入点

```python
def _skip_list_insert_2(self, insert_key, insert_val)
```

### 删除

- Skip List 根据 key 值删除结点，并返回被删除的结点
- 时间复杂度 O(log n) 与树高有关

```python
def skip_list_delete(self, delete_key)
```

## 代码范例

### Python

Python 环境：Python 3.7

[GitHub Code Link](https://github.com/YuweiYin/Code_Play/blob/master/Algorithm-Essence/data-structure/skip-list.py)

## 参考资料

- MIT 6.046J Design and Analysis of Algorithms, Spring 2015 [7. Randomization: Skip Lists](https://www.youtube.com/watch?v=2g9OSRKJuzM)
