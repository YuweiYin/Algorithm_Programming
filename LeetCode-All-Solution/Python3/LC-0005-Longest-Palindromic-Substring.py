#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0005-Longest-Palindromic-Substring.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-27
=================================================================="""

import sys
import time
# from typing import List
# import collections

"""
LeetCode - 0005 - (Medium) - Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring/

Description & Requirement:
    Given a string s, return the longest palindromic substring in s.

Example 1:
    Input: s = "babad"
    Output: "bab"
    Explanation: "aba" is also a valid answer.
Example 2:
    Input: s = "cbbd"
    Output: "bb"

Constraints:
    1 <= s.length <= 1000
    s consist of only digits and English letters.
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # exception case
        if not isinstance(s, str) or len(s) <= 0:
            return ""  # Error input type
        if len(s) == 1:
            return s  # s itself is a palindrome
        if len(s) == 2:
            return s if s[0] == s[1] else s[0]
        # main method: (1. Dynamic Programming; 2. Mid Expansion; 3. Manacher's algorithm.)
        # return self._longestPalindromeDp(s)  # (the slowest, may TTL) Time: O(n^2).  Space: O(n^2)
        # return self._longestPalindromeMidExpand(s)  # (faster) Time: O(n^2).  Space: O(1)
        return self._longestPalindromeManacher(s)  # (best) Time: O(n).  Space: O(n)

    def _longestPalindromeDp(self, s: str) -> str:
        """
        Time: O(n^2).  Space: O(n^2)
        consider all substring, from len==1 to len==len(s), apply dp equation to test if they are palin or not
        Dynamic Programming: dp[i][j] means the length of longest palin substr from index i to index j
             dp equation: if s[i] == s[j], then dp[i][j] = 1 + dp[i+1][j-1]
                          if s[i] != s[j], then dp[i][j] = max(dp[i+1][j], dp[i][j-1])
                          border case 1: if i == j, then dp[i][j] == 1.
                          border case 2: if i == j - 1, then dp[i][j] == 2 if s[i] == s[j]
             init: i == 0, j == -1.  aim: dp[0][-1]
        """
        len_s = len(s)
        assert len_s > 2

        # dp[i][j] is True means s[i: j+1] is a palin
        dp = [[False for _ in range(len_s)] for _ in range(len_s)]
        for i in range(len_s):
            dp[i][i] = True  # each s[i] is a palin
        for i in range(len_s - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True  # palin of length == 2

        palin_start = 0
        max_palin_len = 1  # at least, s[0] is a palin

        for cur_p_len in range(2, len_s + 1):  # p_len is the length of palin, max is len_s
            for left_index in range(len_s):
                right_index = left_index + cur_p_len - 1
                if right_index >= len_s:  # out of index
                    break

                # dp equation
                if s[left_index] == s[right_index]:
                    if right_index - left_index <= 2:  # s[l:r+1] has <= 3 items, and s[l] == s[r], so s[l:r+1] is palin
                        dp[left_index][right_index] = True
                    else:
                        dp[left_index][right_index] = dp[left_index + 1][right_index - 1]  # consider inner string
                else:
                    dp[left_index][right_index] = False

                if dp[left_index][right_index] and cur_p_len > max_palin_len:
                    max_palin_len = cur_p_len  # update the max palin len
                    palin_start = left_index  # record the start index of this palin

        return s[palin_start: palin_start + max_palin_len]

    def _longestPalindromeMidExpand(self, s: str) -> str:
        """
        Time: O(n^2).  Space: O(1)
        Expand to find palin, for each index
        """
        len_s = len(s)
        assert len_s > 2

        def __mid_expand(left_index: int, right_index: int) -> tuple:
            while left_index >= 0 and right_index < len_s and s[left_index] == s[right_index]:
                left_index -= 1  # expand: left go left
                right_index += 1  # expand: right to right
            # now, can't fulfill the loop conditions, return the max expandable interval
            return left_index + 1, right_index - 1

        max_palin_left = 0
        max_palin_right = 0  # init: s[0] is a palin

        for center_index in range(len_s):  # expand from each index
            # case 1: expand from s[i], because s[i] must be a palin
            expand_left_1, expand_right_1 = __mid_expand(center_index, center_index)
            if expand_right_1 - expand_left_1 > max_palin_right - max_palin_left:  # update max len palin
                max_palin_left, max_palin_right = expand_left_1, expand_right_1

            # case 2: expand from s[i] s[i+1], if s[i] == s[i+1]
            expand_left_2, expand_right_2 = __mid_expand(center_index, center_index + 1)
            if expand_right_2 - expand_left_2 > max_palin_right - max_palin_left:  # update max len palin
                max_palin_left, max_palin_right = expand_left_2, expand_right_2

        return s[max_palin_left: max_palin_right + 1]

    def _longestPalindromeManacher(self, s: str) -> str:
        """
        Time: O(n).  Space: O(n)
        Manacher's algorithm to find the longest palindromic substring
        [Wiki](https://en.wikipedia.org/wiki/Longest_palindromic_substring)
        Runtime: 246 ms, faster than 94.10% of Python3 online submissions for Longest Palindromic Substring.
        Memory Usage: 14.5 MB, less than 34.75% of Python3 online submissions for Longest Palindromic Substring.
        """
        assert len(s) > 2

        # preprocess string s, convert even palin to odd palin
        PLACEHOLDER = "$"  # no matter what the placeholder char is, the algorithm will be correct
        new_s = PLACEHOLDER + PLACEHOLDER.join(list(s)) + PLACEHOLDER
        len_new_s = len(new_s)

        def __mid_expand(left_index: int, right_index: int) -> int:
            while left_index >= 0 and right_index < len_new_s and new_s[left_index] == new_s[right_index]:
                left_index -= 1  # expand: left go left
                right_index += 1  # expand: right to right
            # now, can't fulfill the loop conditions, return the arm length of the max expandable interval
            return (right_index - left_index - 2) >> 1

        # a palin consists of 1. left arm; 2. center point; 3. right arm.
        dp_arm_len = []  # dp_arm_len[i] == L means from center point i, the arm length of max expandable palin is L
        # actually, the arm length is exactly the real palin length, removing all the placeholders

        max_center_index = -1  # the former center of max expandable palin
        max_right_arm_index = -1  # the rightmost index of max expandable palin

        max_palin_left = 0  # to get the final result
        max_palin_right = -1  # init: (max_palin_right - max_palin_left) == -1 < 0

        # consider each index in new_s as center point
        # either expand from this center point from scratch, or reuse former expansion results recorded in dp_arm_len
        for cur_center_index in range(len_new_s):
            if max_right_arm_index >= cur_center_index:
                # now, former expansion results recorded in dp_arm_len can be reused
                # because all dp_arm_len[0: cur_center_index] have been calculated,
                # and from max_center_index to max_right_arm_index is a right arm of a palin
                # reuse the information of the symmetric point of cur_center_index about point max_center_index
                # consider how far can that symmetric point expand, skip a certain amount of expansion steps
                cur_center_symmetry = (max_center_index << 1) - cur_center_index
                # reuse dp_arm_len[cur_center_symmetry] though, the definite expansion can't be farther than max_right
                min_expand_arm_len = min(dp_arm_len[cur_center_symmetry], max_right_arm_index - cur_center_index)
                # now, keep expanding
                cur_arm_len = __mid_expand(cur_center_index - min_expand_arm_len, cur_center_index + min_expand_arm_len)
            else:
                # otherwise, do expansion from scratch
                cur_arm_len = __mid_expand(cur_center_index, cur_center_index)

            dp_arm_len.append(cur_arm_len)  # record the current arm length

            # update max expansion center and the rightmost index of its right arm
            if cur_center_index + cur_arm_len > max_right_arm_index:
                max_center_index = cur_center_index
                max_right_arm_index = cur_center_index + cur_arm_len

            # update the max palin (to get the final result palin)
            if (cur_arm_len << 1) + 1 > max_palin_right - max_palin_left:
                max_palin_left = cur_center_index - cur_arm_len
                max_palin_right = cur_center_index + cur_arm_len

        # get the final result, note that gap == 2 to skip all placeholder
        return new_s[max_palin_left + 1: max_palin_right + 1: 2]

    def _longestPalindromeSequence(self, s: str) -> str:
        """
        This function is to find the longest palindromic sequence, not substring (consecutive indices)
        """
        len_s = len(s)
        assert len_s > 2

        # INIT = 1
        # dp = [[INIT for _ in range(len_s)] for _ in range(len_s)]

        def __dp_dfs(left_index: int, right_index: int) -> str:
            if left_index > right_index:
                return ""  # not a palin
            if left_index == right_index - 1:
                if s[left_index] == s[right_index]:
                    return s[left_index: right_index + 1]
                else:
                    return s[left_index]  # or s[right_index]
            if left_index == right_index:
                return s[left_index]
            if s[left_index] == s[right_index]:
                return s[left_index] + __dp_dfs(left_index + 1, right_index - 1) + s[right_index]
            else:
                res_1 = __dp_dfs(left_index + 1, right_index)
                res_2 = __dp_dfs(left_index, right_index - 1)
                return res_1 if len(res_1) >= len(res_2) else res_2

        return __dp_dfs(0, len_s - 1)


def main():
    # Example 1: Output: "bab"
    s = "babad"

    # Example 2: Output: "bb"
    # s = "cbbd"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.longestPalindrome(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
