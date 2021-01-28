/********************************************************
 * CODE INSTRUCTIONS:                                   *
 * 1) The method findInOrderSuccessor you're asked      *
 *    to implement is located at line 26.               *
 * 2) Use the helper code below to implement it.        *
 * 3) In a nutshell, the helper code allows you to      *
 *    to build a Binary Search Tree.                    *
 * 4) Jump to line 94 to see an example for how the     *
 *    helper code is used to test findInOrderSuccessor. *
 ********************************************************/

// if no right child
  // if left child, go up once
  // if right child, go up until left, then once more
    // but if parent node is null, then input has no successor

//if right child, go right, then left until left child is left than root

// Constructor to create a new Node
function Node(key) {
    this.key = key;
    this.parent = null;
    this.left = null;
    this.right = null;
}

// Constructor to create a new BST 
function BinarySearchTree() {
    this.root = null;
}

BinarySearchTree.prototype.findInOrderSuccessor = function(inputNode) {
  
  if (inputNode.right !== null) {
    return this.goLeft(inputNode.right)
  } else {
    if (inputNode === inputNode.parent.left) {
      return inputNode.parent
    } else {
      let temp = inputNode;
      while (temp.parent !== null) {
        if (temp === temp.parent.left) {
          return temp.parent;
        } else {
           temp = temp.parent;
        }
      }
      return null;
    }
  } 
}

BinarySearchTree.prototype.goLeft = function(node) {
  
  while (node.left !== null) {
    node = this.goLeft(node.left)
  }
  return node
}
