#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2347-Best-Poker-Hand.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-02-20
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 2347 - (Easy) - Best Poker Hand
https://leetcode.com/problems/best-poker-hand/

Description & Requirement:
    You are given an integer array ranks and a character array suits. 
    You have 5 cards where the ith card has a rank of ranks[i] and a suit of suits[i].

    The following are the types of poker hands you can make from best to worst:
        "Flush": Five cards of the same suit.
        "Three of a Kind": Three cards of the same rank.
        "Pair": Two cards of the same rank.
        "High Card": Any single card.

    Return a string representing the best type of poker hand you can make with the given cards.

    Note that the return values are case-sensitive.

Example 1:
    Input: ranks = [13,2,3,1,9], suits = ["a","a","a","a","a"]
    Output: "Flush"
    Explanation: The hand with all the cards consists of 5 cards with the same suit, so we have a "Flush".
Example 2:
    Input: ranks = [4,4,2,4,4], suits = ["d","a","a","b","c"]
    Output: "Three of a Kind"
    Explanation: The hand with the first, second, and fourth card consists of 3 cards with the same rank, 
        so we have a "Three of a Kind".
        Note that we could also make a "Pair" hand but "Three of a Kind" is a better hand.
        Also note that other cards could be used to make the "Three of a Kind" hand.
Example 3:
    Input: ranks = [10,10,2,12,9], suits = ["a","b","c","a","d"]
    Output: "Pair"
    Explanation: The hand with the first and second card consists of 2 cards with the same rank, so we have a "Pair".
        Note that we cannot make a "Flush" or a "Three of a Kind".

Constraints:
    ranks.length == suits.length == 5
    1 <= ranks[i] <= 13
    'a' <= suits[i] <= 'd'
    No two cards have the same rank and suit.
"""


class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        # exception case
        assert isinstance(ranks, list) and isinstance(suits, list) and len(ranks) == len(suits) == 5
        # main method: (hash counter)
        return self._bestHand(ranks, suits)

    def _bestHand(self, ranks: List[int], suits: List[str]) -> str:
        assert isinstance(ranks, list) and isinstance(suits, list) and len(ranks) == len(suits) == 5

        if len(set(suits)) == 1:
            return "Flush"

        cnt = collections.Counter(ranks)
        if len(cnt) == 5:
            return "High Card"

        for _, item_2 in cnt.items():
            if item_2 > 2:
                return "Three of a Kind"

        return "Pair"


def main():
    # Example 1: Output: "Flush"
    # ranks = [13, 2, 3, 1, 9]
    # suits = ["a", "a", "a", "a", "a"]

    # Example 2: Output: "Three of a Kind"
    # ranks = [4, 4, 2, 4, 4]
    # suits = ["d", "a", "a", "b", "c"]

    # Example 3: Output: "Pair"
    ranks = [10, 10, 2, 12, 9]
    suits = ["a", "b", "c", "a", "d"]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.bestHand(ranks, suits)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
