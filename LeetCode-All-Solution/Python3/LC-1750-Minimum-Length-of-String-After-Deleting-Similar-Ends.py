#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1750-Minimum-Length-of-String-After-Deleting-Similar-Ends.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-12-28
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 1750 - (Medium) - Minimum Length of String After Deleting Similar Ends
https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/

Description & Requirement:
    Given a string s consisting only of characters 'a', 'b', and 'c'. 
    You are asked to apply the following algorithm on the string any number of times:

        Pick a non-empty prefix from the string s where all the characters in the prefix are equal.
        Pick a non-empty suffix from the string s where all the characters in this suffix are equal.
        The prefix and the suffix should not intersect at any index.
        The characters from the prefix and suffix must be the same.
        Delete both the prefix and the suffix.

    Return the minimum length of s after performing the above operation any number of times (possibly zero times).

Example 1:
    Input: s = "ca"
    Output: 2
    Explanation: You can't remove any characters, so the string stays as is.
Example 2:
    Input: s = "cabaabac"
    Output: 0
    Explanation: An optimal sequence of operations is:
        - Take prefix = "c" and suffix = "c" and remove them, s = "abaaba".
        - Take prefix = "a" and suffix = "a" and remove them, s = "baab".
        - Take prefix = "b" and suffix = "b" and remove them, s = "aa".
        - Take prefix = "a" and suffix = "a" and remove them, s = "".
Example 3:
    Input: s = "aabccabba"
    Output: 3
    Explanation: An optimal sequence of operations is:
        - Take prefix = "aa" and suffix = "a" and remove them, s = "bccabb".
        - Take prefix = "b" and suffix = "bb" and remove them, s = "cca".

Constraints:
    1 <= s.length <= 10^5
    s only consists of characters 'a', 'b', and 'c'.
"""


class Solution:
    def minimumLength(self, s: str) -> int:
        # exception case
        assert isinstance(s, str) and len(s) >= 1
        # main method: (two pointers)
        return self._minimumLength(s)

    def _minimumLength(self, s: str) -> int:
        """
        Time: beats 94.48%; Space: beats 44.79%
        """
        assert isinstance(s, str) and len(s) >= 1

        left, right = 0, len(s) - 1
        while left < right and s[left] == s[right]:
            ch = s[left]
            while left <= right and s[left] == ch:
                left += 1
            while right >= left and s[right] == ch:
                right -= 1

        return right - left + 1


def main():
    # Example 1: Output: 2
    # s = "ca"

    # Example 2: Output: 0
    # s = "cabaabac"

    # Example 3: Output: 3
    s = "aabccabba"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minimumLength(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
