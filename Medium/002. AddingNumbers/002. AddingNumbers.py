from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        out = ListNode()
        head = out

        while l1 or l2 or carry > 0:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            num = l1_val + l2_val + carry

            carry = num // 10
            num %= 10

            if l1:
                l1 = l1.next
            
            if l2:
                l2 = l2.next

            head.next = ListNode(num)
            head = head.next

        return out.next