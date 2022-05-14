#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0691-Stickers-to-Spell-Word.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-05-14
=================================================================="""

import sys
import time
from typing import List
import functools
import collections

"""
LeetCode - 0691 - (Hard) - Stickers to Spell Word
https://leetcode.com/problems/stickers-to-spell-word/

Description & Requirement:
    We are given n different types of stickers. Each sticker has a lowercase English word on it.

    You would like to spell out the given string target by cutting individual letters 
    from your collection of stickers and rearranging them. You can use each sticker more than once if you want, 
    and you have infinite quantities of each sticker.

    Return the minimum number of stickers that you need to spell out target. If the task is impossible, return -1.

    Note: In all test cases, all words were chosen randomly from the 1000 most common US English words, 
    and target was chosen as a concatenation of two random words.

Example 1:
    Input: stickers = ["with","example","science"], target = "thehat"
    Output: 3
    Explanation:
        We can use 2 "with" stickers, and 1 "example" sticker.
        After cutting and rearrange the letters of those stickers, we can form the target "thehat".
        Also, this is the minimum number of stickers necessary to form the target string.
Example 2:
    Input: stickers = ["notice","possible"], target = "basicbasic"
    Output: -1
    Explanation: We cannot form the target "basicbasic" from cutting letters from the given stickers.

Constraints:
    n == stickers.length
    1 <= n <= 50
    1 <= stickers[i].length <= 10
    1 <= target.length <= 15
    stickers[i] and target consist of lowercase English letters.
"""


class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        # exception case
        assert isinstance(target, str) and len(target) >= 1
        assert isinstance(stickers, list) and len(stickers) >= 1
        for sticker in stickers:
            assert isinstance(sticker, str) and len(sticker) >= 1
        # main method: (dynamic programming)
        return self._minStickers(stickers, target)

    def _minStickers(self, stickers: List[str], target: str) -> int:
        # len_stickers = len(stickers)
        len_target = len(target)

        @functools.lru_cache(maxsize=None)
        def dp_top_down(mask: int) -> int:
            # i-th binary bit of mask == 0 means i-th char of target is not chosen.
            if mask == 0:
                return 0
            ans = len_target + 1  # INF
            for sticker in stickers:  # for each available sticker, decide whether choose it or not
                next_mask = mask
                counter = collections.Counter(sticker)
                for idx, ch in enumerate(target):
                    if ((mask >> idx) & 0x01) and counter[ch] > 0:  # if idx-th bit of mask is 1 and counter of ch > 0
                        counter[ch] -= 1
                        next_mask ^= (1 << idx)
                    if next_mask < mask:
                        ans = min(ans, dp_top_down(next_mask) + 1)
            return ans

        res = dp_top_down((1 << len_target) - 1)  # start from all binary bits 1
        return res if res <= len_target else -1


def main():
    # Example 1: Output: 3
    stickers = ["with", "example", "science"]
    target = "thehat"

    # Example 2: Output: -1
    # stickers = ["notice", "possible"]
    # target = "basicbasic"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minStickers(stickers, target)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
