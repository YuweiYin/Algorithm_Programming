#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-INTERVIEW-1711-Find-Closest-LCCI.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-05-21
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - INTERVIEW-1711 - (Medium) - Find Closest LCCI
https://leetcode.cn/problems/find-closest-lcci/

Description & Requirement:
    You have a large text file containing words. Given any two different words, 
    find the shortest distance (in terms of number of words) between them in the file. 
    If the operation will be repeated many times for the same file (but different pairs of words), 
    can you optimize your solution?

Example:
    Input: words = ["I","am","a","student","from","a","university","in","a","city"], word1 = "a", word2 = "student"
    Output: 1

Note:
    words.length <= 100000
"""


class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        # exception case
        assert isinstance(words, list) and len(words) >= 1
        assert isinstance(word1, str) and isinstance(word2, str)
        for word in words:
            assert isinstance(word, str)
        # main method: (construct graph, BFS find the shortest path from word1 to word2)
        # method 2: one scan
        return self._findClosest(words, word1, word2)

    def _findClosestBFS(self, words: List[str], word1: str, word2: str) -> int:
        assert isinstance(words, list) and len(words) >= 1
        assert isinstance(word1, str) and isinstance(word2, str)
        len_words = len(words)

        if word1 == word2:
            return 0

        graph = dict({})
        for word in words:  # add nodes
            if word not in graph:
                graph[word] = set()

        if word1 not in graph or word2 not in graph:
            return -1

        for idx, word in enumerate(words):  # add edges
            if idx - 1 >= 0:
                graph[word].add(words[idx - 1])
            if idx + 1 < len_words:
                graph[word].add(words[idx + 1])

        bfs_queue = collections.deque()
        bfs_queue.append((word1, 0))  # (node, distance)
        visit_words = set()

        while len(bfs_queue) > 0:
            cur_word, cur_dist = bfs_queue.popleft()
            visit_words.add(cur_word)
            if cur_word == word2:
                return cur_dist
            for neighbor in graph[cur_word]:
                if neighbor not in visit_words:
                    visit_words.add(neighbor)
                    bfs_queue.append((neighbor, cur_dist + 1))

        return -1

    def _findClosest(self, words: List[str], word1: str, word2: str) -> int:
        assert isinstance(words, list) and len(words) >= 1
        assert isinstance(word1, str) and isinstance(word2, str)
        len_words = len(words)

        if word1 == word2:
            return 0

        res = len_words
        idx_1, idx_2 = -1, -1
        for idx, word in enumerate(words):
            if word == word1:
                idx_1 = idx
            elif word == word2:
                idx_2 = idx
            # calculate the current distance
            if idx_1 >= 0 and idx_2 >= 0:
                res = min(res, abs(idx_1 - idx_2))

        return res


def main():
    # Example: Output: 1
    words = ["I", "am", "a", "student", "from", "a", "university", "in", "a", "city"]
    word1 = "a"
    word2 = "student"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.findClosest(words, word1, word2)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
