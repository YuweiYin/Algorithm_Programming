#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1531-String-Compression-II.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-10-15
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 1531 - (Hard) - String Compression II
https://leetcode.com/problems/string-compression-ii/

Description & Requirement:
    [Run-length encoding](http://en.wikipedia.org/wiki/Run-length_encoding)
    is a string compression method that works by replacing consecutive identical characters 
    (repeated 2 or more times) with the concatenation of the character and the number marking the count of 
    the characters (length of the run). For example, to compress the string "aabccc" we replace "aa" by "a2" and 
    replace "ccc" by "c3". Thus the compressed string becomes "a2bc3".

    Notice that in this problem, we are not adding '1' after single characters.

    Given a string s and an integer k. You need to delete at most k characters from s such that 
    the run-length encoded version of s has minimum length.

    Find the minimum length of the run-length encoded version of s after deleting at most k characters.

Example 1:
    Input: s = "aaabcccd", k = 2
    Output: 4
    Explanation: Compressing s without deleting anything will give us "a3bc3d" of length 6. 
        Deleting any of the characters 'a' or 'c' would at most decrease the length of the compressed string to 5, 
        for instance delete 2 'a' then we will have s = "abcccd" which compressed is abc3d. 
        Therefore, the optimal way is to delete 'b' and 'd', 
        then the compressed version of s will be "a3c3" of length 4.
Example 2:
    Input: s = "aabbaa", k = 2
    Output: 2
    Explanation: If we delete both 'b' characters, the resulting compressed string would be "a4" of length 2.
Example 3:
    Input: s = "aaaaaaaaaaa", k = 0
    Output: 3
    Explanation: Since k is zero, we cannot delete anything. The compressed string is "a11" of length 3.

Constraints:
    1 <= s.length <= 100
    0 <= k <= s.length
    s contains only lowercase English letters.
"""


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        # exception case
        assert isinstance(s, str) and len(s) >= 1
        assert isinstance(k, int) and 0 <= k <= len(s)
        # main method: (dynamic programming)
        return self._getLengthOfOptimalCompression(s, k)

    def _getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        """
        Runtime: 878 ms, faster than 98.16% of Python3 online submissions for String Compression II.
        Memory Usage: 14.2 MB, less than 94.48% of Python3 online submissions for String Compression II.
        """
        assert isinstance(s, str) and len(s) >= 1
        assert isinstance(k, int) and 0 <= k <= len(s)

        def calc(x):
            return 1 if x == 1 else (2 if x < 10 else (3 if x < 100 else 4))

        n = len(s)
        dp = [[int(1e9+7) for _ in range(k + 1)] for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for j in range(min(i ,k) + 1):
                if j > 0:
                    dp[i][j] = dp[i - 1][j - 1]
                same = diff = 0
                for i0 in range(i, 0, -1):
                    if s[i0 - 1] == s[i - 1]:
                        same += 1
                        dp[i][j] = min(dp[i][j], dp[i0 - 1][j - diff] + calc(same))
                    else:
                        diff += 1
                        if diff > j:
                            break

        return dp[-1][-1]


def main():
    # Example 1: Output: 4
    # s = "aaabcccd"
    # k = 2

    # Example 2: Output: 2
    # s = "aabbaa"
    # k = 2

    # Example 3: Output: 3
    s = "aaaaaaaaaaa"
    k = 0

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.getLengthOfOptimalCompression(s, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
