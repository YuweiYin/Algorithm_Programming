#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0793-Preimage-Size-of-Factorial-Zeroes-Function.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-08-28
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 0793 - (Hard) - Preimage Size of Factorial Zeroes Function
https://leetcode.com/problems/preimage-size-of-factorial-zeroes-function/

Description & Requirement:
    Let f(x) be the number of zeroes at the end of x!. 
    Recall that x! = 1 * 2 * 3 * ... * x and by convention, 0! = 1.

    For example, f(3) = 0 because 3! = 6 has no zeroes at the end, 
        while f(11) = 2 because 11! = 39916800 has two zeroes at the end.

    Given an integer k, return the number of non-negative integers x have the property that f(x) = k.

Example 1:
    Input: k = 0
    Output: 5
    Explanation: 0!, 1!, 2!, 3!, and 4! end with k = 0 zeroes.
Example 2:
    Input: k = 5
    Output: 0
    Explanation: There is no x such that x! ends in k = 5 zeroes.
Example 3:
    Input: k = 3
    Output: 5

Constraints:
    0 <= k <= 10^9
"""


class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        # exception case
        assert isinstance(k, int) and k >= 0
        # main method: (Zeta function)
        return self._preimageSizeFZF(k)

    def _preimageSizeFZF(self, k: int) -> int:
        """
        Runtime: 29 ms, faster than 97.37% of Python3 submissions for Preimage Size of Factorial Zeroes Function.
        Memory Usage: 13.9 MB, less than 14.47% of Python3 submissions for Preimage Size of Factorial Zeroes Function.
        """
        assert isinstance(k, int) and k >= 0

        def __zeta(n: int) -> int:
            # return the number of zeros in the end of n!
            ans = 0
            while n:
                n //= 5
                ans += n
            return ans

        res = 0
        k_origin = k
        k = k_origin * 5
        cur_k = __zeta(k)
        gap = cur_k - k_origin

        k -= gap << 2
        cur_k = __zeta(k)
        gap = cur_k - k_origin

        if gap > 0:
            while cur_k >= k_origin:
                if cur_k > k_origin:
                    k -= 5
                else:
                    res = 5
                    break
                cur_k = __zeta(k)
        elif gap < 0:
            while cur_k <= k_origin:
                if cur_k < k_origin:
                    k += 5
                else:
                    res = 5
                    break
                cur_k = __zeta(k)
        else:
            res = 5

        return res


def main():
    # Example 1: Output: 5
    k = 0

    # Example 2: Output: 0
    # k = 5

    # Example 3: Output: 5
    # k = 3

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.preimageSizeFZF(k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
