#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2032-Two-Out-of-Three.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-12-29
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 2032 - (Easy) - Two Out of Three
https://leetcode.com/problems/two-out-of-three/

Description & Requirement:
    Given three integer arrays nums1, nums2, and nums3, return a distinct array containing all the values 
    that are present in at least two out of the three arrays. You may return the values in any order.

Example 1:
    Input: nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]
    Output: [3,2]
    Explanation: The values that are present in at least two arrays are:
        - 3, in all three arrays.
        - 2, in nums1 and nums2.
Example 2:
    Input: nums1 = [3,1], nums2 = [2,3], nums3 = [1,2]
    Output: [2,3,1]
    Explanation: The values that are present in at least two arrays are:
        - 2, in nums2 and nums3.
        - 3, in nums1 and nums2.
        - 1, in nums1 and nums3.
Example 3:
    Input: nums1 = [1,2,2], nums2 = [4,3,3], nums3 = [5]
    Output: []
    Explanation: No value is present in at least two arrays.

Constraints:
    1 <= nums1.length, nums2.length, nums3.length <= 100
    1 <= nums1[i], nums2[j], nums3[k] <= 100
"""


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        # exception case
        assert isinstance(nums1, list) and len(nums1) >= 1
        assert isinstance(nums2, list) and len(nums2) >= 1
        assert isinstance(nums3, list) and len(nums3) >= 1
        # main method: (hash dict & bit map)
        return self._twoOutOfThree(nums1, nums2, nums3)

    def _twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        """
        Time: beats 80.83%; Space: beats 81.27%
        """
        assert isinstance(nums1, list) and len(nums1) >= 1
        assert isinstance(nums2, list) and len(nums2) >= 1
        assert isinstance(nums3, list) and len(nums3) >= 1

        hash_dict = collections.defaultdict(int)  # bit map

        for idx, nums in enumerate((nums1, nums2, nums3)):
            for num in nums:
                hash_dict[num] |= 1 << idx

        return [num for num, bit_mask in hash_dict.items() if bit_mask & (bit_mask - 1)]


def main():
    # Example 1: Output: [3,2]
    # nums1 = [1, 1, 3, 2]
    # nums2 = [2, 3]
    # nums3 = [3]

    # Example 2: Output: [2,3,1]
    # nums1 = [3, 1]
    # nums2 = [2, 3]
    # nums3 = [1, 2]

    # Example 3: Output: []
    nums1 = [1, 2, 2]
    nums2 = [4, 3, 3]
    nums3 = [5]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.twoOutOfThree(nums1, nums2, nums3)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
