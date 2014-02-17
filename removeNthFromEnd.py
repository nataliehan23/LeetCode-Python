# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        if head == None:
            return head
        if n <=0:
            return head
        fast = head
        slow = head
        prev = head
        ## move fast to the nth location
        for i in range(n):
            if fast:
                fast = fast.next
            else:
                return head
                
        ## remove the head, if the length of the list is the number
        if not fast:
            return head.next
        
        while fast:
            prev = slow
            fast = fast.next
            slow = slow.next
            
        prev.next = slow.next
        return head
        
            
        
        