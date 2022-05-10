#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1728-Cat-and-Mouse-II.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-05-10
=================================================================="""

import sys
import time
from typing import List, Tuple
import collections

"""
LeetCode - 1728 - (Hard) - Cat and Mouse II
https://leetcode.com/problems/cat-and-mouse-ii/

Description:
    A game is played by a cat and a mouse named Cat and Mouse.

    The environment is represented by a grid of size rows x cols, 
    where each element is a wall, floor, player (Cat, Mouse), or food.
        Players are represented by the characters 'C'(Cat),'M'(Mouse).
        Floors are represented by the character '.' and can be walked on.
        Walls are represented by the character '#' and cannot be walked on.
        Food is represented by the character 'F' and can be walked on.
        There is only one of each character 'C', 'M', and 'F' in grid.

    Mouse and Cat play according to the following rules:
        Mouse moves first, then they take turns to move.
        During each turn, Cat and Mouse can jump in one of the four directions (left, right, up, down). 
            They cannot jump over the wall nor outside of the grid.
        catJump, mouseJump are the maximum lengths Cat and Mouse can jump at a time, respectively. 
            Cat and Mouse can jump less than the maximum length.
        Staying in the same position is allowed.
        Mouse can jump over Cat.

    The game can end in 4 ways:
        If Cat occupies the same position as Mouse, Cat wins.
        If Cat reaches the food first, Cat wins.
        If Mouse reaches the food first, Mouse wins.
        If Mouse cannot get to the food within 1000 turns, Cat wins.

    Given a rows x cols matrix grid and two integers catJump and mouseJump, 
    return true if Mouse can win the game if both Cat and Mouse play optimally, otherwise return false.

Example 1:
    Input: grid = ["####F","#C...","M...."], catJump = 1, mouseJump = 2
    Output: true
    Explanation: Cat cannot catch Mouse on its turn nor can it get the food before Mouse.
Example 2:
    Input: grid = ["M.C...F"], catJump = 1, mouseJump = 4
    Output: true
Example 3:
    Input: grid = ["M.C...F"], catJump = 1, mouseJump = 3
    Output: false

Constraints:
    rows == grid.length
    cols = grid[i].length
    1 <= rows, cols <= 8
    grid[i][j] consist only of characters 'C', 'M', 'F', '.', and '#'.
    There is only one of each character 'C', 'M', and 'F' in grid.
    1 <= catJump, mouseJump <= 8
