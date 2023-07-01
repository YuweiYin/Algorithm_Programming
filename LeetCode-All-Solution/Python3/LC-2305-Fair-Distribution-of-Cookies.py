#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2305-Fair-Distribution-of-Cookies.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-07-01
=================================================================="""

import sys
import time
from typing import List
# import functools
# import itertools

"""
LeetCode - 2305 - (Medium) - Fair Distribution of Cookies
https://leetcode.com/problems/fair-distribution-of-cookies/

Description & Requirement:
    You are given an integer array cookies, where cookies[i] denotes the number of cookies in the ith bag. 
    You are also given an integer k that denotes the number of children to distribute all the bags of cookies to. 
    All the cookies in the same bag must go to the same child and cannot be split up.

    The unfairness of a distribution is defined as the maximum total cookies 
    obtained by a single child in the distribution.

    Return the minimum unfairness of all distributions.

Example 1:
    Input: cookies = [8,15,10,20,8], k = 2
    Output: 31
    Explanation: One optimal distribution is [8,15,8] and [10,20]
        - The 1st child receives [8,15,8] which has a total of 8 + 15 + 8 = 31 cookies.
        - The 2nd child receives [10,20] which has a total of 10 + 20 = 30 cookies.
        The unfairness of the distribution is max(31,30) = 31.
        It can be shown that there is no distribution with an unfairness less than 31.
Example 2:
    Input: cookies = [6,1,3,2,2,4,1,2], k = 3
    Output: 7
    Explanation: One optimal distribution is [6,1], [3,2,2], and [4,1,2]
        - The 1st child receives [6,1] which has a total of 6 + 1 = 7 cookies.
        - The 2nd child receives [3,2,2] which has a total of 3 + 2 + 2 = 7 cookies.
        - The 3rd child receives [4,1,2] which has a total of 4 + 1 + 2 = 7 cookies.
        The unfairness of the distribution is max(7,7,7) = 7.
        It can be shown that there is no distribution with an unfairness less than 7.

Constraints:
    2 <= cookies.length <= 8
    1 <= cookies[i] <= 10^5
    2 <= k <= cookies.length
"""


class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        # exception case
        assert isinstance(cookies, list) and len(cookies) >= 2
        assert isinstance(k, int) and 2 <= k <= len(cookies)
        # main method: (dynamic programming)
        return self._distributeCookies(cookies, k)

    def _distributeCookies(self, cookies: List[int], k: int) -> int:
        assert isinstance(cookies, list) and len(cookies) >= 2
        assert isinstance(k, int) and 2 <= k <= len(cookies)

        m = 1 << len(cookies)
        cur_sum = [0] * m
        for i, v in enumerate(cookies):
            bit = 1 << i
            for j in range(bit):
                cur_sum[bit | j] = cur_sum[j] + v

        dp = cur_sum[:]
        for _ in range(1, k):
            for j in range(m - 1, 0, -1):
                s = j
                while s:
                    v = dp[j ^ s]
                    if cur_sum[s] > v:
                        v = cur_sum[s]
                    if v < dp[j]:
                        dp[j] = v
                    s = (s - 1) & j

        return dp[-1]


def main():
    # Example 1: Output: 31
    # cookies = [8, 15, 10, 20, 8]
    # k = 2

    # Example 2: Output: 7
    cookies = [6, 1, 3, 2, 2, 4, 1, 2]
    k = 3

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.distributeCookies(cookies, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
