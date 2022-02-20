#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0516-Longest-Palindromic-Subsequence.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-20
=================================================================="""

import sys
import time
# from typing import List
# import collections

"""
LeetCode - 0516 - (Medium) - Longest Palindromic Subsequence
https://leetcode.com/problems/longest-palindromic-subsequence/

Description & Requirement:
    Given a string s, find the longest palindromic subsequence's length in s.

    A subsequence is a sequence that can be derived from another sequence 
    by deleting some or no elements without changing the order of the remaining elements.

Example 1:
    Input: s = "bbbab"
    Output: 4
    Explanation: One possible longest palindromic subsequence is "bbbb".
Example 2:
    Input: s = "cbbd"
    Output: 2
    Explanation: One possible longest palindromic subsequence is "bb".

Constraints:
    1 <= s.length <= 1000
    s consists only of lowercase English letters.

Related Problem:
    LC-0005-Longest-Palindromic-Substring
"""


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # exception case
        if not isinstance(s, str) or len(s) <= 0:
            return 0  # Error input type
        if len(s) == 1:
            return 1  # s itself is a palindrome
        if len(s) == 2:
            return 2 if s[0] == s[1] else 1
        # main method: (1. DFS; 2. DP.)
        # return self._longestPalindromeSubseqDfs(s)  # DFS, TLE
        #     dp[i][j] is the max len of palin subseq using chars s[i: j+1]
        #     dp equation: dp[i][j] = dp[i+1][j-1] + 2  if s[i] == s[j]
        #                  dp[i][j] = max(dp[i+1][j], dp[i][j-1])  if s[i] != s[j]
        #     dp init: dp[i][i] = 1, dp[i][i+1] == 2 if s[i] == s[i+1] else 1
        #     dp aim: get dp[0][-1]
        #     note that DP start from small intervals, otherwise it's the same as `_longestPalindromeSubseqDfs`
        return self._longestPalindromeSubseqDp(s)  # DP

    def _longestPalindromeSubseqDfs(self, s: str) -> int:
        """
        DFS: from both ends, greedily find palin pairs. (TLE)
        """
        len_s = len(s)
        assert len_s >= 3

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

        longest_subseq = __dp_dfs(0, len_s - 1)
        return len(longest_subseq)

    def _longestPalindromeSubseqDp(self, s: str) -> int:
        len_s = len(s)
        assert len_s >= 3

        # dp[i][j] is the max len of palin subseq using chars s[i: j+1]
        dp = [[0 for _ in range(len_s)] for _ in range(len_s)]

        # dp init: dp[i][i] = 1, dp[i][i+1] == 2 if s[i] == s[i+1] else 1
        for idx in range(len_s):
            dp[idx][idx] = 1
        for idx in range(len_s - 1):
            if s[idx] == s[idx + 1]:
                dp[idx][idx + 1] = 2
            else:
                dp[idx][idx + 1] = 1

        # dp equation: dp[i][j] = dp[i+1][j-1] + 2  if s[i] == s[j]
        #              dp[i][j] = max(dp[i+1][j], dp[i][j-1])  if s[i] != s[j]
        # first interval s[-1][-1], then s[-2][-2] and s[-2][-1], and so on
        #     when start_idx == 0, all the needed sub intervals have been calculated and stored in dp[1][j]
        for start_idx in reversed(range(len_s)):
            for end_idx in range(start_idx + 2, len_s):
                if s[start_idx] == s[end_idx]:
                    dp[start_idx][end_idx] = dp[start_idx + 1][end_idx - 1] + 2
                else:
                    dp[start_idx][end_idx] = max(dp[start_idx + 1][end_idx], dp[start_idx][end_idx - 1])

        return dp[0][-1]


def main():
    # Example 1: Output: 4
    # s = "bbbab"

    # Example 2: Output: 2
    # s = "cbbd"

    # Example 3: Output: 159
    s = "euazbipzncptldueeuechubrcourfpftcebikrxhybkymimgvldiwqvkszfycvqyvtiwfckexmowcxztkfyzqovbtmzpxoj" \
        "fofbvwnncajvrvdbvjhcrameamcfmcoxryjukhpljwszknhiypvyskmsujkuggpztltpgoczafmfelahqwjbhxtjmebnymd" \
        "yxoeodqmvkxittxjnlltmoobsgzdfhismogqfpfhvqnxeuosjqqalvwhsidgiavcatjjgeztrjuoixxxoznklcxolgpukti" \
        "rmduxdywwlbikaqkqajzbsjvdgjcnbtfksqhquiwnwflkldgdrqrnwmshdpykicozfowmumzeuznolmgjlltypyufpzjpuv" \
        "ucmesnnrwppheizkapovoloneaxpfinaontwtdqsdvzmqlgkdxlbeguackbdkftzbnynmcejtwudocemcfnuzbttcoew"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.longestPalindromeSubseq(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
