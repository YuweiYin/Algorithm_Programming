#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0402-Remove-K-Digits.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-18
=================================================================="""

import sys
import time
# from typing import List
# import collections

"""
LeetCode - 0402 - (Medium) - Remove K Digits
https://leetcode.com/problems/remove-k-digits/

Description & Requirement:
    Given string num representing a non-negative integer num, and an integer k, 
    return the smallest possible integer after removing k digits from num.

Example 1:
    Input: num = "1432219", k = 3
    Output: "1219"
    Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:
    Input: num = "10200", k = 1
    Output: "200"
    Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:
    Input: num = "10", k = 2
    Output: "0"
    Explanation: Remove all the digits from the number and it is left with nothing which is 0.

Constraints:
    1 <= k <= num.length <= 10^5
    num consists of only digits.
    num does not have any leading zeros except for the zero itself.
"""


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # exception case
        assert isinstance(num, str) and isinstance(k, int) and 1 <= k <= len(num)
        # main method: (greedy: keep the left digits as small as possible)
        return self._removeKdigits(num, k)

    def _removeKdigits(self, num: str, k: int) -> str:
        # check if k can delete all non-zero digits
        non_zero_counter = 0
        for digit in num:
            if digit != "0":
                non_zero_counter += 1
        if k >= non_zero_counter:
            return "0"

        # perform deletion k times
        for step in range(k):
            digit_idx = 1
            cur_len_num = len(num)
            done_deletion = False
            while digit_idx < cur_len_num:
                if num[digit_idx] < num[digit_idx - 1]:
                    # delete the last bigger digit: num[digit_idx - 1]
                    num = num[0: digit_idx - 1] + num[digit_idx:]
                    done_deletion = True
                    break
                digit_idx += 1
            # if didn't delete any digit in the former while loop, then digits in num must be non-descending order
            # now just delete the end (k - step) digits
            if not done_deletion:
                num = num[0: len(num) - k + step]
                break

        # delete leading zeros
        res_num = ""
        for idx, digit in enumerate(num):
            if digit != "0":
                res_num = num[idx:]
                break
        return res_num if len(res_num) > 0 else "0"


def main():
    # Example 1: Output: "1219"
    num = "1432219"
    k = 3

    # Example 2: Output: "200"
    # num = "10200"
    # k = 1

    # Example 3: Output: "0"
    # num = "10"
    # k = 2

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.removeKdigits(num, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
