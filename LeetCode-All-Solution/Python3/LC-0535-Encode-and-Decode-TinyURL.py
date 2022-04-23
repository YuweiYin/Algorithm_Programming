#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0535-Encode-and-Decode-TinyURL.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-23
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 0535 - (Medium) - Encode and Decode TinyURL
https://leetcode.com/problems/encode-and-decode-tinyurl/

Description & Requirement:
    Note: This is a companion problem to the System Design problem: Design TinyURL.

    TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl 
    and it returns a short URL such as http://tinyurl.com/4e9iAk. Design a class to encode a URL and decode a tiny URL.

    There is no restriction on how your encode/decode algorithm should work. You just need to ensure that 
    a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

    Implement the Solution class:
        Solution() Initializes the object of the system.
        String encode(String longUrl) Returns a tiny URL for the given longUrl.
        String decode(String shortUrl) Returns the original long URL for the given shortUrl. 
            It is guaranteed that the given shortUrl was encoded by the same object.

Example 1:
    Input: url = "https://leetcode.com/problems/design-tinyurl"
    Output: "https://leetcode.com/problems/design-tinyurl"
    Explanation:
        Solution obj = new Solution();
        string tiny = obj.encode(url); // returns the encoded tiny url.
        string ans = obj.decode(tiny); // returns the original url after decoding it.

Constraints:
    1 <= url.length <= 10^4
    url is guaranteed to be a valid URL.
"""


class Codec:

    def __init__(self):
        self.fix_url = "http://tinyurl.com/"
        self.hash_dict = dict({})  # key: tinyurl; value: original url.
        self.key = 0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        tiny_url = self.fix_url + str(self.key)
        self.key += 1
        self.hash_dict[tiny_url] = longUrl
        return tiny_url

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.hash_dict[shortUrl] if shortUrl in self.hash_dict else ""


def main():
    # Example 1: Output: "https://leetcode.com/problems/design-tinyurl"
    url = "https://leetcode.com/problems/design-tinyurl"

    # init instance
    # solution = Solution()
    codec = Codec()

    # run & time
    start = time.process_time()
    temp = codec.encode(url)
    ans = codec.decode(temp)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(temp)
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
