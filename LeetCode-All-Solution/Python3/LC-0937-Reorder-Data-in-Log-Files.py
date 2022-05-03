#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0937-Reorder-Data-in-Log-Files.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-05-03
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0937 - (Easy) - Reorder Data in Log Files
https://leetcode.com/problems/reorder-data-in-log-files/

Description & Requirement:
    You are given an array of logs. Each log is a space-delimited string of words, 
    where the first word is the identifier.

    There are two types of logs:
        Letter-logs: All words (except the identifier) consist of lowercase English letters.
        Digit-logs: All words (except the identifier) consist of digits.

    Reorder these logs so that:
        The letter-logs come before all digit-logs.
        The letter-logs are sorted lexicographically by their contents. 
            If their contents are the same, then sort them lexicographically by their identifiers.
        The digit-logs maintain their relative ordering.

    Return the final order of the logs.

Example 1:
    Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
    Explanation:
        The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
        The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".
Example 2:
    Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
    Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]

Constraints:
    1 <= logs.length <= 100
    3 <= logs[i].length <= 100
    All the tokens of logs[i] are separated by a single space.
    logs[i] is guaranteed to have an identifier and at least one word after the identifier.
"""


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # exception case
        assert isinstance(logs, list) and len(logs) >= 1
        # main method: (record the index of digit-logs, sort letter-logs, and then merge them)
        return self._reorderLogFiles(logs)

    def _reorderLogFiles(self, logs: List[str]) -> List[str]:
        assert isinstance(logs, list) and len(logs) >= 1
        len_logs = len(logs)
        if len_logs == 1:
            return logs

        # record the index of digit-logs
        # digit_logs_set = set()
        digit_logs_list = []
        letter_logs = []
        for idx, log in enumerate(logs):
            assert isinstance(log, str) and len(log) >= 3
            log_list = log.strip().split()
            if len(log_list) >= 2:
                if log_list[1].isdigit():
                    # digit_logs_set.add(idx)
                    digit_logs_list.append(log)
                else:
                    letter_logs.append([log_list[0], " ".join(log_list[1:])])

        # sort letter-logs
        letter_logs.sort(key=lambda x: (x[1], x[0]))
        letter_logs = [" ".join(l_l) for l_l in letter_logs]

        # merge them
        letter_logs.extend(digit_logs_list)

        return letter_logs


def main():
    # Example 1: Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
    logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]

    # Example 2: Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
    # logs = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.reorderLogFiles(logs)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
