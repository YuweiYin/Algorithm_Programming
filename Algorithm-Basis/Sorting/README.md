# Sorting

Algorithm - [YuweiYin](https://github.com/YuweiYin)

---

- [中位数和顺序统计量](./median-order-statistic)

- **内部排序**：待排序的数据全部存放在内存中，无须访问外存。
- **外部排序**：待排序的数据的数量庞大，不能一次全部加载入内存，需要在排序过程中访问外存。

[常用外部排序算法](http://data.biancheng.net/out_sort/)有 **多路归并排序**、**胜者树 & 败者树**、**置换-选择排序**、**最优归并树**（哈夫曼树 Huffman Tree）等，下文主要讨论内部排序算法。

## 基础的内部排序算法概览

[Wiki - Sorting Algorithm](https://en.wikipedia.org/wiki/Sorting_algorithm)

排序算法的 [基类 Sort](./sort-base-class)。

排序算法类型 | 算法名称 | 时间-平均情况 | 时间-最好情况 | 时间-最坏情况 | 空间-辅助存储 | 稳定性
:-: | :-: | :-: | :-: | :-: | :-: | :-:
插入排序 | **[直接插入排序](./insertion-sort)** | O(n^2) | **O(n)** | O(n^2) | O(1) | 稳定
插入排序 | **[希尔排序](./shell-sort)** | **O(n^1.3)** | **O(n)** | O(n^2) | O(1) | 不稳定
插入排序 | **Cube Sort** | O(n log n) | **O(n)** | O(n log n) | O(n) | 稳定
插入排序 | **Library sort** | O(n log n) | **O(n)** | O(n^2) | O(n) | 稳定
选择排序 | **直接选择排序** | O(n^2) | O(n^2) | O(n^2) | O(1) | 不稳定
选择排序 | **[堆排序](./heap-sort)** | **O(n log n)** | O(n log n) | O(n log n) | O(1) | 不稳定
选择排序 | **Smooth Sort** | O(n log n) | **O(n)** | O(n log n) | O(1) | 不稳定
交换排序 | **冒泡排序** | O(n^2) | O(n) | O(n^2) | O(1) | 稳定 | 
交换排序 | **[快速排序](./quick-sort)** | **O(n log n)** | O(n log n) | O(n^2) | O(log n) | 不稳定
归并排序 | **[二路归并排序](./merge-sort)** | **O(n log n)** | O(n log n) | O(n log n) | O(n) | 稳定
归并排序 | **Quad Sort** | O(n log n) | **O(n)** | O(n log n) | O(n) | 稳定
插入&归并 | **[Tim Sort](./tim-sort)** | O(n log n) | **O(n)** | O(n log n) | O(n) | 稳定
插入&归并 | **Block Sort** | O(n log n) | **O(n)** | O(n log n) | O(1) | 稳定
插入&归并 | **Patience Sorting** | / | **O(n)** | O(n log n) | O(n) | 不稳定
/ | **Franceschini's method** | O(n log n) | / | O(n log n) | O(1) | 稳定
[线性时间排序](./linear-time-sort) | **桶排序** | O(n) | O(n) | O(n) | O(n) | 稳定
线性时间排序 | **计数排序** | O(n+k) | O(n+k) | O(n+k) | O(k) | 稳定
线性时间排序 | **基数排序** | O(d(r+n)) | O(d(r+n)) | O(d(r+n)) | O(r) | 稳定

- 注：
	- log 均表示**以 2 为底**的对数值。
	- “时间-” 表示时间复杂度
	- “空间-” 表示空间复杂度。此处仅考虑排序时需要的**额外辅助存储空间**。
	- 如果直接使用桶排序，桶的数量即为全部数据量 n。
	- 计数排序：
		- k 为原始数据的“直径”，即最大数与最小数的差值。这也是计数排序的“桶”数目。
		- 局限一：原始数据必须都要是整数。
		- 局限二：原始数据的“直径”过大时，可能造成很大的空间浪费。
	- 基数排序：
		- n 为关键字的个数，r (radix) 为关键字的基数（常为 10），d 为关键字的长度，d = log_r (number)
		- 例如，数字 128 在基数为 10 的情况下（十进制），长度 d = 3，有个位、十位和百位数字
		- 进行 d 趟排序，每趟对当前位进行桶排序。桶的个数即为 r（基数值）。
	- 原址 in-place 归并排序的空间复杂度为 O(1)，但是时间复杂度变成了 O(N^2)，一般不考虑。
	- 原址快速排序的空间复杂度，主要是栈空间的复杂度，平均 O(log n)、最好 O(1)、最坏 O(n)

## 标准库的排序函数

### C++ 标准库 sort 函数

- 由快速排序、直接插入和堆排序混合而成，可参考《STL 源码剖析》。
- 当数据量比较大的时候先使用快速排序，当数据量较小的时候用直接插入排序。
- 因为当数据量较小时，快排中的每个部分基本有序，接近直接插入的最好情况的时间复杂度 O(n)。

### Java 标准库 sort 函数

- 归并排序的变种
- C++ 模板有着很好的 inline 优化机制，比较操作相对于赋值（移动）操作要快的多（尤其是元素较大时），但 Java 中的情况正好相反，移动（赋值）操作一般比比较操作快。
- 一般情况下，归并排序的比较次数小于快速排序的比较次数，而移动次数一般多于快速排序的移动次数，二者大约都是 2～3 倍的差距。

### Python 标准库 sort 函数

- 1.5.2 版本前，使用 ANSI C 的快速排序 qsort，但不同平台上的 qsort 实现不同，也造成 Python 排序效果的不一致。
- 1.5.2 版本后，Python 实现了自己的排序算法（一种混合算法 Hybrid Algorithm），而不再使用 qsort。

Python 原本使用的是一种 highly tuned samplesort hybrid 的混合排序方法，对不同情况的数据自动采用不同的排序算法：

1. 首先，用 O(N) 时间，检查数据是否已经排好序（升序或者降序），如果已有序，则直接按需求（根据目标是升序还是降序）返回了。
2. 如果已经基本有序，或者数据量很小（小于 100 个），就使用 Binary Insertion Sort 算法。
	- Binary Insertion Sort 与普通的插入排序算法基本一样，只是在确定插入位置时使用 Binary Search 二分查找算法。
3. 如果数据集很大，则会使用 [Sample Sort](https://en.wikipedia.org/wiki/Samplesort) 样本排序算法。
	- Sample Sort 与 qsort 很相似，但在取主元 pivot 值时不像 qsort 只取一个，而是取多个值形成 pivot。

- Tim Peters 在 2002 年设计了 Tim Sort 算法，并在 Python 中使用（TimSort 是 Python 中 sort 函数的默认实现）。
- 该算法找到数据中已经排好序的块 (分区)，每个分区被称为一个 run，然后按规则合并这些 run。
- Pyhton 自从 2.3 版以来一直采用 Timsort 算法排序。Java SE7 和 Android 也采用 Timsort 算法对数组排序。

JSE7 的 Timsort 实现代码中的一段话：

A stable, adaptive, iterative mergesort that requires far fewer than n lg(n) comparisons when running on partially sorted arrays, while offering performance comparable to a traditional mergesort when run on random arrays.  Like all proper mergesorts, this sort is stable and runs O(n log n) time (worst case).  In the worst case, this sort requires temporary storage space for n/2 object  references; in the best case,  it requires only a small constant amount of space.

## 排序算法类型


## 时间复杂度


## 空间复杂度


## 排序算法的稳定性

某排序算法“稳定”，是指该排序算法不会改变相同 key 值的元素 在原无序状态时的相对位置。

例如：原无序数组 `origin = [ 4, 2, 2, 3 ]`，各排序算法进行升序排列之后，结果都是 `res = [ 2, 2, 3, 4 ]`

但是 origin 数组中的两个 2 的相对位置是否在 res 数组中得以保持，就表明算法是否具有稳定性。

### 稳定性的意义

如果仅仅把 origin 数组中的 2 当成是一个数，其相对位置的变动似乎影响不大。

但如果数组中的每个元素都是一个结构体，排序的依据仅仅是结构体中的某一个 key 值（具有全序关系的量），那么相对位置如果改变，就会导致不同的 res 数组。

例如：原无序数组 `origin = [ [4, 11], [2, 22], [2, 33], [3, 44] ]`，排序的 key 是各元素（列表）中的首元素

那么如果是稳定排序，结果 `res = [ [2, 22], [2, 33], [3, 44], [4, 11] ]`

如果是不稳定的排序，结果**可能**为 `res = [ [2, 33], [2, 22], [3, 44], [4, 11] ]`

这就造成了不同的结果，可能影响之后别的操作。
