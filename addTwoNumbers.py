# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        head = None
        carry = 0
        while l1 and l2:
            num = l1.val + l2.val + carry
            if num > 9:
                carry = 1
                num = num - 10
            else:
                carry = 0
            if head == None:
                head = ListNode(num)
                tail = head
            else:
                tail.next = ListNode(num)
                tail = tail.next
            l1 = l1.next
            l2 = l2.next
        
        if l1==None:
            ll = l2
        else:
            ll = l1
        
        while ll:
            num = ll.val + carry
            if num > 9:
                carry = 1
                num = num - 10
            else:
                carry = 0
            if head == None:
                head = ListNode(num)
                tail = head
            else:
                tail.next = ListNode(num)
                tail = tail.next
            ll = ll.next
        
        if carry:
            tail.next = ListNode(1)
        
        return head
            
            
                
            
        