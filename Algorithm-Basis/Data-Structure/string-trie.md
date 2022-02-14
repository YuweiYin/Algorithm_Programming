# Algorithm - String - Trie

By [YuweiYin](https://yuweiyin.github.io/)

## 1. Trie

Trie (Retrieve + Tree) 称为字典树，又称单词查找树。Trie 是一种树形结构，是一种哈希树的变种。典型应用是用于统计，排序和保存大量的字符串（但不仅限于字符串），所以经常被搜索引擎系统用于文本词频统计。它的优点是：利用字符串的公共前缀来减少查询时间，最大限度地减少无谓的字符串比较，查询效率比哈希树高。　

### 1.1. Tire 树的三个基本性质

1. 根节点不包含字符，除根节点外每一个节点都只包含一个字符；
2. 从根节点到某一节点，路径上经过的字符连接起来，为该节点对应的字符串；
3. 每个节点的所有子节点包含的字符都不相同。

### 1.2. Tire 树的应用

1. **串的快速检索**：给出 n 个单词组成的单词表，以及一篇文章 (单词序列)，目标是按出现顺序写出所有生词(不在单词表中出现)。
    - 普通解法：利用数组 or 哈希，进行枚举。
    - 高效解法：把单词表建立成一棵字典树，然后读入文章、逐个搜索文章中的单词。
2. **串字典序排序**：给定 n 个互不相同(且互不为前缀)的单词，目标是按字典序排序。
    - 采用数组的方式创建字典树，孩子结点(字符)在数组中按字典序排列，因此对字典树进行先序遍历即可获得单词升序。
3. **最长公共前缀**：对所有串建立字典树，两个串的最长公共前缀长度 即为二者所在结点的公共祖先个数。
    - 于是问题转化为[最近公共祖先](./lowest-common-ancestor) LCA 问题，可用 RMQ 或者 Tarjan 算法解决。

### 1.3. Trie 设计

设字符表 V 大小为 b，下面以小写英文字母集合 {a, b, c, ..., z} 作为字符表，其秩 b = 26。

- 字典树是一个树型结构，除根结点以外的每个结点 (内部结点 & 叶结点) 对应 V 中的一个字母(存储于该结点的数据域)。
- 每个结点至多有 b 个孩子结点(指针)，分别对应字符表 V 中的各个单词。
- 如果匹配(搜索)过程某个结点 v 是结点 u 的孩子结点，那么 u 结点所对应的字母 w(u) 后面会紧随字母 w(v)。
- 为了判别当前识别到的字母是否为一个单词的结尾，每个结点中还存储一个 bool 型的成员变量。
- 另外，由于分支数 b 较大，所以往往不会设置某个结点的孩子指针为数组，而是会采用字典(哈希表)。而且这样做也不需要知道字符表了，只需要逐个处理单词中的每个字符即可。

字典树中主要的操作是 Insert 插入和 Search 查询。插入和查询操作的时间复杂度均为 O(n)，这里 n 是单词的长度(含有的字母数)。

删除结点也并不困难，只是需要分几种情况处理。

## 2. 01-Trie

01-Trie 主要用于解决求异或最值的问题：给定 n 个数字 (用于构建 01-Trie)，以及 m 次查询。每次查询给出一个数字 x，求 x 与前述 n 个数字中的哪个数字**异或**值最大。

如果处理 32 进制数，则设计 01 字典树是一棵最多 32 层的二叉树。其每个结点的两条边分别表示二进制的某一位的值为 0 还是为 1，将某个路径上边的值连起来就得到一个二进制串。每个结点主要有 4 个属性：结点编号(下标)、结点值、两条边指向的下一结点(孩子)的编号(下标)。

可用数组代替树结构，详见代码范例 `class Trie01`。

## 3. 压缩字典树 Compressed Tree

Compressed Tree 是指对字典树的压缩处理。如果树中的某一段路径里是这样的：除了该路径的最后一个结点(不一定是叶结点)，其余结点的孩子个数(度数)均为 1，例如单链 a -> b -> c，而 c 结点可能有多个孩子，也可能是个叶结点。则可将之压缩为单个结点，结点值为 abc。

## 代码范例

### Python

Python 环境：Python 3.7

### Trie

[GitHub Code Link](https://github.com/YuweiYin/Code_Play/blob/master/Algorithm-Essence/data-structure/string-trie.py)

## 参考资料