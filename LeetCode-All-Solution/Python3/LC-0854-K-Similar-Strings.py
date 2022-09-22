#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0854-K-Similar-Strings.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-09-21
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 0854 - (Hard) - K-Similar Strings
https://leetcode.com/problems/k-similar-strings/

Description & Requirement:
    Strings s1 and s2 are k-similar (for some non-negative integer k) 
    if we can swap the positions of two letters in s1 exactly k times so that the resulting string equals s2.

    Given two anagrams s1 and s2, return the smallest k for which s1 and s2 are k-similar.

Example 1:
    Input: s1 = "ab", s2 = "ba"
    Output: 1
Example 2:
    Input: s1 = "abc", s2 = "bca"
    Output: 2

Constraints:
    1 <= s1.length <= 20
    s2.length == s1.length
    s1 and s2 contain only lowercase letters from the set {'a', 'b', 'c', 'd', 'e', 'f'}.
    s2 is an anagram of s1.
"""


class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        # exception case
        assert isinstance(s1, str) and isinstance(s2, str) and len(s1) == len(s2) >= 1
        # main method: (search algorithm)
        return self._kSimilarity(s1, s2)

    def _kSimilarity(self, s1: str, s2: str) -> int:
        """
        Runtime: 201 ms, faster than 87.24% of Python3 online submissions for K-Similar Strings.
        Memory Usage: 15.3 MB, less than 59.29% of Python3 online submissions for K-Similar Strings.
        """
        assert isinstance(s1, str) and isinstance(s2, str) and len(s1) == len(s2) >= 1

        step, n = 0, len(s1)
        queue, visited = [(s1, 0)], set(s1)

        while True:
            tmp = queue
            queue = []
            for s, i in tmp:
                if s == s2:
                    return step
                while i < n and s[i] == s2[i]:
                    i += 1
                for j in range(i + 1, n):
                    if s[j] == s2[i] != s2[j]:  # 剪枝，只在 s[j] != s2[j] 时去交换
                        t = list(s)
                        t[i], t[j] = t[j], t[i]
                        t = ''.join(t)
                        if t not in visited:
                            visited.add(t)
                            queue.append((t, i + 1))
            step += 1


def main():
    # Example 1: Output: 1
    # s1 = "ab"
    # s2 = "ba"

    # Example 2: Output: 2
    s1 = "abc"
    s2 = "bca"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.kSimilarity(s1, s2)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
