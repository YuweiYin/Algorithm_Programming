#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2325-Decode-the-Message.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-02-01
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 2325 - (Easy) - Decode the Message
https://leetcode.com/problems/decode-the-message/

Description & Requirement:
    You are given the strings key and message, which represent a cipher key and a secret message, respectively. 
    The steps to decode message are as follows:

    Use the first appearance of all 26 lowercase English letters in key as the order of the substitution table.
    Align the substitution table with the regular English alphabet.
    Each letter in message is then substituted using the table.
    Spaces ' ' are transformed to themselves.

    For example, given key = "happy boy" (actual key would have at least one instance of each letter in the alphabet), 
    we have the partial substitution table of ('h' -> 'a', 'a' -> 'b', 'p' -> 'c', 'y' -> 'd', 'b' -> 'e', 'o' -> 'f').

    Return the decoded message.

Example 1:
    Input: key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv"
    Output: "this is a secret"
    Explanation: The diagram above shows the substitution table.
        It is obtained by taking the first appearance of each letter in "the quick brown fox jumps over the lazy dog".
Example 2:
    Input: key = "eljuxhpwnyrdgtqkviszcfmabo", message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"
    Output: "the five boxing wizards jump quickly"
    Explanation: The diagram above shows the substitution table.
        It is obtained by taking the first appearance of each letter in "eljuxhpwnyrdgtqkviszcfmabo".

Constraints:
    26 <= key.length <= 2000
    key consists of lowercase English letters and ' '.
    key contains every letter in the English alphabet ('a' to 'z') at least once.
    1 <= message.length <= 2000
    message consists of lowercase English letters and ' '.
"""


class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        # exception case
        assert isinstance(key, str) and len(key) >= 26
        assert isinstance(message, str) and len(message) >= 1
        # main method: (simulate the process)
        return self._decodeMessage(key, message)

    def _decodeMessage(self, key: str, message: str) -> str:
        assert isinstance(key, str) and len(key) >= 26
        assert isinstance(message, str) and len(message) >= 1

        hash_dict = dict({})

        cur_ch = "a"
        for ch in key:
            if ch != " " and ch not in hash_dict:
                hash_dict[ch] = cur_ch
                cur_ch = chr(ord(cur_ch) + 1)

        return "".join(hash_dict.get(ch, " ") for ch in message)


def main():
    # Example 1: Output: "this is a secret"
    # key = "the quick brown fox jumps over the lazy dog"
    # message = "vkbs bs t suepuv"

    # Example 2: Output: "the five boxing wizards jump quickly"
    key = "eljuxhpwnyrdgtqkviszcfmabo"
    message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.decodeMessage(key, message)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
