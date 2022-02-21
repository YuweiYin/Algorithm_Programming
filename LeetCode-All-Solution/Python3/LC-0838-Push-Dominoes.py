#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0838-Push-Dominoes.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-21
=================================================================="""

import sys
import time
# from typing import List
# import collections

"""
LeetCode - 0838 - (Medium) - Push Dominoes
https://leetcode.com/problems/push-dominoes/

Description & Requirement:
    There are n dominoes in a line, and we place each domino vertically upright. 
    In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

    After each second, each domino that is falling to the left pushes the adjacent domino on the left. 
    Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

    When a vertical domino has dominoes falling on it from both sides, 
    it stays still due to the balance of the forces.

    For the purposes of this question, we will consider that a falling domino 
    expends no additional force to a falling or already fallen domino.

    You are given a string dominoes representing the initial state where:
        dominoes[i] = 'L', if the ith domino has been pushed to the left,
        dominoes[i] = 'R', if the ith domino has been pushed to the right, and
        dominoes[i] = '.', if the ith domino has not been pushed.

    Return a string representing the final state.

Example 1:
    Input: dominoes = "RR.L"
    Output: "RR.L"
    Explanation: The first domino expends no additional force on the second domino.
Example 2:
    Input: dominoes = ".L.R...LR..L.."
    Output: "LL.RR.LLRRLL.."

Constraints:
    n == dominoes.length
    1 <= n <= 10^5
    dominoes[i] is either 'L', 'R', or '.'.
"""


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # exception case
        if not isinstance(dominoes, str) or len(dominoes) <= 0:
            return ""  # Error input type
        if len(dominoes) == 1:
            return dominoes
        # main method: (TODO: simulate)
        #     find the first "R", the left part of this domino won't be affected by the later ones
        #     find the last "L", the right part of this domino won't be affected by the later ones
        #     for the middle part, find all intervals whose leftmost domino is "R" and rightmost domino is "L"
        #         tips: skip the consecutive "LL" or "RR"
        # return self._pushDominoesSimulate(dominoes)
        # method 2: (multi-source BFS, from all "L" and "R" to BFS pushing)
        #     if a "L" meets a left "L" or "R", then stop;
        #         if a "L" meets a left ".", and the left left one is not a "R", then change it to "L", else stop;
        #     if a "R" meets a right "L" or "R", then stop;
        #         if a "R" meets a right ".", and the right right one is not a "L", then change it to "R", else stop;
        return self._pushDominoesBfs(dominoes)

    def _pushDominoesSimulate(self, dominoes: str) -> str:
        len_dominoes = len(dominoes)
        assert len_dominoes >= 2

        res = [char for char in dominoes]

        # find the first "R", the left part of this domino won't be affected by the later ones
        first_r_idx = 0
        rightmost_l_before_first_r_idx = -1
        while first_r_idx < len_dominoes and dominoes[first_r_idx] != "R":
            if dominoes[first_r_idx] == "L":
                rightmost_l_before_first_r_idx = first_r_idx
            first_r_idx += 1
        if first_r_idx == len_dominoes:  # no "R", then just push some dominoes to left
            if rightmost_l_before_first_r_idx >= 0:
                for idx in range(rightmost_l_before_first_r_idx):
                    res[idx] = "L"
                return "".join(res)
            else:  # no "L", all "."
                return dominoes
        # now, find the first "R" domino from index == 0
        if rightmost_l_before_first_r_idx >= 0:
            for idx in range(rightmost_l_before_first_r_idx):
                res[idx] = "L"

        # find the last "L", the right part of this domino won't be affected by the later ones
        last_l_idx = len_dominoes - 1
        leftmost_r_after_last_l_idx = -1
        while last_l_idx >= 0 and dominoes[last_l_idx] != "L":
            if dominoes[last_l_idx] == "R":
                leftmost_r_after_last_l_idx = last_l_idx
            last_l_idx -= 1
        if last_l_idx == -1:  # no "L", then just push some dominoes to right
            if leftmost_r_after_last_l_idx >= 0:
                for idx in range(leftmost_r_after_last_l_idx, len_dominoes):
                    res[idx] = "R"
                return "".join(res)
            else:  # no "R", all "."
                return dominoes
        # now, find the last "L" domino from index == -1
        if leftmost_r_after_last_l_idx >= 0:
            for idx in range(leftmost_r_after_last_l_idx, len_dominoes):
                res[idx] = "R"

        # TODO: for the middle part, find all intervals whose leftmost domino is "R" and rightmost domino is "L"
        left_boundary = first_r_idx
        right_boundary = last_l_idx

        while left_boundary < right_boundary:
            pass

        return "".join(res)

    def _pushDominoesBfs(self, dominoes: str) -> str:
        len_dominoes = len(dominoes)
        assert len_dominoes >= 2

        res = [char for char in dominoes]
        bfs_queue = []  # deal with all elements in the queue for a step
        for idx, char in enumerate(res):
            if char != ".":
                bfs_queue.append((idx, char))

        while len(bfs_queue) > 0:
            new_queue = []
            new_res = res.copy()
            for cur_domino in bfs_queue:
                cur_idx, cur_char = cur_domino
                # if a "L" meets a left "L" or "R", then stop;
                #     if a "L" meets a left ".", and the left left one is not a "R", then change it to "L", else stop
                if cur_char == "L":
                    if cur_idx > 0 and res[cur_idx - 1] == ".":
                        if not (cur_idx > 1 and res[cur_idx - 2] == "R"):
                            new_res[cur_idx - 1] = "L"
                            new_queue.append((cur_idx - 1, "L"))
                # if a "R" meets a right "L" or "R", then stop;
                #     if a "R" meets a right ".", and the right right one is not a "L", then change it to "R", else stop
                if cur_char == "R":
                    if cur_idx < len_dominoes - 1 and res[cur_idx + 1] == ".":
                        if not (cur_idx < len_dominoes - 2 and res[cur_idx + 2] == "L"):
                            new_res[cur_idx + 1] = "R"
                            new_queue.append((cur_idx + 1, "R"))
            bfs_queue = new_queue
            res = new_res

        return "".join(res)


def main():
    # Example 1: Output: "RR.L"
    # dominoes = "RR.L"

    # Example 2: Output: "LL.RR.LLRRLL.."
    dominoes = ".L.R...LR..L.."

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.pushDominoes(dominoes)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
