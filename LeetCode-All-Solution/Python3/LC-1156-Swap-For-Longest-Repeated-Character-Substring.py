#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1156-Swap-For-Longest-Repeated-Character-Substring.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-06-03
=================================================================="""

import sys
import time
# from typing import List
import collections
# import functools

"""
LeetCode - 1156 - (Medium) - Swap For Longest Repeated Character Substring
https://leetcode.com/problems/swap-for-longest-repeated-character-substring/

Description & Requirement:
    You are given a string text. You can swap two of the characters in the text.

    Return the length of the longest substring with repeated characters.

Example 1:
    Input: text = "ababa"
    Output: 3
    Explanation: We can swap the first 'b' with the last 'a', or the last 'b' with the first 'a'. 
        Then, the longest repeated character substring is "aaa" with length 3.
Example 2:
    Input: text = "aaabaaa"
    Output: 6
    Explanation: Swap 'b' with the last 'a' (or the first 'a'), and 
        we get longest repeated character substring "aaaaaa" with length 6.
Example 3:
    Input: text = "aaaaa"
    Output: 5
    Explanation: No need to swap, longest repeated character substring is "aaaaa" with length is 5.

Constraints:
    1 <= text.length <= 2 * 10^4
    text consist of lowercase English characters only.
"""


class Solution:
    def maxRepOpt1(self, text: str) -> int:
        # exception case
        assert isinstance(text, str) and len(text) >= 1
        # main method: (hash counter)
        return self._maxRepOpt1(text)

    def _maxRepOpt1(self, text: str) -> int:
        assert isinstance(text, str) and len(text) >= 1

        cnt = collections.Counter(text)

        n = len(text)
        res = i = 0
        while i < n:
            j = i
            while j < n and text[j] == text[i]:
                j += 1
            l = j - i
            k = j + 1
            while k < n and text[k] == text[i]:
                k += 1
            r = k - j - 1
            res = max(res, min(l + r + 1, cnt[text[i]]))
            i = j

        return res


def main():
    # Example 1: Output: 3
    # text = "ababa"

    # Example 2: Output: 6
    text = "aaabaaa"

    # Example 3: Output: 5
    # text = "aaaaa"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maxRepOpt1(text)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
