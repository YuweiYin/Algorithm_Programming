#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0373-Find-K-Pairs-with-Smallest-Sums.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-14
=================================================================="""

import sys
import time
from typing import List

"""
LeetCode - 0373 - (Medium) - Find K Pairs with Smallest Sums
https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

Description & Requirement:
    You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.
    Define a pair (u, v) which consists of one element from the first array and one element from the second array.
    Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

Example 1:
    Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
    Output: [[1,2],[1,4],[1,6]]
    Explanation:
        The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:
    Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
    Output: [[1,1],[1,1]]
    Explanation:
        The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
Example 3:
    Input: nums1 = [1,2], nums2 = [3], k = 3
    Output: [[1,3],[2,3]]
    Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]

Constraints:
    1 <= nums1.length, nums2.length <= 10^5
    -10^9 <= nums1[i], nums2[i] <= 10^9
    nums1 and nums2 both are sorted in ascending order.
    1 <= k <= 1000
"""


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # exception case
        if not isinstance(nums1, list) or len(nums1) <= 0:
            return []  # Error input type
        if not isinstance(nums2, list) or len(nums2) <= 0:
            return []  # Error input type
        if k <= 0:  # no result
            return []
        if k >= len(nums1) * len(nums2):  # all combinations
            return [[n1, n2] for n1 in nums1 for n2 in nums2]
        # main method: (DIY heapq & priority queue)
        #     note that (nums1[i] + nums2[j]) must <= (nums1[i+1] + nums2[j]) and (nums1[i] + nums2[j+1])
        #     so from [0][0], scan next smallest pair must be [0][1] or [1][0], BFS, use queue
        #     each step, pop the smallest one, add into res_list, and push 1 or 2 possible next-smallest item in heap
        # return self._kSmallestPairsDictSort(nums1, nums2, k)
        return self._kSmallestPairsHeapq(nums1, nums2, k)

    def _kSmallestPairsDictSort(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        assert len_nums1 > 0 and len_nums2 > 0 and 0 < k < len_nums1 * len_nums2

        res_list = []
        sum_dict = dict({})

        # O(len_nums1 * len_nums2)  TLE
        for idx1, n1 in enumerate(nums1):
            for idx2, n2 in enumerate(nums2):
                cur_sum = n1 + n2
                if cur_sum in sum_dict:  # put the current pair into OrderedDict
                    sum_dict[cur_sum].append([n1, n2])
                else:
                    sum_dict[cur_sum] = [[n1, n2]]

        # bfs_queue = collections.deque()
        # bfs_queue.append([nums1[0] + nums2[0], nums1[0], nums2[0]])
        # bfs_queue = [[0, 0]]  # each time, scan all item in bfs_queue
        # done_search_set = set()
        #
        # while bfs_queue:
        #     new_queue = []
        #     for pos in bfs_queue:
        #         if tuple([pos[0], pos[1]]) not in done_search_set:
        #             done_search_set.add(tuple([pos[0], pos[1]]))  # avoid repeat search
        #             n1 = nums1[pos[0]]  # current: [i][j]
        #             n2 = nums2[pos[1]]
        #             cur_sum = n1 + n2
        #             if cur_sum in sum_dict:  # put the current pair into OrderedDict
        #                 sum_dict[cur_sum].append([n1, n2])
        #             else:
        #                 sum_dict[cur_sum] = [[n1, n2]]
        #
        #             if pos[0] + 1 < len_nums1 and tuple([pos[0] + 1, pos[1]]) not in done_search_set:
        #                 new_queue.append([pos[0] + 1, pos[1]])  # next: [i+1][j]
        #             if pos[1] + 1 < len_nums2 and tuple([pos[0], pos[1] + 1]) not in done_search_set:
        #                 new_queue.append([pos[0], pos[1] + 1])  # next: [i][j+1]
        #     if len(done_search_set) >= k:
        #         break
        #     bfs_queue = new_queue  # update bfs_queue

        sum_dict_items = list(sum_dict.items())
        sum_dict_items.sort(key=lambda x: x[0])  # sort, key is the sum of each pair
        pair_counter = 0
        for k_sum, v_list in sum_dict_items:  # extract top k items
            for v_pair in v_list:
                res_list.append(v_pair)
                pair_counter += 1
                if pair_counter == k:
                    return res_list

        return res_list

    def _kSmallestPairsHeapq(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # import heapq

        class MyHeapqList:
            """
            refer to built-in heapq, DIY the item type as list, key is list[0] (needn't do this...)
            """
            def __init__(self):
                self.heap = []

            def heappush(self, _item_list: list):
                """Push item onto heap, maintaining the heap invariant."""
                self.heap.append(_item_list)
                self._siftdown(0, len(self.heap) - 1)

            def heappop(self):
                """Pop the smallest item off the heap, maintaining the heap invariant."""
                lastelt = self.heap.pop()  # raises appropriate IndexError if heap is empty
                if self.heap:
                    returnitem = self.heap[0]
                    self.heap[0] = lastelt
                    self._siftup(0)
                    return returnitem
                return lastelt

            def _siftdown(self, startpos, pos):
                newitem = self.heap[pos]
                # Follow the path to the root, moving parents down until finding a place
                # newitem fits.
                while pos > startpos:
                    parentpos = (pos - 1) >> 1
                    parent = self.heap[parentpos]
                    # if newitem < parent:
                    if newitem[0] < parent[0]:  # Here, DIY
                        self.heap[pos] = parent
                        pos = parentpos
                        continue
                    break
                self.heap[pos] = newitem

            def _siftup(self, pos):
                endpos = len(self.heap)
                startpos = pos
                newitem = self.heap[pos]
                # Bubble up the smaller child until hitting a leaf.
                childpos = 2 * pos + 1  # leftmost child position
                while childpos < endpos:
                    # Set childpos to index of smaller child.
                    rightpos = childpos + 1
                    # if rightpos < endpos and not self.heap[childpos] < self.heap[rightpos]:
                    if rightpos < endpos and not self.heap[childpos][0] < self.heap[rightpos][0]:  # Here, DIY
                        childpos = rightpos
                    # Move the smaller child up.
                    self.heap[pos] = self.heap[childpos]
                    pos = childpos
                    childpos = 2 * pos + 1
                # The leaf at pos is empty now.  Put newitem there, and bubble it up
                # to its final resting place (by sifting its parents down).
                self.heap[pos] = newitem
                self._siftdown(startpos, pos)

        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        assert len_nums1 > 0 and len_nums2 > 0 and 0 < k < len_nums1 * len_nums2

        res_list = []
        my_heapq = MyHeapqList()
        # # O(len_nums1 * len_nums2)  TLE
        # for n1 in nums1:  # push all items into heapq
        #     for n2 in nums2:
        #         my_heapq.heappush([n1 + n2, n1, n2])
        #
        # pair_counter = 0
        # while pair_counter < k:  # pop one by one
        #     _, n1, n2 = my_heapq.heappop()
        #     pair_counter += 1
        #     res_list.append([n1, n2])
        #
        # return res_list

        my_heapq.heappush([nums1[0] + nums2[0], nums1[0], nums2[0], 0, 0])  # cur_sum, n1, n2, idx1, idx2
        done_search_set = set()  # avoid repeat search
        done_search_set.add(tuple([0, 0]))  # avoid repeat search

        # each step, pop the smallest one, add into res_list, and push 1 or 2 possible next-smallest item in heap
        while len(my_heapq.heap) > 0 and len(res_list) < k:
            # get the current smallest one, pop it and add into res_list
            cur_sum, n1, n2, idx1, idx2 = my_heapq.heappop()
            res_list.append([n1, n2])
            # if len(res_list) == k:
            #     break
            if idx1 + 1 < len_nums1 and tuple([idx1 + 1, idx2]) not in done_search_set:  # next: [i+1][j]
                my_heapq.heappush([nums1[idx1 + 1] + nums2[idx2], nums1[idx1 + 1], nums2[idx2], idx1 + 1, idx2])
                done_search_set.add(tuple([idx1 + 1, idx2]))  # avoid repeat search
            if idx2 + 1 < len_nums2 and tuple([idx1, idx2 + 1]) not in done_search_set:  # next: [i][j+1]
                my_heapq.heappush([nums1[idx1] + nums2[idx2 + 1], nums1[idx1], nums2[idx2 + 1], idx1, idx2 + 1])
                done_search_set.add(tuple([idx1, idx2 + 1]))  # avoid repeat search

        return res_list


def main():
    # Example 1: Output: [[1,2],[1,4],[1,6]]
    # nums1 = [1, 7, 11]
    # nums2 = [2, 4, 6]
    # k = 3

    # Example 2: Output: [[1,1],[1,1]]
    # nums1 = [1, 1, 2]
    # nums2 = [1, 2, 3]
    # k = 2

    # Example 3: Output: [[1,3],[2,3]]
    # nums1 = [1, 2]
    # nums2 = [3]
    # k = 3

    # Example 4: Output: [[1,3],[2,3],[1,5]]
    # nums1 = [1, 2, 4, 5, 6]
    # nums2 = [3, 5, 7, 9]
    # k = 3

    # Example 4: Output: [[1,2],[1,4],[1,6]]
    # nums1 = [1, 7, 11]
    # nums2 = [2, 4, 6]
    # k = 3

    # Example 5: Output: [[0,-3],[0,-3],[0,-3],[0,-3],[0,-3],[0,22],[0,22],[0,22],[0,22],[0,22],[0,35],
    #     [0,35],[0,35],[0,35],[0,35],[0,56],[0,56],[0,56],[0,56],[0,56],[0,76],[0,76]]
    nums1 = [0, 0, 0, 0, 0]
    nums2 = [-3, 22, 35, 56, 76]
    k = 22

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.kSmallestPairs(nums1, nums2, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
