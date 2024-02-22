class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Linkedlist:
    def deleteNode(node):
        node.val = node.next.val
        node.next = node.next.next

    