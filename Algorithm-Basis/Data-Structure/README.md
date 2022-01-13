# Data Structure

Algorithm - [YuweiYin](https://github.com/YuweiYin)

> Data structures are nothing different. They are like the bookshelves of your application where you can organize your data. Different data structures will give you different facility and benefits. To properly use the power and accessibility of the data structures you need to know the trade-offs of using one.

## Directory

- 基础结构
    - 数组、链表、栈、队列
    - 指针与对象的实现 (例如用数组实现)
    - 块状链表
- [哈希散列](./hashing)
    - 直接寻址表 Direct-Access Table、散列表 Hashing Table
    - 散列表解决碰撞/冲突：链接法 Chaining、开放寻址法 Open Addressing
        - 线性探查 Linear Probing
        - 二次探查 Quadratic Probing
        - 双重散列 Double Hashing
    - 散列函数 Hash Function
        - 除法散列法 Division Hashing
        - 乘法散列法 Multiplication Hashing
        - 全域散列法 Universal Hashing
    - 散列表的动态扩缩 grow / shrink
    - 完全散列 Perfect Hashing、动态完全散列 Dynamic Perfect Hashing
    - 布谷鸟散列 Cuckoo Hashing、布隆过滤器 Bloom Filter
    - 一致性散列 Consistent Hashing (分布式系统的负载均衡)
- 树形结构
    - 二叉树及其各类树遍历算法 (深度/广度)
        - 前序遍历 Preorder Traversal
        - 中序遍历 Inorder Traversal
        - 后序遍历 Postorder Traversal
        - 层序遍历 Level Traversal
    - [二叉排序/搜索树](./binary-search-tree) (Binary Sort/Search Tree, BST)
    - [高度平衡二叉搜索树](./avl-tree) AVL 树 (Adelson-Velsky-Landis Tree) (Height Balanced Binary Search Tree)
    - [红黑树](./red-black-tree) (Red Black Tree, RBT)
        - 红黑树的变种: AA 树
        - 红黑树的扩张: [顺序统计树](./order-statistic-tree) (Order Statistic Tree, OST)
        - 红黑树的扩张: [区间树](./interval-tree) (Interval Tree)
    - [堆树](./treap) (Treap)
    - [伸展树](./splay-tree) (Splay Tree)
    - [跳表](./skip-list) Skip List
    - 替罪羊树
    - 带权平衡树
    - [B-Tree](./b-tree)
        - 2-3 树、B- 树、B+ 树、B\* 树
    - [哈夫曼树](../greedy-algorithm/huffman) (Huffman Tree)
    - [van Emde Boas 树](./van-emde-boas-tree)
    - k 近邻树、k 维树 (k-dimensional Tree, kd-Tree)
- 区间查询 Range Query
    - [线段树](./segment-tree) (Segment Tree, ST)
    - [树状数组](./binary-indexed-tree) Fenwick Tree (Binary Indexed Tree, BIT)
    - [区间最值查询](./range-min-max-query) Sparse Table (Range Minimum/Maximum Query, RMQ)
    - [最近公共祖先](./lowest-common-ancestor) (Lowest Common Ancestors, LCA)
- 堆
    - [二叉堆与优先队列](./heap-priority-queue)
    - 双端队列 Deque
    - 可合并堆 Mergeable Heap
        - 左偏堆 Leftist Heap
        - [斐波那契堆](./fibonacci-heap)
- 不相交集合 (Disjoint Set)
    - [并查集](./union-find) (Union Find)
- [图结构与图算法](../graph-theory)
- 字符串相关 (算法/数据结构)
    - [子串匹配](../other-topics/string-matching)
        - 朴素字符串匹配算法 Naive String Matching
        - Finite Automaton 有限自动机-字符串匹配算法
        - Rabin-Karp 算法
        - KMP 算法 (D.E.Knuth，J.H.Morris and V.R.Pratt)
    - AC 自动机 (Aho-Corasick Automaton)
    - [前缀树/字典树](./string-trie) (Trie Tree)、01-字典树
    - 后缀数据结构
        - [(广义)后缀树](./string-suffix) (Generalized) Suffix Trie
        - 后缀树的普通构造算法: 先用各个后缀构造普通的字典树，再进行结点压缩
        - 后缀树的线性构造算法: Ukkonen (Ukk)在线算法 & McCreight (Mcc)算法
        - 后缀数组 Suffix Array
        - (广义)后缀自动机 (Generalized) Suffix Automaton (SAM)
    - 回文串 Palindrome
        - 回文树 Palindromic Tree
        - 回文自动机 (Palindromic Automaton, PAM)
        - 马拉车算法 Manacher's Algorithm

## 数据结构的扩张

对基本的数据结构进行扩张，在算法设计过程中时相当常见的。比如对 [红黑树](./red-black-tree) 进行扩张可以设计出 [顺序统计树](./order-statistic-tree)、[区间树](./interval-tree) (Interval Tree) 等。

扩张一种数据结构通常可以分为如下 4 个步骤：

1. 选择一种适合当前任务的基础数据结构；
    - 所谓“适合”，是指部分任务所需的功能 已在基础数据结构上 (近似地)得到了满足，并能易于扩张出当前任务需要的功能；
    - 挑选出一个适合的基础数据结构，前提是要对基础数据结构的优缺点、各操作的性能有较好的理解。
2. 增添基础数据结构中要额外维护的附加信息；
3. 检验基础数据结构上的基本修改操作能否(容易地)维护附加信息；
    - “容易维护”一般有两点考量：1. 方便实现新功能；2. 不增加原本操作的渐近时间复杂度。
4. 设计一些基于附加信息的新操作，已完成目标新功能。

以上步骤仅作参考。如下以顺序统计树为例阐述对红黑树的扩张：

1. 步骤一：在设计 顺序统计树 时选用了 红黑树 作为基础数据结构。要扩张“求顺序统计量”这个任务，红黑树是一种合适的选择，这源于它能够有效地支持一些基于**全序**的动态集合操作，如：求最小值 minimum、求最大值 maximum、求后继 successor、求前驱 predecessor 等。
2. 步骤二：增添了 size 属性，存储了以当前结点为根的子树的大小（含有的结点总数目）。一般而言，附加信息可使得**目标操作更有效率**。例如，本可以在直接利用树结点的关键字比较就完成 `os_select` 求顺序统计量和 `os_rank` 求某个结点的排序号，但这不能够在 O(log n) 运行时间内完成，而是需要 $ \Theta(n) $ 运行时间。有时候，附加信息是**指针类信息**，而不是具体的数值。
3. 步骤三：保证了插入和删除操作仍能在 O(log n) 时间内维护红黑树本身的性质 以及 size 属性。比较理想的情况是：某个结点附加信息变化，**只用更新临近的少数几个结点信息**。如果顺序统计树的额外附加信息不是 size，而是直接存储当前结点的 rank 秩/排序，那么当插入一个新的最小 key 元素时，所有结点的 rank 都需要改变、维护，需要 O(n) 时间，这就比红黑树插入操作原本的 O(log n) 差多了。
4. 步骤四：很多时候考虑扩张一个数据结构的原因就是为了满足**新操作**的需求。但有时也并不是为了设计一些新操作，而是利用附加信息来**加速已有的操作**。

利用附加信息来**加速已有的操作**，例如：可以在顺序统计树上为结点增加前驱、后继指针，从而使得 求最小值 minimum、求最大值 maximum、求后继 successor、求前驱 predecessor 这些操作可以在最坏 O(1) 时间内完成，并且维护时不改变插入和删除操作 O(log n) 的渐近时间性能。

### 对红黑树的扩张

当红黑树作为基础数据结构时，可以证明，某些类型的附加信息总是可以用插入和删除操作来进行有效的维护。

《CLRS》**定理 14.1（红黑树的扩张）**：设 f 是 n 个结点的红黑树 T 扩张的结点属性，且假设对任一结点 x，**f 的值仅依赖于结点 x、x.left 和 x.right 的信息**（可能包括 x.left.f 和 x.right.f）。那么，可以在 insert 插入和 delete 删除操作期间对 T 的所有结点的 f 值进行维护，并且不影响这两个操作 O(log n) 的渐近时间性能。

证明详细过程见《CLRS》Chapter 14.2，主要思想是：对树 T 中某结点 x 的 f 属性变动 只会影响到 x 的祖先结点。即 修改了 x.f 只需要更新 x.parent.f、x.parent.parent.f 如此沿树向上，一旦更新到 T.root.f 就不再有其它任何结点依赖于新值，于是过程结束。因为红黑树的高度为 O(log n)，所以改变某结点的 f 属性后仅需耗费 O(log n) 时间来维护。
