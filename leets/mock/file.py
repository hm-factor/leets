# https://www.bloomberg.com/opinion/articles/2021-01-27/reddit-driven-surge-puts-gamestop-and-ryan-cohen-in-a-weird-spot

# You are given the head of a linked list, and an integer k.
# Return the head of the linked list after swapping the values of the kth node 
# from the beginning and the kth node from the end (the list is 1-indexed).
# [1, 2, 3, 4, 5], k = 2
#     ^     ^
# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        counter = 0
        dummy = head 
        k_end = self.kFromEnd(head, k)
        k_begin = None

        while dummy is not None:
            counter += 1
            if counter == k:
                k_begin = dummy
                break
            dummy = dummy.next
        
        k_begin.val, k_end.val = k_end.val, k_begin.val

        tm = head
        while tm is not None:
            print(tm.val)
            tm = tm.next

        return head

    def kFromEnd(self, head, k):
        count = 0
        temp = head

        while temp is not None:
            count += 1
            temp = temp.next

        k_len = count - k
        k_node = None
        dummy = head

        while k_len > 0:
            k_len -= 1
            k_node = dummy.next
            dummy = dummy.next

        return k_node
        
arr = [i + 1 for i in range(5)]

tmp = ListNode(0)
ll = tmp # [0, 1, 2, 3, 4, 5]
for i in arr:
    tmp.next = ListNode(i)
    tmp = tmp.next

sol = Solution()
sol.swapNodes(ll, 2)


class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        length = 0
        k_begin = None
        
        tmp = head
        while tmp:
            length += 1
            if length == k:
                k_begin = tmp
            tmp = tmp.next
        
        k_end = head
        
        for _ in range(length - k):
            k_end = k_end.next
            
        k_end.val, k_begin.val = k_begin.val, k_end.val
        return head