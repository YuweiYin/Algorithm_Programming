#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0944-Delete-Columns-to-Make-Sorted.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-05-12
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0944 - (Easy) - Delete Columns to Make Sorted
https://leetcode.com/problems/delete-columns-to-make-sorted/

Description & Requirement:
    You are given an array of n strings strs, all of the same length.

    The strings can be arranged such that there is one on each line, making a grid. 
    For example, strs = ["abc", "bce", "cae"] can be arranged as:
        abc
        bce
        cae

    You want to delete the columns that are not sorted lexicographically. 
    In the above example (0-indexed), columns 0 ('a', 'b', 'c') and 2 ('c', 'e', 'e') 
    are sorted while column 1 ('b', 'c', 'a') is not, so you would delete column 1.

    Return the number of columns that you will delete.

Example 1:
    Input: strs = ["cba","daf","ghi"]
    Output: 1
    Explanation: The grid looks as follows:
        cba
        daf
        ghi
        Columns 0 and 2 are sorted, but column 1 is not, so you only need to delete 1 column.
Example 2:
    Input: strs = ["a","b"]
    Output: 0
    Explanation: The grid looks as follows:
        a
        b
        Column 0 is the only column and is sorted, so you will not delete any columns.
Example 3:
    Input: strs = ["zyx","wvu","tsr"]
    Output: 3
    Explanation: The grid looks as follows:
        zyx
        wvu
        tsr
        All 3 columns are not sorted, so you will delete all 3.

Constraints:
    n == strs.length
    1 <= n <= 100
    1 <= strs[i].length <= 1000
    strs[i] consists of lowercase English letters.
"""


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # exception case
        assert isinstance(strs, list) and len(strs) >= 1 and isinstance(strs[0], str)
        len_s = len(strs[0])
        assert all([isinstance(string, str) and len(string) == len_s for string in strs])
        # main method: (check every column)
        return self._minDeletionSize(strs)

    def _minDeletionSize(self, strs: List[str]) -> int:
        assert isinstance(strs, list) and len(strs) >= 1 and isinstance(strs[0], str)
        len_strs = len(strs)
        len_s = len(strs[0])

        res = 0
        for idx in range(len_s):
            cur_col = [string[idx] for string in strs]
            is_sorted = True
            for k in range(len_strs - 1):
                if cur_col[k] > cur_col[k + 1]:
                    is_sorted = False
                    break
            if not is_sorted:
                res += 1

        return res


def main():
    # Example 1: Output: 1
    # strs = ["cba", "daf", "ghi"]

    # Example 2: Output: 0
    # strs = ["a", "b"]

    # Example 3: Output: 3
    strs = ["zyx", "wvu", "tsr"]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minDeletionSize(strs)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
