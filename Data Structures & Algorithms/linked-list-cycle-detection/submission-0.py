# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashM = set()
        hashM.add(head)
        while head:
            if head.next in hashM:
                return True
            head = head.next
            hashM.add(head)
        return False

        