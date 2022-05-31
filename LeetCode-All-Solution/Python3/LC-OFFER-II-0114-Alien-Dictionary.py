#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-OFFER-II-0114-Alien-Dictionary.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-05-31
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - OFFER II 0114 - (Hard) Alien Dictionary
https://leetcode.cn/problems/Jf1JuT/

Description & Requirement:
    现有一种使用英语字母的外星文语言，这门语言的字母顺序与英语顺序不同。

    给定一个字符串列表 words ，作为这门语言的词典，words 中的字符串已经 按这门新语言的字母顺序进行了排序 。

    请你根据该词典还原出此语言中已知的字母顺序，并 按字母递增顺序 排列。若不存在合法字母顺序，返回 "" 。
    若存在多种可能的合法字母顺序，返回其中 任意一种 顺序即可。

    字符串 s 字典顺序小于 字符串 t 有两种情况：
        在第一个不同字母处，如果 s 中的字母在这门外星语言的字母顺序中位于 t 中字母之前，那么 s 的字典顺序小于 t 。
        如果前面 min(s.length, t.length) 字母都相同，那么 s.length < t.length 时，s 的字典顺序也小于 t 。

Example 1：
    Input: words = ["wrt","wrf","er","ett","rftt"]
    Output: "wertf"
Example 2：
    Input: words = ["z","x"]
    Output: "zx"
Example 3：
    Input: words = ["z","x","z"]
    Output: ""
    Explanation: 不存在合法字母顺序，因此返回 "" 。

Constrains:
    1 <= words.length <= 100
    1 <= words[i].length <= 100
    words[i] 仅由小写英文字母组成

Note:
    本题与主站 269 题相同: https://leetcode-cn.com/problems/alien-dictionary/
"""


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # exception case
        assert isinstance(words, list) and len(words) >= 1
        for word in words:
            assert isinstance(word, str) and len(word) > 0 and word.islower()
        # main method: (Topological sorting + DFS/BFS check loop)
        return self._alienOrder(words)

    def _alienOrder(self, words: List[str]) -> str:
        assert isinstance(words, list) and len(words) >= 1
        n = len(words)

        graph = dict({})  # key: char; value: to list
        in_degree = dict({})
        for ch in words[0]:
            in_degree[ch] = 0

        for idx in range(1, n):
            _from, _to = words[idx - 1], words[idx]
            for ch in _to:
                if ch not in in_degree:
                    in_degree[ch] = 0
            for ch_from, ch_to in zip(_from, _to):
                if ch_from != ch_to:
                    if ch_from not in graph:
                        graph[ch_from] = [ch_to]
                    else:
                        graph[ch_from].append(ch_to)
                    in_degree[ch_to] += 1
                    break  # only deal with the first different char
            else:  # end loop without break
                if len(_from) > len(_to):
                    return ""

        # BFS start from nodes that in_degree == 0
        bfs_queue = collections.deque()
        visit_list = []
        for ch, degree in in_degree.items():
            if degree == 0:
                bfs_queue.append(ch)
                visit_list.append(ch)
        while len(bfs_queue) > 0:
            cur_node = bfs_queue.popleft()
            if cur_node not in graph:
                continue
            for to_node in graph[cur_node]:
                in_degree[to_node] -= 1
                if in_degree[to_node] == 0:
                    bfs_queue.append(to_node)
                    visit_list.append(to_node)

        return "".join(visit_list) if len(visit_list) == len(in_degree) else ""

        # bfs_queue = [ch for ch, degree in in_degree.items() if degree == 0]
        # for cur_node in bfs_queue:
        #     if cur_node not in graph:
        #         continue
        #     for to_node in graph[cur_node]:
        #         in_degree[to_node] -= 1
        #         if in_degree[to_node] == 0:
        #             bfs_queue.append(to_node)
        #
        # return "".join(bfs_queue) if len(bfs_queue) == len(in_degree) else ""


def main():
    # Example 1： Output: "wertf"
    words = ["wrt", "wrf", "er", "ett", "rftt"]

    # Example 2： Output: "zx"
    # words = ["z", "x"]

    # Example 3： Output: ""
    # words = ["z", "x", "z"]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.alienOrder(words)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
