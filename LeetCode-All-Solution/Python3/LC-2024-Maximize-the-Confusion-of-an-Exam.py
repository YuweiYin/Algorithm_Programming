#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2024-Maximize-the-Confusion-of-an-Exam.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-29
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 2024 - (Medium) - Maximize the Confusion of an Exam
https://leetcode.com/problems/maximize-the-confusion-of-an-exam/

Description & Requirement:
    A teacher is writing a test with n true/false questions, with 'T' denoting true and 'F' denoting false. 
    He wants to confuse the students by maximizing the number of consecutive questions with the same answer 
    (multiple trues or multiple falses in a row).

    You are given a string answerKey, where answerKey[i] is the original answer to the ith question. 
    In addition, you are given an integer k, the maximum number of times you may perform the following operation:
        Change the answer key for any question to 'T' or 'F' (i.e., set answerKey[i] to 'T' or 'F').

    Return the maximum number of consecutive 'T's or 'F's in the answer key 
    after performing the operation at most k times.

Example 1:
    Input: answerKey = "TTFF", k = 2
    Output: 4
    Explanation: We can replace both the 'F's with 'T's to make answerKey = "TTTT".
        There are four consecutive 'T's.
Example 2:
    Input: answerKey = "TFFT", k = 1
    Output: 3
    Explanation: We can replace the first 'T' with an 'F' to make answerKey = "FFFT".
        Alternatively, we can replace the second 'T' with an 'F' to make answerKey = "TFFF".
        In both cases, there are three consecutive 'F's.
Example 3:
    Input: answerKey = "TTFTTFTT", k = 1
    Output: 5
    Explanation: We can replace the first 'F' to make answerKey = "TTTTTFTT"
        Alternatively, we can replace the second 'F' to make answerKey = "TTFTTTTT". 
        In both cases, there are five consecutive 'T's.

Constraints:
    n == answerKey.length
    1 <= n <= 5 * 10^4
    answerKey[i] is either 'T' or 'F'
    1 <= k <= n

Related Problem:
    LC-1004-Max-Consecutive-Ones-III
"""


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        # exception case
        assert isinstance(answerKey, str) and len(answerKey) >= 1
        assert isinstance(k, int) and 1 <= k <= len(answerKey)
        # main method: (slide window, separately deal with "T" and "F")
        return self._maxConsecutiveAnswers(answerKey, k)

    def _maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def __max_consecutive(target: str) -> int:
            res = 0
            window_start = 0  # guarantee all answers in the window is the target (if not, use operation to change)
            k_counter = 0  # how many operations have used
            for window_end in range(len(answerKey)):
                if answerKey[window_end] != target:  # new window end is not the target answer, so use an operation
                    k_counter += 1
                while k_counter > k:  # out of limit of k operations
                    if answerKey[window_start] != target:
                        # this means to convert answerKey[window_start] to target, one operation was used
                        k_counter -= 1  # recover it
                    window_start += 1
                res = max(res, window_end - window_start + 1)
            return res

        return max(__max_consecutive("T"), __max_consecutive("F"))


def main():
    # Example 1: Output: 4
    # answerKey = "TTFF"
    # k = 2

    # Example 2: Output: 3
    # answerKey = "TFFT"
    # k = 1

    # Example 3: Output: 5
    answerKey = "TTFTTFTT"
    k = 1

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maxConsecutiveAnswers(answerKey, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
