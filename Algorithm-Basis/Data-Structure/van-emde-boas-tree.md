# Algorithm - Data Structure - van Emde Boas Tree

By [YuweiYin](https://yuweiyin.github.io/)

## 简介

当关键字是有限范围内的整数时，某些排序算法（如计数排序）可以超越比较排序的 $ \Omege(n log n) $ 时间下界，达到线性时间复杂度。因此考虑：当关键字同是有限范围内的整数时，是否可以设计一种数据结构，使其支持动态集合上的 search、insert、delete、minimum、maximum、successor、predecessor 等操作仅需花费 O(log n) 时间？

van Emde Boas Tree (此后简称 vEB) 能够做到。

这是一个使用了 Divide and Conquer **分治法**思想的递归数据结构。如果关键字是来自离散集合 {0, 1, 2, ..., u-1} 的互异整数（如果不互异，则采用覆盖机制），且该集合的秩（全域大小）u 恰是 2 的自然数次幂，那么 van Emde Boas Tree 就能在 O(log log u) 的时间内完成上述每个操作。

## vEB 分析

关键字 key 取自全域 U = {0, 1, ..., u-1} 这样一个整数集合，且 vEB 树中的 key 不重复。

这里假定 u 是 2 的正整数幂次，比如 2^64 或 2^32。如果 u = 2^64，则 log\_{2} log\_{2} u = 6，这相比于数据量 n 而言（n 最多可以达到 u 个）可以视作常数级别。

进一步而言，如果 u = n^{O(1)} 或者 u = n^{(log n)^O(1)}，则 log log u = O(log log n)。这也说明了该渐进时间复杂度是很好的。

目标是以 O(log log u) 的时间完成如下操作：

- 判断存在性 `is_member(key)`
- 查找 `search(key)`
- 插入 `insert(key, val)`
- 删除 `delete(key)`
- 后继 `successor(key)`
- 前驱 `predecessor(key)`

此数据结构**重点解决的问题**是：全域空间 U 上稀疏地散布着许多点，给定一个新的关键字 key，以很快的速度找到其**前驱/后继**。

如果仅仅是为了查找、插入、删除这种字典操作，那么具有 O(1) 时间复杂度的哈希表结构是更优的选择。

如果是使用基于 BST 二叉搜索树的结构，那么各操作的时间复杂度一般都是 O(log n)。而 vEB 树则能达到 O(log log u)。

## vEB 应用

**网络路由器** Network Router 常使用 vEB 数据结构来存储 Routing Table **路由表**。路由表记录了各个区间(网段)的 IP 地址应该被转发往哪个路由器端口。用 vEB 中的整数 key 来表达各 IP 地址区间的边界，key 对应结点的 val 值对象 表达此 IP 区间的各种处理方式。

则 Query 就是：给定一个确切的 IP 地址，希望找到它属于哪个区间，从而执行相应的操作。

转换到 vEB 的任务，就是将新 Query 里的 IP 地址转成整数 key，迅速（O(log log u) 时间）找出此 key 的前驱/后继，便能确定该 IP 所在的区间，以及应该执行的路由操作（根据结点内的 val 值对象）。

虽然**区间查询任务**也可以考虑 [线段树](./segment-tree) (Segment Tree, ST)、[树状数组](./binary-indexed-tree) Fenwick Tree (Binary Indexed Tree, BIT)、[区间最值查询](./range-min-max-query) Sparse Table (Range Minimum/Maximum Query, RMQ) 等数据结构，但针对路由这个任务，IP 地址数量庞大、网段数目也可能特别多（IPv4 有 2^32 个 IP 地址、IPv6 有 2^128 个 IP 地址），并且需要转发速度很快，因此线段树和树状数组的 O(log n) 时间复杂度可能还是偏慢了。至于 Sparse Table RMQ，虽然查询的时间复杂度是 O(1)，但是一旦路由表项变化、增减就需要重建，这远达不到路由表的动态需求。

## 设计 & 细节

### 如何得到 O(log log u) ?

直觉 1：O(log n) 往往是指二叉搜索树的树高，如果能够对此树高进行二分查找，则可以达到 O(log log n)。

直觉 2：根据时间复杂度分析的主方法，式子 T(k) = T(k/2) + O(1)，意味着将数据规模为 k 的过程拆解为规模为 k/2 的过程 加上一个时间复杂度为 O(1) 的过程。这个式子可以推出 T(k) = O(log k)。那么将 k 替换为 log u，则 T(log u) = T((log u)/2) + O(1) 可以推出 T(log u) = O(log log u)。

但是 T(log u) 不够直观。由主方法可知，式子 `T(k) = T(\sqrt(u)) + O(1)` 就可以推出 T(k) = O(log log k)。此式子意味着要有一种算法，能够把数据规模为 k 的过程拆解为规模为 `\sqrt(k)` 的过程 加上一个时间复杂度为 O(1) 的过程。这就正是 vEB 数据结构的设计目标。

### bit vector + Tree

如果使用一个长度为 u 的 bit vector 位向量来记录某个 key 是否在 vEB 中（0-absence, 1-present）。那么插入和删除仅需 O(1) 时间便可完成：插入即为某位置 1、删除即为某位清 0。但是查找前驱或后继的操作需要 O(u) 的时间才能完成。

考虑直接在此长度为 u 的 bit vector 位向量上建立二叉树，则树高为 O(log u)，不是目标的 O(log log u)。下文先对此情况进行分析，然后再改进此方案。

先将此长度为 u 的位向量按固定长度 l 进行 clustering 分组，再在各个分组上建二叉树。比如 u = 2^4 = 16，而 `l = \sqrt(u) = 4`，则会将位向量分为长度为 4 的 4 组。随后在各个分组内建立二叉树，叶结点为分组内的 0 或者 1。从下往上，使用 逻辑或 运算得到父结点的值。树的高度为 `log_{2} l = log_{2} \sqrt(u) = 2`

例如，位向量为 `[0, 1, 0, 0,   0, 0, 0, 0,   0, 1, 1, 0,   0, 0, 0, 1]`

则高度为 1（叶结点高度为 0）的结点为 `[1, 0,   0, 0,   1, 1,   0, 1]`

高度为 2 的结点为 `[1,   0,   1,   1]`

若某个非叶结点的值为 1，就表明以此内部结点为根的子树的叶结点存在 1；否则表明不存在 1、全为 0。起到了总结的作用，因此将高度为 log\_{2} l = 2 的这层结点 `[1,   0,   1,   1]` 称为 summary vector。

当从位向量的某个位置查找其前驱/后继时，先查看此位向量所在的结点的 bit vector 如果没找到，则往上查找，查看相邻结点的 summary vector，若为 1，则在相邻结点往下找，否则往上找。（下图为《CLRS》中的示意图，前述位向量为 MIT 6.046J 的例子。）

![vEB-1](/img/info-technology/algorithm/data-structure/vEB-1.png)

从上可知，由于是二叉树是每两个结点进行“合并”，所以树高只能是 O(log\_{2} u)，但如果是 `\sqrt(u)` 个合并，即上例中的 4 个一组共同做逻辑或运算得到 1 个结果，则可以大幅缩减树高。

![vEB-2](/img/info-technology/algorithm/data-structure/vEB-2.png)

这样改进后，每个树结点只需存储自己的分组的 bit vector 和相应的 summary vector。搜索前驱/后继只需要对两个长度为 `\sqrt(u)` 位的 bit vector 以及一个长度也为 `\sqrt(u)` 的 summary vector 数组进行搜索，所以每个操作耗费 `O(\sqrt(u))` 时间。

此时仍未达到 O(log log u) 的目标。不过使用结点**度**为 `\sqrt(u)` 的树是产生 vEB 树的**关键思想**。回顾前面关于时间复杂度的主方法分析，此改进方案正是做到了式子 `T(k) = T(\sqrt(k)) + O(1)`！一次的规模缩小无法获得最优性能，那么多次缩小、让式子递归下去就可以了，最终能达到 T(k) = O(log log k)！

递归是针对于每个 `T(\sqrt(k))` 的：`T(\sqrt(k)) = T(\sqrt(\sqrt(k))) + O(1)`，即 每个分组(对应一个结点)也要被继续以根号长度被拆分，不断递归直到基本情况。

另外，在此改进版本中，插入操作仍然只需要 O(1) 时间，因为只需要将相应的位置以及 summary 改为 1。但删除操作稍微 tricky 些，因为 bit vector 是通过逻辑或运算得到的 summary，所以某一位改为 0 不一定表示 summary 要改为 0。（只有在此分组的 bit vector 全零时 summary 才会是 0）

确定 key=x 的簇号 i 和簇内偏移 j（以 `\sqrt(u)` 为簇长度）：由 `x = i * \sqrt(u) + j` 知， `i = int(x / \sqrt(u))` 和 `j = x % \sqrt(u)`

此后记簇号为 `high(x) = int(x / \sqrt(u))`，簇内偏移为 `low(x) = x % \sqrt(u)`

### 递归结构

![vEB-3](/img/info-technology/algorithm/data-structure/vEB-3.png)

- “原型”树 V 含有 n 个 vEB 结点
- 对每个 vEB 结点 v 而言
	- v.cluster 是长度为 `\sqrt(u)` 的 vEB 结点指针列表
	- v.summary 是指向相应的 summary（也是一个 vEB 结点）的指针。

### 查找后继 successor(v, x)

设置每个列表的最左哨兵为 -inf 负无穷，最右哨兵为 inf 无穷。

1. 先从 x 所在的 v.cluster 中找 x 的后继：
	- i = high(x)
	- j = successor(v.cluster[i], low(x))
2. 如果找不到，此时 j 为 inf 无穷
	1. 则查看 summary 结构中的后继簇号 i = successor(v.summary, i)
	2. 找到后继簇号后，从此簇中查找最左元素 j = successor(v.cluster[i], -inf)
3. 返回 i、j 的下标

如果使用上述方案来查找后继，由于进行了三次递归调用，因此时间分析：`T(k) = 3 T(\sqrt(k)) + O(1)`，从而 T(u) = O(log u)^(log 3)，而不是 O(log log u)。

如果只进行一次递归调用，让表达式变为 `T(k) = T(\sqrt(k)) + O(1)`，则可以达到 T(u) = O(log log u)。

为了避免 2.2 的递归调用，可以在每个 vEB 结点中存储并维护每个簇中的最左/小元素 v.min。方式：在往 v 中插入 x 时，增添此操作：`if x < v.min: v.min = x`。此时 2.2 的递归调用就可以改为 `j = v.cluster[i].min`，仅需 O(1) 时间。

现在考虑如何让 1.2 的递归 和 2.1 的递归不会一起调用，而是在不同的分支中。如果能在 O(1) 时间判断后继是否在 v.cluster[high(x)] 簇中，则可以根据此判断结果，要么执行 1.2 递归，要么执行 2.1 递归，而不会两者均执行，这便能将时间分析式改为 `T(k) = T(\sqrt(k)) + O(1)` 了。

为了做到这点，可以在每个 vEB 结点中存储并维护每个簇中的最右/大元素 v.max。方式：在往 v 中插入 x 时，增添此操作：`if x > v.max: v.max = x`。这样只需比较 x 与 v.cluster[high(x)].max 即可判断 x 的后继是否在 v.cluster[high(x)] 簇中了。

![vEB-4](/img/info-technology/algorithm/data-structure/vEB-4.png)

因此改进的 O(log log u) 时间复杂度的查找后继操作伪代码如下：

```python
def successor(self, v, x)
	# 先判断 x 所在的 v.cluster 中是否存在 x 的后继：
	i = high(x)
	if low(x) < v.cluster[i].max:
		j = self.successor(v.cluster[i], low(x))
	# 如果找不到
	else:
		# 查看 summary 结构中的后继簇号
		i = self.successor(v.summary, i)
		if i < len(v.summary):
			# 找到后继簇号后，从此簇中获取最左元素
			j = v.cluster[i].min
		else:
			# 找不到后继簇号，没有后继
			return -1, -1
	# 返回 i、j 的下标
	return index(i, j)
```

另外，可以看出，successor 操作里的分支选择，实际上就在对整个 vEB 树的树高进行二分搜索，因此直觉上可以达到 O(log log u) 的时间复杂度。

至于查找前驱 predecessor(v, x) 操作则与之对称了，但有一处需额外注意。下面给出完整的查找前驱代码：

```python
# 根据 key 值查找前驱结点
# 查找成功返回该前驱的 key, val；否则返回 inf, None
# 时间复杂度 O(log log u)
def predecessor(self, key):
    if isinstance(key, int) and 0 <= key <= self.veb_u:
        if isinstance(self.veb, TreeNode):
            return self._predecessor(self.veb, key)
        else:
            # vEB 树为空树
            return self.inf, None
    else:
        print('predecessor: key invalid:', key)
        return self.inf, None

def _predecessor(self, v, key):
    if isinstance(v, TreeNode):
        assert v.power >= 0 and v.u == (1 << v.power) and v.sqrt_u == (1 << (v.power >> 1))
        # 基本情况：当 power=1 (也即 u=2 和 sqrt_u=1) 时，为叶结点，至多含两个值 min/max
        if v.power == 1:
            # 当前是叶结点，如果 key 比 max_key 大，则前驱为 max
            if v.max_key != self.inf and key > v.max_key:
                return v.max_key, v.max_val
            # 如果 key 等于 max_key 并且 min 存在，则前驱为 min
            elif v.max_key != self.inf and key == v.max_key and v.min_key != self.inf and key > v.min_key:
                return v.min_key, v.min_val
            # 否则找不到后继结点
            else:
                return self.inf, None
        # 如果当前不是叶结点，且 key 大于当前结点的 max_key，则 max 就是其前驱
        elif v.max_key != self.inf and key > v.max_key:
            return v.max_key, v.max_val
        else:
            hi = self.high(key, v.power)
            lo = self.low(key, v.power)
            # 注意：由于 Lazy Insertion 策略，当前 key 可能不会被插入 v.cluster[hi] 中
            # 如果 v.cluster[hi] 不存在，表示当前 key 是该簇中的唯一元素，所以要查 summary
            is_pred_in = False  # 标志 key 的前驱是否位于 key 应在的簇 v.cluster[hi] 中
            if hi in v.cluster and isinstance(v.cluster[hi], TreeNode):
                # 获得 key 对应簇中的最小元素
                min_low = v.cluster[hi].min_key
                # 根据簇内偏移 lo，如果该簇中存在小于 key 的元素，则前驱就在此簇中
                if min_low != self.inf and lo > min_low:
                    is_pred_in = True
            # 如果在簇不存在或者该簇中找不到前驱，则通过查 summary 来确定前驱所在的 cluster
            # 而不是顺序遍历各个 cluster 来检查，从而提高了速度
            if is_pred_in:
                offset_key, offset_val = self._predecessor(v.cluster[hi], lo)
                return (hi << (v.power >> 1)) + offset_key, offset_val
            else:
                # 关键是找簇号 pred_key 而非值元素 pred_val
                pred_key, pred_val = self._predecessor(v.summary, hi)
                if pred_key != self.inf:
                    assert pred_key in v.cluster and isinstance(v.cluster[pred_key], TreeNode)
                    # 找到前驱簇号后，从此簇中获取最大元素
                    offset_key = v.cluster[pred_key].max_key
                    return (pred_key << (v.power >> 1)) + offset_key, v.cluster[pred_key].max_val
                else:
                    # 找不到前驱簇号
                    if v.min_key != self.inf and key > v.min_key:
                        # 与求后继不同的附加情况：x 的前驱存在，且是 v.min，因此前驱结点就是 v.min
                        # 但此时会 pred_key 会是 self.inf
                        return v.min_key, v.min_val
                    else:
                        return self.inf, None
    else:
        return self.inf, None
```

### 插入操作 insert(v, x)

为满足前述 successor 操作，insert 需要先执行：`if x < v.min: v.min = x` 和 `if x > v.max: v.max = x` 更新当前 vEB 结点 v 的最小值 min 和最大值 max。随后如下操作：

1. 先将 x 插入簇号为 high(x) 的簇中，即 v.cluster[high(x)]。再在此簇中的具体插入位置，即为簇内偏移 low(x)。因此需要递归调用插入操作：`insert(v.cluster[high(x)], low(x))`
2. 然后修改 v.summary 中的相应位，即执行 `insert(v.summary, high(x))`

如果使用上述方案进行插入，由于进行了两次递归调用，因此时间分析：`T(k) = 2 T(\sqrt(k)) + O(1)`，从而 T(u) = O(log u)^(log 2) = O(log u)，而不是 O(log log u)。

观察此过程，发现很多时间第 2 步的递归操作可以不用执行，因为此簇的 summary 位已经是 1 了。如果能 O(1) 时间内检测到这点，那么第 1 步和第 2 步就可以处在不同的分支中，从而让 insert 实际只执行一次递归。

另外，是否可以不让第 1 步一直递归地往下 insert，使得第 1 步的递归调用实则非常容易停下来呢？

idea: Lazy Insertion: Don't store the min recursively!

当新的元素 insert 进来时，如果它在某个 vEB 结点处是 min，则存储之，并终止递归。当另一个元素 insert 到此 vEB 结点，并且比原先的 min 更小，则替换之，并执行第 1 步的递归操作，将被替换的 old_min 往下插入。

结合上述两种改进，O(log log u) 时间复杂度的插入操作伪代码如下：

```python
def insert(self, v, x)
	# 先判断 x 所在的 v.cluster 中是否存在最小值 min
	if v.min is None:
		# 若不存在，则修改 min 和 max 后即可返回，不继续往下递归插入了
		v.min = v.max = x
		return
	# 如果此簇存在 min，表示不为空簇，需要递归插入 x
	else:
		# 判断是否需要更新最大值 max 和 最小值 min
		if x > v.max:
			v.max = x
		if x < v.min:
			# 此时不仅要更新最小值，还要将被替换的最小值往下递归插入
			swap(x, v.min)  # 交换 x 与 v.min
		# 判断 x 需要递归删除的簇是否为空
		if v.cluster[high(x)].min is None:
			# 若为空，则需要更新 summary
			# 注意：如果进入了此分支，执行了此分支中的递归，那么表明 v.cluster[high(x)] 簇是空，
			# 因此 self.insert(v.cluster[high(x)], low(x)) 递归仅会耗费 O(1) 时间
			self.insert(v.summary, high(x))
		self.insert(v.cluster[high(x)], low(x))
```

上述 insert 算法看起来在有的情况下会执行两次递归，但是正如注释里描述的那样，一旦进入内部分支需要执行 `self.insert(v.summary, high(x))`，就表明 x 本应插入的簇 `v.cluster[high(x)]` 为空。因此后面执行的递归调用 `self.insert(v.cluster[high(x)], low(x))` 一定会进入 `if v.min is None:` 下的分支中，仅需修改 v.min 和 v.max，此分支的运行时间为 O(1)。

因此，可以保证此插入算法的时间复杂度为 O(log log u)。

但是，由于没有把 x 递归地插入到所有子结点中，所以在查找后继的操作里，一旦 x < v.min，则直接返回 v.min 即可，不能再往下查找。即只需在 `successor(self, v, x)` 函数的第一行增加 `if x < v.min: return v.min` 即可。

### 删除操作 delete(v, x)

算法框架如下：

```python
def delete(self, v, x)
	# 如果删除的是 v.min 最小元素，做一些处理
	if x == v.min:
		pass
	# 执行删除
	self.delete(v.cluster[high(x)], low(x))
	# 如果此簇被删完了，则需要修改相应的 summary 位
	if v.cluster[high(x)].min is None:
		self.delete(v.summary, high(x))
	# 如果删除的是 v.max 最大元素，做一些处理
	if x == v.max:
		pass
```

两个 pass 的部分是删除 min 或 max 元素后的修复工作，

与 insert 操作里解决两个递归调用的想法类似，一旦 delete 操作里的两个递归过程都要执行，则需让其中一个是 O(1) 时间复杂度。具体而言，如果 `self.delete(v.summary, high(x))` 执行了，则让 `self.delete(v.cluster[high(x)], low(x))` 只耗费 O(1) 时间。

继续观察，一旦条件判断 `if v.cluster[high(x)].min is None` 为真，需要执行“内部”递归，表明刚刚删除的是 `v.cluster[high(x)].min`（因为最后一个删除的就是 min 元素）。这意味着进入“外部”递归后会进入 `if x == v.min` 分支，所以要在此分支中保证只进行 O(1) 时间的工作。

```python
if x == v.min:
	# 根据 v.summary.min，找到第一个非空的簇
	s_min = v.summary.min
	# 如果 v.summary.min 为 None，表明 v.summary 为空
	# 这表明：维持此结构不为空的唯一元素，仅是待删除的 x 元素，也即是 v.min
	if s_min is None:
		v.min = v.max = None
		return
	# 也有可能是：正在删除 v.min，但它并不是仅剩的唯一元素，因此要让另一个最小元素替换 v.min
	# 替换之后，再递归地删除用于替换的 v.cluster[s_min].min
	x = v.min = index(s_min, v.cluster[s_min].min)
```


```python
if x == v.max:
	if v.summary.max is None:
		# 有两种情况会进入此分支：1. 刚刚删除了最后一个元素，使得没有非空的簇了
		# 2. 前面的删除操作结束后，仅剩一个元素，即 v.min 了
		v.max = v.min
	else:
		# 根据 v.summary.max，找到最后一个非空的簇
		s_max = v.summary.max
		# 将此簇中的最大元素赋予 v.max
		v.max = index(s_max, v.cluster[s_max].max)
```

同样，可以保证此删除算法的时间复杂度为 O(log log u)。

### 建立 vEB

以 array 中的每个元素为 key，调用 insert 插入，逐步建立 vEB。时间复杂度 O(n log log u)

以 kv_array 中的每个元素为 [key, value] 数组，构建树结点。树结点设计如下：

```python
class TreeNode:
    def __init__(self, min_key=0x3f3f3f3f, min_val=None, max_key=0x3f3f3f3f, max_val=None, power=1):
        # 注意表示 min_key 和 max_key 为无的 inf 值可能需要根据场景变化
        # 因为有的应用（比如路由表）中全域 u 比 0x3f3f3f3f 还大，所以要重设 inf 值
        self.min_key = min_key  # 本结点存储的最小关键字 inf 表示无 min
        self.max_key = max_key  # 本结点存储的最大关键字 inf 表示无 max
        self.min_val = min_val  # 最小关键字的值对象，可以为任意对象
        self.max_val = max_val  # 最大关键字的值对象，可以为任意对象

        # 当 power=1 (也即 u=2 和 sqrt_u=1) 时，为叶结点
        # 叶结点至多含两个值 min/max，当只有一个值时，为 min
        self.power = power               # 全域大小 u = 2^power
        self.u = 1 << power              # 本结点的全域大小，为 2 的正整数 power 次幂
        self.sqrt_u = 1 << (power >> 1)  # 全域大小 u 的平方根

        # 可优化 self.cluster 为 dict 字典数据结构 (而不是 list 列表)，不存储为空的簇
        # 使得空间复杂度由 O(u) 降到 O(n log log u)。u 是整棵树的全域大小、n 是实际数据量
        self.cluster = dict({})  # 本结点的簇结点列表 (叶结点中没有子簇)
        self.summary = None      # 本结点的 summary 摘要结点 (叶结点中没有 summary 结点)
        self.is_summary = False  # 标志本结点是否为 summary 摘要结点。有些操作可能要据此区分处理
```

### 各种操作的下界分析

2007 年证明了：当全域大小 `u = n^{(log n)^{O(1)}}`，空间占用 `space = O(n poly(log n))` 时（poly 表示某个多项式函数），各种操作的渐进时间复杂度下界为 `\Omege(log log u)`。

因此，vEB 的各操作时间复杂度是紧确界 `\Theta(log log u)`

### 空间复杂度

vEB 树的空间复杂度为 O(u) 而非 O(n)。整棵树可以视作是建立在长度为 u 的 bit vector 上的，总共会有 2u - 1 个 vEB 结点。

**优化方案：仅存储非空的簇。**这样会使得空间复杂度降到接近 O(n)，具体而言，是 O(n log log u)。

但是，v.cluster 不应是 array 数组（或者 list 列表）类型了，而应该是 hash table [哈希表](./hashing)。当然，也可以不去手动实现哈希表，而是直接用 Python 的 dict 数据结构来存储簇。

## 代码范例

### Python

Python 环境：Python 3.7

[GitHub Code Link](https://github.com/YuweiYin/Code_Play/blob/master/Algorithm-Essence/data-structure/van-emde-boas-tree.py)

## 参考资料

- Introduction to Algorithm (aka CLRS) Third Edition - Chapter 20 van Emde Boas Tree
- MIT 6.046J Design and Analysis of Algorithms, Spring 2015
    - [4. Divide & Conquer: van Emde Boas Trees](https://www.youtube.com/watch?v=hmReJCupbNU)
