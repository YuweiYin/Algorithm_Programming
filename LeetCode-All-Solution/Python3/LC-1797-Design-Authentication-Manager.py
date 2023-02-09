#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1797-Design-Authentication-Manager.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-02-09
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 1797 - (Medium) - Design Authentication Manager
https://leetcode.com/problems/design-authentication-manager/

Description & Requirement:
There is an authentication system that works with authentication tokens. For each session, the user will receive a new authentication token that will expire timeToLive seconds after the currentTime. If the token is renewed, the expiry time will be extended to expire timeToLive seconds after the (potentially different) currentTime.

Implement the AuthenticationManager class:

AuthenticationManager(int timeToLive) constructs the AuthenticationManager and sets the timeToLive.
generate(string tokenId, int currentTime) generates a new token with the given tokenId at the given currentTime in seconds.
renew(string tokenId, int currentTime) renews the unexpired token with the given tokenId at the given currentTime in seconds. If there are no unexpired tokens with the given tokenId, the request is ignored, and nothing happens.
countUnexpiredTokens(int currentTime) returns the number of unexpired tokens at the given currentTime.
Note that if a token expires at time t, and another action happens on time t (renew or countUnexpiredTokens), the expiration takes place before the other actions.

 

Example 1:
    Input
        ["AuthenticationManager", "renew", "generate", "countUnexpiredTokens", 
            "generate", "renew", "renew", "countUnexpiredTokens"]
        [[5], ["aaa", 1], ["aaa", 2], [6], ["bbb", 7], ["aaa", 8], ["bbb", 10], [15]]
    Output
        [null, null, null, 1, null, null, null, 0]
    Explanation
        AuthenticationManager authenticationManager = new AuthenticationManager(5); 
            // Constructs the AuthenticationManager with timeToLive = 5 seconds.
        authenticationManager.renew("aaa", 1); 
            // No token exists with tokenId "aaa" at time 1, so nothing happens.
        authenticationManager.generate("aaa", 2); 
            // Generates a new token with tokenId "aaa" at time 2.
        authenticationManager.countUnexpiredTokens(6); 
            // The token with tokenId "aaa" is the only unexpired one at time 6, so return 1.
        authenticationManager.generate("bbb", 7); 
            // Generates a new token with tokenId "bbb" at time 7.
        authenticationManager.renew("aaa", 8); 
            // The token with tokenId "aaa" expired at time 7, and 8 >= 7, 
            // so at time 8 the renew request is ignored, and nothing happens.
        authenticationManager.renew("bbb", 10); 
            // The token with tokenId "bbb" is unexpired at time 10, 
            // so the renew request is fulfilled and now the token will expire at time 15.
        authenticationManager.countUnexpiredTokens(15); 
            // The token with tokenId "bbb" expires at time 15, and the token with tokenId "aaa" expired at time 7, 
            // so currently no token is unexpired, so return 0.

Constraints:
    1 <= timeToLive <= 10^8
    1 <= currentTime <= 10^8
    1 <= tokenId.length <= 5
    tokenId consists only of lowercase letters.
    All calls to generate will contain unique values of tokenId.
    The values of currentTime across all the function calls will be strictly increasing.
    At most 2000 calls will be made to all functions combined.
"""


class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.hash_map = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.hash_map[tokenId] = currentTime + self.ttl

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.hash_map and self.hash_map[tokenId] > currentTime:
            self.hash_map[tokenId] = self.ttl + currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        res = 0
        for _time in self.hash_map.values():
            if _time > currentTime:
                res += 1
        return res


def main():
    # Example 1: Output: [null, null, null, 1, null, null, null, 0]
    command_list = ["AuthenticationManager", "renew", "generate", "countUnexpiredTokens",
                    "generate", "renew", "renew", "countUnexpiredTokens"]
    param_list = [[5], ["aaa", 1], ["aaa", 2], [6], ["bbb", 7], ["aaa", 8], ["bbb", 10], [15]]

    # init instance
    # solution = Solution()
    timeToLive = param_list[0][0]
    obj = AuthenticationManager(timeToLive)
    ans = ["null"]

    # run & time
    start = time.process_time()
    assert len(command_list) == len(param_list)
    for idx in range(1, len(command_list)):
        command = command_list[idx]
        param = param_list[idx]
        if command == "renew" and isinstance(param, list) and len(param) == 2:
            obj.renew(param[0], param[1])
            ans.append("null")
        elif command == "generate" and isinstance(param, list) and len(param) == 2:
            obj.generate(param[0], param[1])
            ans.append("null")
        elif command == "countUnexpiredTokens" and isinstance(param, list) and len(param) == 1:
            ans.append(obj.countUnexpiredTokens(param[0]))
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
