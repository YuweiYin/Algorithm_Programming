#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1994-The-Number-of-Good-Subsets.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-22
=================================================================="""

import sys
import time
from typing import List
import collections

"""
LeetCode - 1994 - (Hard) - The Number of Good Subsets
https://leetcode.com/problems/the-number-of-good-subsets/

Description & Requirement:
    You are given an integer array nums. We call a subset of nums good 
    if its product can be represented as a product of one or more distinct prime numbers.

    For example, if nums = [1, 2, 3, 4]:
        [2, 3], [1, 2, 3], and [1, 3] are good subsets with products 6 = 2*3, 6 = 2*3, and 3 = 3 respectively.
        [1, 4] and [4] are not good subsets with products 4 = 2*2 and 4 = 2*2 respectively.

    Return the number of different good subsets in nums modulo 109 + 7.

    A subset of nums is any array that can be obtained by deleting some (possibly none or all) elements from nums. 
    Two subsets are different if and only if the chosen indices to delete are different.

Example 1:
    Input: nums = [1,2,3,4]
    Output: 6
    Explanation: The good subsets are:
        - [1,2]: product is 2, which is the product of distinct prime 2.
        - [1,2,3]: product is 6, which is the product of distinct primes 2 and 3.
        - [1,3]: product is 3, which is the product of distinct prime 3.
        - [2]: product is 2, which is the product of distinct prime 2.
        - [2,3]: product is 6, which is the product of distinct primes 2 and 3.
        - [3]: product is 3, which is the product of distinct prime 3.
Example 2:
    Input: nums = [4,2,3,15]
    Output: 5
    Explanation: The good subsets are:
        - [2]: product is 2, which is the product of distinct prime 2.
        - [2,3]: product is 6, which is the product of distinct primes 2 and 3.
        - [2,15]: product is 30, which is the product of distinct primes 2, 3, and 5.
        - [3]: product is 3, which is the product of distinct prime 3.
        - [15]: product is 15, which is the product of distinct primes 3 and 5.

Constraints:
    1 <= nums.length <= 10^5
    1 <= nums[i] <= 30
