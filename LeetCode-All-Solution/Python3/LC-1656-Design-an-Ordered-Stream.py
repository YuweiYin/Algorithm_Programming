#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1656-Design-an-Ordered-Stream.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-08-16
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1656 - (Easy) - Design an Ordered Stream
https://leetcode.com/problems/design-an-ordered-stream/

Description & Requirement:
    There is a stream of n (idKey, value) pairs arriving in an arbitrary order, 
    where idKey is an integer between 1 and n and value is a string. No two pairs have the same id.

    Design a stream that returns the values in increasing order of their IDs 
    by returning a chunk (list) of values after each insertion. 
    The concatenation of all the chunks should result in a list of the sorted values.

    Implement the OrderedStream class:
        OrderedStream(int n) Constructs the stream to take n values.
        String[] insert(int idKey, String value) Inserts the pair (idKey, value) into the stream, 
            then returns the largest possible chunk of currently inserted values that appear next in the order.

Example:
    Input
        ["OrderedStream", "insert", "insert", "insert", "insert", "insert"]
        [[5], [3, "ccccc"], [1, "aaaaa"], [2, "bbbbb"], [5, "eeeee"], [4, "ddddd"]]
    Output
        [null, [], ["aaaaa"], ["bbbbb", "ccccc"], [], ["ddddd", "eeeee"]]
    Explanation
        // Note that the values ordered by ID is ["aaaaa", "bbbbb", "ccccc", "ddddd", "eeeee"].
        OrderedStream os = new OrderedStream(5);
        os.insert(3, "ccccc"); // Inserts (3, "ccccc"), returns [].
        os.insert(1, "aaaaa"); // Inserts (1, "aaaaa"), returns ["aaaaa"].
        os.insert(2, "bbbbb"); // Inserts (2, "bbbbb"), returns ["bbbbb", "ccccc"].
        os.insert(5, "eeeee"); // Inserts (5, "eeeee"), returns [].
        os.insert(4, "ddddd"); // Inserts (4, "ddddd"), returns ["ddddd", "eeeee"].
        // Concatentating all the chunks returned:
        // [] + ["aaaaa"] + ["bbbbb", "ccccc"] + [] + ["ddddd", "eeeee"] = ["aaaaa", "bbbbb", "ccccc", "ddddd", "eeeee"]
        // The resulting order is the same as the order above.

Constraints:
    1 <= n <= 1000
    1 <= id <= n
    value.length == 5
    value consists only of lowercase letters.
    Each call to insert will have a unique id.
    Exactly n calls will be made to insert.
"""


class OrderedStream:

    def __init__(self, n: int):
        self.stream = ["" for _ in range(n + 1)]
        self.index = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        cur_stream = self.stream

        cur_stream[idKey] = value
        res = []
        while 0 <= self.index < len(cur_stream) and len(cur_stream[self.index]) > 0:
            res.append(cur_stream[self.index])
            self.index += 1

        return res


def main():
    # Example: Output: [null, [], ["aaaaa"], ["bbbbb", "ccccc"], [], ["ddddd", "eeeee"]]
    command_list = ["OrderedStream", "insert", "insert", "insert", "insert", "insert"]
    param_list = [[5], [3, "ccccc"], [1, "aaaaa"], [2, "bbbbb"], [5, "eeeee"], [4, "ddddd"]]

    # init instance
    # solution = Solution()
    obj = OrderedStream(param_list[0][0])
    ans = ["null"]

    # run & time
    start = time.process_time()
    assert len(command_list) == len(param_list)
    for idx in range(1, len(command_list)):
        command = command_list[idx]
        param = param_list[idx]
        if command == "insert" and isinstance(param, list) and len(param) == 2:
            ans.append(obj.insert(param[0], param[1]))
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
