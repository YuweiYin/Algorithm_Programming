#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1647-Minimum-Deletions-to-Make-Character-Frequencies-Unique.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-06-28
=================================================================="""

import sys
import time
import collections
# from typing import List
# import functools

"""
LeetCode - 1647 - (Medium) - Minimum Deletions to Make Character Frequencies Unique
https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

Description & Requirement:
    A string s is called good if there are no two different characters in s that have the same frequency.

    Given a string s, return the minimum number of characters you need to delete to make s good.

    The frequency of a character in a string is the number of times it appears in the string. 
    For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

Example 1:
    Input: s = "aab"
    Output: 0
    Explanation: s is already good.
Example 2:
    Input: s = "aaabbbcc"
    Output: 2
    Explanation: You can delete two 'b's resulting in the good string "aaabcc".
    Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".
Example 3:
    Input: s = "ceabaacb"
    Output: 2
    Explanation: You can delete both 'c's resulting in the good string "eabaab".
    Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).

Constraints:
    1 <= s.length <= 10^5
    s contains only lowercase English letters.
"""


class Solution:
    def minDeletions(self, s: str) -> int:
        # exception case
        assert isinstance(s, str) and len(s) >= 1 and s.islower()
        # main method: (sort and greedy)
        return self._minDeletions(s)

    def _minDeletions(self, s: str) -> int:
        assert isinstance(s, str) and len(s) >= 1 and s.islower()

        s_list = sorted(list(collections.Counter(s).values()), reverse=True)
        res = 0
        for idx in range(1, len(s_list)):
            if s_list[idx] >= s_list[idx - 1]:  # move all chars in s_list[idx] to s_list[idx - 1]
                if s_list[idx - 1] > 0:  # s_list[idx - 1] is not empty
                    res += s_list[idx] - s_list[idx - 1] + 1
                    s_list[idx] = s_list[idx - 1] - 1
                else:  # s_list[idx - 1] is empty
                    res += s_list[idx]
                    s_list[idx] = 0

        return res


def main():
    # Example 1: Output: 0
    # s = "aab"

    # Example 2: Output: 2
    # s = "aaabbbcc"

    # Example 3: Output: 2
    s = "ceabaacb"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minDeletions(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