"""


class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        # exception case
        if not isinstance(nums, list) or len(nums) <= 0:
            return 0 # Error input type
        # main method: (Dynamic Programming)
        # every integer that > 1 can be converted into the product of some prime numbers,
        # consider this conversion for each number in nums list,
        # when a good subset has some prime factors, the new number can be incorporated if prime factors don't overlap
        # dfs & backtrace find all good subsets
        # note that, in this problem, duplicate result is not pointless
        #     e.g., for set {2, 2}, the subset {2} (index=0) and {2} (index=1) are considered as different subsets
        # return self._numberOfGoodSubsetsNoDuplication(nums)  # TLE
        # return self._numberOfGoodSubsetsWithDuplication(nums)  # TLE
        return self._numberOfGoodSubsetsDP(nums)

    def _numberOfGoodSubsetsNoDuplication(self, nums: List[int]) -> int:
        len_nums = len(nums)
        assert len_nums > 0

        # MOD = int(1e9+7)
        # MAX_NUM = 30  # 1 <= nums[i] <= 30

        # def __get_prime_sieve_of_Eratosthenes(max_size: int) -> list:
        #     prime_number = [0 for _ in range(max_size)]  # prime number sequence: 2, 3, 5, 7, ... (1-indexed)
        #     prime_counter = 0
        #     used_prime = [False for _ in range(max_size)]  # record the used prime numbers, for sieve
        #     used_prime[0] = used_prime[1] = True  # 0 and 1 are not prime number
        #
        #     cur_prime = 2
        #     while cur_prime < max_size:
        #         if not used_prime[cur_prime]:  # add cur_prime into prime_number sequence
        #             prime_counter += 1
        #             prime_number[prime_counter] = cur_prime
        #         # sieve all composite numbers based on cur_prime (also, limited by max_size)
        #         sieve_index = 1
        #         while sieve_index <= prime_counter and cur_prime * prime_number[sieve_index] < max_size:
        #             used_prime[cur_prime * prime_number[sieve_index]] = True  # do sieve
        #             if prime_number[sieve_index] == 0:  # already 0, stop sieve
        #                 break
        #             sieve_index += 1
        #         cur_prime += 1
        #
        #     return prime_number

        # get prime numbers that <= MAX_NUM
        # prime_number_seq = __get_prime_sieve_of_Eratosthenes(max_size=MAX_NUM)
        # prime_number_set = set(prime_number_seq)
        # if 0 in prime_number_set:
        #     prime_number_set.discard(0)
        # del prime_number_seq

        # prime_number_set = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29}  # prime number set
        prime_number_dict = dict({
            2: False, 3: False, 5: False, 7: False, 11: False,
            13: False, 17: False, 19: False, 23: False, 29: False
        })  # key: prime number; value: True if it has been used, False otherwise
        num_with_square_factor = {4, 8, 9, 12, 16, 18, 20, 24, 25, 27, 28}  # (k n^2) won't be a element of good subset
        other_num = dict({
            6: {2, 3}, 10: {2, 5}, 14: {2, 7}, 15: {3, 5}, 21: {3, 7}, 22: {2, 11}, 26: {2, 13}, 30: {2, 3, 5}
        })  # key: a non-prime number; value: the prime factor set

        # counter of each num in nums (duplicate num in nums is pointless)
        # nums_counter = dict({})
        # for num in nums:
        #     if num not in nums_counter:
        #         nums_counter[num] = 1
        #     else:
        #         nums_counter[num] += 1
        nums_unique = set(nums).difference(num_with_square_factor)
        exist_1 = False
        if 1 in nums_unique:
            exist_1 = True
            nums_unique.discard(1)
        nums_unique = list(nums_unique)
        len_nums = len(nums_unique)

        good_subsets = set()  # all good subsets

        def __dfs(cur_subset: List[int], cur_num_index: int):
            if cur_num_index >= len_nums:
                return
            cur_num = nums_unique[cur_num_index]
            new_prime_factors = []
            can_put_in = True
            # if cur_num is a prime
            if cur_num in prime_number_dict:
                if not prime_number_dict[cur_num]:
                    new_prime_factors.append(cur_num)  # this prime factor will be joined in
                else:
                    can_put_in = False  # the prime factor has been used
            # if cur_num is not prime or 1, and don't have square factors
            elif cur_num in other_num:
                for factor in other_num[cur_num]:
                    if prime_number_dict[factor]:
                        can_put_in = False  # the prime factor has been used
                        break
                if can_put_in:  # all prime factors have not been used
                    for factor in other_num[cur_num]:  # all these prime factors will be joined in
                        new_prime_factors.append(factor)
            else:
                can_put_in = False

            if can_put_in:
                for factor in new_prime_factors:  # mark the new prime factors as used
                    prime_number_dict[factor] = True
                cur_subset.append(cur_num)  # append new number
                if tuple(cur_subset) not in good_subsets:  # avoid duplicate result
                    good_subsets.add(tuple(cur_subset[:]))  # new res
                for next_num_index in range(cur_num_index + 1, len_nums):  # explore all rest numbers
                    __dfs(cur_subset, next_num_index)  # go deeper
                # backtrace
                cur_subset.pop()
                for factor in new_prime_factors:
                    prime_number_dict[factor] = False
            else:  # skip this number
                for next_num_index in range(cur_num_index + 1, len_nums):  # explore all rest numbers
                    __dfs(cur_subset, next_num_index)  # go deeper

        for start_num_index in range(len_nums):  # start from every number
            __dfs([], start_num_index)

        # if 1 exist, all good subsets can be appended by 1, result *= 2
        return len(good_subsets) << 1 if exist_1 else len(good_subsets)

    def _numberOfGoodSubsetsWithDuplication(self, nums: List[int]) -> int:
        len_nums = len(nums)
        assert len_nums > 0

        # prime_number_set = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29}  # prime number set
        prime_number_dict = dict({
            2: False, 3: False, 5: False, 7: False, 11: False,
            13: False, 17: False, 19: False, 23: False, 29: False
        })  # key: prime number; value: True if it has been used, False otherwise
        num_with_square_factor = {4, 8, 9, 12, 16, 18, 20, 24, 25, 27, 28}  # (k n^2) won't be a element of good subset
        other_num = dict({
            6: {2, 3}, 10: {2, 5}, 14: {2, 7}, 15: {3, 5}, 21: {3, 7}, 22: {2, 11}, 26: {2, 13}, 30: {2, 3, 5}
        })  # key: a non-prime number; value: the prime factor set

        # counter of each num in nums (duplicate num in nums is NOT pointless)
        nums_counter = dict({})
        for num in nums:
            if num not in nums_counter:
                nums_counter[num] = 1
            else:
                nums_counter[num] += 1

        # counter of 1
        if 1 in nums_counter:
            exist_1_counter = nums_counter[1]
            nums_counter.pop(1)
        else:
            exist_1_counter = 0

        # get rid of numbers in num_with_square_factor set, because they won't be factors of good subsets
        todo_nums_dict = dict({})
        for num, counter in nums_counter.items():
            if num not in num_with_square_factor:
                todo_nums_dict[num] = counter
        del nums_counter

        todo_nums_list = list(todo_nums_dict.keys())
        len_nums = len(todo_nums_list)

        good_subsets = set()  # all good subsets
        res = [0]  # use list so that can be maintained in `__dfs` function

        def __dfs(cur_subset: List[int], cur_num_index: int):
            if cur_num_index >= len_nums:
                return
            cur_num = todo_nums_list[cur_num_index]
            new_prime_factors = []
            can_put_in = True
            # if cur_num is a prime
            if cur_num in prime_number_dict:
                if not prime_number_dict[cur_num]:
                    new_prime_factors.append(cur_num)  # this prime factor will be joined in
                else:
                    can_put_in = False  # the prime factor has been used
            # if cur_num is not prime or 1, and don't have square factors
            elif cur_num in other_num:
                for factor in other_num[cur_num]:
                    if prime_number_dict[factor]:
                        can_put_in = False  # the prime factor has been used
                        break
                if can_put_in:  # all prime factors have not been used
                    for factor in other_num[cur_num]:  # all these prime factors will be joined in
                        new_prime_factors.append(factor)
            else:
                can_put_in = False

            if can_put_in:
                for factor in new_prime_factors:  # mark the new prime factors as used
                    prime_number_dict[factor] = True
                cur_subset.append(cur_num)  # append new number
                if tuple(cur_subset) not in good_subsets:  # avoid duplicate result
                    good_subsets.add(tuple(cur_subset[:]))  # new res
                    res_gain = 1
                    for _num in cur_subset:  # consider the counter of all numbers in cur_subset
                        res_gain *= todo_nums_dict[_num]
                    res[0] += res_gain
                for next_num_index in range(cur_num_index + 1, len_nums):  # explore all rest numbers
                    __dfs(cur_subset, next_num_index)  # go deeper
                # backtrace
                cur_subset.pop()
                for factor in new_prime_factors:
                    prime_number_dict[factor] = False
            else:  # skip this number
                for next_num_index in range(cur_num_index + 1, len_nums):  # explore all rest numbers
                    __dfs(cur_subset, next_num_index)  # go deeper

        for start_num_index in range(len_nums):  # start from every number
            __dfs([], start_num_index)

        # if 1 exist, all good subsets can be appended by 1, result *= (exist_1_counter + 1)
        return res[0] * (exist_1_counter + 1) if exist_1_counter > 0 else res[0]

    def _numberOfGoodSubsetsDP(self, nums: List[int]) -> int:
        MOD = int(1e9 + 7)
        prime_number_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]  # prime number list
        num_with_square_factor = {4, 8, 9, 12, 16, 18, 20, 24, 25, 27, 28}  # (k n^2) won't be a element of good subset

        len_prime = len(prime_number_list)

        # counter of each num in nums (duplicate num in nums is NOT pointless)
        num_counter = collections.Counter(nums)

        # dp[i][j] is the number of subsets using numbers 2, 3, ..., i
        #     and use j mask to indicate whether a prime is used
        dp = [0 for _ in range(1 << len_prime)]
        dp[0] = pow(2, num_counter[1], MOD)

        for cur_num, counter in num_counter.items():
            # skip 1 and num_with_square_factor
            if cur_num == 1 or cur_num in num_with_square_factor:
                continue

            # check the prime factor usage of the current subset: each prime factor can be used at most once
            subset_prime_usage = 0
            for idx, prime_number in enumerate(prime_number_list):
                if cur_num % prime_number == 0:  # if a prime is used, set a bit in subset_prime_usage as 1
                    subset_prime_usage |= (1 << idx)

            # mask is a len_prime-bit number to indicate whether a prime is used
            for mask in range((1 << len_prime) - 1, 0, -1):
                # if the current prime usage of subset is within the limit the mask
                if (mask & subset_prime_usage) == subset_prime_usage:  # subset_prime_usage is the subset of mask
                    # accumulate dp[mask ^ subset_prime_usage] * counter to dp[mask]
                    # (mask ^ subset_prime_usage) means delete all 1s of subset_prime_usage in mask
                    dp[mask] = (dp[mask] + dp[mask ^ subset_prime_usage] * counter) % MOD

        return sum(dp[1:]) % MOD


def main():
    # Example 1: Output: 6
    #     Explanation: The good subsets are:
    #         - [1,2]: product is 2, which is the product of distinct prime 2.
    #         - [1,2,3]: product is 6, which is the product of distinct primes 2 and 3.
    #         - [1,3]: product is 3, which is the product of distinct prime 3.
    #         - [2]: product is 2, which is the product of distinct prime 2.
    #         - [2,3]: product is 6, which is the product of distinct primes 2 and 3.
    #         - [3]: product is 3, which is the product of distinct prime 3.
    # nums = [1, 2, 3, 4]

    # Example 2: Output: 5
    # nums = [4, 2, 3, 15]

    # Example 3: Output: 62
    # nums = [6, 8, 1, 8, 6, 5, 6, 11, 17]

    # Example 4: Output: 5368
    nums = [5, 10, 1, 26, 24, 21, 24, 23, 11, 12, 27, 4, 17, 16, 2, 6, 1, 1, 6, 8, 13, 30, 24, 20, 2, 19]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.numberOfGoodSubsets(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
