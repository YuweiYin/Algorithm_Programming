#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0948-Bag-of-Tokens.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-09-12
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 0948 - (Medium) - Bag of Tokens
https://leetcode.com/problems/bag-of-tokens/

Description & Requirement:
    You have an initial power of power, an initial score of 0, and a bag of tokens 
    where tokens[i] is the value of the ith token (0-indexed).

    Your goal is to maximize your total score by potentially playing each token in one of two ways:
        If your current power is at least tokens[i], you may play the ith token face up, losing tokens[i] power and gaining 1 score.
        If your current score is at least 1, you may play the ith token face down, gaining tokens[i] power and losing 1 score.

    Each token may be played at most once and in any order. You do not have to play all the tokens.

    Return the largest possible score you can achieve after playing any number of tokens.

Example 1:
    Input: tokens = [100], power = 50
    Output: 0
    Explanation: Playing the only token in the bag is impossible 
        because you either have too little power or too little score.
Example 2:
    Input: tokens = [100,200], power = 150
    Output: 1
    Explanation: Play the 0th token (100) face up, your power becomes 50 and score becomes 1.
        There is no need to play the 1st token since you cannot play it face up to add to your score.
Example 3:
    Input: tokens = [100,200,300,400], power = 200
    Output: 2
    Explanation: Play the tokens in this order to get a score of 2:
        1. Play the 0th token (100) face up, your power becomes 100 and score becomes 1.
        2. Play the 3rd token (400) face down, your power becomes 500 and score becomes 0.
        3. Play the 1st token (200) face up, your power becomes 300 and score becomes 1.
        4. Play the 2nd token (300) face up, your power becomes 0 and score becomes 2.

Constraints:
    0 <= tokens.length <= 1000
    0 <= tokens[i], power < 10^4
"""


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        # exception case
        assert isinstance(power, int) and power >= 0
        assert isinstance(tokens, list)
        for token in tokens:
            assert isinstance(token, int) and token >= 0
        # main method: (greedy: get the maximum power to get the maximum score)
        return self._bagOfTokensScore(tokens, power)

    def _bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        """
        Runtime: 49 ms, faster than 100.00% of Python3 online submissions for Bag of Tokens.
        Memory Usage: 14.1 MB, less than 38.14% of Python3 online submissions for Bag of Tokens.
        """
        assert isinstance(power, int) and power >= 0
        assert isinstance(tokens, list)

        tokens.sort()  # get tokens with the lowest power first
        queue = collections.deque(tokens)
        res = 0
        new_res = 0

        while len(queue) > 0 and (power >= queue[0] or new_res > 0):
            while queue and power >= queue[0]:  # play tokens face up
                power -= queue.popleft()  # consume the current power
                new_res += 1
            res = max(res, new_res)

            if len(queue) > 0 and new_res > 0:  # play tokens face down
                power += queue.pop()
                new_res -= 1

        return res


def main():
    # Example 1: Output: 0
    # tokens = [100]
    # power = 50

    # Example 2: Output: 1
    # tokens = [100, 200]
    # power = 150

    # Example 3: Output: 2
    tokens = [100, 200, 300, 400]
    power = 200

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.bagOfTokensScore(tokens, power)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
