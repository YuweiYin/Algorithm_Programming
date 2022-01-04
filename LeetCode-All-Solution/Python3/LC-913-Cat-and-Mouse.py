#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-913-Cat-and-Mouse.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-04
=================================================================="""

import sys
import time
from typing import List

"""
LeetCode - 913 - (Hard) - Cat and Mouse
https://leetcode.com/problems/cat-and-mouse/

Description:
    A game on an undirected graph is played by two players, Mouse and Cat, who alternate turns.
    The graph is given as follows: graph[a] is a list of all nodes b such that a-b is an edge of the graph.
    The mouse starts at node 1 and goes first, the cat starts at node 2 and goes second, and there is a hole at node 0.
    During each player's turn, they must travel along one edge of the graph that meets where they are.
    For example, if the Mouse is at node 1, it must travel to any node in graph[1].

    Additionally, it is not allowed for the Cat to travel to the Hole (node 0.)
    Then, the game can end in three ways:
        If ever the Cat occupies the same node as the Mouse, the Cat wins.
        If ever the Mouse reaches the Hole, the Mouse wins.
        If ever a position is repeated (i.e., the players are in the same position as a previous turn, 
            and it is the same player's turn to move), the game is a draw.
Requirement:
    Given a graph, and assuming both players play optimally, return
        1 if the mouse wins the game,
        2 if the cat wins the game, or
        0 if the game is a draw.

Example 1:
    Input: graph = [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
    Output: 0
Example 2:
    Input: graph = [[1,3],[0],[3],[0,2]]
    Output: 1

Constraints:
    3 <= graph.length <= 50
    1 <= graph[i].length < graph.length
    0 <= graph[i][j] < graph.length
    graph[i][j] != i
    graph[i] is unique.
    The mouse and the cat can always move.
"""


class Solution:
    def __init__(self):
        self.GAME_DRAW = 0
        self.MOUSE_WIN = 1
        self.CAT_WIN = 2

    def catMouseGame(self, graph: List[List[int]]) -> int:
        # exception case
        if not isinstance(graph, list) or len(graph) <= 0:
            return 0
        # main method: (Game Theory & Dynamic Programming O(n^4))
        return self._catMouseGame(graph)

    def _catMouseGame(self, graph: List[List[int]]) -> int:
        """
        - According to Game Theory [Zermelo's theorem](https://abel.math.harvard.edu/~elkies/FS23j.03/zermelo.pdf)
        In game theory, Zermelo's theorem is a theorem about finite two-person games of perfect information
        in which the players move alternately and in which chance does not affect the decision-making process.
        It says that if the game cannot end in a draw, then one of the two players must have a winning strategy
        (i.e. force a win). An alternate statement is that for a game meeting all of these conditions
        except the condition that a draw is not possible, then either the first-player can force a win,
        or the second-player can force a win, or both players can force a draw.
        The theorem is named after Ernst Zermelo, a German mathematician and logician.
        Zermelo's theorem can be proofed by mathematical induction.

        - In this problem, either the mouse wins or the cat wins or draw.
        - Dynamic Programming state: dp[mouse_position][cat_position][turn_count] = -1; 0; 1; 2
            - If mouse_position == 0, then return self.MOUSE_WIN: dp[0][cat_position][turn_count] = self.MOUSE_WIN;
            - If mouse_position == cat_position = x != 0, then return self.CAT_WIN: dp[x][x][turn_count] = self.CAT_WIN;
            - If turn_count >= 2n-1, then return self.GAME_DRAW, because:
                - The turn_count has increased from 0 to 2n-1, which means players have moved 2n-1 turns (mouse first).
                - The mouse have traveled n nodes but didn't reach the hole, so it must have repeated at least one node;
                - And the cat have traveled n-1 nodes but didn't catch the mouse, so it must have repeated too.
                - (The cat can't reach to hole, so there are only n-1 nodes for it to move, including its initial node.)
        """
        n = len(graph)
        max_turn = (n << 1) - 1
        # max_turn = n << 1
        # dp[mouse_position][cat_position][turn_count] = -1: can't tell who will definitely win at the moment
        # dp[mouse_position][cat_position][turn_count] = 0: the game will definitely be a draw
        # dp[mouse_position][cat_position][turn_count] = 1: the mouse will definitely win
        # dp[mouse_position][cat_position][turn_count] = 2: the cat will definitely win
        dp = [[[-1 for _ in range(n << 1)] for _ in range(n)] for _ in range(n)]  # n * n * 2n

        def __get_result_from_dp_state(mouse_position: int, cat_position: int, turn_count: int) -> int:
            """
            - Judge the game result from the current dp state.
            - -1: not sure; 0: must be a draw; 1: the mouse must win; 2: the cat must win.
            - If 0/1/2 cannot be determined from the current state, then call `__get_next_dp_state` to continue game.
            """
            if turn_count == max_turn:  # both the cat and mouse can't win anymore, it must be a draw
                return self.GAME_DRAW

            res = dp[mouse_position][cat_position][turn_count]  # get current state value
            if res != -1:  # if res != -1: the game must be either a draw or mouse's win or cat's win
                return res

            # now, res == -1: can't tell who will definitely win at the moment
            # according to current position state, decide either mouse or cat or no one will definitely win
            if mouse_position == 0:  # the mouse reach the hole, so the mouse will definitely win
                res = self.MOUSE_WIN
            elif cat_position == mouse_position:  # the cat catch the mouse, so the cat will definitely win
                res = self.CAT_WIN
            else:  # can't tell who will definitely win now, so take the next turn and keep moving
                res = __get_next_dp_state(mouse_position, cat_position, turn_count)  # DFS till determine a must-winner

            # now, the dp value has been calculated, the game must be either a draw or the mouse's win or the cat's win
            dp[mouse_position][cat_position][turn_count] = res  # update the dp state tensor
            return res  # return res recursively (note that res won't be -1 now)

        def __get_next_dp_state(mouse_position: int, cat_position: int, turn_count: int) -> int:
            """
            - Entering this function means that the former turn/state cannot determine a winner or the game is a draw,
            - So the game will continue and search every possible position to move
            - After each movement, call `__get_result_from_dp_state` to see if the game result can be determined
            """
            cur_move = cat_position if (turn_count & 0x01) else mouse_position  # odd: cat move; even: mouse move
            # set an impossible res (If this is not the mouse's turn, it cannot win, so does the cat) as default
            default_res = self.MOUSE_WIN if cur_move != mouse_position else self.CAT_WIN
            res = default_res
            # cur_move player move to all possible next_move_position
            for next_move_position in graph[cur_move]:
                if cur_move == cat_position and next_move_position == 0:
                    continue  # cat can't move to the hole (node 0)

                # next_mouse_position is the mouse_position in next dp state;
                # if currently mouse move, then next_mouse_position = next_move_position, else mouse will stay still
                next_mouse_position = next_move_position if cur_move == mouse_position else mouse_position
                next_cat_position = next_move_position if cur_move == cat_position else cat_position

                # do move, and check the next dp state, see if the winner or draw can be determined
                next_res = __get_result_from_dp_state(next_mouse_position, next_cat_position, turn_count + 1)

                # trim DFS tree (note that the return value of __get_result_from_dp_state won't be -1)
                if next_res != default_res:  # this means next_res is not impossible (= 0 or (1 xor 2))
                    res = next_res  # update res, which will be returned to the upper recursion
                    if res != self.GAME_DRAW:  # this means next_res has determined a winner (1 xor 2)
                        break  # game over, stop DFS. (when res is 0, there may be a must-winner later, so keep moving)
            return res

        # initial state: mouse_position = 1, cat_position = 2, turn_count = 0
        return __get_result_from_dp_state(1, 2, 0)


def main():
    # Example 1: Output: 0
    graph = [[2, 5], [3], [0, 4, 5], [1, 4, 5], [2, 3], [0, 2, 3]]

    # Example 2: Output: 1
    # graph = [[1, 3], [0], [3], [0, 2]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.catMouseGame(graph)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
