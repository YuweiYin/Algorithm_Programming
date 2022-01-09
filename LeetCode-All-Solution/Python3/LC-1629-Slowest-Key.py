#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1629-Slowest-Key.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-09
=================================================================="""

import sys
import time
from typing import List
# import queue
# import collections

"""
LeetCode - 1629 - (Easy) - Slowest Key
https://leetcode.com/problems/slowest-key/

Description:
    A newly designed keypad was tested, where a tester pressed a sequence of n keys, one at a time.

    You are given a string keysPressed of length n, 
    where keysPressed[i] was the ith key pressed in the testing sequence, 
    and a sorted list releaseTimes, where releaseTimes[i] was the time the ith key was released. 
    Both arrays are 0-indexed. The 0th key was pressed at the time 0, 
    and every subsequent key was pressed at the exact time the previous key was released.

    The tester wants to know the key of the keypress that had the longest duration. 
    The ith keypress had a duration of releaseTimes[i] - releaseTimes[i - 1], 
    and the 0th keypress had a duration of releaseTimes[0].

    Note that the same key could have been pressed multiple times during the test, 
    and these multiple presses of the same key may not have had the same duration.

Requirement:
    Return the key of the keypress that had the longest duration. 
    If there are multiple such keypresses, return the lexicographically largest key of the keypresses.

Example 1:
    Input: releaseTimes = [9,29,49,50], keysPressed = "cbcd"
    Output: "c"
    Explanation: The keypresses were as follows:
        Keypress for 'c' had a duration of 9 (pressed at time 0 and released at time 9).
        Keypress for 'b' had a duration of 29 - 9 = 20 
            (pressed at time 9 right after the release of the previous character and released at time 29).
        Keypress for 'c' had a duration of 49 - 29 = 20 
            (pressed at time 29 right after the release of the previous character and released at time 49).
        Keypress for 'd' had a duration of 50 - 49 = 1 
            (pressed at time 49 right after the release of the previous character and released at time 50).
        The longest of these was the keypress for 'b' and the second keypress for 'c', both with duration 20.
        'c' is lexicographically larger than 'b', so the answer is 'c'.
Example 2:
    Input: releaseTimes = [12,23,36,46,62], keysPressed = "spuda"
    Output: "a"
    Explanation: The keypresses were as follows:
        Keypress for 's' had a duration of 12.
        Keypress for 'p' had a duration of 23 - 12 = 11.
        Keypress for 'u' had a duration of 36 - 23 = 13.
        Keypress for 'd' had a duration of 46 - 36 = 10.
        Keypress for 'a' had a duration of 62 - 46 = 16.
        The longest of these was the keypress for 'a' with duration 16.

Constraints:
    releaseTimes.length == n
    keysPressed.length == n
    2 <= n <= 1000
    1 <= releaseTimes[i] <= 10^9
    releaseTimes[i] < releaseTimes[i+1]
    keysPressed contains only lowercase English letters.
"""


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        # exception case
        if not isinstance(releaseTimes, list) or len(releaseTimes) <= 0:
            return ""
        if not isinstance(keysPressed, str) or len(keysPressed) <= 0:
            return ""
        if len(releaseTimes) != len(keysPressed):
            return ""
        if len(releaseTimes) == 1:
            return keysPressed
        # main method: easily scan the list, use dict to store every key's longest duration
        return self._slowestKey(releaseTimes, keysPressed)

    def _slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        len_time = len(releaseTimes)
        assert len_time == len(keysPressed) and len_time > 1

        key_du_dict = dict({})  # key: key; value: the key's longest duration
        key_du_dict[keysPressed[0]] = releaseTimes[0]  # the first key

        cur_time = 1
        while cur_time < len_time:  # record each key and its longest duration in dict (except the first key)
            cur_key = keysPressed[cur_time]
            cur_duration = releaseTimes[cur_time] - releaseTimes[cur_time - 1]
            if cur_key in key_du_dict:
                key_du_dict[cur_key] = max(key_du_dict[cur_key], cur_duration)
            else:
                key_du_dict[cur_key] = cur_duration
            cur_time += 1

        longest_duration = releaseTimes[0]
        slowest_key = keysPressed[0]
        for k, du in key_du_dict.items():
            if du == longest_duration:
                # get the lexicographically larger key
                if k > slowest_key:
                    slowest_key = k
            elif du > longest_duration:
                slowest_key = k
                longest_duration = du

        return slowest_key


def main():
    # Example 1: Output: "c"
    releaseTimes = [9, 29, 49, 50]
    keysPressed = "cbcd"

    # Example 2: Output: "a"
    # releaseTimes = [12, 23, 36, 46, 62]
    # keysPressed = "spuda"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.slowestKey(releaseTimes, keysPressed)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
