# Algorithm - Data Structure - Hashing

By [YuweiYin](https://yuweiyin.github.io/)

---

## 1. 简介

**Hash 哈希/散列**，是 1650 年代出现的英文单词，原意是 cut into small pieces 切成小片，常用于厨房。该英文单词起源于法国单词 hacher，意为 chop up 切碎，与英文单词 hatchet 小斧近似。该法语单词又是古法语单词 hache 演变而来的，意为 axe 斧头。

有另一种调侃的说法：hash 来自 Vulcan（电影《星际迷航》中的瓦肯人）的单词 la'ash，意思也是 axe 斧头。

---

### 1.1. 哈希散列 Hashing

许多应用都需要一种**动态集合结构**，它至少要支持 **Insert、Search 和 Delete** 这三种**字典操作**。例如，用于程序语言编译的编译器维护了一个**符号表**，其中元素的关键字为任意字符串，它与程序中的标识符相对应。

**散列表** (Hash Table) 是实现字典操作的一种有效数据结构。尽管在最坏情况下，散列表中查找一个元素的时间与链表中查找的时间相同，达到了 `\Theta(n)`。然而在**实际应用**中，散列表**查找的性能是极好的**。在一些**合理的假设**下，在散列表中查找一个元素的平均时间是 O(1)。

**散列表是普通数组概念的推广**。由于对普通数组可以直接寻址，使得能在 O(1) 时间内访问数组中的任一位置。

散列是一种极其有效和实用的技术：基本的字典操作平均只需要 O(1) 的时间。

Python 语言中的内建 dict 字典类型即为一种哈希表。几乎所有的现代高级编程语言中均有内建的字典类型。

---

## 2. 直接寻址 Direct-Access Table

当**关键字的全域 U 比较小时**，直接寻址是一种简单而有效的技术。假设某应用要用到一个动态集合，其中每个元素都是取自于全域 `U={0, 1, ..., m-1}` 中的一个关键字 key，这里 m 不是一个很大的数。另外，假设没有两个元素具有相同的关键字。

为表示动态集合，用一个数组（**直接寻址表** direct-address table），记为 `T[0..m-1]`。其中每个位置，或称为 **槽** slot，对应全域 U 中的一个关键字 key。下图描绘了此方法，槽 k 指向集合中一个关键字为 k 的元素。如果该集合中没有关键字为 k 的元素，则 `T[k]=NIL`。

![hashing-1](/img/info-technology/algorithm/data-structure/hashing-1.png)

如果**存储空间允许**，可以提供一个数组，为每个可能的关键字保留一个位置，以利用直接寻址技术的优势。

在直接寻址表中，实现字典操作很简单：

```
DIRECT-ADDRESS-SEARCH(T, key)
1     return T[key]
```

```
DIRECT-ADDRESS-INSERT(T, node)
1     T[node.key] = node
```

```
DIRECT-ADDRESS-DELETE(T, node)
1     T[node.key] = NIL
```

上述每一个操作都只需要 O(1) 的时间。

注：哈希表中的 search 查找操作属于 **exact search 精确查找**，目标元素要么找到、要么找不到（找不到的同时，没法像 BST 二叉搜索树那样能找到目标元素的前驱或后继）。

对于某些应用，直接寻址表本身就可以存放动态集合中的元素。即，并**不**把每个元素的关键字及其附带的卫星数据都放在直接寻址表外部的一个对象中，再由表中某个槽的指针指向该对象。而是**直接把该对象存放在直接寻址表的槽中**，从而节省了空间。

使用对象内的一个特殊关键字来表明该槽为**空槽**即可。而且，通常可不必存储该对象的关键字属性，因为如果知道一个对象在表中的下标，就可以得到它的关键字（因为二者之间是双射）。然而，如果不存储关键字，我们就必须要有某种方法来确定某个槽是否为空槽。

**位向量** (bit vector) 是一个仅包含 0 和 1 的数组。长度为 m 的位向量所占的空间要比包含 m 个指针的数组少得多，因此可以利用一个位向量来表示一个包含不同元素（无附带的卫星数据）的动态集合，在其上的字典操作的运行时间为 O(1)。

如果想要在一个**非常大**的数组上，通过直接寻址的方式实现一个字典，对整个数组进行初始化是不太实际的。但是可以利用一个附加数组，其处理方式类似于栈，其大小等于实际存储在字典中的关键字数目，以辅助确定大数组中某个给定的项是否有效。从而也能达到每个操作（初始化、搜索、插入、删除）的时间为 O(1)，并且每个存储对象占用 O(1) 的空间。

上述操作常被称为 **预哈希 Pre-Hashing**，将原始的 key（可以不是整数，Python 中的原始 key 即为字符串）映射成与输入量等长（或者是 O(n) 量级，n 为实际要存储的对象数目）的整数（常为自然数）集合 A，然后对 A 做直接寻址哈希。而 Pre-Hashing 要保证没有冲突，即此映射必须为**单射**。也有可能为双射，不过关键是单射，而且一般而言 哈希表长度 m 都会大于 n，只需保证 m=O(n)，则直接寻址哈希表效率为 O(1)。

在 Python 中预哈希操作可以通过重载 `__hash__` 函数来自定义，其默认映射方式是调用 id 函数，取对象的物理地址来作为 Pre-Hashing 的结果。

- **注意**：
	- Pre-Hashing 的一定要是双射，只要 `__eq__` 函数（也可以自定义）认为两个原始 key 是相同的，那么其 `__hash__` 函数的结果必须相同。
	- 另外，被用于作为原始 key 的对象需要是 immutable 不可变对象（比如 str、int、tuple 对象），而不是 mutable 可变对象（比如 list 对象）。
	- 对于原始 key 是自定义类型的对象，需要同时实现 `__eq__` 和 `__hash__` 函数，才能正常使用 hash 操作。（当然，同时要保证该 key 对象是不可变类型）
	- Python 的 dict 字典，对于相同 key、不同 value 的赋值，会采用 overwrite 覆盖机制，只记住最后一次携带的 value。Python dict 的简易使用方式可以[参考在线教程](https://www.runoob.com/python/python-dictionary.html)。

- [Python 3.7 hash](https://docs.python.org/3.7/library/functions.html#hash)

> Return the hash value of the object (if it has one). **Hash values are integers**. They are used to quickly compare dictionary keys during a dictionary lookup. Numeric values that compare equal have the same hash value (even if they are of different types, as is the case for 1 and 1.0).
> **Note**: For objects with custom `__hash__()` methods, note that `hash()` **truncates the return value** *based on the bit width* of the host machine. See `__hash__()` for details.

- [Python 3.7 \_\_hash\_\_](https://docs.python.org/3.7/reference/datamodel.html#object.__hash__)

> Called by built-in function `hash()` and for operations on members of hashed collections including **set**, **frozenset**, and **dict**. `__hash__()` should **return an integer**. The **only required property** is that *objects which compare equal have the same hash value*;
> it is advised to mix together the hash values of the components of the object that also play a part in comparison of objects by packing them into a tuple and hashing the tuple. Example:
> `def __hash__(self):  return hash((self.name, self.nick, self.color))`
> **Note**: `hash()` truncates the value returned from an object’s custom `__hash__()` method to the size of a `Py_ssize_t`. This is typically 8 bytes on 64-bit builds and 4 bytes on 32-bit builds. If an object’s `__hash__()` must interoperate on builds of different bit sizes, be sure to check the width on all supported builds. An easy way to do this is with `python -c "import sys; print(sys.hash_info.width)"`.
> **Note**: By default, the `__hash__()` values of **str, bytes and datetime** objects are “salted” with an **unpredictable random value**. Although they *remain constant within an individual Python process*, they are **not predictable** between repeated invocations of Python.
---

## 3. 散列表

直接寻址技术的**缺点**是非常明显的：如果**全域 U 很大**，则在一台标准的计算机可用内存容量中，要存储大小为 `|U|` 的一张表 T 也许不太实际，甚至是无法做到的。另外，实际存储的关键字集合 K 相对于 U 来说可能很小，使得分配给 T 的**大部分空间都将被浪费掉**。

当实际存储的关键字数目 K 比全部可能的关键字总数 U 要**小许多**时，采用**散列表**就能成为直接数组寻址的一种有效替代。因为散列表使用一个长度与实际存储的关键字数目成比例的数组来存储，能将散列表的存储需求降至 `\Theta (|K|)`，同时散列表中查找一个元素的优势仍然得到保持，平均只需要 O(1) 的时间。

在直接寻址方式下，具有关键字 k 的元素被存放在槽 k 中。在散列表中，不是直接把关键字作为数组的下标，而是根据关键字（利用**散列函数** hash function）计算出相应的槽下标 h(k)。哈希函数 h 将关键字 k 的全域 U 映射到散列表 `T[0..m-1]` 的各槽位上，而 m 一般远小于 `|U|`。可以说一个具有关键字 k 的元素被 **散列** 到槽 h(k) 上，也可以说 h(k) 是关键字 k 的 ***散列值***。

![hashing-2](/img/info-technology/algorithm/data-structure/hashing-2.png)

---

## 4. 散列函数

一个**好的散列函**数应该(近似地)满足**简单均匀散列** (Simple Uniform Hashing) 假设：每个关键字都等可能地被散列到 m 个槽位中的任何一个（**均匀分布**），并与其它关键字已散列到哪个槽位无关（**独立采样**）。遗憾的是，一般无法检查这一条件是否成立，因为很少能知道关键字散列所满足的概率分布，而且各关键字可能并不是完全独立的。

有时，我们知道关键字的概率分布。例如，如果各关键字都是随机的实数 k，它们独立均匀地分布于 0 <= k < 1 范围中，那么散列函数 `h(k) = \floor(km)` 就能满足简单均匀散列的假设条件。实际上，桶排序就正是这样做的。

在实际应用中，常常可以运用**启发式方法**来构造性能好散列函数。设计过程中，可以利用关键字分布的有用信息。例如，在一个编译器的符号表中，关键字都是字符串，表示程序中的标识符。一些很相近的符号经常会出现在同一个程序中，如 pt 和 pts。好的散列函数应能将这些相近符号散列到相同槽中的可能性最小化。

一种好的方法导出的散列值，在某种程度上应**独立于数据可能存在的任何模式**。例如，“除法散列”用一个特定的素数来除任何所给的关键字，所得的余数即为该关键字的散列值。假定所选择的素数与关键字分布中的任何模式都是无关的，这种方法常常可以给出好的结果。

另外，散列函数的某些应用可能会要求**比简单均匀散列更强的性质**。例如，可能希望某些很近似的关键字具有截然不同的散列值（使用后文所述的线性探查技术时，这一特性特别有用）。后文的**全域散列** Universal Hashing 通常能够提供这些性质。

多数散列函数都假定关键字的**全域为自然数集** N = {0, 1, 2, ...}。因此，如果所给关键字不是自然数，通常需要前文所述的 Pre-Hashing 操作将之转换为自然数，从而直接作为哈希表的下标来使用。

---

### 4.1. 除法散列法 Division Hashing

`h(k) = k \mod p`

在应用除法散列法时，p 不一定为素数，但要避免选择某些 p 值。例如，p 不应为 2 的幂，因为如果 p = 2^q，则 h(k) 就是 k 的 q 个最低位数字。除非已知各种最低 q 位的排列形式为等可能的，否则在设计散列函数时，最好考虑关键字的所有位。

另外，当 k 是一个按基数 2^q 表示的字符串时，选 p = (2^q) - 1 可能是一个糟糕的选择，因为排列 k 的各字符并不会改变其散列值。

**一个不太接近 2 的整数幂的素数**，常常是 p 的一个较好的选择。例如，假如要分配一张散列表并用链接法解决冲突，表中大约要存放 n=2000 个字符串，其中每个字符有 8 位。如果不介意一次不成功的查找需要平均检查 3 个元素，那么这样分配散列表的大小为 m=701。选择 701 的原因是：它是一个接近 2000/3 但又不接近 2 的任何次幂的素数。把每个关键字 k 视为一个常数，则散列函数为 `h(k) = k \mod 701`。

---

### 4.2. 乘法散列法 Multiplication Hashing

`h(k) = \floor(p (kA \mod 1))`

其中，A 被某个被随机选定的数字，虽然这个方法对任何的 A 值都适用，但对某些值的效果更好，最佳的选择与待散列的数据的特征有关。比如 Knuth 认为 `A = (\sqrt(5) - 1) / 2`（约等于 0.6180339887...）是一个比较理想的值。`kA mod 1` 表示取 kA 乘积的小数部分，等同于 `kA - \floor(kA)`。

乘法散列法的一个**优点是对 p 的选择不是特别关键**，一般选择它为 2 的某个幂次（p = 2^q，q 为某个正整数）而非素数。这是因为可以在大多数计算机上，通过下面这个等价的式子来运算：

`h(k) = ((kA) \mod 2^w) >> (w - r)`

w 是当前机器的字长（一个字所占的 bit 数），k 和 A 的乘积 kA 为两个字长（即 2w 双字）。kA 模 2^w 即为取低 w 位的单字（这里假设 endianness 字节顺序是 little-endian 小端模式，即数据的高(低)字节保存在内存的高(低)地址中，而非 big-endian 大端模式）。最后将前述结果右移 (w-r) 位，即只取该单字中的高 r 位（m = 2^r），因此最终的结果是一个位于闭区间 [0, m-1] 的自然数。

---

### 4.3. 全域散列法 Universal Hashing

如果让一个恶意的对手来针对某个特定的散列函数选择要散列的关键字，那么他会将 n 个关键字全部散列到同一个槽中，使得平均的检索时间为 `\Theta(n)`。**任何一个特定的散列函数**都可能出现这种最坏情况，**唯一有效**的改进方法是**随机地选择散列函数**，使之独立于要存储的关键字。这种方法被称为 **全域散列** (Universal Hashing)，不管对手选择了怎么样的关键字，其平均性能都很好。

全域散列法在执行开始时，就从一组精心设计的函数中，**随机地选择一个作为散列函数**。就像在快速排序中一样，随机化保证了没有哪一种输入会导致最坏的情况性能。因为随机地选择散列函数，算法在每一次执行时都会有所不同，甚至对于相同的输入也会如此。这样就可以确保对于任何输入，算法都具有较好的平均情况性能。

对于编译器的符号表，在全域散列方法中，可以发现程序员对标识符的选择就不会总是导致较差的散列性能了。仅当编译器选择了一个随机的散列函数，使得标识符的散列效果较差时，才会出现较差的性能。但出现这种情况的概率很小，并且这一概率对于任何相同大小的标识符集合而言都是一样的。

设 H 为一个**有限的散列函数集合** (Universal Hash Family)，它将给定的关键字全域 U 映射到集合 {0, 1, ..., m-1} 中。这样的一个函数组被称为 **全域的** (universal)，如果对每一对不同的关键字 `k1, k2 \in U` ，满足 h(k1) = h(k2) 的散列函数 `h \in H` 的个数至多为 `|H| / m`。换句话说，如果**从 H 中随机地选择一个散列函数**，当关键字 k1 != k2 时，两者发生冲突的概率不大于 1/m，这也正是从集合 {0, 1, ..., m-1} 中**独立随机**地选择 h(k1) 和 h(k2) 时发生冲突的概率。

例如，Python 会使用名为 PYTHONHASHSEED 的值来为 str, bytes and datetime objects 设置随机化种子，并且在使用了之后就固定住（一个原始 key 指定一个 PYTHONHASHSEED）。这样即为哈希函数的结果提供了随机性（从而让映射成的哈希表下标接近均匀分布），也能够保证相同的原始 key 的哈希值不会变化。

- [PYTHONHASHSEED](https://docs.python.org/3.7/using/cmdline.html#envvar-PYTHONHASHSEED)

> If this variable is not set or set to random, a **random value** is used to **seed the hashes** of *str, bytes and datetime* objects.
> If PYTHONHASHSEED is set to an integer value, it is **used as a fixed seed** for generating the `hash()` of the types covered by the hash randomization.
> Its purpose is to **allow repeatable hashing**, such as for selftests for the interpreter itself, or to allow a cluster of python processes to share hash values.
> The integer must be a **decimal number** in the range [0,4294967295]. Specifying the **value 0** will *disable hash randomization*.

- 回顾符号：
	- **全域** U 是指所有可能的关键字 key 空间。即 # possible keys
	- n 是指当前实际存储于数据结构（哈希表）的元素数目。即 # keys currently in DS
	- m 是指当前哈希表的大小（总槽数）。即 # slots in hash table
	- H 为一个**有限的散列函数集合** (Universal Hash Family)
	- 哈希函数 `h \in H` 是从全域集合 U = {0, 1, ..., u-1} 到哈希值集合 {0, 1, ..., m-1} 的映射。

在全域散列法中，假设输入的 keys 关键字是任意的（任意值、任意顺序），**不会去假定输入关键字的分布**（比如 Simple Uniform Hashing），但是哈希函数 h 是从函数族 H 中独立均匀采样的。对于从 H 中随机选出的哈希函数 h，我们希望冲突的概率不超过 1/m，即：对于任意 key1 != key2，Pr{h(key1) = h(key2)} <= 1/m。

个人认为：全域散列法的**核心思想**，就是把对输入关键字的独立均匀分布假设，转为（从哈希函数集合 H 中）选择哈希函数时的独立均匀采样假设，而后者是编程者可以主动保证的！“攻击者” (效率破坏者) 无法通过精心设计输入数据 keys 的值或者顺序来破坏哈希性能。

---

### 4.4. 全域散列函数族 Universal Hashing Family

**1. 可以设计一个全域散列函数族如下**：

`h_{ab}(k) = ((ak + b) \mod p) \mod m`

- 此函数族为 1979 年提出
- 是《CLRS》书中讲述的方式
- 其中 **p 为某个大素数**，使得每一个可能的关键字 k 都落在闭区间 `[ 0, p-1 ]` 内
- 而 a 和 b 是从闭区间 [0, p-1] 中随机取值的
- 大素数是可以在 Polynomial Time 多项式时间内找到的

这一类散列函数具有一个良好的性质，即输出范围的大小 m（也即哈希表大小）可以是任意的，不必一定是个素数。这种特性对哈希表的扩缩变化而言很方便。（另外，给定一个正整数，寻找离它最近的素数的也是可以在多项式时间内做到的。）

可以证明，对于全域散列法，在最坏情况下，冲突的概率是 1/m。即：对任意 k1 != k2 而言，Pr{h(k1) = h(k2)} = 1/m。

---

**2. 也可以设计全域散列函数族如下**：

`h_{a}(k) = (a \circ k) \mod m`，即：向量 a 与 k 的内积 模 m。 

- 由 Eric Demaine 在 MIT 6.046J 中讲述
- m 为一个素数
- u 为 m^r，其中 r 为某一个正整数
- 将所有的关键字 key 看作是以 m 为基
- `k = < k_0, k_1, ..., k_{r-1} >`，其中 `0 <= k_i <= m-1`
- 另一个 key 是从全域中独立均匀随机选择的：`a = < a_0, a_1, ..., a_{r-1} >`

对于 word RAM model 这种计算模型，只要保证 key 的长度不超过 word 单字，那么内积计算 `a \circ b` 就很快，可以看作是 O(1) 耗时。

---

**3. 也可以这样设计全域散列函数族**：

`h_{ab}(k) = (ak + b) >> (log u - log m)`

- 此函数族为 1997 年提出
- 由 Eric Demaine 在 MIT 6.851 Advanced Data Structures 中讲述
- 其中 u 和 m 均为 2 的正整数幂次

---

**4. 满足 K-wise Independence 性质的全域散列函数族**：

K-wise Independence 性质：从**全域散列函数族** H 中选择哈希函数 h，使得概率 `Pr{h(x_1)=t_1 & h(x_2)=t_2 & ... & h(x_k)=t_K} = O(1 / m^K)`，其中 x\_i 为两两互异的 key 关键字， t\_i 是哈希表的某个 slot 槽位。

满足此性质的一个全域散列函数族为 `h_{a}(x) = ((\sum_{i=1}^{K-1} a_i * x^i) \mod p) \mod m`

- 此函数族为 1981 年由 Wegman 和 Carter 提出
- 由 Eric Demaine 在 MIT 6.851 Advanced Data Structures 中讲述
- 其中 a\_i 是随机取值的，取值范围为半闭半开区间 `[ 0, p )`
- `\sum_{i=1}^{K-1} a_i * x^i)` 是以 x 为自变量的多项式表达式
- 时间复杂度为 O(k)
- 2004 年提出的两个实现
	- 1：耗费 `O(n^{\epsilon})` 空间，f(K) 的查询时间。此哈希表是 Uniform 很均匀的，所以比较实用。（K=5 较为常用）
	- 2：耗费 `O(n^{\epsilon})` 空间，O(1) 的查询时间。如果 `K=\Theta(log n)`

---

**5. Simple Tabulation Hashing 简单表格哈希**：

- 将关键字 x（整数）以某个 base 基展开 为向量 `< x_1, x_2, ..., x_c>`，这里称 x\_i 为 character 字符
- 对于每个字符 x\_i，各自建立完全随机的哈希表 T\_i。总空间复杂度为 `O(c u^{1/c})`，这与 K-wise Independence 的 `O(n^{\epsilon})` 空间相近。因此从空间复杂度而言，这种哈希方法并不算很好。
- 哈希函数为 `h(x) = T_1(x_1) \xor T_1(x_1) \xor ... T_i(x_i) ... T_c(x_c)`。其中运算符 `\xor` 表示异或运算；T\_i 表示前述对第 i 个字符位置建立的哈希表(所对应的哈希函数)。
- 此方法耗费 O(c) 的查询时间。
- 此方法是 c-wise Independence 的（即 K 值为 c）。

---

## 5. 解决冲突 - 链接法

所谓冲突，就是指多个关键字映射到散列表的同一个下标。即 h(k1) = h(k2)，其中 k1 != k2。

散列表解决 **碰撞/冲突** (collision) 的最简单方式就是 **链接** (chaining) 方法。链接法与 **[桶排序](../sort/linear-time-sort)** (Bucket Sort) 类似，散列表中的一个槽就类似于桶排序中的一个桶。

冲突时，将相同 key 的元素链接到同一个单链表中。

最坏的情况，就是所有元素都映射到哈希表的同一位置，从而形成一个特别长的单链表，搜索性能退化到了 O(n)。

桶排序假设输入是接近**均匀分布**的，从而能达到很好的效果。对哈希表而言，也希望输入的分布尽量时均匀分布，但这种假设往往只是一种被动的 hope（Simple Uniform Hashing）。所以一般会主动地通过在 Pre-Hashing 操作中加入**随机因子**，迫使映射到哈希表的下标分布尽量均匀，从而提升哈希表的性能。

可以证明：在简单均匀散列 (Simple Uniform Hashing) 的假设下，对于用链接法解决冲突的散列表，一次成功 (或者一次不成功) 查找的平均时间为 `\Theta(1 + \alpha)`。

哈希链接表（Hash Chaining Table）中，假设待存储对象有 n 个，哈希表长度为 m，则哈希链接表中的每个链表的期望长度为 n/m。记 `\Alpha = n/m`，称为此哈希表的 **load factor 加载因子**（或称**装载因子**），它表达了链的平均存储元素数。可以根据哈希表当前的 加载因子 来决定动态地 扩张 / 缩减 表大小。（后文会细述哈希表的扩缩）

---

### 5.1. 链接表上的操作

- 在采用链接法解决冲突后，散列表 T 上的字典操作就很容易实现
	- 搜索 search：先将原始的 key 通过 hash 映射成哈希表下标、找到对应的链表，耗时 O(1)；然后在链表中查询（链表结点中存储了原始数据对象，此时可以对 key 值进行精确匹配），耗时 O(l)，l 为此链表长度，其期望值为加载因子 Alpha。
	- 插入 insert：先将原始的 key 通过 hash 映射成哈希表下标、找到对应的链表，耗时 O(1)；然后在链表首部（如果不考虑排序）插入，耗时 O(1)。 
	- 删除 delete：先搜索，耗时 O(l)；搜索到了后修改链表结构，耗时 O(1)。

```
CHAINED-HASH-SEARCH(T, key)
1     search for an element with key in list T[hash(key)]
```

```
CHAINED-HASH-INSERT(T, node)
1     insert node at the head of list T[hash(node.key)]
```

```
CHAINED-HASH-DELETE(T, node)
1     delete node from the list T[hash(node.key)]
```

### 5.2. 链接表的时间复杂度分析

如果 1. 采用**随机因子**使得哈希值尽量服从均匀分布；2. 根据**加载因子**动态扩缩哈希表（使得 m > n 且 m = O(n)）。那么上述 search 和 delete 操作的时间复杂度都能特别接近于 O(1)，同 insert 操作一样（插入操作的最坏运行时间为 O(1)）。

另外，如果使用**双向链表**，那么删除操作的最坏运行时间也能是 O(1)。因为这里删除操作接收的参数是结点对象，所以直接修改其前后结点的指针域即可。但如果是单向链表，为了寻找其前一个结点，还得进行链表遍历。如果删除操作接收的参数是待删除元素的 key，那么无论是单向列表还是双向链表，都得要进行链表遍历了。

在哈希链接表场景下，链的最大长度记为 L。在前文分析可知，在简单均匀散列的假设下，最长链的期望长度为 `O(1 + \alpha)`。现分析 在很高的概率情况下，L = O(log n / (log log n)) w.h.p. (with hign probability)，w.h.p. 意为：对任意常数 c > 0 而言，某事件发生的概率大于等于 `1 - 1/(n^c)`。由于 w.h.p. 所表达的界 是比期望时间、平均时间更紧的界，但这个界不是 O(1)，因此哈希链接表的最大长度很可能高于 O(1) 量级。下面来证明并分析此界限：

对此上界的**证明**：

利用 [Chernoff bound 切尔诺夫界](http://math.mit.edu/~goemans/18310S15/chernoff-notes.pdf)：`Pr{L > c \mu} < (e^{c-1} / c^c)^{\mu}`

记 `\mu = E[L] = O(1)`。取 `c = O(log n / (log log n)) = a * (log n / (log log n))`，a 为任意常数。将 c 代入 Chernoff bound。关注不等式右侧，发现分母占主导地位，因此忽略分子。不等式右侧约等于 `O(1 / n^a)`。

这意味着：`Pr{L > O(log n / (log log n))} < 1 /(n^a)`，也即 `Pr{L <= O(log n / (log log n))} >= 1 - 1 /(n^a)`，这就表示了 L = O(log n / (log log n)) w.h.p.，证毕。

现考虑 L 的方差 `Var[L] = E[L^2] + E^2[L]`。前面已经论述了 E[L] = O(1)，现考虑 E[L^2]。

记 L\_i 为哈希表中第 i 个槽的链长度，故有 `E^2[L] = (\sum_{i=0}^{m-1} E[L_i^2]) / m`。注意到只有碰撞冲突才会增加链的长度，因此有 `E^2[L] = (\sum_{i,j} Pr{h(x_i) = h(x_j)}) / m`，而根据 Universality 全域性质，`Pr{h(x_i) = h(x_j)} = 1/m`，因此 `E^2[L] = (m^2 * (1/m)) / m`，即 O(1)。因此 `Var[L] = O(1)` 是很小的。

至此，高概率、低方差，因此**很可能存在**某条长为 O(log n / (log log n)) 的链。诚然，这个量级并不算高，但在 n 很大时，也往往会比常数级别 O(1) 高一些。

---

## 6. 解决冲突 - 开放寻址法

开放寻址法 Open Addressing 是处理散列表冲突的另一种方法。在开放寻址法中，**所有元素都存放在散列表中**，即：每个表项要么包含动态集合的一个元素，要么为 NIL。这一点与直接寻址法相似。

当查找某个元素时，要**系统地检查**（后文称为 probe 探查）**所有**的表项，**直到找到**所需的元素，或者**最终查明**该元素不在表中。

不像链接表，开放寻址法的散列表中没有链表，散列表可能会被填满（此时装载因子 `\alpha = 1`），以至于不能插入任何新的元素。此方法的**装载因子是绝对不会超过 1 的**。另外，由于散列表将近满的时候需要探查很多位置，造成较大的开销，因此往往会指定达到某个**装载因子阈值**（比如 Java 采用 0.75）时，进行散列表的动态扩张。

开放寻址法的**好处就在于它不用指针**（获取元素间的链指关系），而是直接通过计算来得到要存取的槽序列。于是，不用存储指针而节省出来的空间，使得可以用同样的空间来**提供更多的散列表槽位，潜在地减少了冲突，提高了检索速度**。因此特别常用。

而且在这种情况下，仅使用相对简单的 array / list 数据结构就可以实现哈希散列表。

在开放寻址法中，为了确定某个 key 在哈希表中对应的的下标位置，采用了 Probing 探查技术，用于生成一个**探查序列** Probe Sequence。下文会介绍三种探查函数，每个探查函数 h 都利用到了前文所述的普通哈希函数。探查函数是一个下标集合 `{0, 1, 2, ..., m-1}` 的置换（从该集合映射到自身的双射），探查序列即为 `< h(k, 0), h(k, 1), h(k, 2), ..., h(k, m-1) >`，每次关键字为 key 的元素进行搜索/插入/删除操作时，都先查看 h(key, 0) 位置，然后 h(key, 1) 位置，不断往后。（中间的某些判断会让循环终止）

---

在 JDK 1.8 之前，Java 的哈希表底层采用 数组 + 链表 实现，即使用链接法解决冲突。在 JDK 1.8 中，哈希表存储采用 数组 + 链表 + 红黑树实现，当链表长度超过阈值（设置为 8）时，将链表转换为红黑树，加速查找。

---

### 6.1. 线性探查 Linear Probing

给定一个普通的散列函数 h': U -> {0, 1, 2, ..., m-1}，称之为 **辅助散列函数** (Auxiliary Hash Function)，线性探查方法采用的散列函数如下：

`h(k, i) = (h'(k) + i) \mod m`

其中 h' 为辅助散列函数，可以为普通的散列函数 h(k)，i 的取值为 0, 1, 2, ..., m-1，而 m 是哈希表长度。

给定一个关键字，首先探查哈希表的槽 T[h(k, 0)]，不满足条件则继续探查槽 T[h(k, 1)]，以此类推，直到槽 T[h(k, m-1)]。在线性探查方法中，初始探查位置决定了整个序列，故只有 m 种不同的探查序列。

线性探查方法比较容易实现，但它存在一个问题，被称为 **一次集群** (Primarily Clustering)。随着连续被占用的槽不断增加，平均查找时间也随之不断增加。由于线性探查方法的特性，集群现象很容易。这是因为当一个空槽前有 i 个满的槽时，该空槽为下一个将被占用的概率是 (i+1)/m，于是连续被占用的槽就会变得越来越长，因而平均查找时间也会越来越大。

但是，在 MIT 6.851 - [Dictionaries](https://www.youtube.com/watch?v=Mf9Nn9PbGsE) 课程中，Eric Demaine 说明了线性探查在某些场景下的实践中还是很高效的。场景如下：

- 对散列表空间的限制不大，即内存空间比较充足
- 散列表大小 `m >= (1 + \epsilon) n`
- 若散列函数的选择是完全随机的，则每个字典操作的期望时间为 `O(1 / (\epsilon)^2)`
	- 完全随机过于理想，考虑其它哈希函数
	- 如果使用 Universal Hashing 全域哈希函数，线性探查效果很差。
	- 如果使用 K-wise Independence，其中 K = O(log n)，则线性探查效果不错。
	- 2007 年：如果使用 K-wise Independence，其中 K = 5，则线性探查效果很好，每个操作期望时间为常数时间（依赖于 `\epsilon`）。
	- 但是如果使用 K-wise Independence，其中 K = 5，则线性探查效果很差，达到了 `\Omega(log n)` 的期望时间复杂度，与 BST 二叉搜索树类似了。
	- 如果使用 Simple Tabulation Hashing 简单表格哈希，能达到与完全随机级别的时间复杂度，即 `O(1 / (\epsilon)^2)`。
- 另外，如果使用 cache 机制缓存 `log^(1 + \epsilon) n` 的哈希查询，则能获得 O(1) 的摊还时间 w.h.p.。
- 因为线性探查对 cache 的利用效率本就更高，当访问了一个槽，与之相邻的一个 block 的槽都会被加载，从而加速线性探查的访问。经实验，它仅比直接内存访问慢 10%。

---

### 6.2. 二次探查 Quadratic Probing

二次探查采用如下形式的散列函数：

`h(k, i) = (h'(k) + c_1 * i + c_2 * i^2) \mod m`

其中 h' 为辅助散列函数，可以为普通的散列函数 h(k)，c\_1 和 c\_2 位正的辅助常数。i 的取值为 0, 1, 2, ..., m-1，而 m 是哈希表长度。

初始的探查位置为 T[h(k, 0)] = T[h'(k) + 0 + 0]，后续的探查位置要加上一个偏移量，该偏移量以二次的方式依赖于序号 i。这种探查方法的效果比线性探查好得多。但是，为了能够充分利用散列表，c\_1、c\_2 和 m 的值要收到限制。

此外，如果两个关键字的初始探测位置相同（即 h' 出现了碰撞冲突），那么它们的探测序列也是完全相同的，这一性质可导致一种相对轻度的集群，被称为 **二次集群** (Secondary Clustering)。像在线性探查中一样，初始探查位置决定了整个序列，这样也仅有 m 个不同的探查序列能被使用。

---

### 6.3. 双重散列 Double Hashing

双重散列是用于开放寻址法的**最好方法之一**，因为它所产生的排序具有随机选择排列的许多特性。双重散列采用如下形式的散列函数：

`h(k, i) = (h_1(k) + i * h_2(k)) \mod m`

其中 h_1 和 h_2 为辅助散列函数，可以为普通的散列函数 h(k)，i 的取值为 0, 1, 2, ..., m-1，而 m 是哈希表长度。

初始探查位置为 T[h(k, 0)] = T[h\_1(k) + 0]，后续的探查位置是前一个位置加上偏移量 h\_2(k) 模 m。因此，不像线性探查或二次探查那样仅依赖于初始位置，双重散列的探查序列会以两种不同的方式依赖于关键字 k，因为初始探查位置、偏移量或者二者都有可能发生变化。

为了能够查找整个散列表，值 h\_2(k) 必须要与哈希表的大小 m 互素。有两种简便的方法可以确保这个条件成立：

1. 取 m 为 2 的某个正整数幂，并设计一个总是产生奇数的辅助哈希函数 h\_2。
	- 而且取哈希表大小为 2 的幂，更方便于表的扩张/缩小操作，即采用加倍/减半策略。
2. 取 m 为某个素数，并设计一个总是产生比 m 小的正整数的辅助哈希函数 h\_2。
	- 例如，可以取哈希表大小 m 为素数，并取 `h_1(k) = k \mod m` 和 `h_2(k) = 1 + (k \mod m')`，其中 m' 略小于 m，比如取 m' = m - 1。

当 m 为素数或者 2 的幂时，双重散列法中用到了 `\Theta(m^2)` 种探查序列，而线性探查或二次探查仅用到了 `\Theta(m)` 种，故前者是后两种方法的一种改进。双重散列的性能看起来非常接近“理想的”均匀散列的性能。

尽管除素数和 2 的幂以外的 m 值在理论上也能用于双重散列中，但是在实际中，要高效地产生 h\_2(k) 确保使其与 m 互素，将变得更加困难。部分原因是这些数的相对密度 `\phi(m) / m` 可能较小。（可参考《CLRS》第 31 章 数论算法 第 3 节 模运算 公式 31.24）

---

### 6.4. 开放寻址散列表上的操作

- 在采用开放寻址法解决冲突后，散列表 T 上的字典操作如下：
	- 搜索 search：循环，从 index=0 开始到 m-1，通过某种探查技术计算出 h(key, index) 作为下标 去索引哈希表，查询到关键字后 与目标关键字匹配。如果为空，则表示找不到；如果为 DELETE 元素被删除标志，则跳到下个循环；如果关键字不相等，也跳到下个循环，计算 h(key, index+1)；如果关键字相等，则返回此元素。
	- 插入 insert：循环，从 index=0 开始到 m-1，通过某种探查技术计算出 h(key, index) 作为下标 去索引哈希表。如果当前位置为空，或者为 DELETE 元素被删除标志，则在当前位置插入；否则跳到下个循环，计算 h(key, index+1) 继续探查。
	- 删除 delete：进行搜索，如果搜索到了，则将此位置的元素删除，并置 DELETE 元素被删除标志，返回被删除的元素。

---

### 6.5. 开放寻址散列表时间复杂度分析

《CLRS》**定理 11.6**：给定一个装载因子为 `\alpha = n/m < 1` 的开放寻址散列表，并假设是均匀散列的，则对于一次不成功的查找，其期望的探查次数至多为 `1 / (1 - \alpha)`。

因此，如果 `\alpha` 是一个常数，由定理 11.6 可知，一次不成功的查找的运行时间为 O(1)。如果散列表是半满的，则一次不成功的查找的平均探查次数至多是 1 / (1 - 0.5) = 2。如果散列表是 90% 满的，则一次不成功的查找的平均探查次数至多是 1 / (1 - 0.9) = 10。

《CLRS》**推论 11.7**：假设采用的是均匀散列，平均情况下，向一个装载因子为 `\alpha` 的开放寻址散列表中插入一个元素至多需要做 `1 / (1 - \alpha)` 次探查。

《CLRS》**定理 11.8**：对于一个装载因子为 `\alpha < 1` 的开放寻址散列表，一次成功查找中的探查期望次数至多为 `(1 / \alpha) ln (1 / (1 - \alpha))`。假设采用均匀散列，且表中的每个关键字被查找的可能性是相同的。

因此，如果 `\alpha` 是一个常数，由定理 11.8 可知，一次成功的查找的运行时间为 O(1)。如果散列表是半满的，则一次不成功的查找的平均探查次数小于 1.387。如果散列表是 90% 满的，则一次不成功的查找的平均探查次数小于 2.559。

综上分析可知，开放寻址散列表的**性能通常很好**，只需要**在装载因子较高时进行哈希表扩张**（重建 rehash 的时候要注意把删除操作带来的 DELETE 标志给清除/忽略掉），避免哈希表过于充满，就可以维持此高效性。

---

## 7. 散列表的动态扩缩 grow / shrink

虽然知道 m 应该等于 O(n)，但是 n 是动态的，所以 m 也应是动态的，才能实用。

另外，Python 的 list 数据结构也支持动态扩缩，有时也被称为 resizable array，其原理与哈希表的扩缩也是类似的，根据当前的 load factor 加载因子 n/m 来决定。顺带一提，Python 的 `append(obj)` 尾部追加操作、`pop(index=-1)` 尾部删除都是 O(1) 的时间，但是在任意位置（尤其是首部）`insert(index, obj)` 插入、`pop(index)` 删除、`remove(obj)` 移除元素的耗时均为 O(n)，因为中间位置删除后，需要将后面的元素一一往左“挪动”。

不过与普通的 list 不同，**哈希表在扩张或者缩小后，都需要 rehash 重新散列**，所以为了避免过多的 rehash 影响实际性能，初始哈希表不能太小，扩缩哈希表的策略要精心设计。

重新建立哈希表耗时 O(n + m + m')。加 m 是因为要查看原本长度为 m 的哈希表中所有的 slot，而 m' 是新的哈希表大小。

注意：在建立新的哈希表前，要**更换哈希函数**（具体实现里，一般只需把哈希函数的某一个参数从 m 改为 m' 即可），记为 h'。

一般来说，扩张哈希表时，m' = 2m，这被称为 **Table Doubling**。考虑哈希表从 0 开始不断扩张，进行 n 次插入，重建哈希表的总耗时为 O(1 + 2 + 4 + ... + n) = O(n)，所以每次插入所造成的哈希表扩张的 Amortized Time **摊还时间为 O(1)**。

“摊还时间”的可以这么理解：就是按各 operation 操作的总时间进行平均。比如如果 k 次操作的总时间为 k T(n)，则单次操作的摊还时间就是 T(n)。进行摊还分析是很实用的，因为实际数据结构存储的元素往往是动态变化的。可以参考《CLRS》的第 17 章，也可以查看[此视频](https://www.youtube.com/watch?v=3MpzavN3Mco)。

同理，考虑哈希表缩小，k 次删除操作，每次删除操作所造成的哈希表缩小的摊还时间也为 O(1)。

如果加载因子为 1，即 n = m 时，再插入就扩张；加载因子为 1/2，即 n = m/2 时，就减半缩小，则有可能会“震荡”：比如当前有 n=8 个元素，m 也等于 8。插入第 9 个元素时，会扩张表 m' = 2m = 16。此后如果立即删除一个元素，则此时 n=8 = m'/2，又需要缩小表。

更好的方案是：当加载因子为 1/4，即 n = m/4 时，才减半缩小 m' = m/2，这样缩小之后还有 m/4 = m'/2 的空间是空闲的，此后进行的 m'/2 次插入也不会引起扩张。此时，可以证明，每次插入/删除操作所造成的哈希表扩张/缩小的摊还时间为 O(1)。

当然，如果预先知道当前数据量 n，可以直接初始化哈希表为 O(n)，比如 m = n 或者 2n 是个不错的初始化方式。

Java JDK 1.7 的 HashMap 数据结构的加载因子为 0.75，官方文档解释如下：

> As a general rule, the **default load factor (.75)** offers a **good tradeoff between time and space costs**. Higher values decrease the space overhead but increase the lookup cost (reflected in most of the operations of the HashMap class, including get and put). The expected number of entries in the map and its load factor should be taken into account when **setting its initial capacity**, so as to **minimize the number of rehash operations**. If the *initial capacity is greater than the maximum number of entries divided by the load factor*, no rehash operations will ever occur.

初始的哈希表容量 m 大于(当前)最大条目数 n 除以加载因子 (0.75)，则效率一般来说很好。并且当当前的加载因子达到 0.75 时扩张，而不是装满时才扩张。（这一点，在使用开放寻址法解决哈希冲突时 尤其重要，因为不能等到哈希表快满了才扩容，否则会极大地影响操作效率。）

---

## 8. 完全散列 Perfect Hashing

**完全散列 Perfect Hashing**，又被称为 **FKS Hashing**，由 Fredman, Komlos and Szemeredi 在 1984 年发明，其论文名为《Storing a Sparse Table with O(1) Worst Case Access Time》。

当关键字集合时 static **静态存储**（即关键字集合一旦存入后就**不再改变**，没有 insert 和 delete 操作，**只有 search 操作**），完全散列能够在 **O(1) 的最坏时间**内完成关键字查找。一些应用存在天然的静态关键字集合，如程序设计语言中的保留字集合，或者 CD-ROM 上的文件名集合。

完全散列采用**两级的散列方法**，在每级上都是用**全域散列** Universal Hashing，如下图所示：

![hashing-3](/img/info-technology/algorithm/data-structure/hashing-3.png)

第一级与带链接 chaining 的散列表基本上是一样的：利用从某一 Universal Hashing 全域散列函数簇中选出的一个散列函数 h，将 n 个关键字散列到 m 个槽中。

然后，不是将散列到槽 j 中的所有关键字建立一个链表，而是采用一个较小的 **二次散列表** (Secondary Hash Table) S\_j 及相关的散列函数 h\_j。利用精心选择的散列函数 h\_j，可以确保在第二级上不会出现碰撞冲突。为了确保这一点，需要让二级散列表 S\_j 的大小 m\_j 为散列到槽 j 中的关键字数目 n\_j 的平方，即 m\_j = (n\_j)^2。这种平方项的依赖看似会使得总体存储需求很大，但是通过适当地选择第一级散列函数，让第一级哈希值分布尽量均匀，可以将预期使用的总体存储空间限制为 O(n)。

另外，建立完全哈希表的期望时间为多项式时间，接近线性时间 O(n)，最坏期望不高于 O(n log^2 n)。

---

### 8.1. 完全散列的时空复杂度分析

根据 Birthday Paradox **生日悖论**，如果有 n 个人，其生日可选范围为 n^2，则任两人生日相同的概率为 1/2。即如下定理：

《CLRS》**定理 11.9**：如果从一个全域散列函数类中随机选出散列函数 h，将 n 个关键字存储在一个大小为 m = n^2 的散列表中，则表中出现冲突的概率小于 1/2。

**证明**：共有 组合数 `C_n^2` 对关键字可能发生冲突，如果 h 是从全域散列函数类 H 中均匀随机选出的，那么每一对关键字冲突的概率为 1/m。设 X 是一个统计冲突次数的随机变量，当 m = n^2 时，期望的冲突次数为 E[X] = (C_n^2) / n^2 = (n^2 - n) / 2 / n^2 < 1/2。此时再运用 Markov Inequality **马尔可夫不等式** Pr{X >= t} <= E[X] / t，将 t=1 代入，即完成证明。

当然，1/2 的概率是不算很高的，但是我们可以多次重复选择：一旦从 H 中选出的 h 不能满足（在当前第二级散列表上）无冲突，则重新随机选择另一个 h'，直到第二级散列表无冲突为止。

这是一个成功概率 p > 1/2 的 Geometric Distribution **几何分布**。假设 p=1/2，则 X\~G(1/2)，其期望为 1/p = 2，方差为 (1-p) / p^2 = 2。因此**期望的尝试次数仅为 2 次**，仍然是常数级的、高效的。另外，可以说 尝试次数为 O(log n) w.h.p.。

另外，为了尽量保证第二级上的冲突不高，避免大量空间浪费，在选择第一级散列函数时也是需要不断尝试，直到二级散列表的所需空间之和小于 cn，这里 c 为某个预设的常数，即 `\sum_{j=0}^{m-1} m_i^2 <= c * n`。为了保证第一级散列函数的期望尝试/选择次数为 O(1)，有如下定理：

《CLRS》定理 11.10：如果从某一个全域散列函数类 H 中随机选出散列函数 h，用它将 n 个关键字存储到一个大小为 m=n 的散列表中，则有 `E[\sum_{j=0}^{m-1} n_j^2] < 2n` 其中 n\_j 为散列到槽 j 中的关键字数目。

证明：对于任何自然数 a 而言，此恒等式成立：`a^2 = a + 2 C_a^2`，其中 `C_a^2` 为组合数。

于是有：`E[\sum_{j=0}^{m-1} n_j^2] = E[\sum_{j=0}^{m-1} (n_j + 2 C_{n_j}^2)]`

由期望的线性性，展开得 `= E[\sum_{j=0}^{m-1} n_j] + 2 E[\sum_{j=0}^{m-1} C_{n_j}^2]`

将加号左边的第一项求和起来，得 `= E[n] + 2 E[\sum_{j=0}^{m-1} C_{n_j}^2]`

由 `E[n] = n`，得 `= n + 2 E[\sum_{j=0}^{m-1} C_{n_j}^2]`

而对于求和式 `\sum_{j=0}^{m-1} C_{n_j}^2`，注意到它正是散列表中发生冲突的关键字的总对数。根据 Universality 全域散列性质，这一求和式的期望至多为 `C_n^2 / m = n(n-1) / (2m)`。

又因为定理中说明了 m=n，故有 `E[\sum_{j=0}^{m-1} n_j^2] <= n - 2n(n-1)/(2n) = 2n - 1 < 2n`，证毕。

《CLRS》**推论 11.11**：如果从某一全域散列函数类 H 中随机选出散列函数 h，用它将 n 个关键字存储到一个大小为 m=n 的散列表中，并将每个二次散列表的大小设置为 m\_j = n\_j^2 (j = 0, 1, ..., m-1)，则在一个完全散列方案中，存储所有二次散列表所需的存储总量的期望值小于 2n。

证明：此时 `m_j = n_j^2`，由定理 11.10，得 `E[\sum_{j=0}^{m-1} m_j] = E[\sum_{j=0}^{m-1} n_j^2] < 2n`，证毕。

《CLRS》**推论 11.12**：如果从某一全域散列函数类 H 中随机选出散列函数 h，用它将 n 个关键字存储到一个大小为 m=n 的散列表中，并将每个二次散列表的大小设置为 m\_j = n\_j^2 (j = 0, 1, ..., m-1)，则用于存储所有二级散列表的存储总量大于等于 4n 的概率小于 1/2。

证明：应用 Markov Inequality 马尔可夫不等式 Pr{X >= t} <= E[X] / t，并将 `X = \sum_{j=0}^{m-1} m_j` 和 t = 4n 代入推论 11.11 的不等式。得：

`Pr{\sum_{j=0}^{m-1} m_j >= 4n} <= E[\sum_{j=0}^{m-1} m_j] / (4n) < (2n) / (4n) = 1/2`，证毕。

因此，同第二级的几何分布 G(1/2) 一样，第一级散列也只需从全域散列函数类 H 中随机选出散列函数 h，尝试几次（**期望为 2 次**，也可以说次数为 O(log n) w.h.p.），就可以快速地找到一个所需存储量较为合理（即 O(n)）的散列函数。

---

### 8.2. 动态完全散列 Dynamic Perfect Hashing

对完全散列表而言，增删元素并不是不可能的。

对于一级散列表，也应根据当前的装载因子进行扩张/缩小。扩/缩之后，一级表和二级表都要重建，所以阈值设置要较高些，避免频繁重建。

增添元素：首先进行一级散列，然后进行二级散列。如果二级散列没有出现冲突，则增添元素成功。如果二级散列冲突了，则重建此二级散列表即可。重建包括：修改此二级散列表的大小，然后重新从 H 中散列函数 h，不断尝试直到无冲突，即重建成功。

删除元素：首先查找目标元素。一旦找到，先在二级散列表中删除。此二级散列表根据自己的装载因子来决定是否缩小。

---

## 9. 布谷鸟散列 Cuckoo Hashing

**简介**

- 布谷鸟哈希最早于 2001 年由 Rasmus Pagh 和 Flemming Friche Rodler 提出。
- 该哈希方法是为了解决哈希冲突的问题而提出，**利用较少计算换取了较大空间**。
- 名称源于该哈希方法行为类似于布谷鸟在别的鸟巢中下蛋，并将别的鸟蛋挤出的行为。
- 它具有**占用空间小、查询迅速**等特性，可用于**布隆过滤器** (Bloom Filter, BF) 和内存管理。

---

**具体算法**

- 使用 2 个哈希表 TA 和 TB，其大小 ma、mb 均不小于 `(1 + \epsilon) n`
- 每个哈希表有自己的哈希函数(族) ha 和 hb
- 对每个关键字 x，会利用 ha 和 hb 分别映射到哈希表 TA 和 TB 上
- **查询操作**：
	- 查找 TA[ha(x)] 和 TB[hb(x)]，取其中关键字等于 x.key 的元素。
	- 如果没有关键字匹配的元素，则表示找不到。
	- 时间复杂度为 O(1)
- **删除操作**：
	- 先查找，若找到，就直接从表中删除。
- **插入操作**：
	- 如果 TA 的 ha(x) 位置为空，则插入到 TA。
	- 如果 TB 的 hb(x) 位置为空，则插入到 TB。
	- 可以两个表都插入。
	- 如果两个表的目标位置都不为空，则从 TA 或者 TB 中替换占位了的元素，并重新将之插入另一个表。
		- 比如插入 x 时，在 TA 表中替换了元素 y，则将 y 插入 TB 的 hb(y.key) 位置（此位置可能也已被占用，则替换之，递归进行此操作）。
		- 需要进行限制，避免“无限递归”（这是有可能发生的，尽管概率不高）。
- **更新操作**（包含 rebuild/rehash 重建）：
	- 如果哈希函数的选择是完全随机的，或者是 K-wise Independent，其中 K = O(log n)，则 update 更新操作的摊还期望时间复杂度为 O(1)。
	- 但是重建时，存在 O(1/n) 的失败可能性。
	- 如果重建失败了，则重新重建即可。
	- 另外，如果 K = 6，则重建失败的可能性是很高的。
	- 如果使用 Simple Tabulation Hashing 简单表格哈希，则重建失败的可能性为 `\Theta(1 / n^{1/3})` w.h.p.。

Cuckoo Hashing 与 Perfect Hashing 完全哈希有相似之处，前者是同时进行两个 hash 运算，后者是连续进行两次 hash 运算。

---

## 10. 布隆过滤器 Bloom Filter

- Bloom Filter 是由 Howard Bloom 在 1970 年提出的 bit vector **二进制向量** **概率型数据结构** (Probabilistic Data Structure)，它常被用来**检测一个元素是不是集合中的一个成员**，具有**很好的空间和时间效率**。
- Bloom Filter 的原理：
	- 当一个元素被加入集合时，通过 K 个 hash 散列函数将这个元素映射成一个位数组中的 K 位 (bit)，把它们置为 1。
	- 在检索时，只需要检查这 K 位是不是都是 1 就（大约）知道集合中有没有它了：
	- 如果这些点有任何一个 0，则被检元素**一定不存在**；如果都是 1，则被检元素**很可能存在**。
- Bloom Filter 的**插入和查询操作十分高效**，但是**传统的 Bloom Filter 不支持删除操作**，后来提出的 Counting Bloom Filter 可以支持元素删除。
- Bloom Filter 中 bit 数组大小 m 的选择，要基于预估的数据量 n 和预期的误判率 fpp，一般设置为 `m = (-n ln(fpp)) / (ln 2)^2`。
- Bloom Filter 中哈希函数数量 K 的选择，要基于预估的数据量 n 和 bit 数组大小 m，一般设置为 `K = (m/n) ln 2`。
- 哈希函数的选择对 BF 性能的影响很大，一个好的哈希函数要能近似等概率地将关键字 key 映射到 bit 数组的各位。可以考虑从全域散列函数族 H 中选择 K 个不同的哈希函数。

---

## 11. 一致性散列 Consistent Hashing

一致性哈希 Consistent Hashing 于 1997 年的[论文](https://dl.acm.org/doi/10.1145/258533.258660)《Consistent hashing and random trees: distributed caching protocols for relieving hot spots on the World Wide Web》中被提出。

在做**服务器负载均衡**时候可供选择的负载均衡的算法有很多，包括：轮循算法 Round Robin、哈希算法 Hashing、最少连接算法 Least Connection、响应速度算法 Response Time、加权法 Weighted 等。其中**哈希算法是最为常用的算法**。

在 MemCached、Key-Value Store、BitTorrent DHT、LVS 中都采用了 Consistent Hashing 算法，可以说 Consistent Hashing 是分布式系统负载均衡的首选算法。

一致性哈希 Consistent Hashing 的**典型应用场景**：有 N 台提供缓存服务的 cache 服务器（如 Redis）。需要对服务器进行负载均衡，将请求平均地分发到每台服务器上，让每台机器负责 1 / N 的服务。

简单直接的哈希算法是让 hash 函数的结果 mod 模机器的数量 N。对机器编号从 0 到 N-1，先计算哈希值 `index = h(x)` 作为机器下标，然后将请求分发给下标为 index 的机器。其中用到的散列函数常为全域散列函数 `h_{ab}(x) = ((ax + b) \mod p) \mod N`。注意：这里的“散列表”大小即为机器数量 N。

但这样的方法存在如下**致命问题**：

- 如果某一台机器宕机：
	- 那么应该落在该机器的请求就无法得到正确的处理
	- 这时需要将宕掉的服务器从算法从去除，即修改哈希公式，从 `\mod N` 变为 `\mod (N-1)`
	- 因此其余 N - 1 台服务器的缓存数据都需要重新进行计算
- 如果需要新增一台机器：
	- 也需要修改哈希公式，从 `\mod N` 变为 `\mod (N+1)`
	- 因此原先的 N 台服务器的缓存数据也都需要重新进行计算

对于系统而言，这通常是**不可接受的颠簸**，因为这意味着大量缓存的失效或者数据需要转移。而且如果在机器数量变化的时候，清除所有缓存，可能会导致缓存击穿甚至缓存雪崩，严重情况下可能会引发数据库宕机。

可以看出，上述问题是由于公式 `index = h_{ab}(x) = ((ax + b) \mod p) \mod N` 中需要对当前机器数量 N 做模运算，因此机器数量的改变 会使得原本被散列好的数据需要 rehash 重建。

---

Consistent Hashing 解决此问题的核心思想，就是**修改上述公式，不对机器数量取模，同时尽量保证负载均衡**。

由于 hash 算法结果一般为 unsigned int 型，因此我们希望 hash 函数的结果应该均匀分布在闭区间 \[ 0, 2^32 - 1 \] 内。因此 Consistent Hashing 假设用 2^32 个离散点来均匀切割一个“圆环”，首先按照散列函数 `server_index = h_{ab}(x) = ((ax + b) \mod p) \mod m` 算出服务器（节点）的哈希值，这里 m = 2^32。server_index 表示某台服务器位于此下标位置。

而对于新的请求/对象，也使用同一个散列函数将之散列到“圆环”上。不过服务器数量一般很小，所以新请求的散列值刚好等于某个 server_index 的可能性并不高，因此通常的做法是将该请求分配给“最近”（一般固定为顺时针/逆时针寻找）的服务器节点来执行。

![consistent-hashing-1](/img/info-technology/algorithm/data-structure/consistent-hashing-1.png)

如上图所示，图中圆形结点表示服务器节点，而五角星表示 Query 请求 / 需缓存的数据。缓存请求都是顺时针地寻找服务器节点来处理的。

在这种情况下，服务器的增/减 只会影响一个 server_index 节点。从左图到右图，增加了红色的结点，那么将原本分配给紫色服务器节点的其中一些缓存数据 重新分配给红色服务器节点即可。从右图到左图，删除了红色服务器节点，便将原本分配给红色服务器的缓存数据 重新分配给紫色结点
即可。

因此 Consistent Hashing 可以很好地解决由于新增/删除服务器节点所引起的 hash 值颠簸问题。

---

Consistent Hashing 存在的问题：如果服务器节点在“圆环上”分布不均匀，就可能导致负载不均衡。比如前面图片的左图，紫色服务器节点的负担重于蓝色服务器和绿色服务器。图像比较简略，如果是实际情况，可能负载不均衡的情况更为严重。

在不做特殊处理的情况下，由于服务器的数量相比于 2^32 而言是相当小的，因而服务器节点在“圆环”上的分布也是很稀疏的，所以无法奢望服务器节点的散列值均匀分布在“圆环”上，因此有如下**虚拟节点**的提出来解决负载均衡问题。

**虚拟节点 Virtual Nodes** 可以被认为是实际节点的复制品 (replicas)，其本质与实际节点是一样的（但与实际节点的关键字 key 并不相同）。引入虚拟节点后，将每个实际的服务器节点 按照一定的比例“扩大”为虚拟节点。例如扩大 100 倍，则对于每一个实际服务器节点而言，都会被散列到圆环上的 100 个不同位置。如果某个新请求被分配给了某个虚拟节点，会交给相应的实际服务器节点来处理。从而解决了节点数较少的情况下哈希值在圆环上分布不均的问题。

当然，虚拟节点的使用也是需要考量、运用一些启发式规则的。比如先检查当前服务器节点在“圆环”上的分布，然后在稀疏的区域插入虚拟节点。注意：如果虚拟节点过多，在增删机器时可能也会造成比较大的颠簸问题，尽管这个颠簸程度远不及简单直接的哈希算法那么致命。

Consistent Hashing 的实现可以使用 Random Tree 数据结构（度为 d 的多叉树）。参见课程 [Consistent Hashing and Random Trees](https://www.youtube.com/watch?v=hM547xRIdzc)。

## 12. Python dict

在 Python 中，build-in 内建的数据结构 **字典 dict 是通过散列表实现的**。字典也被称为**关联数组**、**哈希数组**等。Python dict 也是一个数组，其索引是原始 key 键经过哈希函数处理后得到的散列值。

Python dict 中使用的散列函数即为[内建的 hash 函数](https://docs.python.org/3.7/library/functions.html#hash)。

Python2 使用**开放寻址法**解决冲突，CPython 使用 Pseudo-Random Probing **伪随机探测技术**的 Hash Table 散列表 作为字典的底层数据结构。Python 也是根据**装载因子** `\alpha = n/m` 来决定**表的扩张/缩小**。一般选取在装载因子 0.75 的时候扩张，而在 0.25 的时候缩小。

---

在 Python dict 的哈希表中，一个 key-value 对被称为一个 entry（也即 slot），封装为 PyDictEntry 结构体，如下：

```c
typedef struct {
    /* Cached hash code of me_key.  Note that hash codes are C longs.
     * We have to use Py_ssize_t instead because dict_popitem() abuses
     * me_hash to hold a search finger.
     */
    Py_ssize_t me_hash;
    PyObject *me_key;
    PyObject *me_value;
} PyDictEntry;
```

me\_hash 用于**缓存 me\_key 的哈希值**，防止每次查询时都要计算哈希值，entry 有如下三种状态：

- **Unused**：me\_key 和 me\_value 均为 None
	- Unused 是 entry 的初始状态，me\_key 和 me\_value 均为 None
	- 插入元素后，Unused 状态转换成 Active 状态
	- 这是 me\_key 为 None 的唯一情况
- **Active**： me\_key 不为空且不为 Dummy，并且 me\_value 不为空
	- 插入元素后，entry 就成了 Active 状态，这是 me\_value 唯一不为 None 的情况
	- 删除元素后 Active 状态转换成 Dummy 状态
	- 进入 Active 状态后不会再变成 Unused 状态
- **Dummy**： me\_key 为 Dummy，并且 me\_value 为空
	- 此处的 Dummy 对象实际上一个 PyStringObject 对象，仅作为指示标志
	- Dummy 状态的元素仅作占位，可以在插入操作后被新元素覆盖，并变为 Active 状态
	- 进入 Dummy 状态后不会再变成 Unused 状态

![python-dict-state-1](/img/info-technology/algorithm/data-structure/python-dict-state-1.png)

---

PyDictObject 就是 PyDictEntry 对象的集合，其结构如下：

```c
typedef struct _dictobject PyDictObject;
struct _dictobject {
    PyObject_HEAD
    Py_ssize_t ma_fill;  /* # Active + # Dummy */
    Py_ssize_t ma_used;  /* # Active */

    /* The table contains ma_mask + 1 slots, and that's a power of 2.
     * We store the mask instead of the size because the mask is more
     * frequently needed.
     */
    Py_ssize_t ma_mask;

    /* ma_table points to ma_smalltable for small tables, else to
     * additional malloc'ed memory.  ma_table is never NULL!  This rule
     * saves repeated runtime null-tests in the workhorse getitem and
     * setitem calls.
     */
    PyDictEntry *ma_table;
    PyDictEntry *(*ma_lookup)(PyDictObject *mp, PyObject *key, long hash);
    PyDictEntry ma_smalltable[PyDict_MINSIZE];
};
```

- ma\_fill ：所有处于 Active 以及 Dummy 状态的元素总数
- ma\_used ：所有处于 Active 状态的元素总数
- ma\_mask ：所有 entry 的元素总数 (Unused + Active + Dummy)
- ma\_smalltable：创建字典对象时，会创建一个大小为 PyDict_MINSIZE == 8 的 PyDictEntry 数组。
- ma\_table：当 entry 数量小于 PyDict\_MINSIZE，ma\_table 指向 ma\_smalltable 的首地址，当 entry 数量大于 8 时，Python 把它当做一个大字典来处理，此刻会申请额外的内存空间，同时将 ma\_table 指向这块空间。
- ma\_lookup：字典元素的搜索策略

PyDictObject 使用 PyObject\_HEAD 而不是 PyObject\_Var\_HEAD，虽然字典也是变长对象，但此处并不是通过 ob\_size 来存储字典中元素的长度，而是通过 ma\_used 字段。

---

字典的三个基本操作（insert、search、delete）的平均时间复杂度均为 O(1)。

- **insert**：
	1. 把新元素 ele 的关键字 ele.key 通过哈希函数映射成一个整型数字 x，
	2. 然后让 x 对哈希数组的长度 m 进行模运算，其结果作为哈希数组的下标 index，
	3. 如果此位置已有元素
	4. 将新元素的值对象 ele.value 存储在下标为 index 的位置。
- **search**：同上，把查询关键字 key 通过哈希函数和模运算转换为下标 index。如果哈希数组中此下标位置有值对象，则直接返回；否则搜索不到，抛出 KeyError。
- **delete**：先 search 到目标元素，如果有此元素，则删除，并将此位置标记为 dummy。

另外，Python 中的 set 集合数据结构底层也是基于散列表实现的，只是 set 的哈希表只存储关键字/键 key 的引用，而没有对值元素 value 的引用，其它的和 dict 数据结构基本上是一致的。

---

注意：

1. Python dict 只允许可哈希的对象才能作为字典的键，包括 number 数值、str 字符串、tuple 元组等不可变的内置类型。而可变类型（如 list 列表，dict 字典和 set 集合）都是不可哈希的，因此不能作为字典的键。
2. 至于自定义的对象，如果想要支持内置的 hash 函数，需要在对象中实现 \_\_eq\_\_ 方法来检测元素的相等关系。若 a == b 为真，则 hash(a) == hash(b) 也为真。
3. 字典的内存开销较大，是一种以空间换时间的策略。
4. dict 字典中键查询速度很快 O(1)，相对地，list 列表查询则是按顺序一个个地遍历。
5. 往字典里面添加新键可能导致哈希表扩容，并导致哈希数组中键的次序变化（因为会 reahsh 重建表）。因此，不应在遍历字典的同时进行字典的修改（类似于数据库事务中的“读脏数据”问题）。

---

## 应用场景

- search engine
	- 比如搜索引擎输入框的 spelling correction 词语纠错，原本所有词汇都在一个已经建立好的词典（哈希表）中，在用户输入英文词语后，如果该词语在字典中搜索不到，就有可能是用户输入了错词。那么此时(以一定策略)修改词语中的某些字母、反复查询字典，找到正确的拼写，并提示用户。
- doc dist
- databases
- compilers & interpreters
- virtual memory / MMU
- network router / server
- ...

更细粒度的应用，比如：

- substring search
	- Unix 中的 grep 命令即是如此，见[字符串](./string) 的 Rabin-Karp 算法
- string commonality（比如比较两字符串的 edit distance 编辑距离）
- file and dictionary synchronization（比如 Unix 中的 rsync 命令、unison 命令，以及 Dropbox 应用）
	- 使用 hashing 操作来记录文档的变化
- cryptography & digital signature & authentication
	- 比如可以在数据库中存储 password 密码被哈希函数 one-way 单向运算 后的结果，而非明文。这样使得即便 sysadmin 系统管理员也不能获取此密码。（这个方法成功的关键在于 要求极低的哈希碰撞可能性）
- ...

---

## 代码范例

### Python

Python 环境：Python 3.7

[GitHub Code Link](https://github.com/YuweiYin/Code_Play/blob/master/Algorithm-Essence/data-structure/hashing.py)

## 参考资料

- Introduction to Algorithm (aka CLRS) Third Edition - Chapter 11
- MIT 6.006 Introduction to Algorithms, Fall 2011
    - 8. [Hashing with Chaining](https://www.youtube.com/watch?v=0M_kIqhwbFo)
    - 9. [Table Doubling, Karp-Rabin](https://www.youtube.com/watch?v=BRO7mVIFt08)
    - 10. [Open Addressing, Cryptographic Hashing](https://www.youtube.com/watch?v=rvdJDijO2Ro)
- MIT 6.046J Design and Analysis of Algorithms, Spring 2015
    - 8. Randomization: [Universal & Perfect Hashing](https://www.youtube.com/watch?v=z0lJ2k0sl1g)
- MIT 6.851 Advanced Data Structures, Spring 2012
	- 10. [Dictionaries](https://www.youtube.com/watch?v=Mf9Nn9PbGsE)
- MIT 6.854J Advanced Algorithms
    - Lecture 06, 09/18: [Hashing](https://www.youtube.com/watch?v=z8DD-ikAjzM)
    - Lecture 07, 09/23: [Perfect Hashing](https://www.youtube.com/watch?v=N0COwN14gt0)
- MIT 6.854 (Advanced Algorithms), Spring 2016
    - Lecture 3: [Consistent Hashing and Random Trees](https://www.youtube.com/watch?v=hM547xRIdzc)
