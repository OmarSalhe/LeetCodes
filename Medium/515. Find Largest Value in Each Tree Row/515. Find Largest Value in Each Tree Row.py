from typing import Optional, List
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = collections.deque()
        q.append(root)

        ans = []
        while q:
            lvl_num = float('-inf')
            for _ in range(len(q)):
                cur = q.popleft()
                
                lvl_num = max(lvl_num, cur.val)

                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            
            ans.append(lvl_num)
    
        return ans
