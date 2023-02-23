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
public:
    void flatten(TreeNode* root) {
        // Note the flatten linked list is in pre-order traversal of the tree
        while (root) {
          if (root->left) {
            TreeNode * left = root->left;
            TreeNode * right = root->right;
            TreeNode * left_rightmost_branch = left->right;
            
            // retrieve the rightmost branch of left subtree 
            if (left_rightmost_branch) {
              while (left_rightmost_branch->right) left_rightmost_branch = left_rightmost_branch->right;  
              left_rightmost_branch->right = right;
            } else {
              left->right = right;
            }
            
            
            root->right = left;
            root->left = nullptr;  
          }
          
          root = root->right;
        }
    }
};