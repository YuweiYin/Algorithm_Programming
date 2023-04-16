#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1639-Number-of-Ways-to-Form-a-Target-String-Given-a-Dictionary.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-04-16
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 1639 - (Hard) - Number of Ways to Form a Target String Given a Dictionary
https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/

Description & Requirement:
    You are given a list of strings of the same length words and a string target.

    Your task is to form target using the given words under the following rules:
        target should be formed from left to right.
        To form the i-th character (0-indexed) of target, you can choose the kth character of the j-th string 
            in words if target[i] = words[j][k].
        Once you use the kth character of the j-th string of words, you can no longer use the x-th character of 
            any string in words where x <= k. In other words, all characters to the left of or at index k 
            become unusuable for every string.
        Repeat the process until you form the string target.

    Notice that you can use multiple characters from the same string in words provided the conditions above are met.

    Return the number of ways to form target from words. Since the answer may be too large, return it modulo 109 + 7.

Example 1:
    Input: words = ["acca","bbbb","caca"], target = "aba"
    Output: 6
    Explanation: There are 6 ways to form target.
        "aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("caca")
        "aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("caca")
        "aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("acca")
        "aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("acca")
        "aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("acca")
        "aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("caca")
Example 2:
    Input: words = ["abba","baab"], target = "bab"
    Output: 4
    Explanation: There are 4 ways to form target.
        "bab" -> index 0 ("baab"), index 1 ("baab"), index 2 ("abba")
        "bab" -> index 0 ("baab"), index 1 ("baab"), index 3 ("baab")
        "bab" -> index 0 ("baab"), index 2 ("baab"), index 3 ("baab")
        "bab" -> index 1 ("abba"), index 2 ("baab"), index 3 ("baab")

Constraints:
    1 <= words.length <= 1000
    1 <= words[i].length <= 1000
    All strings in words have the same length.
    1 <= target.length <= 1000
    words[i] and target contain only lowercase English letters.
"""


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        # exception case
        assert isinstance(words, list) and len(words) >= 1
        assert isinstance(target, str) and len(target) >= 1
        # main method: (dynamic programming)
        return self._numWays(words, target)

    def _numWays(self, words: List[str], target: str) -> int:
        assert isinstance(words, list) and len(words) >= 1
        assert isinstance(target, str) and len(target) >= 1

        MOD = int(1e9+7)
        n = len(words[0])
        m = len(words)

        len_target = len(target)
        dp = [[0] * len_target for _ in range(n)]
        dict_list = [collections.Counter([words[i][k] for i in range(m)]) for k in range(n)]

        cur = 0
        for i in range(n):
            if target[0] in dict_list[i]:
                cur += dict_list[i][target[0]]
            dp[i][0] = cur

        for i in range(1, n):
            for j in range(1, len_target):
                if target[j] in dict_list[i]:
                    dp[i][j] = dict_list[i][target[j]] * dp[i - 1][j - 1] + dp[i - 1][j] % MOD
                else:
                    dp[i][j] = dp[i - 1][j] % MOD

        return dp[-1][-1] % MOD


def main():
    # Example 1: Output: 6
    # words = ["acca", "bbbb", "caca"]
    # target = "aba"

    # Example 2: Output: 4
    words = ["abba", "baab"]
    target = "bab"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.numWays(words, target)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
