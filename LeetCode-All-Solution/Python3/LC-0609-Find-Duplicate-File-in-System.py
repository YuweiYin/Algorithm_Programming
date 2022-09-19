#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0609-Find-Duplicate-File-in-System.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-09-19
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0609 - (Medium) - Find Duplicate File in System
https://leetcode.com/problems/find-duplicate-file-in-system/

Description & Requirement:
    Given a list paths of directory info, including the directory path, 
    and all the files with contents in this directory, 
    return all the duplicate files in the file system in terms of their paths. 
    You may return the answer in any order.

    A group of duplicate files consists of at least two files that have the same content.

    A single directory info string in the input list has the following format:
        "root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)"

    It means there are n files (f1.txt, f2.txt ... fn.txt) with content (f1_content, f2_content ... fn_content) 
    respectively in the directory "root/d1/d2/.../dm". Note that n >= 1 and m >= 0. 
    If m = 0, it means the directory is just the root directory.

    The output is a list of groups of duplicate file paths. For each group, 
    it contains all the file paths of the files that have the same content. 
    A file path is a string that has the following format:
        "directory_path/file_name.txt"

Example 1:
    Input: paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
    Output: [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]
Example 2:
    Input: paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"]
    Output: [["root/a/2.txt","root/c/d/4.txt"],["root/a/1.txt","root/c/3.txt"]]

Constraints:
    1 <= paths.length <= 2 * 10^4
    1 <= paths[i].length <= 3000
    1 <= sum(paths[i].length) <= 5 * 10^5
    paths[i] consist of English letters, digits, '/', '.', '(', ')', and ' '.
    You may assume no files or directories share the same name in the same directory.
    You may assume each given directory info represents a unique directory. 
        A single blank space separates the directory path and file info.

Follow up:
    Imagine you are given a real file system, how will you search files? DFS or BFS?
    If the file content is very large (GB level), how will you modify your solution?
    If you can only read the file by 1kb each time, how will you modify your solution?
    What is the time complexity of your modified solution? 
        What is the most time-consuming part and memory-consuming part of it? How to optimize?
    How to make sure the duplicated files you find are not false positive?
"""


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        # exception case
        assert isinstance(paths, list) and len(paths) >= 1
        for path in paths:
            assert isinstance(path, str) and len(path) >= 1
        # main method: (hash dict)
        return self._findDuplicate(paths)

    def _findDuplicate(self, paths: List[str]) -> List[List[str]]:
        assert isinstance(paths, list) and len(paths) >= 1

        hash_map = dict({})

        for path in paths:
            val_list = path.split()
            for val in val_list[1:]:

                name = val.split("(")
                name[1] = name[1].replace(")", "")
                _dir = val_list[0] + "/" + name[0]
                if name[1] in hash_map:
                    hash_map[name[1]].append(_dir)
                else:
                    hash_map[name[1]] = [_dir]

        res = []
        for k in hash_map.keys():
            if len(hash_map[k]) > 1:
                res.append(hash_map[k])

        return res


def main():
    # Example 1: Output: [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]
    # paths = ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]

    # Example 2: Output: [["root/a/2.txt","root/c/d/4.txt"],["root/a/1.txt","root/c/3.txt"]]
    paths = ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)"]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.findDuplicate(paths)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
