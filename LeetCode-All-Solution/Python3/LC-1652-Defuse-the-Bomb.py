#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1652-Defuse-the-Bomb.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-09-24
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1652 - (Medium) - Defuse the Bomb
https://leetcode.com/problems/defuse-the-bomb/

Description & Requirement:
    You have a bomb to defuse, and your time is running out! 
    Your informer will provide you with a circular array code of length of n and a key k.

    To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.
        If k > 0, replace the ith number with the sum of the next k numbers.
        If k < 0, replace the ith number with the sum of the previous k numbers.
        If k == 0, replace the ith number with 0.

    As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].

    Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!

Example 1:
    Input: code = [5,7,1,4], k = 3
    Output: [12,10,16,13]
    Explanation: Each number is replaced by the sum of the next 3 numbers. 
        The decrypted code is [7+1+4, 1+4+5, 4+5+7, 5+7+1]. Notice that the numbers wrap around.
Example 2:
    Input: code = [1,2,3,4], k = 0
    Output: [0,0,0,0]
    Explanation: When k is zero, the numbers are replaced by 0. 
Example 3:
    Input: code = [2,4,9,3], k = -2
    Output: [12,5,6,13]
    Explanation: The decrypted code is [3+9, 2+3, 4+2, 9+4]. 
        Notice that the numbers wrap around again. If k is negative, the sum is of the previous numbers.

Constraints:
    n == code.length
    1 <= n <= 100
    1 <= code[i] <= 100
    -(n - 1) <= k <= n - 1
"""


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        # exception case
        assert isinstance(code, list) and len(code) >= 1
        for c in code:
            assert isinstance(c, int) and c >= 1
        n = len(code)
        assert isinstance(k, int) and -(n - 1) <= k <= n - 1
        # main method: (sliding window)
        return self._decrypt(code, k)

    def _decrypt(self, code: List[int], k: int) -> List[int]:
        assert isinstance(code, list) and len(code) >= 1
        n = len(code)
        assert isinstance(k, int) and -(n - 1) <= k <= n - 1

        if k == 0:
            return [0 for _ in range(n)]

        if k > 0:
            left, right = 1, k
        else:
            left, right = n + k, n - 1
        code += code
        res = []

        cur_sum = sum(code[left: right + 1])
        for idx in range(n):
            res.append(cur_sum)
            cur_sum -= code[left]
            cur_sum += code[right + 1]
            left += 1
            right += 1

        return res


def main():
    # Example 1: Output: [12,10,16,13]
    # code = [5, 7, 1, 4]
    # k = 3

    # Example 2: Output: [0,0,0,0]
    # code = [1, 2, 3, 4]
    # k = 0

    # Example 3: Output: [12,5,6,13]
    code = [2, 4, 9, 3]
    k = -2

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.decrypt(code, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
