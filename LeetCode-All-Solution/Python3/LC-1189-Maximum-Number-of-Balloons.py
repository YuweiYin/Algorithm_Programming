#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1189-Maximum-Number-of-Balloons.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-11
=================================================================="""

import sys
import time
# from typing import List
# import collections

"""
LeetCode - 1189 - (Easy) - Maximum Number of Balloons
https://leetcode.com/problems/maximum-number-of-balloons/

Description & Requirement:
    Given a string text, you want to use the characters of text to 
    form as many instances of the word "balloon" as possible.

    You can use each character in text at most once. 
    Return the maximum number of instances that can be formed.

Example 1:
    Input: text = "nlaebolko"
    Output: 1
Example 2:
    Input: text = "loonbalxballpoon"
    Output: 2
Example 3:
    Input: text = "leetcode"
    Output: 0

Constraints:
    1 <= text.length <= 10^4
    text consists of lower case English letters only.
"""


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # exception case
        if not isinstance(text, str) or len(text) <= 0:
            return 0  # Error input type
        if len(text) < 7:  # len("balloon") == 7
            return 0
        # main method: (hash dict, counter)
        return self._maxNumberOfBalloons(text)

    def _maxNumberOfBalloons(self, text: str) -> int:
        len_text = len(text)
        assert len_text >= 7

        balloon_dict = {"b": 0, "a": 0, "l": 0, "o": 0, "n": 0}
        for char in text:
            if char in balloon_dict:
                balloon_dict[char] += 1

        balloon_counter = 0
        while balloon_dict["b"] >= 1 and balloon_dict["a"] >= 1 and balloon_dict["l"] >= 2 and \
                balloon_dict["o"] >= 2 and balloon_dict["n"] >= 1:
            balloon_counter += 1
            balloon_dict["b"] -= 1
            balloon_dict["a"] -= 1
            balloon_dict["l"] -= 2
            balloon_dict["o"] -= 2
            balloon_dict["n"] -= 1

        return balloon_counter


def main():
    # Example 1: Output: 1
    # text = "nlaebolko"

    # Example 2: Output: 2
    text = "loonbalxballpoon"

    # Example 3: Output: 0
    # text = "leetcode"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maxNumberOfBalloons(text)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
