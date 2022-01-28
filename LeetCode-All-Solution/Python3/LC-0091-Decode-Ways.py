#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0091-Decode-Ways.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-28
=================================================================="""

import sys
import time
# from typing import List
# import collections

"""
LeetCode - 0091 - (Medium) - Decode Ways
https://leetcode.com/problems/decode-ways/

Description & Requirement:
    A message containing letters from A-Z can be encoded into numbers using the following mapping:
        'A' -> "1"
        'B' -> "2"
        ...
        'Z' -> "26"
    To decode an encoded message, all the digits must be grouped then mapped back into letters 
    using the reverse of the mapping above (there may be multiple ways). 
    For example, "11106" can be mapped into:
        "AAJF" with the grouping (1 1 10 6)
        "KJF" with the grouping (11 10 6)
    Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' 
        since "6" is different from "06".

    Given a string s containing only digits, return the number of ways to decode it.

    The test cases are generated so that the answer fits in a 32-bit integer.

Example 1:
    Input: s = "12"
    Output: 2
    Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
Example 2:
    Input: s = "226"
    Output: 3
    Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
Example 3:
    Input: s = "06"
    Output: 0
    Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").

Constraints:
    1 <= s.length <= 100
    s contains only digits and may contain leading zero(s).
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        # exception case
        if not isinstance(s, str) or len(s) <= 0:
            return 0  # Error input type
        if s[0] == "0":
            return 0  # heading 0, no way!
        assert s.isdigit()
        if len(s) == 1:
            return 1
        # main method: (Dynamic Programming: dp[i] is the max decoding ways using s[0: i+1])
        #     dp equation: dp[i] = dp[i-1] if decoding single number s[i-1] and 1 <= s[i-1] <= 9
        #                  dp[i] = dp[i-2] if decoding two numbers s[i-2] s[i-1] and 10 <= s[i-2] s[i-1] <= 26
        #                  dp[i] = 0, otherwise
        #     dp init: dp[0] = 1 if s[0] != 0, else: overall result is 0
        #     dp aim: get dp[-1]
        return self._numDecodings(s)

    def _numDecodings(self, s: str) -> int:
        """
        Runtime: 28 ms, faster than 92.19% of Python3 online submissions for Decode Ways.
        Memory Usage: 14 MB, less than 99.19% of Python3 online submissions for Decode Ways.
        """
        len_s = len(s)
        assert len_s >= 2 and s.isdigit() and s[0] != "0"

        dp = [0 for _ in range(len_s + 1)]  # i = 0, 1, ..., len_s
        dp[0] = 1

        for index in range(1, len_s + 1):
            if s[index - 1] != "0":
                dp[index] += dp[index - 1]  # decoding single number s[i-1] and 1 <= s[i-1] <= 9
            if index >= 2 and s[index - 2] != "0" and 10 <= int(s[index - 2: index]) <= 26:
                dp[index] += dp[index - 2]  # decoding two numbers s[i-2] s[i-1] and 10 <= s[i-2] s[i-1] <= 26

        return dp[-1]


def main():
    # Example 1: Output: 2
    #     Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
    # s = "12"

    # Example 2: Output: 3
    #     Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
    s = "226"

    # Example 3: Output: 0
    #     Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
    # s = "06"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.numDecodings(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
