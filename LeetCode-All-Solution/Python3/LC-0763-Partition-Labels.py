#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0763-Partition-Labels.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-17
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0763 - (Medium) - Partition Labels
https://leetcode.com/problems/partition-labels/

Description & Requirement:
    You are given a string s. 
    We want to partition the string into as many parts as possible so that each letter appears in at most one part.

    Note that the partition is done so that after concatenating all the parts in order, 
    the resultant string should be s.

    Return a list of integers representing the size of these parts.

Example 1:
    Input: s = "ababcbacadefegdehijhklij"
    Output: [9,7,8]
    Explanation:
    The partition is "ababcbaca", "defegde", "hijhklij".
    This is a partition so that each letter appears in at most one part.
    A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
Example 2:
    Input: s = "eccbbbbdec"
    Output: [10]

Constraints:
    1 <= s.length <= 500
    s consists of lowercase English letters.
"""


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # exception case
        assert isinstance(s, str) and len(s) > 0
        # main method: (record each letter and its indices, partition as many parts as possible)
        return self._partitionLabels(s)

    def _partitionLabels(self, s: str) -> List[int]:
        """
        Runtime: 44 ms, faster than 82.56% of Python3 online submissions for Partition Labels.
        Memory Usage: 14 MB, less than 41.14% of Python3 online submissions for Partition Labels.
        """
        len_s = len(s)
        assert len_s > 0

        # record each letter and its indices
        letter_index = dict({})  # key: letter; value: index list (lists[0] is the smallest, list[-1] is the largest)
        for idx, ch in enumerate(s):
            if ch not in letter_index:
                letter_index[ch] = [idx]
            else:
                letter_index[ch].append(idx)

        res = []
        cur_start = 0
        while cur_start < len_s:
            cur_index_list = letter_index[s[cur_start]]
            cur_smallest, cur_largest = cur_index_list[0], cur_index_list[-1]
            # consider the end border of each letter in [cur_smallest, cur_largest]
            cur_end = cur_largest
            cur_idx = cur_start
            while cur_idx < cur_end:
                cur_end = max(cur_end, letter_index[s[cur_idx]][-1])
                cur_idx += 1
            # record the length of this part and move on
            res.append(cur_end - cur_start + 1)
            cur_start = cur_end + 1  # next part

        return res


def main():
    # Example 1: Output: [9,7,8]
    # s = "ababcbacadefegdehijhklij"

    # Example 2: Output: [10]
    s = "eccbbbbdec"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.partitionLabels(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
