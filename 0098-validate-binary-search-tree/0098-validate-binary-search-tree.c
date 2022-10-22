/**
 * Definition for a binary tree node->
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

bool validate(struct TreeNode * root, long low, long high) {
    if(root == NULL) return true;
    if((root->val <= low)|| (root->val >= high)) {
        return false;
    }
    
    return validate(root->left, low, (long)root->val) &&
            validate(root->right, (long)root->val, high);
}

bool isValidBST(struct TreeNode* root){
    return validate(root, LONG_MIN, LONG_MAX);
}

