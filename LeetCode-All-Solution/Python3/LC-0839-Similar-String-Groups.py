#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0839-Similar-String-Groups.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-04-28
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0839 - (Hard) - Similar String Groups
https://leetcode.com/problems/similar-string-groups/

Description & Requirement:
    Two strings X and Y are similar if we can swap two letters (in different positions) of X, 
    so that it equals Y. Also two strings X and Y are similar if they are equal.

    For example, "tars" and "rats" are similar (swapping at positions 0 and 2), 
    and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".

    Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}. 
    Notice that "tars" and "arts" are in the same group even though they are not similar. 
    Formally, each group is such that a word is in the group if and only if 
    it is similar to at least one other word in the group.

    We are given a list strs of strings where every string in strs 
    is an anagram of every other string in strs. How many groups are there?

Example 1:
    Input: strs = ["tars","rats","arts","star"]
    Output: 2
Example 2:
    Input: strs = ["omv","ovm"]
    Output: 1

Constraints:
    1 <= strs.length <= 300
    1 <= strs[i].length <= 300
    strs[i] consists of lowercase letters only.
    All words in strs have the same length and are anagrams of each other.
"""


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        # exception case
        assert isinstance(strs, list) and len(strs) >= 1
        # main method: (Union-Find Set)
        return self._numSimilarGroups(strs)

    def _numSimilarGroups(self, strs: List[str]) -> int:
        assert isinstance(strs, list) and len(strs) >= 1

        n = len(strs)
        ufs = list(range(n))

        def __find(x: int) -> int:
            if ufs[x] == x:
                return x
            ufs[x] = __find(ufs[x])
            return ufs[x]

        def __check(string_1: str, string_2: str) -> bool:
            cnt = 0
            for ch_1, ch_2 in zip(string_1, string_2):
                if ch_1 != ch_2:
                    cnt += 1
                    if cnt > 2:
                        return False
            return True

        for i in range(n):
            for j in range(i + 1, n):
                root_i, root_j = __find(i), __find(j)
                if root_i == root_j:
                    continue
                if __check(strs[i], strs[j]):
                    ufs[root_i] = root_j

        return sum(1 for i in range(n) if ufs[i] == i)


def main():
    # Example 1: Output: 2
    strs = ["tars", "rats", "arts", "star"]

    # Example 2: Output: 1
    # strs = ["omv", "ovm"]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.numSimilarGroups(strs)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
