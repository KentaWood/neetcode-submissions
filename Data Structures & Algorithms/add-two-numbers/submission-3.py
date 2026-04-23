# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry = 0
        dummy = ListNode(-1)
        prev = dummy

        while l1 or l2 or carry:
            
            # create the new node make it be the next of the previous iteration
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            newNode = ListNode(val= (val1 + val2 + carry) % 10)
            prev.next = newNode
            prev = newNode

            #check if there's a need to carry 
            carry = (val1 + val2 + carry ) // 10 

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next


        