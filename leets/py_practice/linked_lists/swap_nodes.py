# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head.next is None:
            return head

        if head.next.next is None:
            temp = head.next
            head.next = None
            temp.next = head
            return temp

        temp = head
        result = temp
        while temp.val is not None:
            # second node becomes new head
            newHead = temp.next
            # assign original head the rest of the list
            others = temp.next.next
            temp.next = others
            newHead.next = temp

            temp = temp.next.next

        return result
