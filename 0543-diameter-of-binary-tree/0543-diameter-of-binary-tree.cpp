/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */



class Solution {
  int global_diameter;
public:
    int depth(TreeNode* root) {
      if (root) {
        int left_tree_depth = depth(root->left);
        int right_tree_depth = depth(root->right);
        int diameter = left_tree_depth + right_tree_depth + 1;
        global_diameter = max(diameter, global_diameter);
        
        return max(left_tree_depth, right_tree_depth) + 1;
      }
      return 0;
    }
    int diameterOfBinaryTree(TreeNode* root) {
      global_diameter = -1;
       // depth(tree) = max(depth(left tree), depth(right tree)) + 1
       // diameter of a binary tree: depth(left tree) +  depth(right tree) + 1 
        
       // Algorithm
       // post order traversal to find depth of left tree and right 
      depth(root);
      return global_diameter - 1;
    }
};