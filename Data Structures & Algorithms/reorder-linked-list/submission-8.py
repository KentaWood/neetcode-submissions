# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        if not head or not head.next:
            return 
        

        slow = head
        fast = head.next
        # print("dsfsdf")

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next
        
        # print(slow.val)
        second = slow.next
        slow.next = None

        prev = None
        curr = second 
        
        while curr:
            tmp = curr.next

            curr.next = prev
            prev = curr
            curr = tmp
        
        # test = second

        # while test:
        #     print(test.val)
        #     test = test.next

        second = prev

        curr = head
        

        while second:
            tmp1, tmp2 = curr.next, second.next

            curr.next = second
            second.next = tmp1

            curr = tmp1
            second = tmp2

        return


        

        


        