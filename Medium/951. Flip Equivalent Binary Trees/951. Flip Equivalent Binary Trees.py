from typing import Optional
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2: return True
        if not root1 or not root2: return False
        if root1.val != root2.val: return False

        q = collections.deque()

        q.append((root1, root1.val))
        child_sum = [0] * 102
        while q:
            for _ in range(len(q)):
                cur, parent_val = q.popleft()
                cur_val = cur.val if cur.val > 0 else 101
                child_sum[parent_val] += cur_val

                if cur.left: q.append((cur.left, cur.val))
                if cur.right: q.append((cur.right, cur.val))
        
        q.append((root2, root2.val))
        child_sum2 = [0] * 100
        while q:
            for _ in range(len(q)):
                cur, parent_val = q.popleft()
                cur_val = cur.val if cur.val > 0 else 101
                child_sum2[parent_val] += cur_val

                cur_val = cur.val if cur.val > 0 else 101

                if cur.left: q.append((cur.left, cur.val))
                if cur.right: q.append((cur.right, cur.val))


        # just check to see if every node has the same children
        # flipping = switching left or right child not their depths so children sum should remain the same
        for i in range(100):
            if child_sum[i] != child_sum2[i]: return False
        
        return True