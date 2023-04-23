#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1105-Filling-Bookcase-Shelves.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-04-23
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1105 - (Medium) - Filling Bookcase Shelves
https://leetcode.com/problems/filling-bookcase-shelves/

Description & Requirement:
    You are given an array books where books[i] = [thickness_i, height_i] indicates 
    the thickness and height of the i-th book. You are also given an integer shelfWidth.

    We want to place these books in order onto bookcase shelves that have a total width shelfWidth.

    We choose some of the books to place on this shelf such that the sum of their thickness is 
    less than or equal to shelfWidth, then build another level of the shelf of the bookcase so that 
    the total height of the bookcase has increased by the maximum height of the books we just put down. 
    We repeat this process until there are no more books to place.

    Note that at each step of the above process, the order of the books we place is 
    the same order as the given sequence of books.

    For example, if we have an ordered list of 5 books, we might place the first and second book 
        onto the first shelf, the third book on the second shelf, and the fourth and fifth book on the last shelf.

    Return the minimum possible height that the total bookshelf can be after placing shelves in this manner.

Example 1:
    Input: books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelfWidth = 4
    Output: 6
    Explanation:
        The sum of the heights of the 3 shelves is 1 + 3 + 2 = 6.
        Notice that book number 2 does not have to be on the first shelf.
Example 2:
    Input: books = [[1,3],[2,4],[3,2]], shelfWidth = 6
    Output: 4

Constraints:
    1 <= books.length <= 1000
    1 <= thickness_i <= shelfWidth <= 1000
    1 <= height_i <= 1000
"""


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        # exception case
        assert isinstance(books, list) and len(books) >= 1
        assert isinstance(shelfWidth, int) and shelfWidth >= 1
        # main method: (dynamic programming)
        return self._minHeightShelves(books, shelfWidth)

    def _minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        assert isinstance(books, list) and len(books) >= 1
        assert isinstance(shelfWidth, int) and shelfWidth >= 1

        n = len(books)
        dp = [int(1e9+7)] * (n + 1)
        dp[0] = 0

        for i, b in enumerate(books):
            curWidth = 0
            maxHeight = 0
            j = i
            while j >= 0:
                curWidth += books[j][0]
                if curWidth > shelfWidth:
                    break
                maxHeight = max(maxHeight, books[j][1])
                dp[i + 1] = min(dp[i + 1], dp[j] + maxHeight)
                j -= 1

        return dp[-1]


def main():
    # Example 1: Output: 6
    books = [[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]]
    shelfWidth = 4

    # Example 2: Output: 4
    # books = [[1, 3], [2, 4], [3, 2]]
    # shelfWidth = 6

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minHeightShelves(books, shelfWidth)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
