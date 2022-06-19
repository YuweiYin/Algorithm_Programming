#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1268-Search-Suggestions-System.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-06-19
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 1268 - (Medium) - Search Suggestions System
https://leetcode.com/problems/search-suggestions-system/

Description & Requirement:
    You are given an array of strings products and a string searchWord.

    Design a system that suggests at most three product names from products after each character of searchWord is typed.
    Suggested products should have common prefix with searchWord. If there are more than three products 
    with a common prefix return the three lexicographically minimums products.

    Return a list of lists of the suggested products after each character of searchWord is typed.

Example 1:
    Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
    Output: [
        ["mobile","moneypot","monitor"],
        ["mobile","moneypot","monitor"],
        ["mouse","mousepad"],
        ["mouse","mousepad"],
        ["mouse","mousepad"]
    ]
    Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
        After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
        After typing mou, mous and mouse the system suggests ["mouse","mousepad"]
Example 2:
    Input: products = ["havana"], searchWord = "havana"
    Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
Example 3:
    Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
    Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]

Constraints:
    1 <= products.length <= 1000
    1 <= products[i].length <= 3000
    1 <= sum(products[i].length) <= 2 * 10^4
    All the strings of products are unique.
    products[i] consists of lowercase English letters.
    1 <= searchWord.length <= 1000
    searchWord consists of lowercase English letters.
"""


class Trie:
    def __init__(self):
        self.products = []
        self.child = dict({})


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # exception case
        assert isinstance(searchWord, str) and len(searchWord) >= 1
        assert isinstance(products, list) and len(products) >= 1
        for product in products:
            assert isinstance(product, str) and len(product) >= 1
        # main method: (Trie)
        return self._suggestedProducts(products, searchWord)

    def _suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        assert isinstance(searchWord, str) and len(searchWord) >= 1
        assert isinstance(products, list) and len(products) >= 1

        root = Trie()

        for product in products:  # Trie construction
            cur_node = root
            for ch in product:
                if ch not in cur_node.child:
                    cur_node.child[ch] = Trie()
                cur_node = cur_node.child[ch]
                cur_node.products.append(product)
                cur_node.products.sort()
                if len(cur_node.products) > 3:
                    cur_node.products.pop()

        res = []
        cur_node = root
        FIRST = False
        for ch in searchWord:  # Trie matching
            if FIRST or ch not in cur_node.child:
                res.append([])
                FIRST = True
            else:
                cur_node = cur_node.child[ch]
                res.append(cur_node.products)

        return res


def main():
    # Example 1: Output: [
    #         ["mobile","moneypot","monitor"],
    #         ["mobile","moneypot","monitor"],
    #         ["mouse","mousepad"],
    #         ["mouse","mousepad"],
    #         ["mouse","mousepad"]
    #     ]
    products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    searchWord = "mouse"

    # Example 2: Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
    # products = ["havana"]
    # searchWord = "havana"

    # Example 3: Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
    # products = ["bags", "baggage", "banner", "box", "cloths"]
    # searchWord = "bags"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.suggestedProducts(products, searchWord)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
