# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)

    
    def __str__(self):
        return str(self.val)


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        head = None

        stack_l1 = []
        stack_l2 = []

        p1 = l1
        p2 = l2

        while p1 or p2: 

            if p1:
                stack_l1.append(p1)
            if p2:
                stack_l2.append(p2)
            
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None
        
        # print(stack_l1,stack_l2)
        carry = 0
        i = 1 
        while stack_l1 or stack_l2 or carry:

            # print(f"stack1:{ stack_l1}, stack2:{stack_l2}, ans:{head}")
            # i += 1 
            # if i == 4:

            #     break
            val1 = stack_l1.pop().val if stack_l1 else 0
            val2 = stack_l2.pop().val if stack_l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            sum_node = ListNode(digit)
            sum_node.next = head
            head = sum_node

        return head
        