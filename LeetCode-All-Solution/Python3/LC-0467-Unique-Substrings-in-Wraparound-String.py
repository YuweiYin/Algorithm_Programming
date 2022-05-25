#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0467-Unique-Substrings-in-Wraparound-String.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-05-25
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 0467 - (Medium) - Unique Substrings in Wraparound String
https://leetcode.com/problems/unique-substrings-in-wraparound-string/

Description & Requirement:
    We define the string s to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz", 
    so s will look like this:
        "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".

    Given a string p, return the number of unique non-empty substrings of p are present in s.

Example 1:
    Input: p = "a"
    Output: 1
    Explanation: Only the substring "a" of p is in s.
Example 2:
    Input: p = "cac"
    Output: 2
    Explanation: There are two substrings ("a", "c") of p in s.
Example 3:
    Input: p = "zab"
    Output: 6
    Explanation: There are six substrings ("z", "a", "b", "za", "ab", and "zab") of p in s.

Constraints:
    1 <= p.length <= 10^5
    p consists of lowercase English letters.
"""


class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        # exception case
        assert isinstance(p, str) and len(p) >= 1
        # main method: (scan p, find all consecutive substrings that are also substrings of s.)
        # return self._findSubstringInWraproundString(p)
        return self._findSubstringInWraproundStringDP(p)

    def _findSubstringInWraproundString(self, p: str) -> int:
        assert isinstance(p, str) and len(p) >= 1
        len_p = len(p)

        s_base = "abcdefghijklmnopqrstuvwxyz"
        len_s_base = len(s_base)
        ch_list = [ch for ch in s_base]
        ch_to_idx = dict({})
        idx = 0
        for ch in ch_list:
            ch_to_idx[ch] = idx
            idx += 1

        idx = 0
        sub_set = set()
        while idx < len_p:
            start_idx = idx
            next_idx = idx + 1
            while next_idx < len_p and ch_to_idx[p[next_idx]] % len_s_base == (ch_to_idx[p[idx]] + 1) % len_s_base:
                idx += 1
                next_idx += 1
            cur_substring = p[start_idx: next_idx]
            if cur_substring not in sub_set:
                sub_set.add(cur_substring)
            idx += 1

        res_set = set()
        for substr in sub_set:
            len_substr = len(substr)
            # consider all substrings
            for start_idx in range(len_substr):
                for end_idx in range(start_idx + 1, len_substr + 1):
                    cur_substring = substr[start_idx: end_idx]
                    if cur_substring not in res_set:
                        res_set.add(cur_substring)

        return len(res_set)

    def _findSubstringInWraproundStringDP(self, p: str) -> int:
        """
        Runtime: 88 ms, faster than 90.82% of Python3 online submissions for Unique Substrings in Wraparound String.
        Memory Usage: 14.2 MB, less than 20.29% of Python3 online submissions for Unique Substrings in Wraparound Str.
        """
        assert isinstance(p, str) and len(p) >= 1

        s_base = "abcdefghijklmnopqrstuvwxyz"
        len_s_base = len(s_base)
        dp = dict({})  # dp[ch] is the max-length valid substring that ends with ch
        for ch in s_base:
            dp[ch] = 0

        cur_substr_max_len = 0
        for idx, ch in enumerate(p):
            if idx > 0 and (ord(ch) - ord(p[idx - 1])) % len_s_base == 1:
                cur_substr_max_len += 1
            else:
                cur_substr_max_len = 1
            dp[ch] = max(dp[ch], cur_substr_max_len)

        return sum(dp.values())


def main():
    # Example 1: Output: 1
    # p = "a"

    # Example 2: Output: 2
    # p = "cac"

    # Example 3: Output: 6
    p = "zab"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.findSubstringInWraproundString(p)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
