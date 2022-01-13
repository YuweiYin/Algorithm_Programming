# Algorithm - Sort - Median & Order Statistic

By [YuweiYin](https://yuweiyin.github.io/)

## 简介

**中位数**和**顺序统计量** (Median & Order Statistic)

在一个由 n 个元素组成的集合中，第 i 个顺序统计量 (order statistic) 是该集合中**第 i 小**的元素。例如，在一个从 1 到 n 编号的元素集合中，**最小值**是第 1 个顺序统计量 (i=1)，**最大值**是第 n 个顺序统计量 (i=n)。

非形式化地说，**中位数** (median) 是它所属集合的“中点元素”。当集合的秩 n 为奇数时，中位数是唯一的，位于 i=(n+1)/2 处。当 n 为偶数时，存在两个中位数，分别位于 i=n/2 和 i=(n/2)+1 处。因此如果不考虑 n 的奇偶性，中位数总是出现在 `i = \floor((n+1)/2)` 处（**下中位数**）和 `i = \ceil((n+1)/2)` 处（**上中位数**）。

此后的分析中，中位数均指 下中位数。另外，为了方便起见，假设集合中的元素（的关键字 key）都是互异的。不过下述算法是可以推广到包含重复 key 的集合的。

- **选择问题**
	- 输入：一个包含 n 个（互异的）数的集合 A 和一个整数 i，1 <= i <= n。
	- 输出：元素 $ x \in A $，且 A 中恰好有 i - 1 个其它元素小于它。

如果使用比较排序算法，可以在 $ \Omega(n log n) $ 时间内解决此选择问题。比如可以使用[堆排序](./heap-sort)和[归并排序](./merge-sort)在 $ \Theta(n log n) $ 时间内对数据进行排序，然后在输出数组中根据下标找出第 i 小的元素即可。

如果使用[线性时间排序](./linear-time-sort)，可以在 O(n) 时间内解决此问题。但是线性时间排序会对输入集合的 key 做一定的约束限制，因此不算通用。

观察到这个选择问题也需要元素之间的比较，但又不像排序问题那样 需要把所有的元素都排好序。因此考虑是否可以在排序算法的基础上 减少一些对此问题无用的工作，从而达到 O(n) 的时间复杂度。

## 最小值和最大值

在一个有 n 个元素的集合（数组）中，遍历整个集合、做 n - 1 此比较可以确定其最小元素。

```python
# 求集合 (数组) 最小值
# 时间复杂度：O(n)
def minimum(self):
    assert isinstance(self.ele_list, list)
    ele_len = len(self.ele_list)
    if ele_len <= 0:
        # 数组为空，返回 None
        return None
    elif ele_len == 1:
        # 数组仅有一个元素，返回此唯一元素
        return self.ele_list[0]
    else:
        # 数组不止一个元素，先记录 min 为首元素
        min_ele = self.ele_list[0]
        # 然后遍历其余元素，与 min 比较
        for i in range(1, ele_len):
            # 若当前元素比 min 更小，则更新 min
            if self.ele_list[i].key < min_ele.key:
                min_ele = self.ele_list[i]
        return min_ele
```

同理，只需修改比较的条件，就可以改写出 O(n) 时间求最大值的算法。

从执行比较的次数来说，此算法是最优的。因为至少需要考虑到每一个元素，才能确定集合中的最小/最大元素，因此下界为 $ Omega(n) $，此算法的紧确界为 $ \Theta(n) $ 是最优的。

### 同时找到最小值和最大值

为了同时找到某集合的最大值和最小值，最简单的想法是各自执行一次 minimum 和 maximum 函数，分别找出最小值和最大值。这需要 2(n-1) 次比较，在渐近时间复杂度上是最优的。但是从总比较次数来说，只需要 `3 \floor(n/2)` 次比较就可以同时找到最小值和最大值。

具体方法是同时记录已知的最小值和最大值，然后**成对地**将集合元素与当前最值进行比较：

1. 让一对未比较过的集合元素 互相进行比较，得出较小者 和 较大者
2. 然后把较小者与当前 min 比较，并决定是否需要更换 min
3. 把较大者与当前 max 比较，并决定是否需要更换 max

这样每 2 个元素共需 3 次比较，提升了效率。

细节上，如果集合的秩 n 是奇数，则将 min 和 max 均初始化为首元素，然后成对处理余下的偶数个元素；如果 n 是偶数，则先对前两个元素进行比较，取较小者作为 min、较大者作为 max，然后成对处理余下的偶数个元素。

如果 n 是奇数，那么总共进行 `3 \floor(n/2)` 次比较；如果 n 是偶数，先进行 1 次初始比较，然后进行 3(n-2)/2 次比较，总共需要 (3n/2)-2 次比较。因此无论 n 是奇数还是偶数，总的比较次数至多是 `3 \floor(n/2)`。

```python
# 同时求集合 (数组) 最小值和最大值
# 时间复杂度：O(n)
# 需 3 \floor(n/2) 次比较，优于分别调用 minimum 和 maximum 的总共 2(n-1) 次比较
def min_max(self):
    assert isinstance(self.ele_list, list)
    ele_len = len(self.ele_list)
    if ele_len <= 0:
        # 数组为空，返回 None
        return None, None
    elif ele_len == 1:
        # 数组仅有一个元素，返回此唯一元素
        return self.ele_list[0], self.ele_list[0]
    else:
        # 数组不止一个元素，根据列表长度的奇偶性做处理
        if ele_len & 0x1:
            # 集合的秩为奇数，初始化 min 和 max 均为首元素
            min_ele = max_ele = self.ele_list[0]
            start_index = 1  # 之后从下标 1 开始处理剩余元素
        else:
            # 集合的秩为偶数，先进行初始比较，取较小者作为 min、较大者作为 max
            if self.ele_list[0] < self.ele_list[1]:
                min_ele = self.ele_list[0]
                max_ele = self.ele_list[1]
            else:
                min_ele = self.ele_list[1]
                max_ele = self.ele_list[0]
            start_index = 2  # 之后从下标 2 开始处理剩余元素
        # 然后遍历其余元素，成对地处理
        half = (ele_len - start_index) >> 1  # 剩余元素数目的一半
        for i in range(start_index, start_index + half):
            # 先让两个元素进行比较，得到较小者和较大者
            if self.ele_list[i].key < self.ele_list[i + half].key:
                # 若较小者比 min 更小，则更新 min
                if self.ele_list[i].key < min_ele.key:
                    min_ele = self.ele_list[i]
                # 若较大者比 max 更大，则更新 max
                if self.ele_list[i + half].key > max_ele.key:
                    max_ele = self.ele_list[i + half]
            else:
                # 若较小者比 min 更小，则更新 min
                if self.ele_list[i + half].key < min_ele.key:
                    min_ele = self.ele_list[i + half]
                # 若较大者比 max 更大，则更新 max
                if self.ele_list[i].key > max_ele.key:
                    max_ele = self.ele_list[i]
        return min_ele, max_ele
```

## 顺序统计量 - 选择问题

### 期望运行时间为线性的选择算法

这里以类似于 [快速排序](./quick-sort) 的方式，用分治法解决选择问题。与随机化快速排序一样，将输入数组进行递归划分。但与快速排序不同之处在于，快排会递归处理两边的数据，而选择算法则只需要处理其中的一边。根据渐近时间复杂度分析的主方法，可以知道快排的期望运行时间是 $ \Theta(n log n) $，而选择算法则是 $ \Theta(n) $。

```python
# (顺序统计量)选择算法
# 求集合 (数组) 中第 i 小的元素 (1 <= i <= ele_len)
def order_statistic_select(self, i):
    assert isinstance(self.ele_list, list)
    ele_len = len(self.ele_list)
    if ele_len == 0 or i <= 0 or i > ele_len:
        return None
    elif ele_len == 1:
        return self.ele_list[0]
    else:
        return self._quick_select(0, ele_len - 1, i)
        # return self._linear_select(self.ele_list[:], 0, ele_len - 1, i)

# 快速(顺序统计量)选择算法
# 利用类似随机化快速排序的方法
# 期望时间复杂度：\Theta(n)
# 最坏时间复杂度：\Theta(n^2) 不过由于做了随机化处理，几乎不会出现最坏情况
# 注意：由于快排的不稳定性，如果集合中有相同 key 的元素，则此算法求顺序统计量也是不稳定的
# 每次从数组 A 中选取主元 p(pivot) 下标，
# 默认升序排列，如下操作：
# 让 A[lo..p-1] 中的每个元素都小于等于 A[p]
# 让 A[p+1..hi] 中的每个元素都大于等于 A[p]
def _quick_select(self, lo, hi, target_order):
    # 当待排序数组的左下标等于右下标时为基本情况：
    # 该数组只有一个元素，返回之
    assert 0 <= lo <= hi < len(self.ele_list)
    if lo == hi:
        return self.ele_list[lo]
    # p = self._partition(lo, hi)             # 固定选择选取主元、划分区间
    # p = self._randomized_partition(lo, hi)  # 随机选取主元
    # p = self._mid_three_partition(lo, hi)   # 三数取中法
    p = self._mid_three_randomized_partition(lo, hi)  # 随机三数取中法
    assert p >= 0
    left_len = p - lo + 1  # 划分出的左子数组的长度，包括主元 p 在内，这些元素都小于等于主元 p 所代表的元素
    # 如果 left_len 恰等于 i，则找到了目标顺序统计量
    if target_order == left_len:
        return self.ele_list[p]
    # 如果 left_len 大于 i，表示应该在左子数组中寻找目标顺序统计量
    elif target_order < left_len:
        return self._quick_select(lo, p - 1, target_order)  # 在左子数组中递归
    # 如果 left_len 小于 i，表示应该在右子数组中寻找目标顺序统计量
    # 注意搜寻目标 i 要变成相对的"第 i 小"，即右子数组中的第 i - left_len 小
    else:
        return self._quick_select(p + 1, hi, target_order - left_len)  # 在右子数组中递归
```

有如下结论（参见《CLRS》Chapter 9.2）：假设所有元素是**互异**的，在**期望线性时间**内，可以找到任一顺序统计量，特别是中位数。

### 最坏运行时间为线性的选择算法

与前面的 `_quick_select` 方法类似，linear\_select 算法也通过对输入数组进行递归划分来找出所需元素。但是，在该算法中能够**保证**得到对数组的一个**好的划分**。linear\_select 算法使用确定性的（而非随机化的）划分算法（比如三数取中法），但做了一些修改，把划分的主元 pivot 也作为输入参数。

通过执行如下步骤，算法 linear\_select 可以确定一个有 n > 1 个**不同元素**的输入数组中第 i 小的元素。（如果 n = 1，则 linear\_select 只返回它的唯一元素作为第 i 小的元素。）

1. 将输入数组的 n 个元素划分为 `\floor(n/5)` 组，每组有 5 个元素。且至多只有一组由剩下的 n mod 5 个元素组成。
2. 寻找这 `\ceil(n/5)` 组中每一组的中位数：首先对每组元素（共 5 个）进行插入排序，然后确定每组有序元素的中位数（第 3 个元素）。
3. 对第 2 步中找出的 `\ceil(n/5)` 个中位数，递归调用 linear\_select 以找出这 `\ceil(n/5)` 个元素的中位数 x（如果 `\ceil(n/5)` 是偶数，则取 x 为下中位数）。
4. 利用修改过的 partition 划分子过程，以中位数 x 为主元对输入数组进行划分。让 k 比“划分低区”中的元素数目多 1，因此 x 是第 k 小的元素，并且有 n - k 个元素在划分高区。
5. 根据 i 和 k 的大小关系来处理：
	- 如果 i == k，则返回 x
	- 如果 i < k，则在划分低区递归调用 linear\_select 来找出其中第 i 小的元素
	- 如果 i > k，则在划分高区递归调用 linear\_select 来找出其中第 i - k 小的元素

有如下结论（参见《CLRS》Chapter 9.3）：最坏情况下，linear\_select 算法的运行时间是线性的 $ \Theta(n) $。

与比较排序算法类似，quick\_select 和 linear\_select 算法都是通过元素间的比较来确定它们之间的相对次序的。在比较模型中，即便是在平均情况下，排序算法仍然需要 $ \Omega(n log n) $ 时间。而线性时间排序算法在输入上做了一些假设，使得突破了 n log n 的下界，达到了 $ \Theta(n) $。

而上述的两种线性时间(顺序统计量)选择算法不需要任何关于输入的假设，不受限于比较排序的 $ \Omega(n log n) $ 下界，因为选择算法里没有对数据(整体)进行排序。

## 代码范例

### Python

Python 环境：Python 3.7

- **注**：
    - 如果要运行此代码，需先将 Element 类置于本代码中。
    - Element 类完全可以根据程序需求来自定义，但是需要给出该类中的 key 和 value 属性名。

[GitHub Code Link](https://github.com/YuweiYin/Code_Play/blob/master/Algorithm-Essence/sort/median-order-statistic.py)

## 参考资料

- Introduction to Algorithm (aka CLRS) Third Edition - Chapter 9
