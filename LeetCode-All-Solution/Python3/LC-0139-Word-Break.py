#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0139-Word-Break.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-28
=================================================================="""

import sys
import time
from typing import List
# import collections

"""
LeetCode - 0139 - (Medium) - Word Break
https://leetcode.com/problems/word-break/

Description & Requirement:
    Given a string s and a dictionary of strings wordDict, 
    return true if s can be segmented into a space-separated sequence of one or more dictionary words.

    Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
    Input: s = "leetcode", wordDict = ["leet","code"]
    Output: true
    Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:
    Input: s = "applepenapple", wordDict = ["apple","pen"]
    Output: true
    Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
        Note that you are allowed to reuse a dictionary word.
Example 3:
    Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
    Output: false

Constraints:
    1 <= s.length <= 300
    1 <= wordDict.length <= 1000
    1 <= wordDict[i].length <= 20
    s and wordDict[i] consist of only lowercase English letters.
    All the strings of wordDict are unique.
"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # exception case
        if not isinstance(s, str) or len(s) <= 0:
            return False  # Error input type
        if not isinstance(wordDict, list) or len(wordDict) <= 0:
            return False  # Error input type
        if len(s) == 1:
            return True if s in wordDict else False
        # main method: (Dynamic Programming: dp[i] is True means s[0: i+1] can be segmented validly)
        #     dp equation: dp[i] = dp[j] and valid(s[j+1: i]), where j = 0, 1, ..., i-1, valid function is dict map
        #     dp init: dp[0] == True, which means "" is valid
        #     dp aim: get dp[-1]
        return self._wordBreak(s, wordDict)

    def _wordBreak(self, s: str, wordDict: List[str]) -> bool:
        len_s = len(s)
        len_w_dict = len(wordDict)
        assert len_s >= 2 and len_w_dict >= 1

        word_set = set(wordDict)
        dp = [False for _ in range(len_s + 1)]  # dp[i] is True means s[0: i+1] can be segmented validly
        dp[0] = True  # dp[0] == True, which means "" is valid

        for cur_index in range(1, len_s + 1):  # cur_index: i
            for seg_index in range(0, cur_index):  # seg_index: j, to consider each partition of s[0: cur_index + 1]
                if dp[seg_index] and s[seg_index: cur_index] in word_set:  # dp[i] = dp[j] and valid(s[j+1: i])
                    dp[cur_index] = True
                    break  # break inner loop, consider the next cur_index

        return dp[-1]


def main():
    # Example 1: Output: true
    # s = "leetcode"
    # wordDict = ["leet", "code"]

    # Example 2: Output: true
    # s = "applepenapple"
    # wordDict = ["apple", "pen"]

    # Example 3: Output: false
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.wordBreak(s, wordDict)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
