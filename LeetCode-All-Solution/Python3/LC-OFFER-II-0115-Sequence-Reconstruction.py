#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-OFFER-II-0115-Sequence-Reconstruction.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-07-23
=================================================================="""

import sys
import time
from typing import List
import collections
# import itertools
# import functools

"""
LeetCode - OFFER-II-0115 - (Medium) - Sequence Reconstruction
https://leetcode.cn/problems/ur2n8P/
https://leetcode.com/problems/sequence-reconstruction/

Description & Requirement:
    给定一个长度为 n 的整数数组 nums ，其中 nums 是范围为 [1，n] 的整数的排列。
    还提供了一个 2D 整数数组 sequences ，其中 sequences[i] 是 nums 的子序列。

    检查 nums 是否是唯一的最短超序列 。最短 超序列 是 长度最短 的序列，并且所有序列 sequences[i] 都是它的子序列。
    对于给定的数组 sequences ，可能存在多个有效的 超序列 。

    例如，对于 sequences = [[1,2],[1,3]] ，有两个最短的 超序列 ，[1,2,3] 和 [1,3,2] 。
    而对于 sequences = [[1,2],[1,3],[1,2,3]] ，唯一可能的最短 超序列 是 [1,2,3] 。[1,2,3,4] 是可能的超序列，但不是最短的。
    如果 nums 是序列的唯一最短 超序列 ，则返回 true ，否则返回 false 。

    子序列 是一个可以通过从另一个序列中删除一些元素或不删除任何元素，而不改变其余元素的顺序的序列。

Example 1:
    Input: nums = [1,2,3], sequences = [[1,2],[1,3]]
    Output: false
    Explanation: 有两种可能的超序列：[1,2,3]和[1,3,2]。
        序列 [1,2] 是[1,2,3]和[1,3,2]的子序列。
        序列 [1,3] 是[1,2,3]和[1,3,2]的子序列。
        因为 nums 不是唯一最短的超序列，所以返回false。
Example 2:
    Input: nums = [1,2,3], sequences = [[1,2]]
    Output: false
    Explanation: 最短可能的超序列为 [1,2]。
        序列 [1,2] 是它的子序列：[1,2]。
        因为 nums 不是最短的超序列，所以返回false。
Example 3:
    Input: nums = [1,2,3], sequences = [[1,2],[1,3],[2,3]]
    Output: true
    Explanation: 最短可能的超序列为[1,2,3]。
        序列 [1,2] 是它的一个子序列：[1,2,3]。
        序列 [1,3] 是它的一个子序列：[1,2,3]。
        序列 [2,3] 是它的一个子序列：[1,2,3]。
        因为 nums 是唯一最短的超序列，所以返回true。

Constraints:
    n == nums.length
    1 <= n <= 10^4
    nums 是 [1, n] 范围内所有整数的排列
    1 <= sequences.length <= 10^4
    1 <= sequences[i].length <= 10^4
    1 <= sum(sequences[i].length) <= 10^5
    1 <= sequences[i][j] <= n
    sequences 的所有数组都是 唯一 的
    sequences[i] 是 nums 的一个子序列
"""


class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        assert isinstance(sequences, list) and len(sequences) >= 1
        for seq in sequences:
            assert isinstance(seq, list) and len(seq) >= 1
        # main method: (topology sort)
        return self._sequenceReconstruction(nums, sequences)

    def _sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        """
        Runtime: 112 ms, faster than 98.40% of Python3 online submissions for Sequence Reconstruction.
        Memory Usage: 18.7 MB, less than 91.20% of Python3 online submissions for Sequence Reconstruction.
        """
        assert isinstance(nums, list) and len(nums) >= 1
        assert isinstance(sequences, list) and len(sequences) >= 1

        len_nums = len(nums)

        graph = [[] for _ in range(len_nums)]
        in_degree = [0 for _ in range(len_nums)]

        for seq in sequences:
            for idx in range(len(seq) - 1):
                from_node, to_node = seq[idx], seq[idx + 1]
                graph[from_node - 1].append(to_node - 1)
                in_degree[to_node - 1] += 1

        queue = collections.deque([idx for idx, degree in enumerate(in_degree) if degree == 0])

        while queue:
            if len(queue) > 1:
                return False
            cur_node = queue.popleft()
            for next_node in graph[cur_node]:
                in_degree[next_node] -= 1
                if in_degree[next_node] == 0:
                    queue.append(next_node)

        return True


def main():
    # Example 1: Output: false
    # nums = [1, 2, 3]
    # sequences = [[1, 2], [1, 3]]

    # Example 2: Output: false
    # nums = [1, 2, 3]
    # sequences = [[1, 2]]

    # Example 3: Output: true
    nums = [1, 2, 3]
    sequences = [[1, 2], [1, 3], [2, 3]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.sequenceReconstruction(nums, sequences)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
