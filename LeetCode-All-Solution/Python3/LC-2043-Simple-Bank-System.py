#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2043-Simple-Bank-System.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-18
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 2043 - (Medium) - Simple Bank System
https://leetcode.com/problems/simple-bank-system/

Description & Requirement:
    You have been tasked with writing a program for a popular bank that will automate all its incoming transactions 
    (transfer, deposit, and withdraw). The bank has n accounts numbered from 1 to n. 
    The initial balance of each account is stored in a 0-indexed integer array balance, 
    with the (i + 1)th account having an initial balance of balance[i].

    Execute all the valid transactions. A transaction is valid if:
        The given account number(s) are between 1 and n, and
        The amount of money withdrawn or transferred from is less than or equal to the balance of the account.

    Implement the Bank class:
        Bank(long[] balance) Initializes the object with the 0-indexed integer array balance.
        boolean transfer(int account1, int account2, long money) Transfers money dollars 
            from the account numbered account1 to the account numbered account2. 
            Return true if the transaction was successful, false otherwise.
        boolean deposit(int account, long money) Deposit money dollars into the account numbered account. 
            Return true if the transaction was successful, false otherwise.
        boolean withdraw(int account, long money) Withdraw money dollars from the account numbered account. 
            Return true if the transaction was successful, false otherwise.

Example 1:
    Input
        ["Bank", "withdraw", "transfer", "deposit", "transfer", "withdraw"]
        [[[10, 100, 20, 50, 30]], [3, 10], [5, 1, 20], [5, 20], [3, 4, 15], [10, 50]]
    Output
        [null, true, true, true, false, false]
    
    Explanation
        Bank bank = new Bank([10, 100, 20, 50, 30]);
        bank.withdraw(3, 10);    // return true, account 3 has a balance of $20, so it is valid to withdraw $10.
                                 // Account 3 has $20 - $10 = $10.
        bank.transfer(5, 1, 20); // return true, account 5 has a balance of $30, so it is valid to transfer $20.
                                 // Account 5 has $30 - $20 = $10, and account 1 has $10 + $20 = $30.
        bank.deposit(5, 20);     // return true, it is valid to deposit $20 to account 5.
                                 // Account 5 has $10 + $20 = $30.
        bank.transfer(3, 4, 15); // return false, the current balance of account 3 is $10,
                                 // so it is invalid to transfer $15 from it.
        bank.withdraw(10, 50);   // return false, it is invalid because account 10 does not exist.

Constraints:
    n == balance.length
    1 <= n, account, account1, account2 <= 10^5
    0 <= balance[i], money <= 1012
    At most 10^4 calls will be made to each function transfer, deposit, withdraw.
"""


class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 <= 0 or account1 > len(self.balance):
            return False
        if account2 <= 0 or account2 > len(self.balance):
            return False
        if self.balance[account1 - 1] >= money:
            self.balance[account1 - 1] -= money
            self.balance[account2 - 1] += money
            return True
        else:
            return False

    def deposit(self, account: int, money: int) -> bool:
        if account <= 0 or account > len(self.balance):
            return False
        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if account <= 0 or account > len(self.balance):
            return False
        if self.balance[account - 1] >= money:
            self.balance[account - 1] -= money
            return True
        else:
            return False


def main():
    # Example 1: Output: [null, true, true, true, false, false]
    command_list = ["Bank", "withdraw", "transfer", "deposit", "transfer", "withdraw"]
    param_list = [[[10, 100, 20, 50, 30]], [3, 10], [5, 1, 20], [5, 20], [3, 4, 15], [10, 50]]

    # init instance
    # solution = Solution()
    balance = param_list[0][0]
    obj = Bank(balance)

    # run & time
    start = time.process_time()
    ans = ["null"]
    assert len(command_list) == len(param_list)
    for idx in range(1, len(command_list)):
        command = command_list[idx]
        param = param_list[idx]
        if command == "transfer":
            if isinstance(param, list) and len(param) == 3:
                ans.append(obj.transfer(param[0], param[1], param[2]))
            else:
                ans.append("null")
        elif command == "deposit":
            if isinstance(param, list) and len(param) == 2:
                ans.append(obj.deposit(param[0], param[1]))
            else:
                ans.append("null")
        elif command == "withdraw":
            if isinstance(param, list) and len(param) == 2:
                ans.append(obj.withdraw(param[0], param[1]))
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
