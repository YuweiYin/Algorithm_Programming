#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2569-Handling-Sum-Queries-After-Update.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-07-26
=================================================================="""

import sys
import time
from typing import List
# import functools
# import itertools

"""
LeetCode - 2569 - (Hard) - Handling Sum Queries After Update
https://leetcode.com/problems/handling-sum-queries-after-update/

Description & Requirement:
    You are given two 0-indexed arrays nums1 and nums2 and a 2D array queries of queries. 
    There are three types of queries:
        1. For a query of type 1, queries[i] = [1, l, r]. Flip the values from 0 to 1 and 
            from 1 to 0 in nums1 from index l to index r. Both l and r are 0-indexed.
        2. For a query of type 2, queries[i] = [2, p, 0]. For every index 0 <= i < n, 
            set nums2[i] = nums2[i] + nums1[i] * p.
        3. For a query of type 3, queries[i] = [3, 0, 0]. Find the sum of the elements in nums2.

    Return an array containing all the answers to the third type queries.

Example 1:
    Input: nums1 = [1,0,1], nums2 = [0,0,0], queries = [[1,1,1],[2,1,0],[3,0,0]]
    Output: [3]
    Explanation: After the first query nums1 becomes [1,1,1]. After the second query, 
        nums2 becomes [1,1,1], so the answer to the third query is 3. Thus, [3] is returned.
Example 2:
    Input: nums1 = [1], nums2 = [5], queries = [[2,0,0],[3,0,0]]
    Output: [5]
    Explanation: After the first query, nums2 remains [5], 
        so the answer to the second query is 5. Thus, [5] is returned.

Constraints:
    1 <= nums1.length,nums2.length <= 10^5
    nums1.length = nums2.length
    1 <= queries.length <= 10^5
    queries[i].length = 3
    0 <= l <= r <= nums1.length - 1
    0 <= p <= 10^6
    0 <= nums1[i] <= 1
    0 <= nums2[i] <= 10^9
"""


class SegNode:
    def __init__(self):
        self.left = 0
        self.right = 0
        self.sum = 0
        self.lazy_tag = False


class SegTree:
    def __init__(self, nums):
        n = len(nums)
        self.arr = [SegNode() for _ in range(n * 4 + 1)]
        self.build(1, 0, n - 1, nums)

    def sum_range(self, left, right):
        return self.query(1, left, right)

    def reverse_range(self, left, right):
        self.modify(1, left, right)

    def build(self, tree_id, left, right, nums):
        arr = self.arr
        arr[tree_id] = SegNode()
        arr[tree_id].left = left
        arr[tree_id].right = right
        arr[tree_id].lazy_tag = False
        if left == right:
            arr[tree_id].sum = nums[left]
            return
        mid = (left + right) >> 1
        self.build(2 * tree_id, left, mid, nums)
        self.build(2 * tree_id + 1, mid + 1, right, nums)
        arr[tree_id].sum = arr[2 * tree_id].sum + arr[2 * tree_id + 1].sum

    def pushdown(self, x):
        arr = self.arr
        if arr[x].lazy_tag:
            arr[2 * x].lazy_tag = not arr[2 * x].lazy_tag
            arr[2 * x].sum = arr[2 * x].right - arr[2 * x].left + 1 - arr[2 * x].sum
            arr[2 * x + 1].lazy_tag = not arr[2 * x + 1].lazy_tag
            arr[2 * x + 1].sum = arr[2 * x + 1].right - arr[2 * x + 1].left + 1 - arr[2 * x + 1].sum
            arr[x].lazy_tag = False

    def modify(self, tree_id, left, right):
        arr = self.arr
        if arr[tree_id].left >= left and arr[tree_id].right <= right:
            arr[tree_id].sum = (arr[tree_id].right - arr[tree_id].left + 1) - arr[tree_id].sum
            arr[tree_id].lazy_tag = not arr[tree_id].lazy_tag
            return
        self.pushdown(tree_id)
        mid = (arr[tree_id].left + arr[tree_id].right) >> 1
        if arr[2 * tree_id].right >= left:
            self.modify(2 * tree_id, left, right)
        if arr[2 * tree_id + 1].left <= right:
            self.modify(2 * tree_id + 1, left, right)
        arr[tree_id].sum = arr[2 * tree_id].sum + arr[2 * tree_id + 1].sum

    def query(self, tree_id, left, right):
        arr = self.arr
        if arr[tree_id].left >= left and arr[tree_id].right <= right:
            return arr[tree_id].sum
        if arr[tree_id].right < left or arr[tree_id].left > right:
            return 0
        self.pushdown(tree_id)
        mid = (arr[tree_id].left + arr[tree_id].right) >> 1
        res = 0
        if arr[2 * tree_id].right >= left:
            res += self.query(2 * tree_id, left, right)
        if arr[2 * tree_id + 1].left <= right:
            res += self.query(2 * tree_id + 1, left, right)
        return res


class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        # exception case
        assert isinstance(nums1, list) and len(nums1) >= 1
        assert isinstance(nums2, list) and len(nums1) == len(nums2)
        assert isinstance(queries, list) and len(queries) >= 1
        # main method: (Segment Tree)
        return self._handleQuery(nums1, nums2, queries)

    def _handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        assert isinstance(nums1, list) and len(nums1) >= 1
        assert isinstance(nums2, list) and len(nums1) == len(nums2)
        assert isinstance(queries, list) and len(queries) >= 1

        n = len(nums1)
        m = len(queries)
        seg_tree = SegTree(nums1)

        total = sum(nums2)
        res = []
        for i in range(m):
            if queries[i][0] == 1:
                left = queries[i][1]
                right = queries[i][2]
                seg_tree.reverse_range(left, right)
            elif queries[i][0] == 2:
                total += seg_tree.sum_range(0, n - 1) * queries[i][1]
            elif queries[i][0] == 3:
                res.append(total)

        return res


def main():
    # Example 1: Output: [3]
    nums1 = [1, 0, 1]
    nums2 = [0, 0, 0]
    queries = [[1, 1, 1], [2, 1, 0], [3, 0, 0]]

    # Example 2: Output: [5]
    # nums1 = [1]
    # nums2 = [5]
    # queries = [[2, 0, 0], [3, 0, 0]]

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.handleQuery(nums1, nums2, queries)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
