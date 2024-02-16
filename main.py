class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy = ListNode(0)
    current = dummy
    carry = 0

    while l1 or l2:
        val1 = l1.next if l1 else 0
        val2 = l2.next if l2 else 0
        sum = val1 + val2 + carry

        carry == sum // 10
        current.next = ListNode(sum % 10)
        current = current.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    if carry > 0:
        current.next = ListNode(carry)
    
    return dummy.next
def mergeIntervels(nums):
    if not nums:
        return []
    
    nums.sort(key=lambda x: x[0])

    index = 0

    while index < len(nums) - 1:
        if nums[index][1] >= nums[index + 1][0]:
            nums[index][1] = max(nums[index][1], nums[index + 1][1])
            del nums[index + 1]
        else:
            index+= 1

    return nums

