#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0126-Word-Ladder-II.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-08-14
=================================================================="""

import sys
import time
from typing import List
import collections

"""
LeetCode - 0126 - (Hard) - Word Ladder II
https://leetcode.com/problems/word-ladder-ii/

Description & Requirement:
    A transformation sequence from word beginWord to word endWord using a dictionary wordList 
    is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
        Every adjacent pair of words differs by a single letter.
        Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
        sk == endWord

    Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].

Example 1:
    Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
    Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
    Explanation: There are 2 shortest transformation sequences:
        "hit" -> "hot" -> "dot" -> "dog" -> "cog"
        "hit" -> "hot" -> "lot" -> "log" -> "cog"
Example 2:
    Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
    Output: []
    Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

Constraints:
    1 <= beginWord.length <= 5
    endWord.length == beginWord.length
    1 <= wordList.length <= 500
    wordList[i].length == beginWord.length
    beginWord, endWord, and wordList[i] consist of lowercase English letters.
    beginWord != endWord
    All the words in wordList are unique.
"""


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # exception case
        if not isinstance(beginWord, str) or len(beginWord) <= 0 or not beginWord.isalpha():
            return []  # Error input type
        if not isinstance(endWord, str) or len(endWord) <= 0 or not endWord.isalpha():
            return []  # Error input type
        if not isinstance(wordList, list) or len(wordList) <= 0 or endWord not in wordList:
            return []  # Error input type
        if beginWord == endWord:
            return []
        if endWord not in wordList:
            return []
        # main method: (construct graph and perform bi-source BFS to find the shortest path)
        # return self._findLadders(beginWord, endWord, wordList)
        return self._findLadders_TLE1(beginWord, endWord, wordList)

    def _findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)
        if endWord not in wordList:
            return []

        # BFS visit
        cur_level = {beginWord}
        parents = collections.defaultdict(list)
        while cur_level:
            wordList -= cur_level
            next_level = set()
            for word in cur_level:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + c + word[i + 1:]
                        if new_word in wordList:
                            next_level.add(new_word)
                            parents[new_word].append(word)
            if endWord in next_level:
                break
            cur_level = next_level

        # DFS reconstruction
        res = []

        def __dfs(word, path):
            if word == beginWord:
                path.append(word)
                res.append(path[::-1])
            else:
                for p_word in parents[word]:
                    __dfs(p_word, path + [word])

        __dfs(endWord, [])
        return res

    def _findLadders_TLE1(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []

        hash_dict = collections.defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                hash_dict[word[:i] + "*" + word[i + 1:]].append(word)

        def __edges(_word: str):
            for i in range(len(_word)):
                for newWord in hash_dict[_word[:i] + '*' + _word[i + 1:]]:
                    if newWord not in marked:
                        yield newWord

        def __findPath(_end_set):
            ans = []
            for cur_w in _end_set:
                for parent in path[cur_w[0]]:
                    ans.append([parent] + cur_w)
            return ans

        marked = set()
        path = collections.defaultdict(set)
        begin_set = set()
        end_set = set()
        begin_set.add(beginWord)
        end_set.add(endWord)
        direction = True  # BFS direction

        while len(begin_set) > 0 and len(end_set) > 0:
            if len(begin_set) > len(end_set):
                begin_set, end_set = end_set, begin_set
                direction = not direction
            temp = set()
            for word in begin_set:
                marked.add(word)
            for word in begin_set:
                for w in __edges(word):
                    temp.add(w)
                    if direction:
                        path[w].add(word)
                    else:
                        path[word].add(w)
            begin_set = temp
            if begin_set & end_set:
                res = [[endWord]]
                while res[0][0] != beginWord:
                    res = __findPath(res)
                return res

        return []

    def _findLadders_TLE(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        hash_dict = dict({})

        def __bfs(begin_w: str, end_w: str, w_list: list, h_dict: dict):
            set_1 = set()
            set_1.add(begin_w)
            set_2 = set()
            set_2.add(end_w)
            word_set = set(w_list)
            __bfs_recursion(set_1, set_2, word_set, True, h_dict)

        def __bfs_recursion(set_1: set, set_2: set, word_set: set, direction: bool, h_dict: dict):
            if len(set_1) == 0:
                return False
            if len(set_1) > len(set_2):
                return __bfs_recursion(set_2, set_1, word_set, not direction, h_dict)

            word_set = word_set - set_1
            word_set = word_set - set_2

            done_flag = False
            new_set = set()

            ord_a = ord("a")
            ord_z = ord("z")

            for cur_word in set_1:
                assert isinstance(cur_word, str)
                cur_ch_list = list(cur_word)
                for idx, cur_ch in enumerate(cur_word):
                    for new_ord in range(ord_a, ord_z + 1):  # modify one char to construct a new word
                        new_ch = chr(new_ord)
                        if cur_ch == new_ch:
                            continue

                        cur_ch_list[idx] = new_ch
                        new_word = "".join(cur_ch_list)

                        k = cur_word if direction else new_word
                        v = new_word if direction else cur_word
                        w_list = h_dict[k] if k in h_dict else []

                        if new_word in set_2:  # meet the same word, store the result
                            done_flag = True
                            w_list.append(v)
                            h_dict[k] = w_list

                        if not done_flag and new_word in word_set:
                            new_set.add(new_word)
                            w_list.append(v)
                            h_dict[k] = w_list

                        cur_ch_list[idx] = cur_ch  # backtrace

            return done_flag or __bfs_recursion(set_2, new_set, word_set, not direction, h_dict)

        __bfs(beginWord, endWord, wordList, hash_dict)

        path_list = [beginWord]
        res = []

        def __find_word_ladders(begin_w: str, end_w: str, h_dict: dict, p_list: list):
            if begin_w == end_w:
                res.append(path_list[:])
                return
            if begin_w in h_dict:
                neighbors = h_dict[begin_w]
                for nei in neighbors:
                    p_list.append(nei)
                    __find_word_ladders(nei, end_w, h_dict, p_list)
                    p_list.pop()  # backtrace

        __find_word_ladders(beginWord, endWord, hash_dict, path_list)

        return res


def main():
    # Example 1: Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
    # beginWord = "hit"
    # endWord = "cog"
    # wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

    # Example 2: Output: []
    # beginWord = "hit"
    # endWord = "cog"
    # wordList = ["hot", "dot", "dog", "lot", "log"]

    beginWord = "aaaaa"
    endWord = "uuuuu"
    wordList = ["aaaaa", "waaaa", "wbaaa", "xaaaa", "xbaaa", "bbaaa", "bbwaa", "bbwba", "bbxaa", "bbxba", "bbbba",
     "wbbbb", "xbbba", "xbbbb", "cbbbb", "cwbbb", "cwcbb", "cxbbb", "cxcbb", "cccbb", "cccwb", "cccwc", "cccxb",
     "cccxc", "ccccc", "wcccc", "wdccc", "xcccc", "xdccc", "ddccc", "ddwcc", "ddwdc", "ddxcc", "ddxdc", "ddddc",
     "wdddc", "wdddd", "xdddc", "xdddd", "edddd", "ewddd", "ewedd", "exddd", "exedd", "eeedd", "eeewd", "eeewe",
     "eeexd", "eeexe", "eeeee", "weeee", "wfeee", "xeeee", "xfeee", "ffeee", "ffwee", "ffwfe", "ffxee", "ffxfe",
     "ffffe", "wfffe", "wffff", "xfffe", "xffff", "gffff", "gwfff", "gwgff", "gxfff", "gxgff", "gggff", "gggwf",
     "gggwg", "gggxf", "gggxg", "ggggg", "wgggg", "whggg", "xgggg", "xhggg", "hhggg", "hhwgg", "hhwhg", "hhxgg",
     "hhxhg", "hhhhg", "whhhg", "whhhh", "xhhhg", "xhhhh", "ihhhh", "iwhhh", "iwihh", "ixhhh", "ixihh", "iiihh",
     "iiiwh", "iiiwi", "iiixh", "iiixi", "iiiii", "wiiii", "wjiii", "xiiii", "xjiii", "jjiii", "jjwii", "jjwji",
     "jjxii", "jjxji", "jjjji", "wjjji", "wjjjj", "xjjji", "xjjjj", "kjjjj", "kwjjj", "kwkjj", "kxjjj", "kxkjj",
     "kkkjj", "kkkwj", "kkkwk", "kkkxj", "kkkxk", "kkkkk", "wkkkk", "wlkkk", "xkkkk", "xlkkk", "llkkk", "llwkk",
     "llwlk", "llxkk", "llxlk", "llllk", "wlllk", "wllll", "xlllk", "xllll", "mllll", "mwlll", "mwmll", "mxlll",
     "mxmll", "mmmll", "mmmwl", "mmmwm", "mmmxl", "mmmxm", "mmmmm", "wmmmm", "wnmmm", "xmmmm", "xnmmm", "nnmmm",
     "nnwmm", "nnwnm", "nnxmm", "nnxnm", "nnnnm", "wnnnm", "wnnnn", "xnnnm", "xnnnn", "onnnn", "ownnn", "owonn",
     "oxnnn", "oxonn", "ooonn", "ooown", "ooowo", "oooxn", "oooxo", "ooooo", "woooo", "wpooo", "xoooo", "xpooo",
     "ppooo", "ppwoo", "ppwpo", "ppxoo", "ppxpo", "ppppo", "wpppo", "wpppp", "xpppo", "xpppp", "qpppp", "qwppp",
     "qwqpp", "qxppp", "qxqpp", "qqqpp", "qqqwp", "qqqwq", "qqqxp", "qqqxq", "qqqqq", "wqqqq", "wrqqq", "xqqqq",
     "xrqqq", "rrqqq", "rrwqq", "rrwrq", "rrxqq", "rrxrq", "rrrrq", "wrrrq", "wrrrr", "xrrrq", "xrrrr", "srrrr",
     "swrrr", "swsrr", "sxrrr", "sxsrr", "sssrr", "ssswr", "sssws", "sssxr", "sssxs", "sssss", "wssss", "wtsss",
     "xssss", "xtsss", "ttsss", "ttwss", "ttwts", "ttxss", "ttxts", "tttts", "wttts", "wtttt", "xttts", "xtttt",
     "utttt", "uwttt", "uwutt", "uxttt", "uxutt", "uuutt", "uuuwt", "uuuwu", "uuuxt", "uuuxu", "uuuuu", "zzzzz",
     "zzzzy", "zzzyy", "zzyyy", "zzyyx", "zzyxx", "zzxxx", "zzxxw", "zzxww", "zzwww", "zzwwv", "zzwvv", "zzvvv",
     "zzvvu", "zzvuu", "zzuuu", "zzuut", "zzutt", "zzttt", "zztts", "zztss", "zzsss", "zzssr", "zzsrr", "zzrrr",
     "zzrrq", "zzrqq", "zzqqq", "zzqqp", "zzqpp", "zzppp", "zzppo", "zzpoo", "zzooo", "zzoon", "zzonn", "zznnn",
     "zznnm", "zznmm", "zzmmm", "zzmml", "zzmll", "zzlll", "zzllk", "zzlkk", "zzkkk", "zzkkj", "zzkjj", "zzjjj",
     "zzjji", "zzjii", "zziii", "zziih", "zzihh", "zzhhh", "zzhhg", "zzhgg", "zzggg", "zzggf", "zzgff", "zzfff",
     "zzffe", "zzfee", "zzeee", "zzeed", "zzedd", "zzddd", "zzddc", "zzdcc", "zzccc", "zzccz", "azccz", "aaccz",
     "aaacz", "aaaaz", "uuuzu", "uuzzu", "uzzzu", "zzzzu", "wbbba"]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.findLadders(beginWord, endWord, wordList)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
