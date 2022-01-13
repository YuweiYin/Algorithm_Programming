# Algorithm - Sort - Tim Sort

By [YuweiYin](https://yuweiyin.github.io/)

## 简介

TimSort 排序算法 (Tim Sort)

[cpython/Objects/listsort.txt](https://github.com/python/cpython/blob/master/Objects/listsort.txt)

Timsort 是结合了 Merge Sort 归并排序和 Insertion Sort 插入排序而得出的排序算法，它在现实中有很好的效率。Tim Peters 在 2002 年设计了该算法并在 Python 中使用。TimSort 是 Python 中 list.sort 的默认实现。

该算法找到数据中已经排好序的 块-分区，每一个分区叫一个 run，然后按规则合并这些 run。Pyhton 自从 2.3 版以来一直采用 Timsort 算法排序，Java SE7 和 Android 也采用 Timsort 算法对数组排序。

## 场景描述及分析

### 示例

## 设计 & 细节

[A detailed description of timsort follows.](https://github.com/python/cpython/blob/master/Objects/listsort.txt#L211)

### 算法流程

### 实现细节

## 代码范例

[cpython 源码](https://github.com/python/cpython/blob/master/Objects/listobject.c)

### Python

Python 环境：Python 3.7

- **注**：
    - 排序算法的基类 Sort 和元素结构体类 Element 写法与 [此文章](./sort-base-class) 完全相同，故不在下方赘述。
    - 如果要运行此代码，则还需先将 Sort 类和 Element 类置于本代码中。
    - Element 类完全可以根据程序需求来自定义，但是需要给出该类中的 key 和 value 属性名。

[GitHub Code Link](https://github.com/YuweiYin/Code_Play/blob/master/Algorithm-Essence/sort/tim-sort.py)

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================
@Project : algorithm/sort
@File    : tim-sort.py
@Author  : YuweiYin
@Date    : 2020-05-16
=================================================="""

import sys
import time
# import random

"""
TimSort 排序算法 (Tim Sort)
"""


# Tim Sort (继承自 Sort 类)
# 空间复杂度(辅助存储)：O(n)
# 时间复杂度-平均 O(n log n)：对杂乱的数组 进行排序
# 时间复杂度-最好 O(n)：对已经按目标顺序排好序的数组 进行排序
# 时间复杂度-最坏 O(n log n)：对按目标顺序的逆序排列的数组 进行排序
# 算法稳定性：稳定
# Tim Sort 是 Python 中 sort 函数的默认实现
class TimSort(Sort):
    def __int__(self, ele_list, key_name='key', val_name='val'):
        super(TimSort, self).__init__(ele_list, key_name, val_name)
        self.runs = []  # run 列表

        # The maximum number of entries in a MergeState's pending-runs stack.
        # This is enough to sort arrays of size up to about
        #   32 * phi ** MAX_MERGE_PENDING
        # where phi ~= 1.618.  85 is ridiculously large enough, good for an array
        # with 2**64 elements.
        self.MAX_MERGE_PENDING = 85

        # When we get into galloping mode, we stay there until both runs win less
        # often than MIN_GALLOP consecutive times.  See listsort.txt for more info.
        self.MIN_GALLOP = 7

        # Avoid malloc for small temp arrays.
        self.MERGESTATE_TEMP_SIZE = 256

    # 重载 do_sort 方法
    # 排序操作前需已确保每个元素都含指定的 key_name 和 val_name 属性
    # 返回已排序的结果列表
    def do_sort(self, reverse=False):
        res = self._tim_sort()
        if reverse:
            return self.reverse_list(res)
        else:
            return res

    # Tim Sort，升序
    def _tim_sort(self):
        ele_len = len(self.ele_list)
        self.runs = []  # run 列表
        cur_run = [self.ele_list[0]]  # 当前正在处理的 run
        is_ascending = True  # 标志当前 cur_run 是否是升序

        # 先对待排序数组进行一遍扫描，按升序/降序分为多个有序的 runs
        # 如果是升序：a0 <= a1 <= a2 <= ...
        # 如果是降序，为了稳定性，须得是严格降序；a0 > a1 > a2 > ...
        # 随后将严格降序的 runs 反转成严格升序
        for i in range(1, ele_len):
            if i == ele_len - 1:
                # 对最后一个元素特别处理
                if getattr(self.ele_list[i - 1], self.key_name) <= \
                        getattr(self.ele_list[i], self.key_name):
                    # 当前元素相比上一元素是升序
                    if is_ascending:
                        # cur_run 也是升序。则直接加入当前元素
                        cur_run.append(self.ele_list[i])
                    else:
                        # 而 cur_run 是降序。
                        # 则先把 cur_run 逆序后加入 runs，再单独处理最后一个元素
                        cur_run = self.reverse_list(cur_run)
                        self.runs.append(cur_run)
                        cur_run = [self.ele_list[i]]
                else:
                    # 当前元素相比上一元素是严格降序
                    if is_ascending:
                        # 而 cur_run 是升序。则加入当前元素后逆序
                        assert len(cur_run) > 0
                        if len(cur_run) == 1:
                            # 如果当前 cur_run 仅有一个元素，则反转 cur_run
                            cur_run = [self.ele_list[i], self.ele_list[i - 1]]
                        else:
                            # 如果当前 cur_run 中有多个升序元素，
                            # 则需先将此 run 加入 runs，再单独处理最后一个元素
                            self.runs.append(cur_run)
                            cur_run = [self.ele_list[i]]
                    else:
                        # cur_run 也是降序。则加入当前元素后逆序
                        cur_run.append(self.ele_list[i])
                        cur_run = self.reverse_list(cur_run)
                # 把最后的 cur_run 加入 runs，完成扫描
                self.runs.append(cur_run)
                break
            if getattr(self.ele_list[i - 1], self.key_name) <= \
                    getattr(self.ele_list[i], self.key_name):
                # 左侧元素 <= 右侧元素 (升序)
                if is_ascending:
                    # 如果当前是升序，则直接将当前元素加入 cur_run，仍保持升序
                    cur_run.append(self.ele_list[i])
                else:
                    # 否则先把之前的降序 run 反转过来，加入 runs，再处理当前 run
                    cur_run = self.reverse_list(cur_run)
                    self.runs.append(cur_run)
                    cur_run = [self.ele_list[i]]  # 单个元素，改为升序
                    is_ascending = True
            else:
                # 左侧元素 > 右侧元素 (严格降序)
                if is_ascending:
                    # 如果当前是升序，判断 cur_run 中元素个数
                    assert len(cur_run) > 0
                    if len(cur_run) == 1:
                        # 如果当前 cur_run 只有一个元素，加入当前元素，并则改为降序
                        cur_run.append(self.ele_list[i])
                        is_ascending = False
                    else:
                        # 如果当前 cur_run 中有多个升序元素，则需现将此 run 加入 runs
                        self.runs.append(cur_run)
                        cur_run = [self.ele_list[i]]  # 单个元素，仍保持降序
                else:
                    # 如果当前已是严格降序了，则直接将当前元素加入 cur_run，仍保持降序
                    cur_run.append(self.ele_list[i])

        # 当前的 runs 列表中的 run 均为升序 (或严格升序)
        # TODO 调整 run，让其最低长度不低于 minrun 64

        # 对已排序的各个 run 两两进行合并 (必须合并连续的两个 run)
        sorted_list = self.merge_runs(0, len(self.runs) - 1)

        return sorted_list

    # 原址反转列表
    @staticmethod
    def reverse_list(ele_list):
        if isinstance(ele_list, list) and len(ele_list) > 1:
            lo = 0
            hi = len(ele_list) - 1
            # 对撞指针
            while lo < hi:
                temp = ele_list[lo]
                ele_list[lo] = ele_list[hi]
                ele_list[hi] = temp

                lo += 1
                hi -= 1
            return ele_list
        else:
            return ele_list

    # 二分搜索
    # 参数说明：
    #   lo: low，ele_list 的子数组起始下标
    #   hi: high，ele_list 的子数组终止下标
    #   ele: element，目标插入的元素，需是 Element 对象
    # 返回值：
    #   应插入的下标 i（新元素插入到 i 位置，原本 >=i 位置的元素均右挪）
    def binary_search(self, lo, hi, ele):
        assert isinstance(ele, Element)

        if lo > hi:
            return lo
        elif lo == hi:
            if getattr(ele, self.key_name) < \
                    getattr(self.ele_list[lo], self.key_name):
                return lo
            else:
                return lo + 1
        else:
            mid = int((lo + hi) >> 1)
            if getattr(ele, self.key_name) < \
                    getattr(self.ele_list[lo], self.key_name):
                return self.binary_search(mid + 1, hi, ele)
            elif getattr(ele, self.key_name) > \
                    getattr(self.ele_list[lo], self.key_name):
                return self.binary_search(lo, mid - 1, ele)
            else:
                return mid

    # 插入排序。key 升序排序
    # 输入待排序的 Element 结构体列表
    # 返回排序结果列表
    def insertion_sort(self, ele_list):
        for j in range(1, len(ele_list)):
            cur_ele = ele_list[j]  # 当前循环的处理元素
            # 记录 cur_ele 的 key 和 val 值，因为之后可能会被其它元素覆盖掉
            cur_key = getattr(cur_ele, self.key_name)
            cur_val = getattr(cur_ele, self.val_name)
            # 将 ele_list[j] 插入到已排好序的列表 ele_list[0..j-1] 中
            i = j - 1
            # key 升序排序
            while i >= 0 and getattr(ele_list[i], self.key_name) > cur_key:
                # 右移 i 号元素：把 i 号元素的 key 和 val 都赋值给 i+1 号元素
                setattr(ele_list[i + 1], self.key_name, getattr(ele_list[i], self.key_name))
                setattr(ele_list[i + 1], self.val_name, getattr(ele_list[i], self.val_name))
                i -= 1  # 继续往左寻找插入位置
            # 此时 i 号元素不满足 while 循环条件，即表示 i+1 号即为该插入的位置
            # 于是将之前记录好的 cur_key 和 cur_val 赋值给 i+1 号元素，完成插入
            setattr(ele_list[i + 1], self.key_name, cur_key)
            setattr(ele_list[i + 1], self.val_name, cur_val)
        return ele_list

    def merge_runs(self, lo, hi):
        # 当待排序数组的左下标等于右下标时为基本情况：
        # 只有一个 run，是已排好序的，无需处理
        assert lo <= hi
        if lo == hi:
            return self.runs[lo]
        elif lo < hi:
            mid = int((lo + hi) >> 1)  # 二路归并
            left_list = self.merge_runs(lo, mid)
            right_list = self.merge_runs(mid + 1, hi)
            return self.merge(left_list, right_list)

    # 归并排序中的 merge 过程
    # 将两个有序的 Element list 归并成一个 list
    def merge(self, left_list, right_list):
        # 边界情况：某个 list 为空
        if not isinstance(left_list, list) or len(left_list) <= 0:
            return right_list
        if not isinstance(right_list, list) or len(right_list) <= 0:
            return left_list

        left_len = len(left_list)
        right_len = len(right_list)

        # 原数组末尾放置哨兵
        # 如果是求 key 升序排序(默认)，则放置正无穷 inf
        inf = 0x3f3f3f3f  # 哨兵数字 inf，用于升序排序。需要比 ele_list 中的所有 key 都大
        left_list.append(Element(inf))
        right_list.append(Element(inf))

        # 两个有序数组的合并
        i = 0
        j = 0
        res_list = []  # 结果数组
        for k in range(left_len + right_len):
            # 注意：为了算法的稳定性，这里当键 key 相等时，要选用左辅助数组的值，因此条件为 <= 而非 <
            if getattr(left_list[i], self.key_name) <= getattr(right_list[j], self.key_name):
                # 如果 left_list[i] 的 key 更小，则加入 left_list[i] 到结果数组
                res_list.append(left_list[i])
                i += 1
            else:
                # 否则加入 right_list[j] 到结果数组
                res_list.append(right_list[j])
                j += 1
        return res_list


def main():
    # 键值对列表
    kv_list = [
        [3, 300], [1, 100], [2, 200], [8, 800],
        [7, 700], [9, 900], [3, 301]
    ]

    # kv_list = [[x, 100 * x] for x in range(1000)]  # 排序耗时 0.60500 ms
    # kv_list = [[x, 100 * x] for x in reversed(range(1000))]  # 排序耗时 0.79400 ms
    # random.seed(7)
    # kv_list = []
    # for i in range(1000):
    #     cur_key = random.randint(0, 1000)
    #     kv_list.append([cur_key, cur_key * 100])  # 排序耗时 6.14000 ms

    # Element 元素列表(待排序)
    node_list = []
    if isinstance(kv_list, list) and len(kv_list) > 0:
        for kv in kv_list:
            if isinstance(kv, list) and len(kv) == 2:
                node_list.append(Element(kv[0], kv[1]))

    # _sort = Sort(node_list)
    _sort = TimSort(node_list)
    print(_sort.get_key_list())  # [3, 1, 2, 8, 7, 9, 3]

    start = time.process_time()
    sorted_ele_list = _sort.do_sort(reverse=False)
    end = time.process_time()
    print('Running Time: %.5f ms' % ((end - start) * 1000))

    if isinstance(sorted_ele_list, list) and len(sorted_ele_list) > 0:
        for ele in sorted_ele_list:
            if isinstance(ele, Element):
                print('key:', ele.key, '\tval:', ele.val)


if __name__ == "__main__":
    sys.exit(main())

```

## 参考资料

- cpython - listsort
    - [listsort.txt](https://github.com/python/cpython/blob/master/Objects/listsort.txt)
    - [listobject.c](https://github.com/python/cpython/blob/master/Objects/listobject.c)
