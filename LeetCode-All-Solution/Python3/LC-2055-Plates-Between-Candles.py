#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2055-Plates-Between-Candles.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-08
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 2055 - (Medium) - Plates Between Candles
https://leetcode.com/problems/plates-between-candles/

Description & Requirement:
    There is a long table with a line of plates and candles arranged on top of it. 
    You are given a 0-indexed string s consisting of characters '*' and '|' only, 
    where a '*' represents a plate and a '|' represents a candle.

    You are also given a 0-indexed 2D integer array queries where 
    queries[i] = [left_i, right_i] denotes the substring s[left_i...right_i] (inclusive). 
    For each query, you need to find the number of plates between candles that are in the substring. 
    A plate is considered between candles if there is at least one candle to its left and 
    at least one candle to its right in the substring.

    For example, s = "||**||**|*", and a query [3, 8] denotes the substring "*||**|". 
    The number of plates between candles in this substring is 2, 
    as each of the two plates has at least one candle in the substring to its left and right.

    Return an integer array answer where answer[i] is the answer to the ith query.

Example 1:
    Input: s = "**|**|***|", queries = [[2,5],[5,9]]
    Output: [2,3]
    Explanation:
        - queries[0] has two plates between candles.
        - queries[1] has three plates between candles.
Example 2:
    Input: s = "***|**|*****|**||**|*", queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]
    Output: [9,0,0,0,0]
    Explanation:
        - queries[0] has nine plates between candles.
        - The other queries have zero plates between candles.

Constraints:
    3 <= s.length <= 10^5
    s consists of '*' and '|' characters.
    1 <= queries.length <= 10^5
    queries[i].length == 2
    0 <= left_i <= right_i < s.length
"""


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        # exception case
        assert isinstance(s, str) and len(s) >= 3
        assert isinstance(queries, list) and len(queries) > 0
        len_s = len(s)
        for query in queries:
            assert isinstance(query, list) and len(query) == 2 and 0 <= query[0] <= query[1] < len_s
        # main method: (preprocess: for each plate, record the indices of its nearest left and right candles)
        #     then for each query, use the result of preprocess to test if each plate is surrounded by candles
        # return self._platesBetweenCandles(s, queries)
        # other method: prefix sum
        return self._platesBetweenCandlesPrefixSum(s, queries)

    def _platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        """
        Time: O(len(s) * len(queries))
        if "|" is sparse, then Time nearly O(len(s) + len(queries))
        """
        len_s = len(s)
        assert len_s >= 3

        # preprocess: for each plate, record the indices of its nearest left and right candles
        nearest_candle_left = [-1 for _ in range(len_s)]  # -1 means no left candle
        nearest_candle_right = [len_s for _ in range(len_s)]  # len_s means no right candle

        left_candle_index = -1
        for idx, item in enumerate(s):
            if item == "|":
                nearest_candle_left[idx] = idx
                left_candle_index = idx  # update the nearest left candle index
            else:
                nearest_candle_left[idx] = left_candle_index

        right_candle_index = len_s
        idx = len_s - 1
        while idx >= 0:
            item = s[idx]
            if item == "|":
                nearest_candle_right[idx] = 0
                right_candle_index = idx  # update the nearest right candle index
            else:
                nearest_candle_right[idx] = right_candle_index
            idx -= 1

        # for each query, use the result of preprocessing to test if each plate is surrounded by candles
        res = []
        for query in queries:
            valid_plate_counter = 0
            # bound the index
            left_idx, right_idx = max(0, query[0]), min(query[1], len_s - 1)
            cur_idx = left_idx
            while cur_idx <= right_idx:
                if s[cur_idx] == "|":
                    cur_idx += 1
                    continue
                nearest_left_idx, nearest_right_idx = nearest_candle_left[cur_idx], nearest_candle_right[cur_idx]
                if nearest_left_idx < left_idx:  # the nearest left candle is not in the query boundary
                    next_candle = nearest_right_idx
                    cur_idx = next_candle + 1  # skip all the way to the right side of the next candle
                else:  # the nearest left candle is in the query boundary, check the right candle
                    if nearest_right_idx > right_idx:  # no right candles in the query boundary
                        break
                    else:  # now cur_idx is surrounded by left and right candles in the query boundary
                        valid_plate_counter += nearest_right_idx - nearest_left_idx - 1  # all plates
                        cur_idx = nearest_right_idx + 1
            res.append(valid_plate_counter)

        return res

    def _platesBetweenCandlesPrefixSum(self, s: str, queries: List[List[int]]) -> List[int]:
        """
        Time: O(len(s) + len(queries))
        """
        len_s = len(s)
        assert len_s >= 3

        # preprocess: record the prefix sum of the number of plates "*"
        prefix_sum = [0 for _ in range(len_s)]
        cur_sum = 0  # the number of plates "*" in the range s[0: cur_idx + 1]
        # for each plate, record the indices of its nearest left and right candles
        nearest_candle_left = [-1 for _ in range(len_s)]  # -1 means no candle
        nearest_candle_right = [-1 for _ in range(len_s)]  # -1 means no candle

        left_candle_index = -1
        for idx, item in enumerate(s):
            if item == "|":
                left_candle_index = idx
            else:
                cur_sum += 1  # the number of plates "*" in the range s[0: idx + 1]
            prefix_sum[idx] = cur_sum
            nearest_candle_left[idx] = left_candle_index

        right_candle_index = -1
        idx = len_s - 1
        while idx >= 0:
            item = s[idx]
            if item == "|":
                right_candle_index = idx
            nearest_candle_right[idx] = right_candle_index
            idx -= 1

        # for each query, use the result of preprocessing to directly get the aim plate sum
        res = []
        for query in queries:
            left_idx, right_idx = max(0, query[0]), min(query[1], len_s - 1)  # bound the index
            nearest_right_of_left = nearest_candle_right[left_idx]
            nearest_left_of_right = nearest_candle_left[right_idx]
            if 0 <= nearest_right_of_left < nearest_left_of_right:
                res.append(prefix_sum[nearest_left_of_right] - prefix_sum[nearest_right_of_left])
            else:
                res.append(0)

        return res


def main():
    # Example 1: Output: [2,3]
    s = "**|**|***|"
    queries = [[2, 5], [5, 9]]

    # Example 2: Output: [9,0,0,0,0]
    # s = "***|**|*****|**||**|*"
    # queries = [[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.platesBetweenCandles(s, queries)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
