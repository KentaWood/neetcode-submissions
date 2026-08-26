# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head
        curr = head
        prev = dummy

        while curr:
            
            if curr.val == val:

                tmp = curr.next

                # not the head node, prev stays the same, curr goes to curr.next, curr.next points to none
                if prev != dummy:
                    
                    prev.next = curr.next
                    curr.next = None

                    curr = tmp
                # head, the dummy.next moves to new possible head, curr point to none, prev stays the same
                else:

                    dummy.next = head.next
                    curr.next = None
                    curr = tmp
                
            else:
                prev = curr
                curr = curr.next
        
        return dummy.next

            
                






        