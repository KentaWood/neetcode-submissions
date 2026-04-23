# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow, fast = head, head.next
        
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        
        #start of second half of list 
        second = slow.next
        prev = slow.next = None
        
        while(second):
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        #prev is now start of the reversed second hand of the list 
        #head is start of the first half
        list1 = head
        list2 = prev
        
        #used for linking the two lists into one

        while(list2):
            temp1,temp2 = list1.next, list2.next
            list1.next = list2
            list2.next = temp1
            list1 = temp1
            list2 = temp2
        

        