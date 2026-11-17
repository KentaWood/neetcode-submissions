class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        increment_flag = False
        dummy = prev = ListNode()
        
        # attaching the new sum node list
        while(l1 and l2):
            
            if(increment_flag):
                sum = l1.val + l2.val + 1
                increment_flag = False
            else:
                sum = (l1.val + l2.val) 
            
            
            if sum > 10:
                sum -= 10
                increment_flag = True
            
            print(l1.val, l2.val)
            sum_node = ListNode(sum)
            prev.next = sum_node
            prev = sum_node

            l1 = l1.next
            l2 = l2.next
        
        if increment_flag:
            if l1:
                sum_node = ListNode(1) 
                prev.next = sum_node
                prev = sum_node
                l1 = l1.next
                prev.next = l1 
            elif l2:
                sum_node = ListNode(1 + l2.val) 
                prev.next = sum_node
                prev = sum_node
                l2 = l2.next
                prev.next = l1 
            else:
                sum_node = ListNode(1) 
                prev.next = sum_node
                prev = sum_node

            prev.next = l1 or l2
        
        return dummy.next      
            
        
         
            
            
        

            
        

        
        
                
        
                  
            
            
            
            
            