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
    double pre = -INFINITY;
    bool isValidBST(TreeNode* root) {
        if (!root) return true;
        
        // in-order traverse BST
        bool l = isValidBST(root->left);
        if(root->val <= pre) {
            return false;
        }
        pre = root->val;
        bool r = isValidBST(root->right);
        return l && r;
    }
};