"""


class Solution:
    def __init__(self):
        self.MOUSE_TURN = 0
        self.CAT_TURN = 1
        self.UNKNOWN = 0
        self.MOUSE_WIN = 1
        self.CAT_WIN = 2
        self.MAX_MOVE = 1000
        self.DIRECTION = ((-1, 0), (1, 0), (0, -1), (0, 1))

    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        # exception case
        assert isinstance(grid, list) and 1 <= len(grid) and 1 <= len(grid[0])
        assert isinstance(catJump, int) and 1 <= catJump
        assert isinstance(mouseJump, int) and 1 <= mouseJump
        # main method: (Game Theory & Topological Sorting)
        return self._canMouseWin(grid, catJump, mouseJump)

    def _canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        assert isinstance(grid, list)
        max_row = len(grid)
        assert max_row >= 1
        max_col = len(grid[0])
        assert max_col >= 1
        total_block = max_row * max_col

        def __get_pos(_row: int, _col: int) -> int:
            return int(_row * max_col + _col)

        # get the initial positions of the mouse, cat, and food
        mouse_start_pos = cat_start_pos = food_pos = 0
        for row_idx in range(max_row):
            for col_idx in range(max_col):
                cur_block = grid[row_idx][col_idx]
                if cur_block == 'M':
                    mouse_start_pos = __get_pos(row_idx, col_idx)
                elif cur_block == 'C':
                    cat_start_pos = __get_pos(row_idx, col_idx)
                elif cur_block == 'F':
                    food_pos = __get_pos(row_idx, col_idx)

        # calculate the degree of each state
        degrees = [[[0, 0] for _ in range(total_block)] for _ in range(total_block)]
        for mouse in range(total_block):
            row_mouse, col_mouse = divmod(mouse, max_col)
            if grid[row_mouse][col_mouse] == '#':
                continue
            for cat in range(total_block):
                row_cat, col_cat = divmod(cat, max_col)
                if grid[row_cat][col_cat] == '#':
                    continue
                degrees[mouse][cat][self.MOUSE_TURN] += 1
                degrees[mouse][cat][self.CAT_TURN] += 1
                for d_row, d_col in self.DIRECTION:
                    row, col, jump = row_mouse + d_row, col_mouse + d_col, 1
                    while 0 <= row < max_row and 0 <= col < max_col and grid[row][col] != '#' and jump <= mouseJump:
                        next_mouse = __get_pos(row, col)
                        next_cat = __get_pos(row_cat, col_cat)
                        degrees[next_mouse][next_cat][self.MOUSE_TURN] += 1
                        row += d_row
                        col += d_col
                        jump += 1
                    row, col, jump = row_cat + d_row, col_cat + d_col, 1
                    while 0 <= row < max_row and 0 <= col < max_col and grid[row][col] != '#' and jump <= catJump:
                        next_mouse = __get_pos(row_mouse, col_mouse)
                        next_cat = __get_pos(row, col)
                        degrees[next_mouse][next_cat][self.CAT_TURN] += 1
                        row += d_row
                        col += d_col
                        jump += 1

        res = [[[[0, 0], [0, 0]] for _ in range(total_block)] for _ in range(total_block)]
        queue = collections.deque()

        # if the cat and mouse are in the same block, then the cat wins
        for pos in range(total_block):
            row, col = divmod(pos, max_col)
            if grid[row][col] == '#':
                continue
            res[pos][pos][self.MOUSE_TURN][0] = self.CAT_WIN
            res[pos][pos][self.MOUSE_TURN][1] = 0
            res[pos][pos][self.CAT_TURN][0] = self.CAT_WIN
            res[pos][pos][self.CAT_TURN][1] = 0
            queue.append((pos, pos, self.MOUSE_TURN))
            queue.append((pos, pos, self.CAT_TURN))

        # if the cat and food are in the same block, then the cat wins
        for mouse in range(total_block):
            row_mouse, col_mouse = divmod(mouse, max_col)
            if grid[row_mouse][col_mouse] == '#' or mouse == food_pos:
                continue
            res[mouse][food_pos][self.MOUSE_TURN][0] = self.CAT_WIN
            res[mouse][food_pos][self.MOUSE_TURN][1] = 0
            res[mouse][food_pos][self.CAT_TURN][0] = self.CAT_WIN
            res[mouse][food_pos][self.CAT_TURN][1] = 0
            queue.append((mouse, food_pos, self.MOUSE_TURN))
            queue.append((mouse, food_pos, self.CAT_TURN))

        # if the mouse and food are in the same block \land cat is somewhere else, then the mouse wins
        for cat in range(total_block):
            row_cat, col_cat = divmod(cat, max_col)
            if grid[row_cat][col_cat] == '#' or cat == food_pos:
                continue
            res[food_pos][cat][self.MOUSE_TURN][0] = self.MOUSE_WIN
            res[food_pos][cat][self.MOUSE_TURN][1] = 0
            res[food_pos][cat][self.CAT_TURN][0] = self.MOUSE_WIN
            res[food_pos][cat][self.CAT_TURN][1] = 0
            queue.append((food_pos, cat, self.MOUSE_TURN))
            queue.append((food_pos, cat, self.CAT_TURN))

        def __get_prev_state(_mouse: int, _cat: int, _turn: int) -> List[Tuple[int, int, int]]:
            r_mouse, c_mouse = divmod(_mouse, max_col)
            r_cat, c_cat = divmod(_cat, max_col)
            prev_turn = self.CAT_TURN if _turn == self.MOUSE_TURN else self.MOUSE_TURN
            max_jump = mouseJump if prev_turn == self.MOUSE_TURN else catJump
            r_start = r_mouse if prev_turn == self.MOUSE_TURN else r_cat
            c_start = c_mouse if prev_turn == self.MOUSE_TURN else c_cat
            prev_state = [(_mouse, _cat, prev_turn)]
            for d_r, d_c in self.DIRECTION:
                _r, _c, _jump = r_start + d_r, c_start + d_c, 1
                while 0 <= _r < max_row and 0 <= _c < max_col and grid[_r][_c] != '#' and jump <= max_jump:
                    prev_r_mouse = _r if prev_turn == self.MOUSE_TURN else r_mouse
                    prev_c_mouse = _c if prev_turn == self.MOUSE_TURN else c_mouse
                    prev_mouse_pos = __get_pos(prev_r_mouse, prev_c_mouse)

                    prev_r_cat = r_cat if prev_turn == self.MOUSE_TURN else _r
                    prev_c_cat = c_cat if prev_turn == self.MOUSE_TURN else _c
                    prev_cat_pos = __get_pos(prev_r_cat, prev_c_cat)

                    prev_state.append((prev_mouse_pos, prev_cat_pos, prev_turn))
                    _r += d_r
                    _c += d_c
                    _jump += 1
            return prev_state

        # Topological Sorting
        while queue:
            mouse, cat, turn = queue.popleft()
            result = res[mouse][cat][turn][0]
            moves = res[mouse][cat][turn][1]
            for previous_mouse, previous_cat, previous_turn in __get_prev_state(mouse, cat, turn):
                if res[previous_mouse][previous_cat][previous_turn][0] == self.UNKNOWN:
                    if (result == self.MOUSE_WIN and previous_turn == self.MOUSE_TURN) or \
                            (result == self.CAT_WIN and previous_turn == self.CAT_TURN):
                        res[previous_mouse][previous_cat][previous_turn][0] = result
                        res[previous_mouse][previous_cat][previous_turn][1] = moves + 1
                        queue.append((previous_mouse, previous_cat, previous_turn))
                    else:
                        degrees[previous_mouse][previous_cat][previous_turn] -= 1
                        if degrees[previous_mouse][previous_cat][previous_turn] == 0:
                            loseResult = self.CAT_WIN if previous_turn == self.MOUSE_TURN else self.MOUSE_WIN
                            res[previous_mouse][previous_cat][previous_turn][0] = loseResult
                            res[previous_mouse][previous_cat][previous_turn][1] = moves + 1
                            queue.append((previous_mouse, previous_cat, previous_turn))
        if res[mouse_start_pos][cat_start_pos][self.MOUSE_TURN][0] == self.MOUSE_WIN and \
                res[mouse_start_pos][cat_start_pos][self.MOUSE_TURN][1] <= self.MAX_MOVE:
            return True
        else:
            return False


def main():
    # Example 1: Output: true
    # grid = ["####F", "#C...", "M...."]
    # catJump = 1
    # mouseJump = 2

    # Example 2: Output: true
    # grid = ["M.C...F"]
    # catJump = 1
    # mouseJump = 4

    # Example 3: Output: false
    grid = ["M.C...F"]
    catJump = 1
    mouseJump = 3

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.canMouseWin(grid, catJump, mouseJump)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
