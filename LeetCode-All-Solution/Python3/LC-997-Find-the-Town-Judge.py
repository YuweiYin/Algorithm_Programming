#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-997-Find-the-Town-Judge.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-04
=================================================================="""

import sys
import time
from typing import List

"""
LeetCode - 997 - (Easy) - Find the Town Judge
https://leetcode.com/problems/find-the-town-judge/

Description:
    In a town, there are n people labeled from 1 to n. 
    There is a rumor that one of these people is secretly the town judge.

    If the town judge exists, then:
        1. The town judge trusts nobody.
        2. Everybody (except for the town judge) trusts the town judge.
        3. There is exactly one person that satisfies properties 1 and 2.

    You are given an array trust where trust[i] = [ai, bi] representing 
    that the person labeled ai trusts the person labeled bi.

Requirement:
    Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

Example 1:
    Input: n = 2, trust = [[1,2]]
    Output: 2
Example 2:
    Input: n = 3, trust = [[1,3],[2,3]]
    Output: 3
Example 3:
    Input: n = 3, trust = [[1,3],[2,3],[3,1]]
    Output: -1

Constraints:
    1 <= n <= 1000
    0 <= trust.length <= 10^4
    trust[i].length == 2
    All the pairs of trust are unique.
    ai != bi
    1 <= ai, bi <= n
"""


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # border & exception case (len(trust) < n - 1 means there cannot be a person that is trusted by all others)
        if not isinstance(trust, list):
            return -1
        if len(trust) == 0:
            return 1 if n == 1 else -1
        if n <= 1 or len(trust) < n - 1:
            return -1
        if n == 2:
            if len(trust) == 1:
                return trust[0][1]
            else:
                return -1
        # main method: (hash set & dict. consider the in-degree and out-degree of each vertex in graph)
        return self._findJudge(n, trust)

    def _findJudge(self, n: int, trust: List[List[int]]) -> int:
        len_trust = len(trust)
        trust_set = set()  # this set records people who have trusted others (the judge cannot be in trust_set)
        trusted_dict = dict()  # key: every person that is trusted; value: the trust counter
        # first loop: scan the trust list
        cur_index = 0
        while cur_index < len_trust:
            cur_trust_person = trust[cur_index][0]
            # update the trust_set
            if cur_trust_person not in trust_set:
                trust_set.add(cur_trust_person)

            cur_trusted_person = trust[cur_index][1]
            # update the trusted_dict
            if cur_trusted_person in trusted_dict:
                trusted_dict[cur_trusted_person] += 1
            else:  # add cur_diff to diff_dict
                trusted_dict[cur_trusted_person] = 1
            cur_index += 1

        # second loop: find a person in trust_dict that is trusted by (n - 1) people
        for k, v in trusted_dict.items():  # key: every person that is trusted; value: the trust counter
            if v == n - 1 and not (k in trust_set):  # the judge is trusted by all others but doesn't trust anyone
                return k

        return -1


def main():
    # Example 1: Output: 2
    # n = 2
    # trust = [[1, 2]]

    # Example 2: Output: 3
    # n = 3
    # trust = [[1, 3], [2, 3]]

    # Example 3: Output: -1
    # n = 3
    # trust = [[1, 3], [2, 3], [3, 1]]

    # Example 4: Output: 1
    n = 1
    trust = []

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.findJudge(n, trust)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
