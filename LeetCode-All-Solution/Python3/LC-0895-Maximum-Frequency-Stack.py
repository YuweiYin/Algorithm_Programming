#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0895-Maximum-Frequency-Stack.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-19
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 0895 - (Medium) - Maximum Frequency Stack
https://leetcode.com/problems/maximum-frequency-stack/

Description & Requirement:
    Design a stack-like data structure to push elements to the stack 
    and pop the most frequent element from the stack.

    Implement the FreqStack class:
        FreqStack() constructs an empty frequency stack.
        void push(int val) pushes an integer val onto the top of the stack.
        int pop() removes and returns the most frequent element in the stack.
            If there is a tie for the most frequent element, 
            the element closest to the stack's top is removed and returned.

Example 1:
    Input
        ["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"]
        [[], [5], [7], [5], [7], [4], [5], [], [], [], []]
    Output
        [null, null, null, null, null, null, null, 5, 7, 5, 4]

    Explanation
        FreqStack freqStack = new FreqStack();
        freqStack.push(5); // The stack is [5]
        freqStack.push(7); // The stack is [5,7]
        freqStack.push(5); // The stack is [5,7,5]
        freqStack.push(7); // The stack is [5,7,5,7]
        freqStack.push(4); // The stack is [5,7,5,7,4]
        freqStack.push(5); // The stack is [5,7,5,7,4,5]
        freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
        freqStack.pop();   // return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. 
            The stack becomes [5,7,5,4].
        freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,4].
        freqStack.pop();   // return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. 
            The stack becomes [5,7].

Constraints:
    0 <= val <= 10^9
    At most 2 * 10^4 calls will be made to push and pop.
    It is guaranteed that there will be at least one element in the stack before calling pop.
"""


class FreqStack:

    def __init__(self):
        self.max_freq = 0  # the current max freq
        self.freq_to_val = dict({})  # key: an existing freq; value: val list of this freq.
        self.val_to_freq = dict({})  # key: val in stack; value: the freq of the val.

    def push(self, val: int) -> None:
        # val to freq
        if val not in self.val_to_freq:
            self.val_to_freq[val] = 1
        else:
            self.val_to_freq[val] += 1
        # max freq
        new_freq = self.val_to_freq[val]
        self.max_freq = max(self.max_freq, new_freq)
        # freq to val
        if new_freq not in self.freq_to_val:
            self.freq_to_val[new_freq] = [val]
        else:
            self.freq_to_val[new_freq].append(val)

    def pop(self) -> int:
        # assert self.max_freq in self.freq_to_val
        max_freq_val = self.freq_to_val[self.max_freq].pop()  # pop the newest one
        self.val_to_freq[max_freq_val] -= 1
        if len(self.freq_to_val[self.max_freq]) == 0:
            del self.freq_to_val[self.max_freq]
            self.max_freq -= 1
        return max_freq_val


def main():
    # Example 1: Output: [null, null, null, null, null, null, null, 5, 7, 5, 4]
    command_list = ["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"]
    param_list = [[], [5], [7], [5], [7], [4], [5], [], [], [], []]

    # init instance
    # solution = Solution()
    obj = FreqStack()

    # run & time
    start = time.process_time()
    ans = ["null"]
    assert len(command_list) == len(param_list)
    for idx in range(1, len(command_list)):
        command = command_list[idx]
        param = param_list[idx]
        if command == "push":
            if isinstance(param, list) and len(param) == 1:
                obj.push(param[0])
            ans.append("null")
        elif command == "pop":
            get_res = obj.pop()
            if isinstance(get_res, int):
                ans.append(get_res)
            else:
                ans.append("null")
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
