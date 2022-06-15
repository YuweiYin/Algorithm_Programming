#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1048-Longest-String-Chain.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-06-15
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 1048 - (Medium) - Longest String Chain
https://leetcode.com/problems/longest-string-chain/

Description & Requirement:
    You are given an array of words where each word consists of lowercase English letters.

    wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA 
    without changing the order of the other characters to make it equal to wordB.

    For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
    A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, 
    word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.

    Return the length of the longest possible word chain with words chosen from the given list of words.

Example 1:
    Input: words = ["a","b","ba","bca","bda","bdca"]
    Output: 4
    Explanation: One of the longest word chains is ["a","ba","bda","bdca"].
Example 2:
    Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
    Output: 5
    Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].
Example 3:
    Input: words = ["abcd","dbqca"]
    Output: 1
    Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
    ["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.

Constraints:
    1 <= words.length <= 1000
    1 <= words[i].length <= 16
    words[i] only consists of lowercase English letters.
"""


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # exception case
        assert isinstance(words, list) and len(words) >= 1
        for word in words:
            assert isinstance(word, str) and len(word) >= 1
        # main method: (construct graph, BFS find the longest path)
        # return self._longestStrChain(words)
        # method: sort and dynamic programming
        return self._longestStrChainDP(words)

    def _longestStrChainDP(self, words: List[str]) -> int:
        assert isinstance(words, list) and len(words) >= 1

        def __check_path(x, y):
            m, n = len(x), len(y)
            if m + 1 != n:
                return False
            i, j = 0, 0
            while i < m and j < n:
                if x[i] == y[j]:
                    i += 1
                j += 1
            return i == len(x)

        words.sort(key=lambda x: len(x))
        dp = [1 for _ in range(len(words))]  # dp[i] is the length of the longest path that ends with words[i]

        res = 0
        for end_idx in range(len(words)):
            for start_idx in range(end_idx):
                if __check_path(words[start_idx], words[end_idx]):
                    dp[end_idx] = max(dp[end_idx], dp[start_idx] + 1)
            res = max(res, dp[end_idx])

        return res

    def _longestStrChain(self, words: List[str]) -> int:
        assert isinstance(words, list) and len(words) >= 1
        n = len(words)

        graph = dict({})  # key: word; value: to-neighbor list
        length_words = dict({})  # key: length; value: words of this length
        for word in words:
            graph[word] = []
            if len(word) not in length_words:
                length_words[len(word)] = [word]
            else:
                length_words[len(word)].append(word)

        length_list = []
        for length, word_list in length_words.items():
            length_list.append(length)

        length_list.sort()
        for length_idx in range(len(length_list) - 1):
            cur_length = length_list[length_idx]
            next_length = length_list[length_idx + 1]
            if cur_length + 1 == next_length:
                for cur_word in length_words[cur_length]:
                    for next_word in length_words[next_length]:
                        for ch_idx in range(len(next_word)):
                            if next_word[:ch_idx] + next_word[ch_idx + 1:] == cur_word:
                                graph[cur_word].append(next_word)  # set link
                                # graph[next_word].append(cur_word)
                                break
            else:
                pass

        res = 1
        visited_words = set()
        while len(visited_words) < n:  # since the graph is probably not connected, so make sure every word is visited
            bfs_queue = collections.deque()
            for length in length_list:
                cur_word_list = length_words[length]
                for word in cur_word_list:
                    if word not in visited_words:
                        visited_words.add(word)
                        bfs_queue.append((word, 1))  # (word, path_length)
                if len(bfs_queue) > 0:
                    break

            while len(bfs_queue) > 0:
                cur_word, path_len = bfs_queue.popleft()
                res = max(res, path_len)
                for next_word in graph[cur_word]:
                    if next_word not in visited_words:
                        visited_words.add(next_word)
                        bfs_queue.append((next_word, path_len + 1))

        return res


def main():
    # Example 1: Output: 4
    # words = ["a", "b", "ba", "bca", "bda", "bdca"]

    # Example 2: Output: 5
    # words = ["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]

    # Example 3: Output: 1
    words = ["abcd", "dbqca"]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.longestStrChain(words)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
