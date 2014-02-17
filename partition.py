# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
 
class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        if head == None:
            return None
        if head.next == None:
            return head
            
        p = ListNode(x-1)
        p.next = head
        head = p
        prev = p
        ## find the location cur and insert smalller node after cur
        while p != None and p.val < x:
            prev = p
            p = p.next
        if p:
            cur = prev
        while p != None:
            if p.val < x:
                tmp = cur.next
                prev.next = p.next
                cur.next = p
                cur = p
                p.next = tmp
            prev = p
            p = p.next
                    
        return head.next
    