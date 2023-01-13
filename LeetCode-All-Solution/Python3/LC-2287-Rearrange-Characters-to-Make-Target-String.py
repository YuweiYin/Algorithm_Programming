#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2287-Rearrange-Characters-to-Make-Target-String.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-01-13
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 2287 - (Easy) - Rearrange Characters to Make Target String
https://leetcode.com/problems/rearrange-characters-to-make-target-string/

Description & Requirement:
    You are given two 0-indexed strings s and target. 
    You can take some letters from s and rearrange them to form new strings.

    Return the maximum number of copies of target that can be formed by taking letters from s and rearranging them.

Example 1:
    Input: s = "ilovecodingonleetcode", target = "code"
    Output: 2
    Explanation:
        For the first copy of "code", take the letters at indices 4, 5, 6, and 7.
        For the second copy of "code", take the letters at indices 17, 18, 19, and 20.
        The strings that are formed are "ecod" and "code" which can both be rearranged into "code".
        We can make at most two copies of "code", so we return 2.
Example 2:
    Input: s = "abcba", target = "abc"
    Output: 1
    Explanation:
        We can make one copy of "abc" by taking the letters at indices 0, 1, and 2.
        We can make at most one copy of "abc", so we return 1.
        Note that while there is an extra 'a' and 'b' at indices 3 and 4, 
        we cannot reuse the letter 'c' at index 2, so we cannot make a second copy of "abc".
Example 3:
    Input: s = "abbaccaddaeea", target = "aaaaa"
    Output: 1
    Explanation:
        We can make one copy of "aaaaa" by taking the letters at indices 0, 3, 6, 9, and 12.
        We can make at most one copy of "aaaaa", so we return 1.

Constraints:
    1 <= s.length <= 100
    1 <= target.length <= 10
    s and target consist of lowercase English letters.
"""


class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        # exception case
        assert isinstance(s, str) and len(s) >= 1 and s.isalpha() and s.islower()
        assert isinstance(target, str) and len(target) >= 1 and target.isalpha() and target.islower()
        # main method: (hash counter)
        return self._rearrangeCharacters(s, target)

    def _rearrangeCharacters(self, s: str, target: str) -> int:
        """
        Time: beats 70.97%; Space: beats 64.41%
        """
        assert isinstance(s, str) and len(s) >= 1 and s.isalpha() and s.islower()
        assert isinstance(target, str) and len(target) >= 1 and target.isalpha() and target.islower()

        cnt_s = dict({})
        for ch in s:
            if ch not in cnt_s:
                cnt_s[ch] = 1
            else:
                cnt_s[ch] += 1

        cnt_t = dict({})
        for ch in target:
            if ch not in cnt_t:
                cnt_t[ch] = 1
            else:
                cnt_t[ch] += 1

        res_list = []
        for ch in set(target):
            if ch in cnt_s:
                res_list.append(int(cnt_s[ch] / cnt_t[ch]))
            else:
                return 0

        return min(res_list)


def main():
    # Example 1: Output: 2
    # s = "ilovecodingonleetcode"
    # target = "code"

    # Example 2: Output: 1
    # s = "abcba"
    # target = "abc"

    # Example 3: Output: 1
    s = "abbaccaddaeea"
    target = "aaaaa"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.rearrangeCharacters(s, target)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
