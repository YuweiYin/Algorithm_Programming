# Algorithm - Sort - Shell Sort

By [YuweiYin](https://yuweiyin.github.io/)

## 简介

希尔排序算法 (Shell Sort) 是 Insertion Sort [直接插入排序](./insertion-sort)的改进方法，并将直接插入排序作为其子过程
在处理中等规模数据时比直接插入排序好，但不如快速排序。

## 场景描述及分析

希尔排序的算法实现很简单，效率也较好，不过此排序算法是不稳定的，可能打乱相同 key 元素的原始相对位置。

- 时间复杂度：
    - 平均：O(n^1.3)
    - 最好：O(n)
    - 最坏：O(n^2)
- (辅助)空间复杂度：
    - O(1)
- 稳定性：
    - 不稳定

### 示例

## 设计 & 细节

### 算法流程

希尔排序同时利用了归并排序和插入排序的思想，先对待排记录进行细粒度的分组，每个小组内调用插入排序。然后通过不断地成倍扩大分组大小，每次组内排序都采用直接插入排序（利用了直接插入排序的特性：对几乎有序的数组排序效率很高）。

希尔排序对数组的划分不像二路归并排序那样是从数组中间一分为二，而是设置一个下标增量/间隔 gap，使得下标相距 gap 的元素们被分为同一个小组。

一开始 `gap = len(ele_list) // 2`，每次组内排序完 缩小间隔 `gap //= 2` 从而增大分组内元素的数目。最终循环的 gap 为 1，表示对整个待排数组进行排序。

## 代码范例

### Python

Python 环境：Python 3.7

- **注**：
    - 排序算法的基类 Sort 和元素结构体类 Element 写法与 [此文章](./sort-base-class) 完全相同，故不在下方赘述。
    - 如果要运行此代码，则还需先将 Sort 类和 Element 类置于本代码中。
    - Element 类完全可以根据程序需求来自定义，但是需要给出该类中的 key 和 value 属性名。

[GitHub Code Link](https://github.com/YuweiYin/Code_Play/blob/master/Algorithm-Essence/sort/shell-sort.py)

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================
@Project : algorithm/sort
@File    : shell-sort.py
@Author  : YuweiYin
@Date    : 2020-05-16
=================================================="""

import sys
import time

"""
希尔排序 Shell Sort
"""


# 希尔排序 (继承自 Sort 类)
# 空间复杂度(辅助存储)：O(1)
# 时间复杂度-平均 O(n^1.3)：对杂乱的数组 进行排序
# 时间复杂度-最好 O(n)：对已经按目标顺序排好序的数组 进行排序
# 时间复杂度-最坏 O(n^2)：对按目标顺序的逆序排列的数组 进行排序
# 算法稳定性：不稳定
# 希尔排序是 Insertion Sort 直接插入排序的改进方法，并将直接插入排序作为其子过程
# 在处理中等规模数据时比直接插入排序好，但不如快速排序。
class ShellSort(Sort):
    # 重载 do_sort 方法
    # 排序操作前需已确保每个元素都含指定的 key_name 和 val_name 属性
    def do_sort(self, reverse=False):
        self._shell_sort(reverse=reverse)

    # 希尔排序
    # 增量 gap 从 n // 2 开始降到 1，依增量分组，组内进行直接插入排序
    def _shell_sort(self, reverse=False):
        ele_len = len(self.ele_list)
        gap = ele_len // 2  # 初始增量
        while gap > 0:
            for i in range(gap, ele_len):
                # 分组内进行直接插入排序
                if not reverse:
                    # 升序排序(默认)
                    while i >= gap and getattr(self.ele_list[i], self.key_name) < \
                            getattr(self.ele_list[i - gap], self.key_name):
                        temp = self.ele_list[i]
                        self.ele_list[i] = self.ele_list[i - gap]
                        self.ele_list[i - gap] = temp
                        i -= gap
                else:
                    # 降序排序
                    while i >= gap and getattr(self.ele_list[i], self.key_name) > \
                            getattr(self.ele_list[i - gap], self.key_name):
                        temp = self.ele_list[i]
                        self.ele_list[i] = self.ele_list[i - gap]
                        self.ele_list[i - gap] = temp
                        i -= gap
            gap //= 2  # 缩小增量


def main():
    # 键值对列表
    kv_list = [
        [3, 300], [1, 100], [2, 200], [8, 800],
        [7, 700], [9, 900], [3, 301]
    ]

    # Element 元素列表(待排序)
    node_list = []
    if isinstance(kv_list, list) and len(kv_list) > 0:
        for kv in kv_list:
            if isinstance(kv, list) and len(kv) == 2:
                node_list.append(Element(kv[0], kv[1]))

    # _sort = Sort(node_list)
    _sort = ShellSort(node_list)
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
