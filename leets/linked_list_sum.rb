# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val = 0, _next = nil)
#         @val = val
#         @next = _next
#     end
# end
# @param {ListNode} l1
# @param {ListNode} l2
# @return {ListNode}
def add_two_numbers(l1, l2)

    carry = 0
    curr_node_1 = l1.val
    curr_node_2 = l2.val
    storage = []

    while curr_node_1 || curr_node_2 || carry == 1 do
        num = curr_node_1 + curr_node_2 + carry
        if num > 9 do
            carry = 1
            storage.unshift(num % 10)
        else
            carry = 0
            storage.unshift(num)
        end
        curr_node_1 = l1.next
        curr_node_2 = l2.next
    end

    storage


end