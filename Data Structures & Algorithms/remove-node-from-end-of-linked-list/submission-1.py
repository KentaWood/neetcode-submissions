class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        l = head
        r = head
        prev = dummy
        
        for i in range(n):
            r = r.next

        while(r):
            r = r.next
            prev = l
            l = l.next
            
        
        if prev:
            prev.next = l.next
            
                    
        return dummy.next   
        
        
        