class ListNode(object):
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
class Solution(object):
    def deleteDuplicates(self, head):
        if head is None:
            return None
        dummy = ListNode(0)
        dummy.next = head
        current = dummy


        while current.next and current.next.next:
            if current.next.val == current.next.next.val:
                nodeRemoved = current.next.val
                while current.next and current.next.val == nodeRemoved:
                    current.next = current.next.next
            else:
                current = current.next

        return dummy.next
        
