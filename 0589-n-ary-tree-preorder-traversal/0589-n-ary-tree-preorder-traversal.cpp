/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

// Recursive
// class Solution {
// public:
//     vector<int> ans;
//     void traverse(Node* root) {
//       if (root) {
//         ans.push_back(root->val);
//         for (Node* child: root->children) // for in
//           traverse(child);
//       }
//     }
//     vector<int> preorder(Node* root) {
//         traverse(root);
//         return ans;
//     }
// };

// Iterative
class Solution {
public:
    vector<int> ans;
    stack<Node*> stack;
    vector<int> preorder(Node* root) {
        if (!root) return {};
        
        Node* t;
        stack.push(root);
        while(!stack.empty()) {
          t = stack.top();
          stack.pop();
          
          ans.push_back(t->val); // add to ans
          
          // push stack from right to left, so they leave from left to right
          for(int i = t->children.size() - 1; i >= 0; --i) 
            stack.push(t->children[i]);
        }
        
        return ans;
    }
};