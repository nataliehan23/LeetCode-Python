# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        head = None
        runner = None
        p1 = l1
        p2 = l2
        while p1 and p2:
            if not head:
                if p1.val <= p2.val:
                    head = p1
                    runner = head
                    p1 = p1.next
                else:
                    head = p2
                    runner = head
                    p2 = p2.next
            else:
                if p1.val <= p2.val:
                    runner.next = p1
                    runner = runner.next
                    p1 = p1.next
                else:
                    runner.next = p2
                    runner = runner.next
                    p2 = p2.next
        if p1:
            runner.next = p1
        if p2:
            runner.next = p2
        return head
                    
                
     