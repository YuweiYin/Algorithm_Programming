#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0710-Random-Pick-with-Blacklist.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-06-26
=================================================================="""

import sys
import time
from typing import List
import random
# import functools

"""
LeetCode - 0710 - (Hard) - Random Pick with Blacklist
https://leetcode.com/problems/random-pick-with-blacklist/

Description & Requirement:
    You are given an integer n and an array of unique integers blacklist. 
    Design an algorithm to pick a random integer in the range [0, n - 1] that is not in blacklist. 
    Any integer that is in the mentioned range and not in blacklist should be equally likely to be returned.

    Optimize your algorithm such that it minimizes the number of calls to the built-in random function of your language.

    Implement the Solution class:
        Solution(int n, int[] blacklist) Initializes the object with the integer n and the blacklisted integers blacklist.
        int pick() Returns a random integer in the range [0, n - 1] and not in blacklist.

Example 1:
    Input
        ["Solution", "pick", "pick", "pick", "pick", "pick", "pick", "pick"]
        [[7, [2, 3, 5]], [], [], [], [], [], [], []]
    Output
        [null, 0, 4, 1, 6, 1, 0, 4]
    Explanation
        Solution solution = new Solution(7, [2, 3, 5]);
        solution.pick(); // return 0, any integer from [0,1,4,6] should be ok. Note that for every call of pick,
                         // 0, 1, 4, and 6 must be equally likely to be returned (i.e., with probability 1/4).
        solution.pick(); // return 4
        solution.pick(); // return 1
        solution.pick(); // return 6
        solution.pick(); // return 1
        solution.pick(); // return 0
        solution.pick(); // return 4

Constraints:
    1 <= n <= 10^9
    0 <= blacklist.length <= min(10^5, n - 1)
    0 <= blacklist[i] < n
    All the values of blacklist are unique.
    At most 2 * 10^4 calls will be made to pick.
"""


class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        width = n - len(blacklist)
        self.boundary = n - len(blacklist)
        black = {b for b in blacklist if b >= self.boundary}
        self.b2w = dict({})
        for b in blacklist:
            if b < self.boundary:
                while width in black:
                    width += 1
                self.b2w[b] = width
                width += 1

    def pick(self) -> int:
        x = random.randrange(self.boundary)
        return self.b2w[x] if x in self.b2w else x


def main():
    # Example 1: Output: [null, 0, 4, 1, 6, 1, 0, 4]
    command_list = ["Solution", "pick", "pick", "pick", "pick", "pick", "pick", "pick"]
    param_list = [[7, [2, 3, 5]], [], [], [], [], [], [], []]

    # init instance
    # solution = Solution()
    n, blacklist = param_list[0]
    obj = Solution(n, blacklist)
    ans = ["null"]

    # run & time
    start = time.process_time()
    assert len(command_list) == len(param_list)
    for idx in range(len(command_list)):
        command = command_list[idx]
        # param = param_list[idx]
        if command == "pick":
            ans.append(obj.pick())
        else:
            ans.append("null")
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
