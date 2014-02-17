# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        p = ListNode(0)
        p.next = head
        head = p
        
        while True:
            if p.next == None: 
                break
            if p.next.next == None:
                break
            q1 = p.next
            q2 = q1.next
            q1.next = q2.next
            q2.next = q1
            p.next = q2
            p = q1

        return head.next

        
        
        