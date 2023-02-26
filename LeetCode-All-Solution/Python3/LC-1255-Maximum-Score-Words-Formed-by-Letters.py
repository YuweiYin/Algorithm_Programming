#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1255-Maximum-Score-Words-Formed-by-Letters.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-02-26
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 1255 - (Hard) - Maximum Score Words Formed by Letters
https://leetcode.com/problems/maximum-score-words-formed-by-letters/

Description & Requirement:
    Given a list of words, list of  single letters (might be repeating) and score of every character.

    Return the maximum score of any valid set of words formed by using the given letters 
    (words[i] cannot be used two or more times).

    It is not necessary to use all characters in letters and each letter can only be used once. 
    Score of letters 'a', 'b', 'c', ... ,'z' is given by score[0], score[1], ... , score[25] respectively.

Example 1:
    Input: words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","d","g","o","o"], 
        score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
    Output: 23
    Explanation:
        Score  a=1, c=9, d=5, g=3, o=2
        Given letters, we can form the words "dad" (5+1+5) and "good" (3+2+2+5) with a score of 23.
        Words "dad" and "dog" only get a score of 21.
Example 2:
    Input: words = ["xxxz","ax","bx","cx"], letters = ["z","a","b","c","x","x","x"], 
        score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
    Output: 27
    Explanation:
        Score  a=4, b=4, c=4, x=5, z=10
        Given letters, we can form the words "ax" (4+5), "bx" (4+5) and "cx" (4+5) with a score of 27.
        Word "xxxz" only get a score of 25.
Example 3:
    Input: words = ["leetcode"], letters = ["l","e","t","c","o","d"], 
        score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]
    Output: 0
    Explanation: Letter "e" can only be used once.

Constraints:
    1 <= words.length <= 14
    1 <= words[i].length <= 15
    1 <= letters.length <= 100
    letters[i].length == 1
    score.length == 26
    0 <= score[i] <= 10
    words[i], letters[i] contains only lower case English letters.
"""


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        # exception case
        assert isinstance(words, list) and len(words) >= 1
        assert isinstance(letters, list) and len(letters) >= 1
        assert isinstance(score, list) and len(score) == 26
        # main method: (counter)
        return self._maxScoreWords(words, letters, score)

    def _maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        assert isinstance(words, list) and len(words) >= 1
        assert isinstance(letters, list) and len(letters) >= 1
        assert isinstance(score, list) and len(score) == 26

        res = 0

        cnt = collections.Counter(letters)
        n = len(words)
        ord_a = ord('a')

        for i in range(1 << n):
            cur = collections.Counter(''.join([words[j] for j in range(n) if (i >> j) & 1]))
            if all(v <= cnt[ch] for ch, v in cur.items()):
                t = sum(v * score[ord(ch) - ord_a] for ch, v in cur.items())
                res = max(res, t)

        return res


def main():
    # Example 1: Output: 23
    # words = ["dog", "cat", "dad", "good"]
    # letters = ["a", "a", "c", "d", "d", "d", "g", "o", "o"]
    # score = [1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # Example 2: Output: 27
    # words = ["xxxz", "ax", "bx", "cx"]
    # letters = ["z", "a", "b", "c", "x", "x", "x"]
    # score = [4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 10]

    # Example 3: Output: 0
    words = ["leetcode"]
    letters = ["l", "e", "t", "c", "o", "d"]
    score = [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.maxScoreWords(words, letters, score)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
