class ListNode(object):
    def __init__(self, val=0, next=None):
        self.next = next
        self.val = val


class Solution(object):
    def reverseSingleLinkedList(self, head):
        previous = None
        current = head

        while current:
            next_temp = current.next
            current.next = previous
            previous = current
            current = next_temp
        return previous
    