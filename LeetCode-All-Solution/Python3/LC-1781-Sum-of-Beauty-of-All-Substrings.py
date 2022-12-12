#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1781-Sum-of-Beauty-of-All-Substrings.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-12-12
=================================================================="""

import sys
import time
import collections
# from typing import List
# import functools

"""
LeetCode - 1781 - (Medium) - Sum of Beauty of All Substrings
https://leetcode.com/problems/sum-of-beauty-of-all-substrings/

Description & Requirement:
    The beauty of a string is the difference in frequencies between the most frequent and least frequent characters.

    For example, the beauty of "abaacc" is 3 - 1 = 2.

    Given a string s, return the sum of beauty of all of its substrings.

Example 1:
    Input: s = "aabcb"
    Output: 5
    Explanation: The substrings with non-zero beauty are ["aab","aabc","aabcb","abcb","bcb"], 
        each with beauty equal to 1.
Example 2:
    Input: s = "aabcbaa"
    Output: 17

Constraints:
    1 <= s.length <= 500
    s consists of only lowercase English letters.
"""


class Solution:
    def beautySum(self, s: str) -> int:
        # exception case
        assert isinstance(s, str) and len(s) >= 1 and s.islower()
        # main method: (hash dict counter)
        return self._beautySum(s)

    def _beautySum(self, s: str) -> int:
        """
        Time: beats 97.55%; Space: beats 97.55%
        """
        assert isinstance(s, str) and len(s) >= 1 and s.islower()
        n = len(s)

        # def _beauty(string: str) -> int:
        #     counter = dict({})
        #     for ch in s:
        #         if ch not in counter:
        #             counter[ch] = 1
        #         else:
        #             counter[ch] += 1
        #     freq = list(counter.values())
        #     return max(freq) - min(freq)

        res = 0
        for i in range(n):
            cnt = collections.Counter()
            max_freq = 0
            for j in range(i, n):
                cnt[s[j]] += 1
                max_freq = max(max_freq, cnt[s[j]])
                res += max_freq - min(cnt.values())

        return res


def main():
    # Example 1: Output: 5
    # s = "aabcb"

    # Example 2: Output: 17
    s = "aabcbaa"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.beautySum(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
