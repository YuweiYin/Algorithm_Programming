#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1487-Making-File-Names-Unique.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-03-03
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1487 - (Medium) - Making File Names Unique
https://leetcode.com/problems/making-file-names-unique/

Description & Requirement:
    Given an array of strings names of size n. You will create n folders in your file system such that, 
    at the i-th minute, you will create a folder with the name names[i].

    Since two files cannot have the same name, if you enter a folder name that was previously used, 
    the system will have a suffix addition to its name in the form of (k), where, 
    k is the smallest positive integer such that the obtained name remains unique.

    Return an array of strings of length n where ans[i] is the actual name the system 
    will assign to the i-th folder when you create it.

Example 1:
    Input: names = ["pes","fifa","gta","pes(2019)"]
    Output: ["pes","fifa","gta","pes(2019)"]
    Explanation: Let's see how the file system creates folder names:
        "pes" --> not assigned before, remains "pes"
        "fifa" --> not assigned before, remains "fifa"
        "gta" --> not assigned before, remains "gta"
        "pes(2019)" --> not assigned before, remains "pes(2019)"
Example 2:
    Input: names = ["gta","gta(1)","gta","avalon"]
    Output: ["gta","gta(1)","gta(2)","avalon"]
    Explanation: Let's see how the file system creates folder names:
        "gta" --> not assigned before, remains "gta"
        "gta(1)" --> not assigned before, remains "gta(1)"
        "gta" --> the name is reserved, system adds (k), 
            since "gta(1)" is also reserved, systems put k = 2. it becomes "gta(2)"
        "avalon" --> not assigned before, remains "avalon"
Example 3:
    Input: names = ["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece"]
    Output: ["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece(4)"]
    Explanation: When the last folder is created, the smallest positive valid k is 4, 
        and it becomes "onepiece(4)".

Constraints:
    1 <= names.length <= 5 * 10^4
    1 <= names[i].length <= 20
    names[i] consists of lowercase English letters, digits, and/or round brackets.
"""


class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        # exception case
        assert isinstance(names, list) and len(names) >= 1
        # main method: (hashing)
        return self._getFolderNames(names)

    def _getFolderNames(self, names: List[str]) -> List[str]:
        assert isinstance(names, list) and len(names) >= 1

        res = []
        hash_dict = dict({})
        for name in names:
            if name not in hash_dict:
                res.append(name)
                hash_dict[name] = 1
            else:
                k = hash_dict[name]
                while name + '(' + str(k) + ')' in hash_dict:
                    k += 1
                filename = name + '(' + str(k) + ')'
                res.append(filename)
                hash_dict[name] = k + 1
                hash_dict[filename] = 1

        return res


def main():
    # Example 1: Output: ["pes","fifa","gta","pes(2019)"]
    # names = ["pes", "fifa", "gta", "pes(2019)"]

    # Example 2: Output: ["gta","gta(1)","gta(2)","avalon"]
    # names = ["gta", "gta(1)", "gta", "avalon"]

    # Example 3: Output: ["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece(4)"]
    names = ["onepiece", "onepiece(1)", "onepiece(2)", "onepiece(3)", "onepiece"]

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.getFolderNames(names)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
