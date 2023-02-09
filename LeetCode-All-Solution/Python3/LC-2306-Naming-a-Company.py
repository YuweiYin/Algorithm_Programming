#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2306-Naming-a-Company.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-02-09
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 2306 - (Hard) - Naming a Company
https://leetcode.com/problems/naming-a-company/

Description & Requirement:
    You are given an array of strings ideas that represents a list of names to be used in the process of 
    naming a company. The process of naming a company is as follows:

    Choose 2 distinct names from ideas, call them ideaA and ideaB.
    Swap the first letters of ideaA and ideaB with each other.
    If both of the new names are not found in the original ideas, then the name ideaA ideaB 
        (the concatenation of ideaA and ideaB, separated by a space) is a valid company name.
    Otherwise, it is not a valid name.

    Return the number of distinct valid names for the company.

Example 1:
    Input: ideas = ["coffee","donuts","time","toffee"]
    Output: 6
    Explanation: The following selections are valid:
        - ("coffee", "donuts"): The company name created is "doffee conuts".
        - ("donuts", "coffee"): The company name created is "conuts doffee".
        - ("donuts", "time"): The company name created is "tonuts dime".
        - ("donuts", "toffee"): The company name created is "tonuts doffee".
        - ("time", "donuts"): The company name created is "dime tonuts".
        - ("toffee", "donuts"): The company name created is "doffee tonuts".
        Therefore, there are a total of 6 distinct company names.
        The following are some examples of invalid selections:
        - ("coffee", "time"): The name "toffee" formed after swapping already exists in the original array.
        - ("time", "toffee"): Both names are still the same after swapping and exist in the original array.
        - ("coffee", "toffee"): Both names formed after swapping already exist in the original array.
Example 2:
    Input: ideas = ["lack","back"]
    Output: 0
    Explanation: There are no valid selections. Therefore, 0 is returned.

Constraints:
    2 <= ideas.length <= 5 * 10^4
    1 <= ideas[i].length <= 10
    ideas[i] consists of lowercase English letters.
    All the strings in ideas are unique.
"""


class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        # exception case
        assert isinstance(ideas, list) and len(ideas) >= 2
        # main method: (optimize the enumeration)
        return self._distinctNames(ideas)

    def _distinctNames(self, ideas: List[str]) -> int:
        assert isinstance(ideas, list) and len(ideas) >= 2

        N_CHAR = 26
        ORD_a = ord("a")

        group = collections.defaultdict(int)
        size = [0] * N_CHAR
        bad = [[0] * N_CHAR for _ in range(N_CHAR)]
        for string in ideas:
            i = ord(string[0]) - ORD_a
            string = string[1:]
            mask = group[string]
            group[string] |= 1 << i
            size[i] += 1

            for j in range(N_CHAR):
                if mask >> j & 1:
                    bad[i][j] += 1  # count the number of i that can not swap with string that starts with j
                    bad[j][i] += 1  # count the number of j that can not swap with string that starts with i

        res = 0
        for i, b in enumerate(bad):
            for j, m in enumerate(b[:i]):
                res += (size[i] - m) * (size[j] - m)

        return res << 1


def main():
    # Example 1: Output: 6
    ideas = ["coffee", "donuts", "time", "toffee"]

    # Example 2: Output: 0
    # ideas = ["lack", "back"]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.distinctNames(ideas)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
