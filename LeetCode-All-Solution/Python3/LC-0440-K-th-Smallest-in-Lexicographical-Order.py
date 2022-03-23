#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0440-K-th-Smallest-in-Lexicographical-Order.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-23
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 0440 - (Hard) - K-th Smallest in Lexicographical Order
https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/

Description & Requirement:
    Given two integers n and k, 
    return the k-th lexicographically smallest integer in the range [1, n].

Example 1:
    Input: n = 13, k = 2
    Output: 10
    Explanation: The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], 
        so the second smallest number is 10.
Example 2:
    Input: n = 1, k = 1
    Output: 1

Constraints:
    1 <= k <= n <= 10^9
"""


class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        # exception case
        assert isinstance(n, int) and n > 0
        assert isinstance(k, int) and 0 < k <= n
        # main method: (simulate Trie searching process, O(log^2 n))
        return self._findKthNumber(n, k)

    def _findKthNumber(self, n: int, k: int) -> int:
        """
        Runtime: 31 ms, faster than 100.00% of Python3 online submissions for K-th Smallest in Lexicographical Order.
        Memory Usage: 13.9 MB, less than 35.94% of Python3 online submissions for K-th Smallest in Lexicographical Order
        """
        cur_num = 1  # the 1-th lexicographical smallest number is 1, (then 10, 100, ... if they are available)
        k -= 1  # used 1 lexicographical order
        BASE = 10
        while k:
            # lexi_orders is all NUM in the subtree of cur_num such that every NUM is lexicographically <= n
            lexi_orders, min_child, max_child = 0, cur_num, cur_num
            while min_child <= n:
                # the lexicographical orders from min_num to min(max_num, n)
                lexi_orders += min(max_child, n) - min_child + 1
                # search the child nodes (0, 1, 2, ..., 9) of the current Trie node (cur_num)
                min_child *= BASE  # min_num -> ...0 -> ...00
                max_child = max_child * BASE + BASE - 1  # max_num -> ...9 -> ...99
            # lexi_orders <= k means the target k-th number is larger than all NUM in the subtree of cur_num
            if lexi_orders <= k:
                k -= lexi_orders
                cur_num += 1  # consider the children of (cur_num + 1)
            else:  # the target k-th number is in the subtree of cur_num
                k -= 1
                cur_num *= BASE  # go to the "0" child of cur_num

        return cur_num


def main():
    # Example 1: Output: 10
    n = 13
    k = 2

    # Example 2: Output: 1
    # n = 1
    # k = 1

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.findKthNumber(n ,k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
