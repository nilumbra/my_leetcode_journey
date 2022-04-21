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
 * @return {number[]}
 */
var postorderTraversal = function(root) {
    const out = [];
    
    function recurse(root) {
        if (root) { 
            recurse(root.left)
            recurse(root.right)
            out.push(root.val)
        }    
    }
    
    recurse(root)
    return out
};