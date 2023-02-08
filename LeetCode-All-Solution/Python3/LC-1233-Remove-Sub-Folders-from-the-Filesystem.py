#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1233-Remove-Sub-Folders-from-the-Filesystem.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-02-08
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1233 - (Medium) - Remove Sub-Folders from the Filesystem
https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

Description & Requirement:
    Given a list of folders folder, return the folders after removing all sub-folders in those folders. 
    You may return the answer in any order.

    If a folder[i] is located within another folder[j], it is called a sub-folder of it.

    The format of a path is one or more concatenated strings of the form: '/' 
    followed by one or more lowercase English letters.

    For example, "/leetcode" and "/leetcode/problems" are valid paths while an empty string and "/" are not.

Example 1:
    Input: folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
    Output: ["/a","/c/d","/c/f"]
    Explanation: Folders "/a/b" is a subfolder of "/a" and "/c/d/e" is inside of folder "/c/d" in our filesystem.
Example 2:
    Input: folder = ["/a","/a/b/c","/a/b/d"]
    Output: ["/a"]
    Explanation: Folders "/a/b/c" and "/a/b/d" will be removed because they are subfolders of "/a".
Example 3:
    Input: folder = ["/a/b/c","/a/b/ca","/a/b/d"]
    Output: ["/a/b/c","/a/b/ca","/a/b/d"]

Constraints:
    1 <= folder.length <= 4 * 10^4
    2 <= folder[i].length <= 100
    folder[i] contains only lowercase letters and '/'.
    folder[i] always starts with the character '/'.
    Each folder name is unique.
"""


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # exception case
        assert isinstance(folder, list) and len(folder) >= 1
        # main method: (sorting)
        return self._removeSubfolders(folder)

    def _removeSubfolders(self, folder: List[str]) -> List[str]:
        assert isinstance(folder, list) and len(folder) >= 1

        folder.sort()

        res = [folder[0]]
        for i in range(1, len(folder)):
            if not ((pre := len(res[-1])) < len(folder[i]) and res[-1] == folder[i][:pre] and folder[i][pre] == "/"):
                res.append(folder[i])

        return res


def main():
    # Example 1: Output: ["/a","/c/d","/c/f"]
    # folder = ["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]

    # Example 2: Output: ["/a"]
    # folder = ["/a", "/a/b/c", "/a/b/d"]

    # Example 3: Output: ["/a/b/c","/a/b/ca","/a/b/d"]
    folder = ["/a/b/c", "/a/b/ca", "/a/b/d"]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.removeSubfolders(folder)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
