#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1147-Longest-Chunked-Palindrome-Decomposition.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-04-12
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 1147 - (Hard) - Longest Chunked Palindrome Decomposition
https://leetcode.com/problems/longest-chunked-palindrome-decomposition/

Description & Requirement:
    You are given a string text. You should split it to k substrings 
    (subtext1, subtext2, ..., subtextk) such that:

        subtexti is a non-empty string.
        The concatenation of all the substrings is equal to text 
            (i.e., subtext1 + subtext2 + ... + subtextk == text).
        subtexti == subtextk - i + 1 for all valid values of i (i.e., 1 <= i <= k).

    Return the largest possible value of k.

Example 1:
    Input: text = "ghiabcdefhelloadamhelloabcdefghi"
    Output: 7
    Explanation: We can split the string on "(ghi)(abcdef)(hello)(adam)(hello)(abcdef)(ghi)".
Example 2:
    Input: text = "merchant"
    Output: 1
    Explanation: We can split the string on "(merchant)".
Example 3:
    Input: text = "antaprezatepzapreanta"
    Output: 11
    Explanation: We can split the string on "(a)(nt)(a)(pre)(za)(tep)(za)(pre)(a)(nt)(a)".

Constraints:
    1 <= text.length <= 1000
    text consists only of lowercase English characters.
"""


class Solution:
    def longestDecomposition(self, text: str) -> int:
        # exception case
        assert isinstance(text, str) and len(text) >= 1
        # main method: (string hashing)
        return self._longestDecomposition(text)

    def _longestDecomposition(self, text: str) -> int:
        assert isinstance(text, str) and len(text) >= 1

        n = len(text)
        BASE = 131
        MOD = int(1e9 + 7)

        def get(l, r):
            return (h[r] - h[l - 1] * p[r - l + 1]) % MOD

        h = [0] * (n + 10)
        p = [1] * (n + 10)
        for i, c in enumerate(text):
            t = ord(c) - ord("a") + 1
            h[i + 1] = (h[i] * BASE) % MOD + t
            p[i + 1] = (p[i] * BASE) % MOD

        res = 0
        i, j = 0, n - 1
        while i <= j:
            k = 1
            ok = False
            while i + k - 1 < j - k + 1:
                if get(i + 1, i + k) == get(j - k + 2, j + 1):
                    res += 2
                    i += k
                    j -= k
                    ok = True
                    break
                k += 1
            if not ok:
                res += 1
                break

        return res


def main():
    # Example 1: Output: 7
    # text = "ghiabcdefhelloadamhelloabcdefghi"

    # Example 2: Output: 1
    # text = "merchant"

    # Example 3: Output: 11
    text = "antaprezatepzapreanta"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.longestDecomposition(text)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
