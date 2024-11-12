from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        cur = head
        while(list1 != None or list2 != None):
            list1_val = list1.val if list1 else 101
            list2_val = list2.val if list2 else 101
            if list1_val < list2_val:
                cur.next = list1
                list1 = list1.next if list1 else None
            else:
                cur.next = list2
                list2 = list2.next if list2 else None
            cur = cur.next
        return head.next      
