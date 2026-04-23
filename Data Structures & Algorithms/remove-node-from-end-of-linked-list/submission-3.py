# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        l = dummy 
        r = head
        
        #space what end pointer to be n distance apart with remove pointer
        while n > 0:
            r = r.next 
            n -= 1

        #move both pointer so that ep is at the last node and remove is at the prev of the node we want to remove
        while r:
            r = r.next
            l = l.next

        l.next = l.next.next

        return dummy.next