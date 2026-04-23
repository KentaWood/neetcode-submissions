class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1. Find the middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse second half
        second = slow.next
        slow.next = None  # Split the list into two
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        first = head
        second = prev 

        while second:
            tmp1,tmp2 = first.next, second.next

            first.next = second
            second.next = tmp1
            
            first = tmp1
            second = tmp2

        return
            