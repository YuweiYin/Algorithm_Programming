#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1202-Smallest-String-With-Swaps.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-27
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 1202 - (Medium) - Smallest String With Swaps
https://leetcode.com/problems/smallest-string-with-swaps/

Description & Requirement:
    You are given a string s, and an array of pairs of indices in the string pairs where 
    pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.

    You can swap the characters at any pair of indices in the given pairs any number of times.

    Return the lexicographically smallest string that s can be changed to after using the swaps.

Example 1:
    Input: s = "dcab", pairs = [[0,3],[1,2]]
    Output: "bacd"
    Explanation: 
        Swap s[0] and s[3], s = "bcad"
        Swap s[1] and s[2], s = "bacd"
Example 2:
    Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
    Output: "abcd"
    Explanation: 
        Swap s[0] and s[3], s = "bcad"
        Swap s[0] and s[2], s = "acbd"
        Swap s[1] and s[2], s = "abcd"
Example 3:
    Input: s = "cba", pairs = [[0,1],[1,2]]
    Output: "abc"
    Explanation: 
        Swap s[0] and s[1], s = "bca"
        Swap s[1] and s[2], s = "bac"
        Swap s[0] and s[1], s = "abc"

Constraints:
    1 <= s.length <= 10^5
    0 <= pairs.length <= 10^5
    0 <= pairs[i][0], pairs[i][1] < s.length
    s only contains lower case English letters.
"""


class UnionFindSet:
    def __init__(self, n):
        self.n = n  # the number of initial sets
        self.rank = [1 for _ in range(n)]  # initially, each set has only 1 element with rank 1 (rank: set length)
        self.disjoint_set = list(range(n))  # if d_s[i] == d_s[j], then element i and j are in the same set

    def find_set(self, x: int) -> int:
        if self.disjoint_set[x] == x:  # x is the root element of a set, just return it
            return x
        self.disjoint_set[x] = self.find_set(self.disjoint_set[x])  # recursively merge links to the root of the set
        return self.disjoint_set[x]

    def union_set(self, x: int, y: int) -> bool:
        set_x, set_y = self.find_set(x), self.find_set(y)  # find the set roots of element x and y separately
        if set_x == set_y:  # no need to union
            return False

        if self.rank[set_x] < self.rank[set_y]:  # let set_x be the larger set (with larger rank)
            set_x, set_y = set_y, set_x

        self.rank[set_x] += self.rank[set_y]
        self.disjoint_set[set_y] = set_x
        return True


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # exception case
        assert isinstance(s, str) and len(s) >= 1
        assert isinstance(pairs, list)
        len_s = len(s)
        for pair in pairs:
            assert isinstance(pair, list) and len(pair) == 2
            assert isinstance(pair[0], int) and 0 <= pair[0] < len_s
            assert isinstance(pair[1], int) and 0 <= pair[1] < len_s
        # main method: (merge pair in pairs, sort each index group in s)
        return self._smallestStringWithSwaps(s, pairs)

    def _smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        """
        Runtime: 684 ms, faster than 96.47% of Python3 online submissions for Smallest String With Swaps.
        Memory Usage: 50.6 MB, less than 43.32% of Python3 online submissions for Smallest String With Swaps.
        """
        assert isinstance(s, str) and len(s) >= 1
        assert isinstance(pairs, list)
        if len(pairs) == 0:
            return s
        len_s = len(s)
        s_list = [ch for ch in s]

        # clear_pair_set = set()
        # for pair in pairs:
        #     if pair[0] == pair[1]:
        #         continue
        #     if pair[0] > pair[1]:
        #         pair[0], pair[1] = pair[1], pair[0]
        #     if (pair[0], pair[1]) not in clear_pair_set:
        #         clear_pair_set.add((pair[0], pair[1]))
        # pairs = []
        # for pair in clear_pair_set:
        #     pairs.append([pair[0], pair[1]])
        # pairs.sort(key=lambda x: (x[0], x[1]))

        # Union-Find Set, group indices together
        ufs = UnionFindSet(len_s)
        for pair in pairs:
            ufs.union_set(pair[0], pair[1])

        # key: set number; value: [idx_list, ch_list]
        unique_dict = dict({})
        for idx, element in enumerate(ufs.disjoint_set):
            set_root = ufs.find_set(element)
            if set_root not in unique_dict:
                unique_dict[set_root] = [[idx], [s_list[idx]]]
            else:
                unique_dict[set_root][0].append(idx)
                unique_dict[set_root][1].append(s_list[idx])

        # sort ch_list, modify s_list
        for k, v in unique_dict.items():
            idx_list = v[0]
            ch_list = v[1]
            ch_list.sort()
            ch_idx = 0
            for idx in idx_list:
                s_list[idx] = ch_list[ch_idx]
                ch_idx += 1

        return "".join(s_list)


def main():
    # Example 1: Output: "bacd"
    s = "dcab"
    pairs = [[0, 3], [1, 2]]

    # Example 2: Output: "abcd"
    # s = "dcab"
    # pairs = [[0, 3], [1, 2], [0, 2]]

    # Example 3: Output: "abc"
    # s = "cba"
    # pairs = [[0, 1], [1, 2]]

    # Example 4: Output: "lpqqmwm"
    # s = "pwqlmqm"
    # pairs = [[5, 3], [3, 0], [5, 1], [1, 1], [1, 5], [3, 0], [0, 2]]

    # Example 5: Output: "tfikklmqxlyz"
    # s = "tklkxyizmlqf"
    # pairs = [[2, 10], [3, 5], [8, 11], [1, 2], [10, 6], [4, 1], [1, 10], [5, 8], [8, 3], [10, 4], [7, 3], [10, 11]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.smallestStringWithSwaps(s, pairs)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
