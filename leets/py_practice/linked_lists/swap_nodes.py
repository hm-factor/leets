# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        temp, temp.next = dummy, head
        while temp.next and temp.next.next:
            a = temp.next
            b = a.next
            temp.next, b.next, a.next = b, a, b.next
            temp = a

        return dummy.next
