#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1220-Count-Vowels-Permutation.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-17
=================================================================="""

import sys
import time
# from typing import List
import functools

"""
LeetCode - 1220 - (Hard) - Count Vowels Permutation
https://leetcode.com/problems/count-vowels-permutation/

Description & Requirement:
    Given an integer n, your task is to count how many strings of length n can be formed 
    under the following rules:
        Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
        Each vowel 'a' may only be followed by an 'e'.
        Each vowel 'e' may only be followed by an 'a' or an 'i'.
        Each vowel 'i' may not be followed by another 'i'.
        Each vowel 'o' may only be followed by an 'i' or a 'u'.
        Each vowel 'u' may only be followed by an 'a'.
        Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:
    Input: n = 1
    Output: 5
    Explanation: All possible strings are: "a", "e", "i" , "o" and "u".
Example 2:
    Input: n = 2
    Output: 10
    Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".
Example 3: 
    Input: n = 5
    Output: 68

Constraints:
    1 <= n <= 2 * 10^4
"""


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        # exception case
        if not isinstance(n, int) or n <= 0:
            return 0  # Error input type
        if n == 1:
            return 5
        # main method: (DFS, Dynamic Programming)
        #     value of dp[c][l] means the number of valid strings (with end char c) of length l
        #         c is in set C = {'a', 'e', 'i', 'o', 'u'}, l is a integer and starts from 1 to n
        #     dp equation: dp[c][l] = (if c == 'a') dp['e'][l-1] + dp['i'][l-1] + dp['u'][l-1]
        #                           = (if c == 'e') dp['a'][l-1] + dp['i'][l-1]
        #                           = (if c == 'i') dp['e'][l-1] + dp['o'][l-1]
        #                           = (if c == 'o') dp['i'][l-1]
        #                           = (if c == 'u') dp['i'][l-1] + dp['o'][l-1]
        #     dp target: \sum_{c \in C} dp[c][n]
        #     dp init: dp['a'][1] == 1, dp['e'][1] == 1, dp['i'][1] == 1, dp['o'][1] == 1, dp['u'][1] == 1
        #     explanation: 'a' can come from 'e'/'u'/'i', 'e' can come from 'a'/'i', 'i' can come from 'e'/'o'
        #         'o' can come from 'i', 'u' can come from 'i'/'o'
        # based on the dp equation (recurrence relation), fast matrix multiplication can be applied
        # return self._countVowelPermutationDFS(n)  # TTL
        return self._countVowelPermutationDP(n)

    def _countVowelPermutationDFS(self, n: int) -> int:
        assert n > 1
        sys.setrecursionlimit(200000)  # in this problem, n <= 20000

        @functools.lru_cache(maxsize=None)
        def __dfs(rest_n: int, former_vowel: str):
            if rest_n == 1:
                if former_vowel == 'a' or former_vowel == 'u':  # a -> e; u -> a
                    return 1
                elif former_vowel == 'e' or former_vowel == 'o':  # e -> a, i; o -> i, u
                    return 2
                elif former_vowel == 'i':  # i -> a, e, o, u
                    return 4
                else:
                    return 5  # only for the first char, no former vowel constraint

            if former_vowel == 'a':  # a -> e
                return __dfs(rest_n - 1, 'e')
            elif former_vowel == 'e':  # e -> a, i
                return __dfs(rest_n - 1, 'a') + __dfs(rest_n - 1, 'i')
            elif former_vowel == 'i':  # i -> a, e, o, u
                return __dfs(rest_n - 1, 'a') + __dfs(rest_n - 1, 'e') + __dfs(rest_n - 1, 'o') + __dfs(rest_n - 1, 'u')
            elif former_vowel == 'o':  # o -> i, u
                return __dfs(rest_n - 1, 'i') + __dfs(rest_n - 1, 'u')
            elif former_vowel == 'u':  # u -> a
                return __dfs(rest_n - 1, 'a')
            else:  # only for the first char, no former vowel constraint
                return __dfs(rest_n - 1, 'a') + __dfs(rest_n - 1, 'e') + __dfs(rest_n - 1, 'i') + __dfs(rest_n - 1, 'o') + __dfs(rest_n - 1, 'u')

        res = __dfs(n, '')
        return res

    def _countVowelPermutationDP(self, n: int) -> int:
        """
        Runtime: 130 ms, faster than 89.96% of Python3 online submissions for Count Vowels Permutation.
        Memory Usage: 14.3 MB, less than 85.71% of Python3 online submissions for Count Vowels Permutation.
        """
        assert n > 1

        MOD = 1e9+7  # 1e9+7 or 1e9+9 or 998244353 (7 * 17 * 2^23 + 1)

        dp = tuple([1, 1, 1, 1, 1])  # the index set of char set C = {'a', 'e', 'i', 'o', 'u'} is {0, 1, 2, 3, 4}
        # storage compression: don't need the intermediate results, so just use one-dim list/tuple to store results
        cur_length = 1
        while cur_length < n:
            dp = (
                (dp[1] + dp[2] + dp[4]) % MOD,  # 'a' can come from 'e'/'u'/'i'
                (dp[0] + dp[2]) % MOD,  # 'e' can come from 'a'/'i'
                (dp[1] + dp[3]) % MOD,  # 'i' can come from 'e'/'o'
                dp[2] % MOD,  # 'o' can come from 'i'
                (dp[2] + dp[3]) % MOD  # 'u' can come from 'i'/'o'
            )
            cur_length += 1

        return int(sum(dp) % MOD)  # dp target: \sum_{c \in C} dp[c][n]


def main():
    # Example 1: Output: 5
    # n = 1

    # Example 2: Output: 10
    # n = 2

    # Example 3: Output: 68
    # n = 5

    # Example 3: Output: 759959057
    n = 20000

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.countVowelPermutation(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
