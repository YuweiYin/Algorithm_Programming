#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0451-Sort-Characters-By-Frequency.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-31
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 0451 - (Medium) - Sort Characters By Frequency
https://leetcode.com/problems/sort-characters-by-frequency/

Description & Requirement:
    Given a string s, sort it in decreasing order based on the frequency of the characters. 
    The frequency of a character is the number of times it appears in the string.

    Return the sorted string. If there are multiple answers, return any of them.

Example 1:
    Input: s = "tree"
    Output: "eert"
    Explanation: 'e' appears twice while 'r' and 't' both appear once.
    So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:
    Input: s = "cccaaa"
    Output: "aaaccc"
    Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
    Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:
    Input: s = "Aabb"
    Output: "bbAa"
    Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
    Note that 'A' and 'a' are treated as two different characters.

Constraints:
    1 <= s.length <= 5 * 10^5
    s consists of uppercase and lowercase English letters and digits.
"""


class Solution:
    def frequencySort(self, s: str) -> str:
        # exception case
        assert isinstance(s, str) and len(s) >= 1
        # main method: (record frequency counter and sort)
        return self._frequencySort(s)

    def _frequencySort(self, s: str) -> str:
        """
        Runtime: 44 ms, faster than 94.03% of Python3 online submissions for Sort Characters By Frequency.
        Memory Usage: 15.4 MB, less than 36.17% of Python3 online submissions for Sort Characters By Frequency.
        """
        freq_counter = dict({})
        for ch in s:
            if ch not in freq_counter:
                freq_counter[ch] = 1
            else:
                freq_counter[ch] += 1

        char_freq = list(freq_counter.items())
        char_freq.sort(key=lambda x: -x[1])

        res = ""
        for char, freq in char_freq:
            # res += "".join([char for _ in range(freq)])
            res += char * freq

        return res


def main():
    # Example 1: Output: "eert"
    s = "tree"

    # Example 2: Output: "aaaccc"
    # s = "cccaaa"

    # Example 3: Output: "bbAa"
    # s = "Aabb"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.frequencySort(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
