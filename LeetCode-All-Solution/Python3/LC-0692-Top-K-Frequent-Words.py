#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0692-Top-K-Frequent-Words.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-10-19
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0692 - (Medium) - Top K Frequent Words
https://leetcode.com/problems/top-k-frequent-words/

Description & Requirement:
    Given an array of strings words and an integer k, 
    return the k most frequent strings.

    Return the answer sorted by the frequency from highest to lowest. 
    Sort the words with the same frequency by their lexicographical order.

Example 1:
    Input: words = ["i","love","leetcode","i","love","coding"], k = 2
    Output: ["i","love"]
    Explanation: "i" and "love" are the two most frequent words.
        Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:
    Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
    Output: ["the","is","sunny","day"]
    Explanation: "the", "is", "sunny" and "day" are the four most frequent words, 
        with the number of occurrence being 4, 3, 2 and 1 respectively.

Constraints:
    1 <= words.length <= 500
    1 <= words[i].length <= 10
    words[i] consists of lowercase English letters.
    k is in the range [1, The number of unique words[i]]

Follow-up:
    Could you solve it in O(n log(k)) time and O(n) extra space?
"""


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # exception case
        assert isinstance(k, int) and k >= 1
        assert isinstance(words, list) and len(words) >= 1
        for word in words:
            assert isinstance(word, str) and len(word) >= 1
        # main method: (hash dict and sort)
        return self._topKFrequent(words, k)

    def _topKFrequent(self, words: List[str], k: int) -> List[str]:
        """
        Runtime: 65 ms, faster than 86.95% of Python3 online submissions for Top K Frequent Words.
        Memory Usage: 14.1 MB, less than 27.71% of Python3 online submissions for Top K Frequent Words.
        """
        assert isinstance(k, int) and k >= 1
        assert isinstance(words, list) and len(words) >= 1

        hash_dict = dict({})
        for word in words:
            if word not in hash_dict:
                hash_dict[word] = 1
            else:
                hash_dict[word] += 1

        hash_w_cnt = []
        for w, cnt in hash_dict.items():
            hash_w_cnt.append((w, cnt))

        hash_w_cnt.sort(key=lambda x: (-x[1], x[0]))

        return [w_cnt[0] for w_cnt in hash_w_cnt[:k]]


def main():
    # Example 1: Output: ["i","love"]
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 2

    # Example 2: Output: ["the","is","sunny","day"]
    # words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
    # k = 4

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.topKFrequent(words, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
