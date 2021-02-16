# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        nodes = []
        dummy = head
        while head:
            nodes.append(head)
            head = head.next
        if n+1 < len(nodes):
            nodes[-1*(n+1)].next = nodes[-1*(n-1)]
        return dummy
