#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0811-Subdomain-Visit-Count.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-10-05
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0811 - (Medium) - Subdomain Visit Count
https://leetcode.com/problems/subdomain-visit-count/

Description & Requirement:
    A website domain "discuss.leetcode.com" consists of various subdomains. At the top level, we have "com", 
    at the next level, we have "leetcode.com" and at the lowest level, "discuss.leetcode.com". 
    When we visit a domain like "discuss.leetcode.com", 
    we will also visit the parent domains "leetcode.com" and "com" implicitly.

    A count-paired domain is a domain that has one of the two formats "rep d1.d2.d3" or "rep d1.d2" 
    where rep is the number of visits to the domain and d1.d2.d3 is the domain itself.

        For example, "9001 discuss.leetcode.com" is a count-paired domain that 
        indicates that discuss.leetcode.com was visited 9001 times.

    Given an array of count-paired domains cpdomains, 
    return an array of the count-paired domains of each subdomain in the input. 
    You may return the answer in any order.

Example 1:
    Input: cpdomains = ["9001 discuss.leetcode.com"]
    Output: ["9001 leetcode.com","9001 discuss.leetcode.com","9001 com"]
    Explanation: We only have one website domain: "discuss.leetcode.com".
        As discussed above, the subdomain "leetcode.com" and "com" will also be visited. 
        So they will all be visited 9001 times.
Example 2:
    Input: cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
    Output: ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
    Explanation: We will visit "google.mail.com" 900 times, 
        "yahoo.com" 50 times, "intel.mail.com" once and "wiki.org" 5 times.
        For the subdomains, we will visit "mail.com" 900 + 1 = 901 times, 
        "com" 900 + 50 + 1 = 951 times, and "org" 5 times.

Constraints:
    1 <= cpdomain.length <= 100
    1 <= cpdomain[i].length <= 100
    cpdomain[i] follows either the "repi d1i.d2i.d3i" format or the "repi d1i.d2i" format.
    repi is an integer in the range [1, 10^4].
    d1i, d2i, and d3i consist of lowercase English letters.
"""


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        # exception case
        assert isinstance(cpdomains, list) and len(cpdomains) >= 1
        for domain in cpdomains:
            assert isinstance(domain, str) and len(domain) >= 1
        # main method: (break down each domain and store them in a hash dict)
        return self._subdomainVisits(cpdomains)

    def _subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        assert isinstance(cpdomains, list) and len(cpdomains) >= 1

        hash_dict = dict({})
        for domain in cpdomains:
            repi, domain = domain.split()
            repi = int(repi)
            domain_list = domain.split(".")

            cur_d = ""
            for d in domain_list[::-1]:
                cur_d = "." + d + cur_d
                if cur_d not in hash_dict:
                    hash_dict[cur_d] = repi
                else:
                    hash_dict[cur_d] += repi

        res = []
        for k, v in hash_dict.items():
            res.append(f"{str(v)} {k[1:]}")

        return res


def main():
    # Example 1: Output: ["9001 leetcode.com","9001 discuss.leetcode.com","9001 com"]
    # cpdomains = ["9001 discuss.leetcode.com"]

    # Example 2: Output: ["901 mail.com","50 yahoo.com","900 google.mail.com",
    #     "5 wiki.org","5 org","1 intel.mail.com","951 com"]
    cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.subdomainVisits(cpdomains)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
