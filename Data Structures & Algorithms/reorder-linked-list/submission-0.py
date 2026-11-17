# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head 
        fast = head.next 
        first = head 
        
        def revlist( root: Optional[ListNode]) -> ListNode:
            if not root:
                return None
            
            prev = None 
            curr = head 
            while(curr):
                temp = curr.next 
                curr.next = prev
                prev = curr
                curr = temp
            return prev 
        
        
        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next 
        
        first = revlist(slow.next)
        
        second = slow.next
        slow.next = None 
        
        while second:
            temp1, temp2 = first.next, second.next
            
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2