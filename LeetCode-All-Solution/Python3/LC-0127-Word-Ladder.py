#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0127-Word-Ladder.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-12
=================================================================="""

import sys
import time
from typing import List
# import collections

"""
LeetCode - 0127 - (Hard) - Word Ladder
https://leetcode.com/problems/word-ladder/

Description & Requirement:
    A transformation sequence from word beginWord to word endWord 
    using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
        Every adjacent pair of words differs by a single letter.
        Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
        sk == endWord

    Given two words, beginWord and endWord, and a dictionary wordList, 
    return the number of words in the shortest transformation sequence from beginWord to endWord, 
        or 0 if no such sequence exists.

Example 1:
    Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
    Output: 5
    Explanation: One shortest transformation sequence is 
        "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:
    Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
    Output: 0
    Explanation: The endWord "cog" is not in wordList, 
        therefore there is no valid transformation sequence.

Constraints:
    1 <= beginWord.length <= 10
    endWord.length == beginWord.length
    1 <= wordList.length <= 5000
    wordList[i].length == beginWord.length
    beginWord, endWord, and wordList[i] consist of lowercase English letters.
    beginWord != endWord
    All the words in wordList are unique.
"""


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # exception case
        if not isinstance(beginWord, str) or len(beginWord) <= 0 or not beginWord.isalpha():
            return 0  # Error input type
        if not isinstance(endWord, str) or len(endWord) <= 0 or not endWord.isalpha():
            return 0  # Error input type
        if not isinstance(wordList, list) or len(wordList) <= 0 or endWord not in wordList:
            return 0  # Error input type
        if beginWord == endWord:
            return 0
        # main method: (construct graph and perform single-source BFS to find the shortest path)
        #     TODO: optimize: from beginWord and endWord, bi-source BFS, if both searched a node, stop.
        # return self._ladderLength(beginWord, endWord, wordList)
        return self._ladderLengthOptimize(beginWord, endWord, wordList)

    def _ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        len_beginWord = len(beginWord)
        assert len(wordList) >= 1 and len_beginWord == len(endWord)

        # construct graph dict: key: word; value: to-word set.
        word_dict = dict({})
        wordList.append(beginWord)  # integrate beginWord into graph as starting point
        for word in wordList:
            # clear wordList, only remain len == len_beginWord
            if len(word) == len_beginWord and word not in word_dict:
                word_dict[word] = set()

        wordList = list(word_dict.keys())

        for word in wordList:  # O(len_beginWord * len_wordList * len_wordList) TODO: bottleneck
            for to_word in wordList:
                if to_word == word:
                    continue  # no self loop
                # check if to_word and word only diff in one char
                # assert len(word) == len(to_word) == len_beginWord
                diff_counter = 0
                can_link = True
                for char_index in range(len_beginWord):
                    if word[char_index] != to_word[char_index]:
                        diff_counter += 1
                        if diff_counter > 1:
                            can_link = False
                            break
                if can_link:
                    word_dict[word].add(to_word)

        # perform single-source BFS to find the shortest path
        # flood fill, each step consider all possible next to-word
        bfs_queue = set()
        bfs_queue.add(beginWord)
        distance_counter = 0
        max_distance = len(wordList) + 1  # if reach this distance, it means can't find a path to engWord
        can_find = False
        bfs_visited = {word: False for word in wordList}  # avoid repeated bfs
        while len(bfs_queue) > 0:
            # print(bfs_queue)
            distance_counter += 1
            if distance_counter == max_distance:
                return 0
            next_bfs_queue = set()
            for from_word in bfs_queue:  # from all start-word
                bfs_visited[from_word] = True
                for to_word in word_dict[from_word]:  # to all linked to-word
                    if bfs_visited[to_word]:  # avoid repeated bfs
                        continue
                    if to_word == endWord:  # find the end
                        # can_find = True
                        return distance_counter + 1  # plus 1 because the implicit extra jump
                    else:
                        if to_word not in next_bfs_queue:
                            next_bfs_queue.add(to_word)
            bfs_queue = next_bfs_queue

        return distance_counter if can_find else 0

    def _ladderLengthOptimize(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        len_beginWord = len(beginWord)
        assert len(wordList) >= 1 and len_beginWord == len(endWord)

        # construct graph dict: key: word; value: to-word set.
        word_dict = dict({})
        wordList.append(beginWord)  # integrate beginWord into graph as starting point
        for word in wordList:
            # clear wordList, only remain len == len_beginWord
            if len(word) == len_beginWord and word not in word_dict:
                word_dict[word] = set()

        wordList = list(word_dict.keys())

        for word_index in range(len(wordList)):  # O(len_beginWord * len_wordList)
            # optimize: for word "hit", store link "hit"-"*it", "hit"-"h*t", and "hit"-"hi*"
            # each bfs step, say, from "hit" to "hot" will take 2 steps: "hit" -> "h*t" -> "hot"
            # so the final result should be divided by 2
            word = wordList[word_index]
            for convert_index in range(len(word)):
                word_split = list(word)
                word_split[convert_index] = "*"
                convert_word = "".join(word_split)
                word_dict[word].add(convert_word)  # link: word -> convert_word
                if convert_word not in word_dict:  # link: convert_word -> word
                    word_dict[convert_word] = {word}
                    wordList.append(convert_word)
                else:
                    if word not in word_dict[convert_word]:
                        word_dict[convert_word].add(word)

        # perform single-source BFS to find the shortest path
        # flood fill, each step consider all possible next to-word
        bfs_queue = set()
        bfs_queue.add(beginWord)
        distance_counter = 0
        max_distance = len(wordList) + 1  # if reach this distance, it means can't find a path to engWord
        can_find = False
        bfs_visited = {word: False for word in wordList}  # avoid repeated bfs
        while len(bfs_queue) > 0:
            # print(bfs_queue)
            distance_counter += 1
            if distance_counter == max_distance:
                return 0
            next_bfs_queue = set()
            for from_word in bfs_queue:  # from all start-word
                bfs_visited[from_word] = True
                for to_word in word_dict[from_word]:  # to all linked to-word
                    if bfs_visited[to_word]:  # avoid repeated bfs
                        continue
                    if to_word == endWord:  # find the end
                        # can_find = True
                        # each bfs step, say, from "hit" to "hot" will take 2 steps: "hit" -> "h*t" -> "hot"
                        # so the final result should be divided by 2
                        return (distance_counter >> 1) + 1
                    else:
                        if to_word not in next_bfs_queue:
                            next_bfs_queue.add(to_word)
            bfs_queue = next_bfs_queue

        return distance_counter if can_find else 0


def main():
    # Example 1: Output: 5
    #     Explanation: "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

    # Example 2: Output: 0
    # beginWord = "hit"
    # endWord = "cog"
    # wordList = ["hot", "dot", "dog", "lot", "log"]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.ladderLength(beginWord, endWord, wordList)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
