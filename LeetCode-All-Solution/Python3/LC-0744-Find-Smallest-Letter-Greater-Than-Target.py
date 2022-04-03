#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0744-Find-Smallest-Letter-Greater-Than-Target.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-03
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0744 - (Easy) - Find Smallest Letter Greater Than Target
https://leetcode.com/problems/find-smallest-letter-greater-than-target/

Description & Requirement:
    Given a characters array letters that is sorted in non-decreasing order and a character target, 
    return the smallest character in the array that is larger than target.

    Note that the letters wrap around.

    For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.

Example 1:
    Input: letters = ["c","f","j"], target = "a"
    Output: "c"
Example 2:
    Input: letters = ["c","f","j"], target = "c"
    Output: "f"
Example 3:
    Input: letters = ["c","f","j"], target = "d"
    Output: "f"

Constraints:
    2 <= letters.length <= 10^4
    letters[i] is a lowercase English letter.
    letters is sorted in non-decreasing order.
    letters contains at least two different characters.
    target is a lowercase English letter.
"""


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # exception case
        assert isinstance(letters, list) and len(letters) >= 2
        assert isinstance(target, str)
        # main method: (1. scan from left to right; 2. binary search)
        return self._nextGreatestLetter(letters, target)

    def _nextGreatestLetter(self, letters: List[str], target: str) -> str:
        """
        Runtime: 107 ms, faster than 96.27% of Python3 online submissions for Find Smallest Letter Greater Than Target.
        Memory Usage: 14.7 MB, less than 24.34% of Python3 online submissions for Find Smallest Letter Greater Than T.
        """

        # for ch in letters:
        #     if ch > target:
        #         return ch
        # return ""

        def __binary_search(left_idx: int, right_idx: int) -> str:
            if left_idx > right_idx:
                return ""
            if left_idx == right_idx:
                return letters[left_idx] if letters[left_idx] > target else ""

            mid_idx = (left_idx + right_idx) >> 1
            if letters[mid_idx] <= target:
                return __binary_search(mid_idx + 1, right_idx)
            else:
                left_res = __binary_search(left_idx, mid_idx - 1)
                return left_res if len(left_res) > 0 else letters[mid_idx]

        res = __binary_search(0, len(letters) - 1)
        return res if len(res) > 0 else letters[0]


def main():
    # Example 1: Output: "c"
    # letters = ["c", "f", "j"]
    # target = "a"

    # Example 2: Output: "f"
    # letters = ["c", "f", "j"]
    # target = "c"

    # Example 3: Output: "f"
    letters = ["c", "f", "j"]
    target = "d"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.nextGreatestLetter(letters, target)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
