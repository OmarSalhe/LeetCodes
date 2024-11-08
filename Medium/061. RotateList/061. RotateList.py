from collections import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or not head or not head.next:
            return head

        # x = length of ll
        x, cur = 1, head

        # while you can keep going
        while(cur.next):
            cur = cur.next
            x += 1
        
        # connect end to start
        cur.next = head

        # if k = mx (where m is an int), rotation = og ll 
        if k % x == 0:
            cur.next = None
            return head
        
        # find breaking point -> new start after shifting nodes
        for i in range(x - (k % x)):
            cur = cur.next
        
        # save starting point
        out = cur.next
        # break cycle
        cur.next = None
        return out
