#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0212-Word-Search-II.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-11-05
=================================================================="""

import sys
import time
from typing import List
from collections import defaultdict
# import functools

"""
LeetCode - 0212 - (Hard) - Word Search II
https://leetcode.com/problems/word-search-ii/

Description & Requirement:
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example 1:
    Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
    Output: ["eat","oath"]
Example 2:
    Input: board = [["a","b"],["c","d"]], words = ["abcb"]
    Output: []

Constraints:
    m == board.length
    n == board[i].length
    1 <= m, n <= 12
    board[i][j] is a lowercase English letter.
    1 <= words.length <= 3 * 10^4
    1 <= words[i].length <= 10
    words[i] consists of lowercase English letters.
    All the strings of words are unique.
"""


class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.word = ""

    def insert(self, word):
        cur = self
        for c in word:
            cur = cur.children[c]
        cur.is_word = True
        cur.word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # exception case
        assert isinstance(board, list) and len(board) >= 1
        for b in board:
            assert isinstance(b, list) and len(b) >= 1
        assert isinstance(words, list) and len(words) >= 1
        for word in words:
            assert isinstance(word, str) and len(word) >= 1
        # main method: (Trie + DFS & backtrace from each possible start point)
        return self._findWords(board, words)

    def _findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        Runtime: 1084 ms, faster than 92.06% of Python3 online submissions for Word Search II.
        Memory Usage: 16.4 MB, less than 37.50% of Python3 online submissions for Word Search II.
        """
        assert isinstance(board, list) and len(board) >= 1
        assert isinstance(words, list) and len(words) >= 1
        m, n = len(board), len(board[0])

        trie = Trie()
        for word in words:
            trie.insert(word)

        def dfs(now, i1, j1):
            if board[i1][j1] not in now.children:
                return

            ch = board[i1][j1]

            nxt = now.children[ch]
            if nxt.word != "":
                res.append(nxt.word)
                nxt.word = ""

            if nxt.children:
                board[i1][j1] = "#"
                for i2, j2 in [(i1 + 1, j1), (i1 - 1, j1), (i1, j1 + 1), (i1, j1 - 1)]:
                    if 0 <= i2 < m and 0 <= j2 < n:
                        dfs(nxt, i2, j2)
                board[i1][j1] = ch

            if not nxt.children:
                now.children.pop(ch)

        res = []
        for i in range(m):
            for j in range(n):
                dfs(trie, i, j)

        return res

    def _findWords_slow(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        TLE
        """
        assert isinstance(board, list) and len(board) >= 1
        assert isinstance(words, list) and len(words) >= 1
        m, n = len(board), len(board[0])

        trie = Trie()
        for word in words:
            trie.insert(word)

        def __dfs(now, i1, j1):
            if board[i1][j1] not in now.children:
                return

            ch = board[i1][j1]

            now = now.children[ch]
            if now.word != "":
                res.add(now.word)

            board[i1][j1] = "#"
            for i2, j2 in [(i1 + 1, j1), (i1 - 1, j1), (i1, j1 + 1), (i1, j1 - 1)]:
                if 0 <= i2 < m and 0 <= j2 < n:
                    __dfs(now, i2, j2)
            board[i1][j1] = ch

        res = set()
        m, n = len(board), len(board[0])

        start_ch = set()
        for word in words:
            start_ch.add(word[0])

        for i in range(m):
            for j in range(n):
                if board[i][j] in start_ch:
                    __dfs(trie, i, j)

        return list(res)


def main():
    # Example 1: Output: ["eat","oath"]
    board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
    words = ["oath", "pea", "eat", "rain"]

    # Example 2: Output: []
    # board = [["a", "b"], ["c", "d"]]
    # words = ["abcb"]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.findWords(board, words)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
