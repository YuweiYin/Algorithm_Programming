#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0572-Subtree-of-Another-Tree.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-20
=================================================================="""

import sys
import time
from typing import List, Optional

"""
LeetCode - 0572 - (Easy) - Subtree of Another Tree
https://leetcode.com/problems/subtree-of-another-tree/

Description & Requirement:
    Given the roots of two binary trees root and subRoot, 
    return true if there is a subtree of root 
    with the same structure and node values of subRoot and false otherwise.

    A subtree of a binary tree tree is a tree that 
    consists of a node in tree and all of this node's descendants. 
    The tree tree could also be considered as a subtree of itself.

Example 1:
    Input: root = [3,4,5,1,2], subRoot = [4,1,2]
    Output: true
Example 2:
    Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
    Output: false

Constraints:
    The number of nodes in the root tree is in the range [1, 2000].
    The number of nodes in the subRoot tree is in the range [1, 1000].
    -10^4 <= root.val <= 10^4
    -10^4 <= subRoot.val <= 10^4
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right  # the left and right of leaf_node are both None

    @staticmethod
    def build_binary_tree_layer(val_list: List[int]):
        if not isinstance(val_list, list) or len(val_list) <= 0:
            return None

        node_list = []
        for v in val_list:
            if v is None:
                node_list.append(None)
            else:
                node_list.append(TreeNode(val=v))
        len_node_list = len(node_list)
        for idx, cur_node in enumerate(node_list):
            if cur_node is not None:
                cur_node_right_index = (idx + 1) << 1
                cur_node_left_index = cur_node_right_index - 1
                if cur_node_left_index < len_node_list:
                    cur_node.left = node_list[cur_node_left_index]
                if cur_node_right_index < len_node_list:
                    cur_node.right = node_list[cur_node_right_index]
        return node_list[0]  # return root_node

    @staticmethod
    def show_binary_tree_pre_order(root_node) -> List[int]:
        val_list = []

        def __dfs(cur_node):
            if isinstance(cur_node, TreeNode):
                val_list.append(cur_node.val)
                __dfs(cur_node.left)
                __dfs(cur_node.right)

        __dfs(root_node)
        return val_list

    @staticmethod
    def show_binary_tree_mid_order(root_node) -> List[int]:
        val_list = []

        def __dfs(cur_node):
            if isinstance(cur_node, TreeNode):
                __dfs(cur_node.left)
                val_list.append(cur_node.val)
                __dfs(cur_node.right)

        __dfs(root_node)
        return val_list

    @staticmethod
    def show_binary_tree_post_order(root_node) -> List[int]:
        val_list = []

        def __dfs(cur_node):
            if isinstance(cur_node, TreeNode):
                __dfs(cur_node.left)
                __dfs(cur_node.right)
                val_list.append(cur_node.val)

        __dfs(root_node)
        return val_list


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # exception case
        if not isinstance(root, TreeNode) or not isinstance(subRoot, TreeNode):
            return False
        # main method: (1. DFS; 2. Substring match; 3. Tree Hash.)
        # return self._isSubtreeDfs(root, subRoot)  # slowest method
        return self._isSubtreeSubstring(root, subRoot)  # fastest method
        # return self._isSubtreeTreeHash(root, subRoot)

    def _isSubtreeDfs(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        DFS: for each node in root, check the subtree from this node is matched, if not, go left or right
        """
        assert isinstance(root, TreeNode) and isinstance(subRoot, TreeNode)

        def __check_tree(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
            if not isinstance(node1, TreeNode) and not isinstance(node2, TreeNode):
                return True  # both are leaves
            elif not isinstance(node1, TreeNode):
                return False  # only one leaf
            elif not isinstance(node2, TreeNode):
                return False  # only one leaf
            else:
                if node1.val != node2.val:
                    return False
                else:  # keep checking the children
                    return __check_tree(node1.left, node2.left) and __check_tree(node1.right, node2.right)

        def __dfs(node: Optional[TreeNode], sub_node: Optional[TreeNode]) -> bool:
            if not isinstance(node, TreeNode):
                return False
            return __check_tree(node, sub_node) or __dfs(node.left, sub_node) or __dfs(node.right, sub_node)

        return __dfs(root, subRoot)

    def _isSubtreeSubstring(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Substring match: (trick) if subRoot is a subtree of root, then subRoot's pre-order traverse sequence (PTS)
            must be a substring of root's PTS (every leaf must have a left null node and a right null node).
            So first convert both trees into two val_string/list,
            then perform string/list matching. (KMP or Rabin-Karp)
        Runtime: 68 ms, faster than 97.57% of Python3 online submissions for Subtree of Another Tree.
        Memory Usage: 15.9 MB, less than 6.44% of Python3 online submissions for Subtree of Another Tree.
        """
        assert isinstance(root, TreeNode) and isinstance(subRoot, TreeNode)
        LEFT_NULL = int(1e9+7)
        RIGHT_NULL = int(1e9+9)

        def __get_PTS_with_null_leaf(_node: Optional[TreeNode]) -> List[int]:
            val_list = []

            def __dfs(cur_node):
                if isinstance(cur_node, TreeNode):
                    val_list.append(cur_node.val)  # cur value
                    if isinstance(cur_node.left, TreeNode):  # left
                        __dfs(cur_node.left)
                    else:
                        val_list.append(LEFT_NULL)
                    if isinstance(cur_node.right, TreeNode):  # right
                        __dfs(cur_node.right)
                    else:
                        val_list.append(RIGHT_NULL)

            __dfs(_node)
            return val_list

        root_pts = __get_PTS_with_null_leaf(root)
        sub_pts = __get_PTS_with_null_leaf(subRoot)

        def __kmp(src_seq: list, tgt_seq: list):
            len_src = len(src_seq)
            len_tgt = len(tgt_seq)
            assert len_src > 0 and len_tgt > 0

            # fail_match[i] == k means if tgt_seq[i] fails matching, then go back to match tgt_seq[k]
            fail_match = [-1 for _ in range(len_tgt)]  # -1 means there's nowhere to back to
            # KMP preprocessing on tgt_seq
            back_index = -1  # if failed, back here
            tgt_index = 1  # scan cursor
            while tgt_index < len_tgt:
                # find until tgt_seq[tgt_index] == tgt_seq[back_index + 1], this is a back point
                while back_index != -1 and tgt_seq[tgt_index] != tgt_seq[back_index + 1]:
                    back_index = fail_match[back_index]
                if tgt_seq[tgt_index] == tgt_seq[back_index + 1]:
                    back_index += 1
                fail_match[tgt_index] = back_index  # if tgt_seq[tgt_index] fails, back to match tgt_seq[back_index]
                tgt_index += 1

            src_index = 0
            tgt_index = -1
            while src_index < len_src:  # do matching
                # tgt_index != -1 means there's somewhere to go back, so if not match, tgt_index go back
                while tgt_index != -1 and src_seq[src_index] != tgt_seq[tgt_index + 1]:
                    tgt_index = fail_match[tgt_index]  # go back
                if src_seq[src_index] == tgt_seq[tgt_index + 1]:  # match, keep moving
                    tgt_index += 1
                if tgt_index == len_tgt - 1:  # match all tgt_seq
                    return True
                src_index += 1

            return False  # can't match

        return __kmp(root_pts, sub_pts)

    def _isSubtreeTreeHash(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Tree Hash: design a hash function to map each subtree into an integer.
            consider adequate essential factors that may distinguish a subtree.
            H_{cur} = v_{cur} + H_{left} * p(s_{left}) * Alpha + H_{right} * p(s_{right}) * Beta
            where H_{cur}, H_{left}, and H_{right} are the Tree Hash value of the current node (as a subtree),
                its left child, and its right child respectively. (H_{None} = 0)
            v_{cur} is the node val. Alpha and Beta are two chosen prime numbers.
            s_{left} and s_{right} are the subtree size (number of nodes) of left child and right child.
            p(n) is the n-th prime number (n = 1, 2, 3, ...).
            Use [the sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes) to get prime sequence.
        """
        assert isinstance(root, TreeNode) and isinstance(subRoot, TreeNode)
        MOD = int(1e9+7)
        MAX_SIZE = 1009  # max subtree size (> 1000 is fine). can choose prime 1019 or 1021
        ALPHA = 89
        BETA = 211

        def __get_prime_sieve_of_Eratosthenes(max_size: int) -> list:
            prime_number = [0 for _ in range(max_size)]  # prime number sequence: 2, 3, 5, 7, ... (1-indexed)
            prime_counter = 0
            used_prime = [False for _ in range(max_size)]  # record the used prime numbers, for sieve
            used_prime[0] = used_prime[1] = True  # 0 and 1 are not prime number

            cur_prime = 2
            while cur_prime < max_size:
                if not used_prime[cur_prime]:  # add cur_prime into prime_number sequence
                    prime_counter += 1
                    prime_number[prime_counter] = cur_prime
                # sieve all composite numbers based on cur_prime (also, limited by max_size)
                sieve_index = 1
                while sieve_index <= prime_counter and cur_prime * prime_number[sieve_index] < max_size:
                    used_prime[cur_prime * prime_number[sieve_index]] = True  # do sieve
                    if prime_number[sieve_index] == 0:  # already 0, stop sieve
                        break
                    sieve_index += 1
                cur_prime += 1

            return prime_number

        prime_number_seq = __get_prime_sieve_of_Eratosthenes(max_size=MAX_SIZE)

        tree_hash_src = dict({})  # tree hash of src (root)
        tree_hash_tgt = dict({})  # tree hash of tgt (subRoot)

        class TreeHashValue:
            def __init__(self, subtree_hash, subtree_size):
                self.subtree_hash = subtree_hash
                self.subtree_size = subtree_size

        def __dfs(node: TreeNode, tree_hash: dict) -> dict:
            tree_hash[node] = TreeHashValue(subtree_hash=node.val, subtree_size=1)
            if not isinstance(node.left, TreeNode) and not isinstance(node.right, TreeNode):  # leaf
                return tree_hash
            if isinstance(node.left, TreeNode):  # left
                __dfs(node.left, tree_hash)
                assert node.left in tree_hash and isinstance(tree_hash[node.left], TreeHashValue)
                tree_hash[node].subtree_size += tree_hash[node.left].subtree_size  # update subtree_size
                # recursive update: H_{cur} = v_{cur} + H_{left} * p(s_{left}) * Alpha + H_{right} * p(s_{right}) * Beta
                tree_hash[node].subtree_hash = (tree_hash[node].subtree_hash + (
                        ((tree_hash[node.left].subtree_hash * ALPHA) % MOD) *
                        prime_number_seq[tree_hash[node.left].subtree_size]) % MOD) % MOD
            if isinstance(node.right, TreeNode):  # right
                __dfs(node.right, tree_hash)
                assert node.right in tree_hash and isinstance(tree_hash[node.right], TreeHashValue)
                tree_hash[node].subtree_size += tree_hash[node.right].subtree_size  # update subtree_size
                # recursive update: H_{cur} = v_{cur} + H_{left} * p(s_{left}) * Alpha + H_{right} * p(s_{right}) * Beta
                tree_hash[node].subtree_hash = (tree_hash[node].subtree_hash + (
                        ((tree_hash[node.right].subtree_hash * BETA) % MOD) *
                        prime_number_seq[tree_hash[node.right].subtree_size]) % MOD) % MOD
            return tree_hash

        tree_hash_src = __dfs(root, tree_hash_src)  # recursively update the tree hash value
        tree_hash_tgt = __dfs(subRoot, tree_hash_tgt)  # recursively update the tree hash value

        tgt_subtree_hash = tree_hash_tgt[subRoot].subtree_hash  # the tree hash value of subRoot
        for _k, _v in tree_hash_src.items():
            if _v.subtree_hash == tgt_subtree_hash:  # match hash value of every subtree in root
                return True

        return False


def main():
    # Example 1: Output: true
    root = [3, 4, 5, 1, 2]
    subRoot = [4, 1, 2]

    # Example 2: Output: false
    # root = [3, 4, 5, 1, 2, None, None, None, None, 0]
    # subRoot = [4, 1, 2]

    # Example 3: Output: true
    # root = [1, 1]
    # subRoot = [1]

    # Example 4: Output: true
    # root = [1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, 2]
    # subRoot = [1, None, 1, None, 1, None, 1, None, 1, None, 1, 2]

    root_node = TreeNode.build_binary_tree_layer(root)
    sub_node = TreeNode.build_binary_tree_layer(subRoot)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.isSubtree(root_node, sub_node)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
