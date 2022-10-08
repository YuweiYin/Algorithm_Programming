#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0870-Advantage-Shuffle.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-10-08
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0870 - (Medium) - Advantage Shuffle
https://leetcode.com/problems/advantage-shuffle/

Description & Requirement:
    You are given two integer arrays nums1 and nums2 both of the same length. 
    The advantage of nums1 with respect to nums2 is the number of indices i for which nums1[i] > nums2[i].

    Return any permutation of nums1 that maximizes its advantage with respect to nums2.

Example 1:
    Input: nums1 = [2,7,11,15], nums2 = [1,10,4,11]
    Output: [2,11,7,15]
Example 2:
    Input: nums1 = [12,24,8,32], nums2 = [13,25,32,11]
    Output: [24,32,8,12]

Constraints:
    1 <= nums1.length <= 10^5
    nums2.length == nums1.length
    0 <= nums1[i], nums2[i] <= 10^9
"""


class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # exception case
        assert isinstance(nums1, list) and len(nums1) >= 1
        assert isinstance(nums2, list) and len(nums2) == len(nums1)
        for num in (nums1 + nums2):
            assert isinstance(num, int) and num >= 0
        # main method: (sort and greedily match)
        return self._advantageCount(nums1, nums2)

    def _advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Runtime: 1508 ms, faster than 42.54% of Python3 online submissions for Advantage Shuffle.
        Memory Usage: 33.5 MB, less than 91.58% of Python3 online submissions for Advantage Shuffle.
        """
        assert isinstance(nums1, list) and len(nums1) >= 1
        assert isinstance(nums2, list) and len(nums2) == len(nums1)

        n = len(nums1)
        sorted_index_1, sorted_index_2 = list(range(n)), list(range(n))
        sorted_index_1.sort(key=lambda x: nums1[x])
        sorted_index_2.sort(key=lambda x: nums2[x])

        res = [0 for _ in range(n)]
        left, right = 0, n - 1
        for cur_idx in range(n):
            if nums1[sorted_index_1[cur_idx]] > nums2[sorted_index_2[left]]:
                res[sorted_index_2[left]] = nums1[sorted_index_1[cur_idx]]
                left += 1
            else:
                res[sorted_index_2[right]] = nums1[sorted_index_1[cur_idx]]
                right -= 1

        return res


def main():
    # Example 1: Output: [2,11,7,15]
    nums1 = [2, 7, 11, 15]
    nums2 = [1, 10, 4, 11]

    # Example 2: Output: [24,32,8,12]
    # nums1 = [12, 24, 8, 32]
    # nums2 = [13, 25, 32, 11]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.advantageCount(nums1, nums2)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
