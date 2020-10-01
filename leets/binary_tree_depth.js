/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxDepth = function (root) {

  let sumDepth = (node, sum) => {
    if (node === null) {
      return sum;
    };

    return Math.max(sumDepth(node.left, sum + 1), sumDepth(node.right, sum + 1));
  };

  return sumDepth(root, 0);
};