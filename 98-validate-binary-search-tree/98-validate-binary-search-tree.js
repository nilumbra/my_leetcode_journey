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
var isValidBST = function(root) {
    function isValid(root, ub, lb) {   
        return root == null || (ub == null || root.val < ub.val) && (lb == null || root.val > lb.val) && isValid(root.left, root, lb) && isValid (root.right, ub, root)
    }
    
    return isValid(root, null, null)
};