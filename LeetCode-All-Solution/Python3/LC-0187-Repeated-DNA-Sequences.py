#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0187-Repeated-DNA-Sequences.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-19
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0187 - (Medium) - Repeated DNA Sequences
https://leetcode.com/problems/repeated-dna-sequences/

Description & Requirement:
    The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

    For example, "ACGAATTCCG" is a DNA sequence.
        When studying DNA, it is useful to identify repeated sequences within the DNA.
    
        Given a string s that represents a DNA sequence, 
        return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. 
        You may return the answer in any order.

Example 1:
    Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    Output: ["AAAAACCCCC","CCCCCAAAAA"]
Example 2:
    Input: s = "AAAAAAAAAAAAA"
    Output: ["AAAAAAAAAA"]

Constraints:
    1 <= s.length <= 10^5
    s[i] is either 'A', 'C', 'G', or 'T'.
"""


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # exception case
        assert isinstance(s, str) and len(s) > 0
        # main method: (hash set record appeared substr that len(substr) == 10)
        return self._findRepeatedDnaSequences(s)

    def _findRepeatedDnaSequences(self, s: str) -> List[str]:
        len_s = len(s)
        assert len_s > 0

        res = set()
        sub_str = set()

        left_idx = 0
        right_idx = 10
        while right_idx <= len_s:
            cur_s = s[left_idx: right_idx]
            if cur_s not in sub_str:
                sub_str.add(cur_s)
            else:  # now, cur_s appears at least twice
                if cur_s not in res:
                    res.add(cur_s)
            left_idx += 1
            right_idx += 1

        return list(res)


def main():
    # Example 1: Output: ["AAAAACCCCC","CCCCCAAAAA"]
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

    # Example 2: Output: ["AAAAAAAAAA"]
    # s = "AAAAAAAAAAAAA"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.findRepeatedDnaSequences(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
