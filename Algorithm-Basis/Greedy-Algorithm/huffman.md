# Algorithm - Dynamic Programming - Huffman

By [YuweiYin](https://yuweiyin.github.io/)

## 简介

哈夫曼编码 Huffman

### 哈夫曼编码引入

哈夫曼编码可以很有效地**压缩数据**：通常可以节省 20%～90% 的空间，具体压缩率依赖于数据的特性。

可以将待压缩数据看作字符序列，根据**每个字符的出现频率**，哈夫曼贪心算法构造出**字符的最优二进制表示**。

假定希望压缩一个含有 10 万个字符的数据文件，下图给出了此文件中所出现的字符和它们的出现频率。

![huffman-1](/img/info-technology/algorithm/greedy-algorithm/huffman-1.png)

有许多方法可以表示这个文件的信息。这里考虑用**二进制字符编码**（此后简称**编码**），每个字符用一个唯一的二进制串表示，称为**码字**。对于上述文件，如果使用定长编码，需要用 3 位来表示 6 个字符，这样需要 30 万个二进制位来编码文件。

如果使用**变长编码** (variable-length code) 可以达到比定长编码低得多的空间占用。其思想是赋予高频字符 短码字，赋予低频字符 长码字。

### 前缀码

这里考虑**前缀码** (prefix code)，即没有任何码字是其它码字的前缀。可以证明，与任何字符编码相比，前缀码可以保证达到最优数据压缩率。

任何二进制字符码的编码过程都很简单，只要将表示每个字符的码字连接起来即可完成文件的压缩。例如前面图片中的变长前缀码，可以将 3 个字符的单词 abc 编码为 0·101·100 = 0101100，这里符号“·”是表示连结操作。

前缀码的作用是简化编码过程。由于没有码字是其它码字的前缀，编码文件的开始码字是**无歧义**的。因此可以根据固定的规则去识别，先识别出**开始码字**，将其转换回原字符，然后对编码文件剩余部分重复这种解码过程。

解码过程需要前缀码的一种方便的表示形式，以便可以容易地截取开始码字。可以用一种 **左 0 右 1** 的二叉树来表达。每个叶结点标记了一个**字符及其出现的频率**，每个内部结点标记了其子树中叶结点的**频率之和**。前缀码中的二进制 0 意味着“转向左孩子”，二进制 1 意味着“转向右孩子”，直至叶结点（存储对应的原字符），完成当前识别/解码。

![huffman-2](/img/info-technology/algorithm/greedy-algorithm/huffman-2.png)

文件的最优编码方案总是对应一棵 **满二叉树** (full binary tree)，即每个非叶结点都有两个孩子结点。前文给出的定长编码实例不是最优的，因为它的二叉树表示 并非满二叉树（如上图 (a) 所示）。设有 `|C|` 个叶结点，每个叶结点对应字母表中的一个字符，由于最优前缀码对应的树是满二叉树，因此恰有 `|C| - 1` 个内部结点。

给定一棵对应前缀码的树 T，可以很容易地计算出编码一个文件需要多少个二进制位。对于字母表 C 中的每个字符 c，令属性 c.freq 表示 c 在文件中出现的频率，令 dT(c) 表示 c 对应的叶结点在树中的深度。注意到，dT(c) 也是字符 c 的码字的长度。

则编码文件需要 $ B(T) = \sum_{c \in C} c.freq * dT(c) $ 个二进制位。此处将 B(T) 定义为 T 的代价。目标是最小化此代价值。

哈夫曼编码树的思想与 [最优二叉搜索树](../dynamic-programming/optimal-binary-search-tree) 有相似之处。不过二者的目的不同。在实际应用中，可以同时使用两者：对一个长文本，根据**字符出现频率** 用哈夫曼编码每个字符 达到压缩存储功能，根据**单词出现频率** 用最优二叉搜索树 达到快速查词功能。

### 构造哈夫曼编码

Huffman 设计了一个贪心算法来构造**最优前缀码**，被称为哈夫曼编码 (Huffman code)。

它的正确性证明依赖于**贪心选择性质**和**最优子结构**。这里先设计算法， 再回过头来分析其贪心性质。

假定 C 是一个含有 n 个字符的集合，而其中每个字符 $ c \in C $ 都是一个对象，其属性 c.freq 给出了字符的出现频率。算法**自底向上**地构造出对应最优编码的二叉树 T。它从 `|C|` 个叶结点开始，执行 `|C| - 1` 个“结点合并”操作创建出最终的二叉树。算法使用一个以属性 freq 为关键字的 [最小优先队列](../data-structure/heap-priority-queue) Q，每次将当前最低频率的字符合并。当合并两个对象时，得到的一个新对象（内部结点），其 freq 属性值为其左右孩子的 freq 属性之和。

**字符结构体**：

```python
# 字符结构体(哈夫曼树结点)
class Character:
    def __init__(self, ch='', freq=0):
        self.ch = ch        # 本字符未经编码的值
        self.freq = freq    # 本字符出现的频率
        self.left = None    # 左孩子
        self.right = None   # 右孩子
        self.parent = None  # 父结点
```

**类构造函数、用最小二叉堆构建最小优先队列**：

```python
class Huffman:
    def __init__(self, char_list):
        assert isinstance(char_list, list) and len(char_list) > 0

        # 确保 char_list 中每个元素都是 Character 结构体
        # 并通过 char_list 构造用于最小优先队列的 Element 结构体数组
        ele_list = []
        for ch in char_list:
            assert isinstance(ch, Character)
            ele_list.append(Element(key=ch.freq, val=ch))

        self.c_num = len(ele_list)  # 含有的原字符总数
        self.h_root = None          # 哈夫曼树的根结点
        self.heap = Heap(ele_list)  # 建立最小优先队列(最小二叉堆)
        self.prefix_code = []       # 根据哈夫曼树 左 0 右 1 解析每个字符的前缀码
```

**构造哈夫曼树**：

```python
# 哈夫曼编码 Huffman Code
# 返回：哈夫曼树的根结点
def huffman_code(self):
    # 自顶向下递归实现 (贪心算法) \Theta(n)
    # self._huffman_code_recursive(0, n)
    # 循环实现 (贪心算法) \Theta(n)
    self._huffman_code_iteration()
    return self.h_root

# 循环实现 (贪心算法)
# 时间复杂度 \Theta(n)
# 空间复杂度 \Theta(1)
def _huffman_code_iteration(self):
    # 字符表 char_list 的长度
    n = self.c_num

    # n 个字符，则需要处理 n-1 次合并操作，产生 n-1 个内部结点
    for i in range(n - 1):
        # 创建新结点 (内部结点)
        new_char = Character()
        # 取出两个最小元素 Element，其 val 为 Character 结构体
        left_ele = self.heap.extract_min()
        right_ele = self.heap.extract_min()
        assert isinstance(left_ele, Element) and isinstance(right_ele, Element)
        assert isinstance(left_ele.val, Character) and isinstance(right_ele.val, Character)
        # 链接父子结点指针
        new_char.left = left_ele.val
        new_char.right = right_ele.val
        left_ele.val.parent = new_char
        right_ele.val.parent = new_char
        # 新结点的 freq 属性为其左右孩子 freq 之和
        new_char.freq = left_ele.val.freq + right_ele.val.freq
        new_ele = Element(key=new_char.freq, val=new_char)
        # 将新结点封装为 Element 对象，并插入最小优先队列中
        self.heap.min_heap_insert(new_ele)
    # 最小优先队列中最后唯一剩下的结点就是树根
    h_root_ele = self.heap.extract_min()
    assert isinstance(h_root_ele, Element)
    self.h_root = h_root_ele.val
```

### 根据哈夫曼树构造各个字符的前缀码

```python
# 根据哈夫曼树 左 0 右 1 解析每个字符的前缀码
def set_prefix_code(self):
    if isinstance(self.h_root, Character):
        self._set_prefix_code(self.h_root, '')
    else:
        self.prefix_code = []

# 深度优先搜索，叶结点是具体字符
def _set_prefix_code(self, root, prefix):
    assert isinstance(root, Character) and isinstance(prefix, str)
    # 有左孩子则往左搜索
    if isinstance(root.left, Character):
        prefix += '0'
        self._set_prefix_code(root.left, prefix)
        prefix = prefix[: -1]
    # 有右孩子则往右搜索
    if isinstance(root.right, Character):
        prefix += '1'
        self._set_prefix_code(root.right, prefix)
        prefix = prefix[: -1]
    # 叶结点，写入前缀码
    if not isinstance(root.left, Character) and not isinstance(root.right, Character):
        self.prefix_code.append((root.ch, prefix))
```

### 哈夫曼算法分析

如果用[最小二叉堆](../data-structure/heap-priority-queue)实现最小优先队列，对一个 n 个字符的集合 C，建立优先队列的时间为 O(n)。循环总次数为 n-1，每个堆操作需要 O(log n) 的时间，所以循环的总时间为 O(n log n)。因此，处理一个 n 个字符的集合，Huffman 的总运行时间为 O(n log n)。如果将最小二叉堆换为 [van Emde Boas 树]((../data-structure/van-emde-boas-tree))，则可以将运行时间减少为 O(n log log n)。

现分析哈夫曼算法这样一个贪心算法的正确性，要证明确定最优前缀码的问题具有**贪心选择**和**最优子结构**性质。下面的引理证明问题具有贪心选择性质：

《CLRS》**引理 16.2**：令 C 为一个字母表，其中每个字符 $ c \in C $ 都有一个频率 c.freq。令 x 和 y 是 C 中频率最低的两个字符。那么存在 C 的一个最优前缀码，x 和 y 的码字长度相同，且只有最后一个二进制位不同。

![huffman-3](/img/info-technology/algorithm/greedy-algorithm/huffman-3.png)

引理 16.2 说明，不失一般性，通过合并来构造最优树的过程，可以从合并出现频率最低的两个字符这样一个贪心选择开始。

《CLRS》**引理 16.3**：令 C 为一个给定的字母表，其中每个字符 $ c \in C $ 都定义了一个频率 c.freq。令 x 和 y 是 C 中频率最低的两个字符。令 C' 为 C 去掉字符 x 和 y，加入一个新字符 z 后得到的字母表，即 $ C' = C - {x, y} \cup {z} $。类似于集合 C，也为 C' 定义频率属性 freq，不用之处只是 `z.freq = x.freq + y.freq`。令 T' 为字母表 C' 的任意一个最优前缀码对应的编码树。于是可以将 T' 中叶结点 z 替换为一个以 x 和 y 为孩子的内部结点，得到树 T，而 T 表示字母表 C 的一个最优前缀码。

![huffman-4](/img/info-technology/algorithm/greedy-algorithm/huffman-4.png)

引理 16.3 证明了构造最优前缀码的问题具有最优子结构性质。

《CLRS》**定理 16.4**：Huffman 算法会生成一个最优前缀码。

但是 Huffman 编码**更适合于字符出现频率相差比较明显的场景**。《CLRS》练习 16.3-8：假定一个数据文件由 8 位字符组成，其中所有 256 个字符出现的频率大致相同：最高频率不超过最低频率的 2 倍。在此情况下，哈夫曼编码并不比 8 位固定长度编码更高效。

## 代码范例

### Python

Python 环境：Python 3.7

[GitHub Code Link](https://github.com/YuweiYin/Code_Play/blob/master/Algorithm-Essence/greedy-algorithm/huffman.py)

## 参考资料

- Introduction to Algorithm (aka CLRS) Third Edition - Chapter 16
