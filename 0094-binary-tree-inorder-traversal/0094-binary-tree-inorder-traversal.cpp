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
    vector<int> inorderTraversal(TreeNode* root) {
        if (root == nullptr) 
        {
          return {};
        }
        vector<int> res;
        stack<TreeNode*> s;
        s.push(root);
        while (s.size()) {
          TreeNode* top = s.top();
          // implement traversal order
          if (top->left) { 
            s.push(top->left);
            top->left = NULL;
            continue;
          } 
          res.push_back(top->val);
          s.pop();
          if (top->right) {
            s.push(top->right);
            // top->right = NULL;
          }
       }
       
       return res;
    }
};