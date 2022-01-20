#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2029-Stone-Game-IX.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-20
=================================================================="""

import sys
import time
from typing import List

"""
LeetCode - 2029 - (Medium) - Stone Game IX
https://leetcode.com/problems/stone-game-ix/

Description & Requirement:
    Alice and Bob continue their games with stones. 
    There is a row of n stones, and each stone has an associated value. 
    You are given an integer array stones, where stones[i] is the value of the ith stone.

    Alice and Bob take turns, with Alice starting first. 
    On each turn, the player may remove any stone from stones. 
    The player who removes a stone loses if the sum of the values of all removed stones is divisible by 3. 
    Bob will win automatically if there are no remaining stones (even if it is Alice's turn).

    Assuming both players play optimally, return true if Alice wins and false if Bob wins.

Example 1:
    Input: stones = [2,1]
    Output: true
    Explanation: The game will be played as follows:
        - Turn 1: Alice can remove either stone.
        - Turn 2: Bob removes the remaining stone. 
        The sum of the removed stones is 1 + 2 = 3 and is divisible by 3. Therefore, Bob loses and Alice wins the game.
Example 2:
    Input: stones = [2]
    Output: false
    Explanation: Alice will remove the only stone, and the sum of the values on the removed stones is 2. 
        Since all the stones are removed and the sum of values is not divisible by 3, Bob wins the game.
Example 3:
    Input: stones = [5,1,2,4,3]
    Output: false
    Explanation: Bob will always win. One possible way for Bob to win is shown below:
        - Turn 1: Alice can remove the second stone with value 1. Sum of removed stones = 1.
        - Turn 2: Bob removes the fifth stone with value 3. Sum of removed stones = 1 + 3 = 4.
        - Turn 3: Alices removes the fourth stone with value 4. Sum of removed stones = 1 + 3 + 4 = 8.
        - Turn 4: Bob removes the third stone with value 2. Sum of removed stones = 1 + 3 + 4 + 2 = 10.
        - Turn 5: Alice removes the first stone with value 5. Sum of removed stones = 1 + 3 + 4 + 2 + 5 = 15.
        Alice loses the game because the sum of the removed stones (15) is divisible by 3. Bob wins the game.

Constraints:
    1 <= stones.length <= 10^5
    1 <= stones[i] <= 10^4
"""


class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        # exception case
        if not isinstance(stones, list) or len(stones) <= 0:
            return False  # No stone, so Bob automatically wins
        if len(stones) == 1:
            # after Alice's first move, no stone left, so Bob wins
            return False
        if len(stones) == 2:
            if stones[0] % 3 == 0 and stones[1] % 3 == 0:
                return False  # after Alice's first move, the sum of removed number must be divided by 3, so Bob wins
            elif (stones[0] + stones[1]) % 3 == 0:
                return True  # after Bob's first move, the sum of removed number must be divided by 3, so Alice wins
            else:
                return False  # after Bob's first move, no stone left, sum not % 3 == 0, so Bob wins
        # main method: (stimulate the game playing process)
        #     there are 3 types of stones: S_0: %3==0; S_1: %3==1; S_2: %3==2.
        #     if the current removed sum can not be divided by 3 (sure, otherwise someone must lose),
        #         then the current player choose one of the S_0 stones is perfectly fine. (use up all of S_0 first)
        #     consider Alice has just chosen her first stone, now it is Bob's first attempt
        #     if the current removed sum is 1, and there's no S_0 stones, then the current player can only choose S_1,
        #         and then the sum is %3==2, so the next player can only choose S_2,
        #         and then the sum is %3==1, so back to the former situation,
        #         therefore, the choice sequence: (first sum %3==1) B1 --(%3==2)--> A2 --(%3==1)--> B1 -> A2 -> ...
        #     if the current removed sum is 2, and there's no S_0 stones, then the current player can only choose S_2,
        #         and then the sum is %3==1, so the next player can only choose S_1,
        #         and then the sum is %3==2, so back to the former situation,
        #         therefore, the choice sequence: (first sum %3==2) B2 --(%3==1)--> A1 --(%3==2)--> B2 -> A1 -> ...
        #     Therefore, if there's no S_0, the choice sequence from Alice's first choice can only be two types:
        #         A1 -> B1 -> A2 -> B1 -> A2 -> B1 -> A2 -> ...
        #     or  A2 -> B2 -> A1 -> B2 -> A1 -> B2 -> A1 -> ...
        return self._stoneGameIX(stones)

    def _stoneGameIX(self, stones: List[int]) -> bool:
        len_stones = len(stones)
        assert len_stones > 2

        # count all 3 types of stones
        s_0 = s_1 = s_2 = 0
        for stone in stones:
            if stone % 3 == 0:
                s_0 += 1
            elif stone % 3 == 1:
                s_1 += 1
            elif stone % 3 == 2:
                s_2 += 1
            else:
                pass  # error number

        # choose S_0 stones first, so only left one or zero S_0 stone
        s_0 &= 0x01

        # if there's no S_1 and S_2, Alice must lose
        if s_1 == 0 and s_2 == 0:
            return False

        # if there's no S_1
        if s_1 == 0:
            # if there's no s_0, the seq must be: A2 B2 A2 -> Alice loses (or use up stones early, also Alice loses)
            if s_0 == 0:
                return False
            # if there's one s_0, the result depends on the number of S_2
            else:
                if s_2 <= 2:  # seq: A2 B0 or A2 B0 A2 -> Bob wins (coz no stone left)
                    return False
                else:  # seq: A2 B0 A2 B2 or A2 B2 A0 B2 -> Alice wins (coz after Bob's move, sum %3==0)
                    return True

        # if there's no S_2
        if s_2 == 0:
            # if there's no s_0, the seq must be: A1 B1 A1 -> Alice loses (or use up stones early, also Alice loses)
            if s_0 == 0:
                return False
            # if there's one s_0, the result depends on the number of S_1
            else:
                if s_1 <= 2:  # seq: A1 B0 or A1 B0 A1 -> Bob wins (coz no stone left)
                    return False
                else:  # seq: A1 B0 A1 B1 or A1 B1 A0 B1 -> Alice wins (coz after Bob's move, sum %3==0)
                    return True

        # now, S_1 and S_2 both >= 1
        # (SEQ1) if Alice's first choice is S_1, and there's no S_0, then the seq is (A1) B1 A2 B1 A2 B1 A2 B1 A2 ...
        #     it means Alice only remove S_1 at the first step, then always remove S_2, while Bob always remove S_1
        # (SEQ2) if Alice's first choice is S_2, and there's no S_0, then the seq is (A2) B2 A1 B2 A1 B2 A1 B2 A1 ...
        #     it means Alice only remove S_2 at the first step, then always remove S_1, while Bob always remove S_2

        if s_1 == s_2:
            if s_0 == 0:  # Alice must win: choose SEQ1 or SEQ2 (Bob will lose because eventually sum %3==0)
                return True
            else:  # whatever SEQ Alice choose, Bob can always maintain the SEQ till all stones are used up, so Bob wins
                return False

        if s_1 < s_2:
            if s_0 == 0:  # Alice must win: choose SEQ1 (Bob will lose because eventually sum %3==0)
                return True
            else:
                # if Alice choose SEQ1, Bob can use S_0 to force Alice to remove S_1: (A1 B0) A1 B2 A1 B2 ...
                # this is not optimal for Alice, so she has to choose SEQ2,
                # in this case, Bob's first choice still has to be S_0, because if (A2) B2, then Alice can get A0,
                #     later, Bob has to remove S_1 all the time, which is more likely to lose (s_1 < s_2)
                # therefore, the optimal seq: (A2 B0) A2 B1 A2 B1 A2 B1 ...
                # if 1 <= s_2 - s_1 <= 2, then Bob can always maintain the SEQ till all stones are used up, so Bob wins
                # if s_2 - s_1 >= 3, then Bob can not maintain the SEQ and eventually sum %3==0, so Alice wins
                return (s_2 - s_1) >= 3

        if s_1 > s_2:
            if s_0 == 0:  # Alice must win: choose SEQ2 (Bob will lose because eventually sum %3==0)
                return True
            else:
                # similar analysis with the case s_1 < s_2
                return (s_1 - s_2) >= 3

        return True  # won't reach here


def main():
    # Example 1: Output: true
    # stones = [2, 1]

    # Example 2: Output: false
    # stones = [2]

    # Example 3: Output: false
    # stones = [5, 1, 2, 4, 3]

    # Example 4: Output: true
    stones = [19, 2, 17, 20, 7, 17]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.stoneGameIX(stones)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
