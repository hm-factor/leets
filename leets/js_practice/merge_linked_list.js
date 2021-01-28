/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var mergeTwoLists = function (l1, l2) {
  // need a placeholder linked list to attach nodes of l1 and l2 to
  let dummy = new ListNode(-1);
  // the head is a pointer to the initiated node so that we can preserve it for later
  // otherwise we have a constantly updating listnode which isnt helpful
  let head = dummy;

  while (l1 !== null && l2 !== null) {
    // these assignments arent necessary but somehow increased runtime by 20ms
    let x = l1 ? l1.val : 0;
    let y = l2 ? l2.val : 0;

    if (x <= y) {
      dummy.next = l1;
      if (l1) {
        l1 = l1.next
      };
    } else {
      dummy.next = l2;
      if (l2) {
        l2 = l2.next
      };
    };

    dummy = dummy.next;
  };

  if (l1 === null) {
    dummy.next = l2;
  } else if (l2 === null) {
    dummy.next = l1;
  };


  return head.next
};