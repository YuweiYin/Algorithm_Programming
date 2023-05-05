#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1456-Maximum-Number-of-Vowels-in-a-Substring-of-Given-Length.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-05-05
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 1456 - (Medium) - Maximum Number of Vowels in a Substring of Given Length
https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

Description & Requirement:
    Given a string s and an integer k, 
    return the maximum number of vowel letters in any substring of s with length k.

    Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:
    Input: s = "abciiidef", k = 3
    Output: 3
    Explanation: The substring "iii" contains 3 vowel letters.
Example 2:
    Input: s = "aeiou", k = 2
    Output: 2
    Explanation: Any substring of length 2 contains 2 vowels.
Example 3:
    Input: s = "leetcode", k = 3
    Output: 2
    Explanation: "lee", "eet" and "ode" contain 2 vowels.

Constraints:
    1 <= s.length <= 10^5
    s consists of lowercase English letters.
    1 <= k <= s.length
"""


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # exception case
        assert isinstance(s, str) and len(s) >= 1
        assert isinstance(k, int) and k >= 1
        # main method: (sliding window)
        return self._maxVowels(s, k)

    def _maxVowels(self, s: str, k: int) -> int:
        assert isinstance(s, str) and len(s) >= 1
        assert isinstance(k, int) and k >= 1

        def __is_vowel(ch):
            return int(ch in "aeiou")

        vowel_count = sum(1 for i in range(k) if __is_vowel(s[i]))
        res = vowel_count

        for i in range(k, len(s)):
            vowel_count += __is_vowel(s[i]) - __is_vowel(s[i - k])
            res = max(res, vowel_count)

        return res


def main():
    # Example 1: Output: 3
    s = "abciiidef"
    k = 3

    # Example 2: Output: 2
    # s = "aeiou"
    # k = 2

    # Example 3: Output: 2
    # s = "leetcode"
    # k = 3

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maxVowels(s, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
