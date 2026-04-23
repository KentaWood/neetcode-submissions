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
        
        if not head:
            return None

        oldToNew = defaultdict(lambda: None)

        curr = head

        while curr:
            oldToNew[curr] = Node(curr.val)
            curr = curr.next

        dummy = Node(-1)
        prev = dummy
        curr = head

        while curr:
            print(curr.val)
            oldToNew[curr].next = oldToNew[curr.next]
            oldToNew[curr].random = oldToNew[curr.random]
            curr = curr.next



        
        return oldToNew[head]

        