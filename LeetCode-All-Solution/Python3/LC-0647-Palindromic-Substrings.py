#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0647-Palindromic-Substrings.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-05-22
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 0647 - (Medium) - Palindromic Substrings
https://leetcode.com/problems/palindromic-substrings/

Description & Requirement:
    Given a string s, return the number of palindromic substrings in it.
    A string is a palindrome when it reads the same backward as forward.
    A substring is a contiguous sequence of characters within the string.

Example 1:
    Input: s = "abc"
    Output: 3
    Explanation: Three palindromic strings: "a", "b", "c".
Example 2:
    Input: s = "aaa"
    Output: 6
    Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

Constraints:
    1 <= s.length <= 1000
    s consists of lowercase English letters.
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        # exception case
        assert isinstance(s, str) and len(s) >= 1
        # main method: (Manacher's algorithm)
        return self._countSubstrings(s)

    def _countSubstrings(self, s: str) -> int:
        """
        Runtime: 53 ms, faster than 99.18% of Python3 online submissions for Palindromic Substrings.
        Memory Usage: 14 MB, less than 40.70% of Python3 online submissions for Palindromic Substrings.
        """
        assert isinstance(s, str) and len(s) >= 1

        # use "#" to separate each char in string s
        m_s = "^#"  # start with "^"
        for ch in s:
            m_s += ch
            m_s += "#"
        len_ms = len(m_s)
        m_s += "$"  # end with "$"

        m_idx = [0 for _ in range(len_ms)]
        i_max, r_max, res = 0, 0, 0
        for idx in range(len_ms):
            # initiate Manacher index list
            m_idx[idx] = min(r_max - idx + 1, m_idx[(i_max << 1) - idx]) if idx <= r_max else 1
            # central expansion
            while m_s[idx + m_idx[idx]] == m_s[idx - m_idx[idx]]:
                m_idx[idx] += 1
            # maintain i_max and r_max
            if idx + m_idx[idx] - 1 > r_max:
                i_max = idx
                r_max = idx + m_idx[idx] - 1
            # get res count
            res += m_idx[idx] >> 1

        return res


def main():
    # Example 1: Output: 3
    s = "abc"

    # Example 2: Output: 6
    # s = "aaa"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.countSubstrings(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
