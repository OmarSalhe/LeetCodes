from collections import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        prev = ListNode()
        out = head.next

        while head and head.next:
            # save next node
            tmp = head.next
            # skip next node (if possible)
            head.next = head.next.next if head.next else None
            
            # joins broken left side: from 1->2 3 4->5 to 1->2->3 4->5
            prev.next = tmp
            # joins broken right side: from 1->2->3 4->5 to 1->2->3->4->5
            tmp.next = head

            # update new previous node (cur node)
            prev = head
            # continue down LL
            head = head.next

        return out

# TC = O(n) -> just updating pointers (O(1)) n times
# SC = O(1) -> needed 1 dummy node to get started