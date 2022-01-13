# Algorithm - Sort - Merge Sort

By [YuweiYin](https://yuweiyin.github.io/)

## 简介

(二路)归并排序算法 (Merge Sort)

## 代码范例

### Python

Python 环境：Python 3.7

- **注**：
    - 排序算法的基类 Sort 和元素结构体类 Element 写法与 [此文章](./sort-base-class) 完全相同，故不在下方赘述。
    - 如果要运行此代码，则还需先将 Sort 类和 Element 类置于本代码中。
    - Element 类完全可以根据程序需求来自定义，但是需要给出该类中的 key 和 value 属性名。

[GitHub Code Link](https://github.com/YuweiYin/Code_Play/blob/master/Algorithm-Essence/sort/merge-sort.py)

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================
@Project : algorithm/sort
@File    : merge-sort.py
@Author  : YuweiYin
@Date    : 2020-05-07
=================================================="""

import sys
import time
# import random

"""
(二路)归并排序 Merge Sort

参考资料：
Introduction to Algorithm (aka CLRS) Third Edition - Chapter 2
"""


# (二路)归并排序 (继承自 Sort 类)
# 空间复杂度(辅助存储)：O(n)
# 时间复杂度-平均/最好/最坏 O(n log n)
# 算法稳定性：稳定
# 归并排序是十分经典和常用的排序算法，利用了分治法 Divide and Conquer 思想。
class MergeSort(Sort):
    # 重载 do_sort 方法
    # 排序操作前需已确保每个元素都含指定的 key_name 和 val_name 属性
    def do_sort(self, reverse=False):
        self._merge_sort(0, len(self.ele_list) - 1, reverse=reverse)

    # 归并排序
    def _merge_sort(self, l, r, reverse=False):
        # 当待排序数组的左下标等于右下标时为基本情况：
        # 该数组只有一个元素。这自然是已排好序的，无需处理
        if l < r:
            m = int((l + r) >> 1)  # 二路归并
            self._merge_sort(l, m, reverse=reverse)
            self._merge_sort(m + 1, r, reverse=reverse)
            self._merge(l, m, r, reverse=reverse)

    # 合并
    # 该过程假设子数组 ele_list[l..m] 和 ele_list[m+1..r] 都已排好序
    # 合并上述两个子数组为一个排好序的较大数组 ele_list[l..r]
    # 参数范围 l <= m < r
    def _merge(self, l, m, r, reverse=False):
        len_sub1 = m - l + 1   # 左子数组的长度
        len_sub2 = r - m       # 右子数组的长度
        inf = 0x3f3f3f3f       # 哨兵数字 inf，用于升序排序。需要比 ele_list 中的所有 key 都大
        neg_inf = -0x3f3f3f3f  # 哨兵数字 -inf，用于降序排序。需要比 ele_list 中的所有 key 都小

        # 设置左辅助数组的前 len_sub1 项值为左子数组的值
        aux_left = []
        for i in range(len_sub1):
            new_ele = Element(getattr(self.ele_list[l + i], self.key_name),
                              getattr(self.ele_list[l + i], self.val_name))
            aux_left.append(new_ele)

        # 设置右辅助数组的前 len_sub2 项值为右子数组的值
        aux_right = []
        for i in range(len_sub2):
            new_ele = Element(getattr(self.ele_list[m + 1 + i], self.key_name),
                              getattr(self.ele_list[m + 1 + i], self.val_name))
            aux_right.append(new_ele)

        # 辅助数组末尾放置哨兵
        if not reverse:
            # 如果是求 key 升序排序(默认)，则放置正无穷 inf
            aux_left.append(Element(inf))
            aux_right.append(Element(inf))
        else:
            # 如果是求 key 降序排序，则放置负无穷 neg_inf
            aux_left.append(Element(neg_inf))
            aux_right.append(Element(neg_inf))

        # 两个有序数组的合并
        i = 0
        j = 0
        for k in range(l, r + 1):
            if not reverse:
                #
                # 注意：为了算法的稳定性，这里当键 key 相等时，要选用左辅助数组的值，因此条件为 <= 而非 <
                if getattr(aux_left[i], self.key_name) <= getattr(aux_right[j], self.key_name):
                    # 如果 aux_left[i] 的 key 更小，则按 aux_left[i] 的 key 和 val 修改 ele_list[k]
                    setattr(self.ele_list[k], self.key_name, getattr(aux_left[i], self.key_name))
                    setattr(self.ele_list[k], self.val_name, getattr(aux_left[i], self.val_name))
                    i += 1
                else:
                    # 否则按 aux_right[j] 的 key 和 val 修改 ele_list[k]
                    setattr(self.ele_list[k], self.key_name, getattr(aux_right[j], self.key_name))
                    setattr(self.ele_list[k], self.val_name, getattr(aux_right[j], self.val_name))
                    j += 1
            else:
                # key 降序排序
                # 注意：为了算法的稳定性，这里当键 key 相等时，要选用左辅助数组的值，因此条件为 >= 而非 >
                if getattr(aux_left[i], self.key_name) >= getattr(aux_right[j], self.key_name):
                    # 如果 aux_left[i] 的 key 更大，则按 aux_left[i] 的 key 和 val 修改 ele_list[k]
                    setattr(self.ele_list[k], self.key_name, getattr(aux_left[i], self.key_name))
                    setattr(self.ele_list[k], self.val_name, getattr(aux_left[i], self.val_name))
                    i += 1
                else:
                    # 否则按 aux_right[j] 的 key 和 val 修改 ele_list[k]
                    setattr(self.ele_list[k], self.key_name, getattr(aux_right[j], self.key_name))
                    setattr(self.ele_list[k], self.val_name, getattr(aux_right[j], self.val_name))
                    j += 1


def main():
    # 键值对列表
    kv_list = [
        [3, 300], [1, 100], [2, 200], [8, 800],
        [7, 700], [9, 900], [3, 301]
    ]

    # kv_list = [[x, 100 * x] for x in range(1000)]  # 排序耗时 21.79500 ms
    # kv_list = [[x, 100 * x] for x in reversed(range(1000))]  # 排序耗时 23.49500 ms
    # random.seed(7)
    # kv_list = []
    # for i in range(1000):
    #     cur_key = random.randint(0, 1000)
    #     kv_list.append([cur_key, cur_key * 100])  # 排序耗时 22.46900 ms

    # Element 元素列表(待排序)
    node_list = []
    if isinstance(kv_list, list) and len(kv_list) > 0:
        for kv in kv_list:
            if isinstance(kv, list) and len(kv) == 2:
                node_list.append(Element(kv[0], kv[1]))

    # _sort = Sort(node_list)
    _sort = MergeSort(node_list)
    print(_sort.get_key_list())  # [3, 1, 2, 8, 7, 9, 3]

    start = time.process_time()
    _sort.do_sort(reverse=False)
    end = time.process_time()

    print(_sort.get_key_list())  # [1, 2, 3, 3, 7, 8, 9]
    print('Running Time: %.5f ms' % ((end - start) * 1000))

    sorted_ele_list = _sort.get_ele_list()
    if isinstance(sorted_ele_list, list) and len(sorted_ele_list) > 0:
        for ele in sorted_ele_list:
            if isinstance(ele, Element):
                print('key:', ele.key, '\tval:', ele.val)


if __name__ == "__main__":
    sys.exit(main())

```

## 参考资料

- Introduction to Algorithm (aka CLRS) Third Edition - Chapter 2
