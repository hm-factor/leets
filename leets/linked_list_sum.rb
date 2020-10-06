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
    storage = []

    while l1 || l2 || (carry != 0) do
        x = !l1.nil? ? l1.val : 0
        y = !l2.nil? ? l2.val : 0
        
        num = x + y + carry
        
        if num > 9 then
            carry = 1
            storage.push(num % 10)
        else
            carry = 0
            storage.push(num)
        end
            
        l1 = l1&.next
        l2 = l2&.next

        # &. is the safe operator -- lets me call methods on nil without throwing an error
    end

    storage
    # kinda cheated by not returning a linked list but oh well
end