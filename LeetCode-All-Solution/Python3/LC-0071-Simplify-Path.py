#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0071-Simplify-Path.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-06
=================================================================="""
# import functools
import sys
import time
# from typing import List

"""
LeetCode - 0071 - (Medium) - Simplify Path
https://leetcode.com/problems/simplify-path/

Description:
    Given a string path, which is an absolute path (starting with a slash '/') to a file or directory 
    in a Unix-style file system, convert it to the simplified canonical path.
    
    In a Unix-style file system, a period '.' refers to the current directory, 
    a double period '..' refers to the directory up a level, 
    and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. 
    For this problem, any other format of periods such as '...' are treated as file/directory names.

Requirement:
    The canonical path should have the following format:
        - The path starts with a single slash '/'.
        - Any two directories are separated by a single slash '/'.
        - The path does not end with a trailing '/'.
        - The path only contains the directories on the path from the root directory to the target file or directory 
            - (i.e., no period '.' or double period '..')
        - Return the simplified canonical path.

Example 1:
    Input: path = "/home/"
    Output: "/home"
    Explanation: Note that there is no trailing slash after the last directory name.
Example 2:
    Input: path = "/../"
    Output: "/"
    Explanation:
        Going one level up from the root directory is a no-op, as the root level is the highest level you can go.
Example 3:
    Input: path = "/home//foo/"
    Output: "/home/foo"
    Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.

Constraints:
    1 <= path.length <= 3000
    path consists of English letters, digits, period '.', slash '/' or '_'.
    path is a valid absolute Unix path.
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        # exception case
        if not isinstance(path, str) or len(path) <= 0:
            return "/"  # Error input
        # border case
        assert path[0] == "/"
        if len(path) == 1:
            return "/"
        if len(path) == 2:
            return "/" if (path[1] == "." or path[1] == "/") else path
        # main method: split the path string by '/' and deal with the list
        return self._simplifyPath(path)

    def _simplifyPath(self, path: str) -> str:
        # now, 3 <= len(path)
        # clear the head '/' and trailing '/'
        path = path[1: -1] if path[len(path) - 1] == "/" else path[1:]

        # simplify consecutive slashes, and get list
        raw_path_list = path.split("/")  # there are some "" if path has consecutive slashes
        path_list = []
        for r_p in raw_path_list:
            if not (r_p == "") and not (r_p == "."):  # skip "" and "."
                path_list.append(r_p)
        del raw_path_list

        # deal with ".." from left to right, which means its left item and itself should be removed (until the root dir)
        new_path_list = []
        for p in path_list:
            if p == "..":
                if len(new_path_list) > 0:
                    new_path_list.pop()  # pop stack if possible
            else:
                new_path_list.append(p)

        return "/" + "/".join(new_path_list)


def main():
    # Example 1: Output: "/home"
    # path = "/home/"

    # Example 2: Output: "/"
    # path = "/../"

    # Example 3: Output: "/home/foo"
    # path = "/home//foo/"

    # Example 4: Output: "/home/..."
    path = "/home//foo/abc/../cde/../../.../"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.simplifyPath(path)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
