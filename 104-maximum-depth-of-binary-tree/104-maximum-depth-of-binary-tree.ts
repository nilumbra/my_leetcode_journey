/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function maxDepth(root: TreeNode | null): number {
    if (root == null) return 0;
    
    const frontier: Array<[TreeNode, number]> = [];
    
    
    var level: number = 0, tree: TreeNode | null = null;
    frontier.push([root, 0]);
    while (frontier.length > 0) {
        [tree, level] = frontier.shift();
        if (tree.left) {
            frontier.push([tree.left, level + 1])
        }

        if (tree.right) {
            frontier.push([tree.right, level + 1])
        }      
    }

    return level + 1
};