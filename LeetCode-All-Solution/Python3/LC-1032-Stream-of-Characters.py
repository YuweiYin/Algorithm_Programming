#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1032-Stream-of-Characters.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-03-24
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 1032 - (Hard) - Stream of Characters
https://leetcode.com/problems/stream-of-characters/

Description & Requirement:
    Design an algorithm that accepts a stream of characters and 
    checks if a suffix of these characters is a string of a given array of strings words.

    For example, if words = ["abc", "xyz"] and the stream added the four characters (one by one) 
    'a', 'x', 'y', and 'z', your algorithm should detect that 
    the suffix "xyz" of the characters "axyz" matches "xyz" from words.

    Implement the StreamChecker class:
        StreamChecker(String[] words) Initializes the object with the strings array words.
        boolean query(char letter) Accepts a new character from the stream and returns true 
            if any non-empty suffix from the stream forms a word that is in words.

Example 1:
    Input
        ["StreamChecker", "query", "query", "query", "query", "query", "query", 
            "query", "query", "query", "query", "query", "query"]
        [[["cd", "f", "kl"]], ["a"], ["b"], ["c"], ["d"], ["e"], ["f"], ["g"], ["h"], ["i"], ["j"], ["k"], ["l"]]
    Output
        [null, false, false, false, true, false, true, false, false, false, false, false, true]
    Explanation
        StreamChecker streamChecker = new StreamChecker(["cd", "f", "kl"]);
        streamChecker.query("a"); // return False
        streamChecker.query("b"); // return False
        streamChecker.query("c"); // return False
        streamChecker.query("d"); // return True, because 'cd' is in the wordlist
        streamChecker.query("e"); // return False
        streamChecker.query("f"); // return True, because 'f' is in the wordlist
        streamChecker.query("g"); // return False
        streamChecker.query("h"); // return False
        streamChecker.query("i"); // return False
        streamChecker.query("j"); // return False
        streamChecker.query("k"); // return False
        streamChecker.query("l"); // return True, because 'kl' is in the wordlist

Constraints:
    1 <= words.length <= 2000
    1 <= words[i].length <= 200
    words[i] consists of lowercase English letters.
    letter is a lowercase English letter.
    At most 4 * 10^4 calls will be made to query.
"""


class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False
        self.fail = None


class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = Trie()
        for word in words:
            cur = self.root
            for char in word:
                idx = ord(char) - ord("a")
                if not cur.children[idx]:
                    cur.children[idx] = Trie()
                cur = cur.children[idx]
            cur.is_end = True

        self.root.fail = self.root
        queue = collections.deque()
        for i in range(26):
            if self.root.children[i]:
                self.root.children[i].fail = self.root
                queue.append(self.root.children[i])
            else:
                self.root.children[i] = self.root
        while len(queue) > 0:
            node = queue.popleft()
            node.is_end = node.is_end or node.fail.is_end
            for i in range(26):
                if node.children[i]:
                    node.children[i].fail = node.fail.children[i]
                    queue.append(node.children[i])
                else:
                    node.children[i] = node.fail.children[i]

        self.temp = self.root

    def query(self, letter: str) -> bool:
        self.temp = self.temp.children[ord(letter) - ord('a')]
        return self.temp.is_end


def main():
    # Example 1: Output: [null, false, false, false, true, false, true, false, false, false, false, false, true]
    command_list = ["StreamChecker", "query", "query", "query", "query", "query", "query", "query", "query", "query",
                    "query", "query", "query"]
    param_list = [[["cd", "f", "kl"]], ["a"], ["b"], ["c"], ["d"], ["e"], ["f"], ["g"], ["h"], ["i"], ["j"], ["k"],
                  ["l"]]

    # init instance
    obj = StreamChecker(param_list[0][0])
    ans = ["null"]

    # run & time
    start = time.process_time()
    assert len(command_list) == len(param_list)
    for idx in range(1, len(command_list)):
        command = command_list[idx]
        param = param_list[idx]
        if command == "query" and isinstance(param, list) and len(param) == 1:
            ans.append(obj.query(param[0]))
        else:
            ans.append("null")
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
