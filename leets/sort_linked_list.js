/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var sortList = function(head) {
    if (head === null || head.next === null) return head;
    
//     here I split the link into halves
    let mid = findMid(head);
    let left = new ListNode(head);
    let right = new ListNode(mid);
    return mergeLinks(left, right);
};

function mergeLinks (l1, l2) {
    let dummy = new ListNode();
    let head = dummy;
    
    while(l1 && l2) {
        if (l1.val < l2.val) {
            head.next = l1;
            l1 = l1.next;
            head = head.next
        } else {
            head.next = l2;
            l2 = l2.next;
            head = head.next
        }
    }
    
    head.next = l1 ? l1 : l2;
    return dummy.next
}

function findMid (head) {
//     HOW TO SPLIT LINKLIST IN HALF: if you have one pointer move at double speed and one move at single speed,
//  when the double speed pointer makes its way out of the linked list, the slow pointer will be at half!
}