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
 * @param {number} val
 * @return {TreeNode}
 */
var insertIntoBST = function(root, val) {
    // It is guaranteed that the new val does not exist in the original BST
    var head = root,
        insert = function insert (root, val) {
            // Safe to assume root is not none
            if (val < root.val) {
                if (root.left == null) {
                    root.left = new TreeNode(val);    
                } else {
                    insert(root.left, val)
                }
            } 
            
            if (val > root.val) {
                if (root.right == null) {
                    root.right = new TreeNode(val);    
                } else {
                    insert(root.right, val)
                }
            }
        }
    
    if (root == null) {
        return new TreeNode(val)
    }
    
    insert(head, val)
    return root
};