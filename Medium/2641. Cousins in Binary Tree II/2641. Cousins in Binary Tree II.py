from typing import Optional
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # keeps track of the sum of each parents children
        child = collections.defaultdict(int)

        # holds a node and its parent (since all sibling nodes share a parent)
        q = collections.deque()

        q.append((root, None))

        # the root has no parent, nor any cousins so level_sum = root, sibling_sum = root
        # -> cousin_sum = root - root
        child[None] = root.val

        while q:
            # the sum of the entire level/depth/wtv
            total = 0
            for node, parent in q:
                total += node.val
            
            for _ in range(len(q)):
                cur, parent = q.popleft()

                # if left child exists
                if cur.left:
                    # add to sibling_sum
                    child[cur] += cur.left.val
                    q.append((cur.left, cur))
                
                # if right child exists
                if cur.right:
                    # add to sibling_sum
                    child[cur] += cur.right.val
                    q.append((cur.right, cur))

                # subtracts the sum of a nodes siblings from the level sum to get the sum of its cousins
                # level_sum = cousin_sum + sibling_sum
                cur.val = total - child[parent]

        return root

        """
        Time Complexity = traversing to each node and processing children = O(V+E)
        Space Complexity = O(V)
        """
