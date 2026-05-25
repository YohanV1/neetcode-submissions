"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashm = {None:None}

        cur = head
        while cur:
            copy = Node(cur.val)
            hashm[cur] = copy
            cur = cur.next

        cur = head
        while cur:
            copy = hashm[cur]
            copy.next = hashm[cur.next]
            copy.random = hashm[cur.random]
            cur = cur.next

        return hashm[head]
        