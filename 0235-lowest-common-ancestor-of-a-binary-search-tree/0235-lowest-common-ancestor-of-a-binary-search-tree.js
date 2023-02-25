/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
var lowestCommonAncestor = function(root, p, q) {
    if (p.val >= q.val) {
      let t = p
      p = q
      q = t
    }
  
    function lca(root) {
      if ((p.val <= root.val) && (root.val <= q.val)) {
        return root 
      }
      else {
        if ((p.val <= root.val) && (q.val <= root.val)){
          return lca(root.left) // lca must in left sub tree
        }
        else if ((root.val <= p.val) && (root.val <= q.val)) {
          return lca(root.right) 
        }
      }
    } 
    // BST property: 
    // For any node `l` in left subtree of root, l.key <= root.key,
    // For any node `r` in right subtree of root, r.key >= root.key
    
    // the root is an ancestor of p and q, if root.key >= p.key, q.key or root.key <= p.key, q.key 
    // starting from root, the common ancestor of p, q is the first node A s.t. 
    // q.key <= A.key <= p.key
    return lca(root)
};