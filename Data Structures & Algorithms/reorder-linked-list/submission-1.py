# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head 
        fast = head.next 
        
        def revlist( root: Optional[ListNode]) -> None:
            
            prev = None 
            curr = root 
            while(curr):
                temp = curr.next 
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        
        
        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next 
        
        second = revlist(slow.next)
        first = head
        slow.next = None 
        
        while second:
            temp1, temp2 = first.next, second.next
            
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2