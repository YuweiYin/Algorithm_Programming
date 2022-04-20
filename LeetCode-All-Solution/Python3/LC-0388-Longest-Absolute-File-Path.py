#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0388-Longest-Absolute-File-Path.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-20
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0388 - (Medium) - Longest Absolute File Path
https://leetcode.com/problems/longest-absolute-file-path/

Description & Requirement:
    Suppose we have a file system that stores both files and directories. 
    An example of one system in text form looks like this (with ⟶ representing the tab character):
        dir
        ⟶ subdir1
        ⟶ ⟶ file1.ext
        ⟶ ⟶ subsubdir1
        ⟶ subdir2
        ⟶ ⟶ subsubdir2
        ⟶ ⟶ ⟶ file2.ext

    Here, we have dir as the only directory in the root. dir contains two subdirectories, 
    subdir1 and subdir2. subdir1 contains a file file1.ext and subdirectory subsubdir1. 
    subdir2 contains a subdirectory subsubdir2, which contains a file file2.ext.

    If we were to write this representation in code, it will look like this: 
    "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext". 
    Note that the '\n' and '\t' are the new-line and tab characters.

    Every file and directory has a unique absolute path in the file system, 
    which is the order of directories that must be opened to reach the file/directory itself, 
    all concatenated by '/'s. Using the above example, the absolute path to file2.ext is 
    "dir/subdir2/subsubdir2/file2.ext". Each directory name consists of letters, digits, 
    and/or spaces. Each file name is of the form name.extension, 
    where name and extension consist of letters, digits, and/or spaces.

    Given a string input representing the file system in the explained format, 
    return the length of the longest absolute path to a file in the abstracted file system. 
    If there is no file in the system, return 0.

Example 1:
    Input: input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
    Output: 20
    Explanation: We have only one file, and the absolute path is "dir/subdir2/file.ext" of length 20.
Example 2:
    Input: input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    Output: 32
    Explanation: We have two files:
        "dir/subdir1/file1.ext" of length 21
        "dir/subdir2/subsubdir2/file2.ext" of length 32.
        We return 32 since it is the longest absolute path to a file.
Example 3:
    Input: input = "a"
    Output: 0
    Explanation: We do not have any files, just a single directory named "a".

Constraints:
    1 <= input.length <= 10^4
    input may contain lowercase or uppercase English letters, a new line character '\n', 
    a tab character '\t', a dot '.', a space ' ', and digits.
"""


class Solution:
    def lengthLongestPath(self, _input: str) -> int:
        # exception case
        assert isinstance(_input, str) and len(_input) >= 1
        # main method: (deal with each char)
        return self._lengthLongestPath(_input)

    def _lengthLongestPath(self, _input: str) -> int:
        directory_len = []  # the name length of each level directory/file

        res = 0
        cur_idx = 0
        max_idx = len(_input) - 1

        while cur_idx <= max_idx:
            # get the file depth of the current directory
            cur_depth = 1
            while cur_idx <= max_idx and _input[cur_idx] == "\t":
                cur_depth += 1
                cur_idx += 1

            # get the file name length of the current directory
            is_file = False
            filename_length = 0
            while cur_idx <= max_idx and _input[cur_idx] != "\n":
                if _input[cur_idx] == ".":
                    is_file = True
                filename_length += 1
                cur_idx += 1

            # now _input[cur_idx] == "\n", skip it
            cur_idx += 1

            # combine parent directory and the current filename
            while len(directory_len) >= cur_depth:
                directory_len.pop()
            if len(directory_len) > 0:
                filename_length += directory_len[-1] + 1  # parent directory and "/"

            # if is_file, update res; else, update directory_len
            if is_file:
                res = max(res, filename_length)
            else:
                directory_len.append(filename_length)

        return res


def main():
    # Example 1: Output: 20
    # _input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"

    # Example 2: Output: 32
    _input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"

    # Example 3: Output: 0
    # _input = "a"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.lengthLongestPath(_input)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
