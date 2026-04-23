# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow = head
        fast = head.next 

        # get slow to the middle of the list
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # split list 
        sec = slow.next 
        slow.next = None
        
        prev = None
        # print(slow.val,fast.val if fast else -1)
        

        while sec:
            temp = sec.next 
            sec.next = prev
            prev = sec
            sec = temp 
        
        fir, sec = head, prev
        while sec:
            tmp1,tmp2 = fir.next,sec.next

            fir.next = sec
            sec.next = tmp1

            fir, sec = tmp1, tmp2


        # from the middle reverse the list 
        

        return 
        