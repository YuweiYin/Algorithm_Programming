#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1773-Count-Items-Matching-a-Rule.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-10-29
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1773 - (Easy) - Count Items Matching a Rule
https://leetcode.com/problems/count-items-matching-a-rule/

Description & Requirement:
    You are given an array items, where each items[i] = [type_i, color_i, name_i] describes the type, color, 
    and name of the ith item. You are also given a rule represented by two strings, ruleKey and ruleValue.

    The ith item is said to match the rule if one of the following is true:
        ruleKey == "type" and ruleValue == type_i.
        ruleKey == "color" and ruleValue == color_i.
        ruleKey == "name" and ruleValue == name_i.

    Return the number of items that match the given rule.

Example 1:
    Input: items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], 
        ruleKey = "color", ruleValue = "silver"
    Output: 1
    Explanation: There is only one item matching the given rule, which is ["computer","silver","lenovo"].
Example 2:
    Input: items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], 
        ruleKey = "type", ruleValue = "phone"
    Output: 2
    Explanation: There are only two items matching the given rule, which are ["phone","blue","pixel"] and 
        ["phone","gold","iphone"]. Note that the item ["computer","silver","phone"] does not match.

Constraints:
    1 <= items.length <= 10^4
    1 <= type_i.length, color_i.length, name_i.length, ruleValue.length <= 10
    ruleKey is equal to either "type", "color", or "name".
    All strings consist only of lowercase letters.
"""


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        # exception case
        assert isinstance(items, list) and len(items) >= 1
        assert isinstance(ruleKey, str)
        assert isinstance(ruleValue, str) and len(ruleValue) >= 1
        # main method: (process simulation)
        return self._countMatches(items, ruleKey, ruleValue)

    def _countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        assert isinstance(items, list) and len(items) >= 1
        assert isinstance(ruleKey, str)
        assert isinstance(ruleValue, str) and len(ruleValue) >= 1

        index = {"type": 0, "color": 1, "name": 2}[ruleKey]

        return sum(item[index] == ruleValue for item in items)


def main():
    # Example 1: Output: 1
    # items = [["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]]
    # ruleKey = "color"
    # ruleValue = "silver"

    # Example 2: Output: 2
    items = [["phone", "blue", "pixel"], ["computer", "silver", "phone"], ["phone", "gold", "iphone"]]
    ruleKey = "type"
    ruleValue = "phone"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.countMatches(items, ruleKey, ruleValue)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
