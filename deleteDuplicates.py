tion for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head == None:
            return None
        nodes = set()
        nodes.add(head.val)
        fast = head.next
        slow = head
        
        while fast:
            if fast.val in nodes:
                slow.next = fast.next
                fast = fast.next
            else:
                nodes.add(fast.val)
                fast = fast.next
                slow = slow.next
        return head
            
        
