#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0673-Number-of-Longest-Increasing-Subsequence.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-29
=================================================================="""

import sys
import time
from typing import List
# import collections

"""
LeetCode - 0673 - (Medium) - Number of Longest Increasing Subsequence
https://leetcode.com/problems/number-of-longest-increasing-subsequence/

Description & Requirement:
    Given an integer array nums, return the number of longest increasing subsequences.

    Notice that the sequence has to be strictly increasing.

Example 1:
    Input: nums = [1,3,5,4,7]
    Output: 2
    Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
Example 2:
    Input: nums = [2,2,2,2,2]
    Output: 5
    Explanation: The length of the longest continuous increasing subsequence is 1, 
        and there are 5 subsequences' length is 1, so output 5.

Constraints:
    1 <= nums.length <= 2000
    -10^6 <= nums[i] <= 10^6
"""


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # exception case
        if not isinstance(nums, list) or len(nums) <= 0:
            return 0  # Error input type
        if len(nums) == 1:
            return 1
        if len(nums) == 2:
            return 2 if nums[0] >= nums[1] else 1
        # main method: related problem: LC-0300-Longest-Increasing-Subsequence
        # (1. Dynamic Programming)
        # return self._findNumberOfLISdp(nums)  # Time: O(n^2);  Space: O(n).

        # (2. Greedy)
        return self._findNumberOfLISgreedy(nums)  # Time: O(n log n);  Space: O(n).

    def _findNumberOfLISdp(self, nums: List[int]) -> int:
        """
        Time: O(n^2);  Space: O(n).
        """
        len_nums = len(nums)
        assert len_nums >= 3

        res = 0  # counter of the seq with the max len
        max_seq_len = 0  # the max len

        dp = [1 for _ in range(len_nums)]  # dp[i] is the max lengthOfLIS using nums[0: i+1]
        len_counter = [1 for _ in range(len_nums)]  # len_counter[i] is the number of max lengthOfLIS using nums[0: i+1]

        for index in range(len_nums):  # for i = 0, 1, ..., -1
            for seg_index in range(index):  # for j = 0, 1, ..., i - 1
                if nums[index] > nums[seg_index]:  # dp equation: dp[i] = max(dp[j]) + 1
                    # dp[index] = max(dp[index], dp[seg_index] + 1)
                    if dp[index] == dp[seg_index] + 1:  # seq with the same max len
                        len_counter[index] += len_counter[seg_index]
                    elif dp[index] < dp[seg_index] + 1:
                        dp[index] = dp[seg_index] + 1  # update the longest seq
                        len_counter[index] = len_counter[seg_index]  # update the counter of the longest seq
                    else:
                        pass  # don't update dp[index], and len_counter[index] default value is 1
            # update the max_seq_len
            if dp[index] == max_seq_len:  # seq with the same max len
                res += len_counter[index]
            elif dp[index] > max_seq_len:
                max_seq_len = dp[index]  # update the longest seq
                res = len_counter[index]  # update the counter of the longest seq
            else:
                pass

        return res

    def _findNumberOfLISgreedy(self, nums: List[int]) -> int:
        """
        Time: O(n log n);  Space: O(n).
        Space is O(n) not O(n^2) because at most O(n) numbers can be appended into list
        Runtime: 84 ms, faster than 97.49% of Python3 online submissions for Number of Longest Increasing Subseq.
        Memory Usage: 14.6 MB, less than 65.43% of Python3 online submissions for Number of Longest Increasing Subseq.
        """
        len_nums = len(nums)
        assert len_nums >= 3

        min_end = []  # min_end[i][j] means the min end num of the j-th seq, where len(seq) == i
        len_counter = []  # len_counter[i][j] is the (prefix sum) number of seq that end with nums[i][k], 0 <= k <= j

        for idx, num in enumerate(nums):
            # binary search, find out the current seq len. len(min_end) is the len of max seq
            left_index, right_index = 0, len(min_end)
            while left_index < right_index:
                mid_index = (left_index + right_index) >> 1
                # min_end[i][-1] means the min end num of the seq, where len(seq) == i
                # num > min_end[i][-1] means a former seq of len == i append num can form a longer seq. <= otherwise
                if num <= min_end[mid_index][-1]:
                    right_index = mid_index
                else:
                    left_index = mid_index + 1
            cur_seq_len = left_index  # the current max seq len
            cur_len_counter = 1  # the current counter of max seq len
            if cur_seq_len > 0:
                # binary search, find out the num insertion position of the current num (in seq len == cur_seq_len - 1)
                left_index, right_index = 0, len(min_end[cur_seq_len - 1])
                while left_index < right_index:
                    mid_index = (left_index + right_index) >> 1
                    if num > min_end[cur_seq_len - 1][mid_index]:
                        right_index = mid_index
                    else:
                        left_index = mid_index + 1
                min_end_insert_index = left_index  # insertion pos of the current num (in min_end[cur_seq_len - 1])
                # count the number of seq that len(seq) == cur_seq_len - 1
                cur_len_counter = len_counter[cur_seq_len - 1][-1] - \
                    len_counter[cur_seq_len - 1][min_end_insert_index]
            # cur_seq_len == len(min_end) means a new longest seq len can be form
            if cur_seq_len == len(min_end):
                min_end.append([num])  # append the end num of the current seq len
                # len_counter[i][j] is the (prefix sum) number of seq that end with nums[i][k], 0 <= k <= j
                len_counter.append([0, cur_len_counter])
            else:  # this means num is a seq end of the former seq len (i.e., cur_seq_len)
                min_end[cur_seq_len].append(num)  # append it to its niche
                len_counter[cur_seq_len].append(len_counter[cur_seq_len][-1] + cur_len_counter)  # cumulate prefix sum

        return len_counter[-1][-1]  # return the prefix sum of longest seq


def main():
    # Example 1: Output: 2
    #     Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
    nums = [1, 3, 5, 4, 7]

    # Example 2: Output: 5
    #     Explanation: The length of the longest continuous increasing subsequence is 1,
    #         and there are 5 subsequences' length is 1, so output 5.
    # nums = [2, 2, 2, 2, 2]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.findNumberOfLIS(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
