#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0454-4Sum-II.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-03
=================================================================="""

import sys
import time
from typing import List
# import collections

"""
LeetCode - 0454 - (Medium) - 4Sum II
https://leetcode.com/problems/4sum-ii/

Description & Requirement:
    Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, 
    return the number of tuples (i, j, k, l) such that:
        0 <= i, j, k, l < n
        nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

Example 1:
    Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
    Output: 2
    Explanation:
        The two tuples are:
        1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
        2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0
Example 2:
    Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
    Output: 1

Constraints:
    n == nums1.length
    n == nums2.length
    n == nums3.length
    n == nums4.length
    1 <= n <= 200
    -2^28 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 2^28
"""


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # exception case
        if not isinstance(nums1, list) or len(nums1) <= 0:
            return 0  # Error input type
        if not isinstance(nums2, list) or len(nums2) <= 0:
            return 0  # Error input type
        if not isinstance(nums3, list) or len(nums3) <= 0:
            return 0  # Error input type
        if not isinstance(nums4, list) or len(nums4) <= 0:
            return 0  # Error input type
        if not (len(nums1) == len(nums2) == len(nums3) == len(nums4)):
            return 0  # Error input type
        # main method:
        #     1. slow (O(n^3 log n), TTL): fix nums1[i], nums2[j], and nums3[k], binary search find nums4[l]
        # return self._fourSumCountSlow(nums1, nums2, nums3, nums4)
        #     2. fast O(n^2): nums1[i] and nums2[j] is a group, nums3[k] and nums4[l] is a group
        #         if nums1[i] + nums2[j] == - (nums3[k] + nums4[l]), then bingo
        #         use hash dict, key: (nums3[k] + nums4[l]), value: counter of k and l combinations
        return self._fourSumCountFast(nums1, nums2, nums3, nums4)

    def _fourSumCountSlow(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        len_num = len(nums1)
        assert len_num >= 1 and len_num == len(nums2) == len(nums3) == len(nums4)

        def __binary_search(tgt: int, left_index: int, right_index: int) -> int:
            if left_index > right_index:
                return 0
            if left_index == right_index:
                return 1 if tgt == nums4[left_index] else 0
            mid_index = (left_index + right_index) >> 1
            if tgt == nums4[mid_index]:  # find all tgt (may have duplications)
                find_tgt = 1
                cur_index = mid_index + 1
                while cur_index < len_num and nums4[cur_index] == tgt:
                    find_tgt += 1
                    cur_index += 1
                cur_index = mid_index - 1
                while cur_index >= 0 and nums4[cur_index] == tgt:
                    find_tgt += 1
                    cur_index -= 1
                return find_tgt
            elif tgt < nums4[mid_index]:
                return __binary_search(tgt, left_index, mid_index - 1)  # go left
            else:
                return __binary_search(tgt, mid_index + 1, right_index)  # go right

        res = 0  # counter of valid 4-sum indices

        # sort all number lists
        # nums1.sort()
        # nums2.sort()
        # nums3.sort()
        nums4.sort()

        # find all valid 4-sum pairs
        for i, num1 in enumerate(nums1):
            for j, num2 in enumerate(nums2):
                for k, num3 in enumerate(nums3):
                    target = 0 - num1 - num2 - num3
                    res += __binary_search(target, 0, len_num - 1)

        return res

    def _fourSumCountFast(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        len_num = len(nums1)
        assert len_num >= 1 and len_num == len(nums2) == len(nums3) == len(nums4)

        res = 0  # counter of valid 4-sum indices

        # get hash dict, key: (nums3[k] + nums4[l]), value: counter of k and l combinations
        kl_dict = dict({})
        for k, num3 in enumerate(nums3):
            for l, num4 in enumerate(nums4):
                cur_sum = num3 + num4
                if cur_sum not in kl_dict:
                    kl_dict[cur_sum] = 1
                else:
                    kl_dict[cur_sum] += 1

        # get the counter of all valid 4-sum pairs
        for i, num1 in enumerate(nums1):
            for j, num2 in enumerate(nums2):
                # if nums1[i] + nums2[j] == - (nums3[k] + nums4[l]), then bingo
                cur_target = 0 - num1 - num2
                if cur_target in kl_dict:
                    res += kl_dict[cur_target]

        return res


def main():
    # Example 1: Output: 2
    #     Explanation:
    #         The two tuples are:
    #         1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
    #         2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0
    nums1 = [1, 2]
    nums2 = [-2, -1]
    nums3 = [-1, 2]
    nums4 = [0, 2]

    # Example 2: Output: 1
    # nums1 = [0]
    # nums2 = [0]
    # nums3 = [0]
    # nums4 = [0]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.fourSumCount(nums1, nums2, nums3, nums4)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
