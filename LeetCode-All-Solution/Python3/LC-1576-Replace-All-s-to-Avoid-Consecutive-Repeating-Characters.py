#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1576-Replace-All-s-to-Avoid-Consecutive-Repeating-Characters.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-05
=================================================================="""

import sys
import time
# from typing import List

"""
LeetCode - 1576 - (Easy) - Replace All ?'s to Avoid Consecutive Repeating Characters
https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/

Description:
    Given a string s containing only lowercase English letters and the '?' character, 
    convert all the '?' characters into lowercase letters such that 
    the final string does not contain any consecutive repeating characters. 
    You cannot modify the non '?' characters.

    It is guaranteed that there are no consecutive repeating characters in the given string except for '?'.

Requirement:
    Return the final string after all the conversions (possibly zero) have been made. 
    If there is more than one solution, return any of them. 
    It can be shown that an answer is always possible with the given constraints.

Example 1:
    Input: s = "?zs"
    Output: "azs"
    Explanation: There are 25 solutions for this problem. From "azs" to "yzs", all are valid. 
        Only "z" is an invalid modification as the string will consist of consecutive repeating characters in "zzs".
Example 2:
    Input: s = "ubv?w"
    Output: "ubvaw"
    Explanation: There are 24 solutions for this problem. 
        Only "v" and "w" are invalid modifications as the strings will consist of consecutive repeating characters 
        in "ubvvw" and "ubvww".

Constraints:
    1 <= s.length <= 100
    s consist of lowercase English letters and '?'.
"""


class Solution:
    def modifyString(self, s: str) -> str:
        # exception case
        if not isinstance(s, str) or len(s) <= 0:
            return s
        # border case
        if len(s) == 1:
            if s == "?":
                return "a"
            else:
                return s
        if len(s) == 2:
            if s == "??":
                return "ab"
            else:
                if s[0] == "?":
                    return ("a" + s[1]) if (s[1] != "a") else ("b" + s[1])
                elif s[1] == "?":
                    return (s[0] + "a") if (s[0] != "a") else (s[0] + "b")
                else:
                    return s
        # main method: (simply scan the list and replace every '?' to a valid letter)
        return self._modifyString(s)

    def _modifyString(self, s: str) -> str:
        res_s = ''
        len_s = len(s)  # must >= 3
        letter_list = ["a", "b", "c"]  # only 3 letters are enough

        # deal with the first char (it has no left constrain)
        if s[0] == "?":
            for letter in letter_list:  # find a valid letter to replace "?"
                if letter != s[1]:
                    res_s += letter
                    break  # when find one, break loop and consider the next char in s
        else:
            res_s += s[0]

        # deal with middle chars
        cur_ptr = 1
        while cur_ptr < len_s - 1:
            if s[cur_ptr] == "?":
                for letter in letter_list:  # find a valid letter to replace "?"
                    #  when look left, consider res_s string, not s, coz there can be "??"
                    if letter != res_s[cur_ptr - 1] and letter != s[cur_ptr + 1]:
                        res_s += letter
                        break  # when find one, break loop and consider the next char in s
            else:
                res_s += s[cur_ptr]
            cur_ptr += 1

        # deal with the last char (it has no left constrain)
        if s[len_s - 1] == "?":
            for letter in letter_list:  # find a valid letter to replace "?"
                if letter != res_s[len_s - 2]:  # when look left, consider res_s string, not s, coz there can be "??"
                    res_s += letter
                    break  # when find one, break loop and consider the next char in s
        else:
            res_s += s[len_s - 1]

        return res_s


def main():
    # Example 1: Output: "azs"
    # s = "?zs"

    # Example 2: Output: "ubvaw"
    # s = "ubv?w"

    # Example 3: Output: "jaqgacb"
    s = "j?qg??b"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.modifyString(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
