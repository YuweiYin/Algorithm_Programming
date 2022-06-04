#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0929-Unique-Email-Addresses.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-06-04
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0929 - (Easy) - Unique Email Addresses
https://leetcode.com/problems/unique-email-addresses/

Description & Requirement:
    Every valid email consists of a local name and a domain name, separated by the '@' sign. 
    Besides lowercase letters, the email may contain one or more '.' or '+'.

    For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.
    If you add periods '.' between some characters in the local name part of an email address, 
    mail sent there will be forwarded to the same address without dots in the local name. 
    Note that this rule does not apply to domain names.

    For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
    If you add a plus '+' in the local name, everything after the first plus sign will be ignored. 
    This allows certain emails to be filtered. Note that this rule does not apply to domain names.

    For example, "m.y+name@email.com" will be forwarded to "my@email.com".
    It is possible to use both of these rules at the same time.

    Given an array of strings emails where we send one email to each emails[i], return the number of different addresses that actually receive mails.

Example 1:
    Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    Output: 2
    Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.
Example 2:
    Input: emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
    Output: 3

Constraints:
    1 <= emails.length <= 100
    1 <= emails[i].length <= 100
    emails[i] consist of lowercase English letters, '+', '.' and '@'.
    Each emails[i] contains exactly one '@' character.
    All local and domain names are non-empty.
    Local names do not start with a '+' character.
    Domain names end with the ".com" suffix.
"""


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # exception case
        assert isinstance(emails, list) and len(emails) >= 1
        # main method: (hash set & rules)
        return self._numUniqueEmails(emails)

    def _numUniqueEmails(self, emails: List[str]) -> int:
        assert isinstance(emails, list) and len(emails) >= 1

        res = set()
        for email in emails:
            at_idx = email.index("@")
            local_name = email[:at_idx].split("+", 1)[0]  # get rid of the part after the first "+"
            local_name = local_name.replace(".", "")  # remove all "."
            cur_email = local_name + email[at_idx:]
            if cur_email not in res:
                res.add(local_name + email[at_idx:])

        return len(res)


def main():
    # Example 1: Output: 2
    emails = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]

    # Example 2: Output: 3
    # emails = ["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.numUniqueEmails(emails)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
