# Algorithm - Sort - Insertion Sort

By [YuweiYin](https://yuweiyin.github.io/)

## 简介

(直接)插入排序算法 (Insertion Sort)

## 代码范例

### Python

Python 环境：Python 3.7

- **注**：
    - 排序算法的基类 Sort 和元素结构体类 Element 写法与 [此文章](./sort-base-class) 完全相同，故不在下方赘述。
    - 如果要运行此代码，则还需先将 Sort 类和 Element 类置于本代码中。
    - Element 类完全可以根据程序需求来自定义，但是需要给出该类中的 key 和 value 属性名。

[GitHub Code Link](https://github.com/YuweiYin/Code_Play/blob/master/Algorithm-Essence/sort/insertion-sort.py)

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================
@Project : algorithm/sort
@File    : insertion-sort.py
@Author  : YuweiYin
=================================================="""

import sys
import time

"""
(直接)插入排序 Insertion Sort
"""


# 插入排序 (继承自 Sort 类)
# 空间复杂度(辅助存储)：O(1)
# 时间复杂度-平均 O(n^2)：对杂乱的数组 进行排序
# 时间复杂度-最好 O(n)：对已经按目标顺序排好序的数组 进行排序
# 时间复杂度-最坏 O(n^2)：对按目标顺序的逆序排列的数组 进行排序
# 算法稳定性：稳定
# 插入排序在对基本有序的小数组排序时，是比较高效的。
# 因此可以与快速排序结合使用，作为其处理短数组时的子过程。
class InsertionSort(Sort):
    # 重载 do_sort 方法
    # 排序操作前需已确保每个元素都含指定的 key_name 和 val_name 属性
    def do_sort(self, reverse=False):
        self._insertion_sort(reverse=reverse)

    # 插入排序
    def _insertion_sort(self, reverse=False):
        for j in range(1, len(self.ele_list)):
            cur_ele = self.ele_list[j]  # 当前循环的处理元素
            # 记录 cur_ele 的 key 和 val 值，因为之后可能会被其它元素覆盖掉
            cur_key = getattr(cur_ele, self.key_name)
            cur_val = getattr(cur_ele, self.val_name)
            # 将 ele_list[j] 插入到已排好序的列表 ele_list[0..j-1] 中
            i = j - 1
            if not reverse:
                # key 升序排序(默认)
                while i >= 0 and getattr(self.ele_list[i], self.key_name) > cur_key:
                    # 右移 i 号元素：把 i 号元素的 key 和 val 都赋值给 i+1 号元素
                    setattr(self.ele_list[i + 1], self.key_name, getattr(self.ele_list[i], self.key_name))
                    setattr(self.ele_list[i + 1], self.val_name, getattr(self.ele_list[i], self.val_name))
                    i -= 1  # 继续往左寻找插入位置
            else:
                # key 降序排序
                while i >= 0 and getattr(self.ele_list[i], self.key_name) < cur_key:
                    # 右移 i 号元素：把 i 号元素的 key 和 val 都赋值给 i+1 号元素
                    setattr(self.ele_list[i + 1], self.key_name, getattr(self.ele_list[i], self.key_name))
                    setattr(self.ele_list[i + 1], self.val_name, getattr(self.ele_list[i], self.val_name))
                    i -= 1  # 继续往左寻找插入位置
            # 此时 i 号元素不满足 while 循环条件，即表示 i+1 号即为该插入的位置
            # 于是将之前记录好的 cur_key 和 cur_val 赋值给 i+1 号元素，完成插入
            setattr(self.ele_list[i + 1], self.key_name, cur_key)
            setattr(self.ele_list[i + 1], self.val_name, cur_val)


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
    _sort = InsertionSort(node_list)
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
