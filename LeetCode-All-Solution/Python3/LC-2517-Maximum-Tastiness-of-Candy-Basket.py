#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2517-Maximum-Tastiness-of-Candy-Basket.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-06-01
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 2517 - (Medium) - Maximum Tastiness of Candy Basket
https://leetcode.com/problems/maximum-tastiness-of-candy-basket/description/

Description & Requirement:
    You are given an array of positive integers price where price[i] denotes 
    the price of the i-th candy and a positive integer k.

    The store sells baskets of k distinct candies. 
    The tastiness of a candy basket is the smallest absolute difference 
    of the prices of any two candies in the basket.

    Return the maximum tastiness of a candy basket.

Example 1:
    Input: price = [13,5,1,8,21,2], k = 3
    Output: 8
    Explanation: Choose the candies with the prices [13,5,21].
        The tastiness of the candy basket is: min(|13 - 5|, |13 - 21|, |5 - 21|) = min(8, 8, 16) = 8.
        It can be proven that 8 is the maximum tastiness that can be achieved.
Example 2:
    Input: price = [1,3,1], k = 2
    Output: 2
    Explanation: Choose the candies with the prices [1,3].
        The tastiness of the candy basket is: min(|1 - 3|) = min(2) = 2.
        It can be proven that 2 is the maximum tastiness that can be achieved.
Example 3:
    Input: price = [7,7,7,7], k = 2
    Output: 0
    Explanation: Choosing any two distinct candies from the candies we have will result in a tastiness of 0.

Constraints:
    2 <= k <= price.length <= 10^5
    1 <= price[i] <= 10^9
"""


class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        # exception case
        assert isinstance(price, list) and isinstance(k, int) and len(price) >= k >= 2
        # main method: (binary search)
        return self._maximumTastiness(price, k)

    def _maximumTastiness(self, price: List[int], k: int) -> int:
        assert isinstance(price, list) and isinstance(k, int) and len(price) >= k >= 2

        def __check(tastiness: int) -> bool:
            prev = -int(1e9+7)
            cnt = 0
            for p in price:
                if p - prev >= tastiness:
                    cnt += 1
                    prev = p
            return cnt >= k

        price.sort()
        left, right = 0, price[-1] - price[0]
        while left < right:
            mid = (left + right + 1) >> 1
            if __check(mid):
                left = mid
            else:
                right = mid - 1

        return left


def main():
    # Example 1: Output: 8
    price = [13, 5, 1, 8, 21, 2]
    k = 3

    # Example 2: Output: 2
    # price = [1, 3, 1]
    # k = 2

    # Example 3: Output: 0
    # price = [7, 7, 7, 7]
    # k = 2

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maximumTastiness(price, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
