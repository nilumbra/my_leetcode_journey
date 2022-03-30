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
 * @return {boolean}
 */
var isSymmetric = function(root) {
    var isEqualRecursive = function(left, right) {
        if ((left || right) && !(left && right)) { // if either left exclusively or right is True
            return false
        } else if (left && right){
            return left.val == right.val && isEqualRecursive(left.left, right.right) && isEqualRecursive(left.right, right.left)
        } else { // both are null
            return true
        }
    }

    return isEqualRecursive(root.left, root.right)
};