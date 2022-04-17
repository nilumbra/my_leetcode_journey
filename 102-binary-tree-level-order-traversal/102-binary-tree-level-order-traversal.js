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
 * @return {number[][]}
 */
var levelOrder = function(root) {
    
    var this_level = [],
        next_level = [],
        level_values = [];
    
    if (root == null) return []
    
    this_level.push(root);
    level_values.push([root.val])
    while (this_level.length) {
        const next_values = [];
        for (const node of this_level) {
            if (node.left) {
                next_level.push(node.left)
                next_values.push(node.left.val)
            }
            
            if (node.right) {
                next_level.push(node.right)
                next_values.push(node.right.val)
            }
        }
        this_level = next_level;
        next_level = []
        if (next_values.length) {
            level_values.push(next_values)    
        }
    }
    
    return level_values
};