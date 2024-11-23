from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        out = head

        while head:
            nxt = head
            while nxt and head.val == nxt.val:
                nxt = nxt.next
            
            head.next = nxt
            head = head.next

        return out

