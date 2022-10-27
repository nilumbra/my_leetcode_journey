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

class Solution {
public:
    vector<Node*> stack;
    vector<int> postorder(Node* root) {
        if(!root) return {};
        vector<int> ans;
        Node * t;
      
        stack.push_back(root);
        for (Node* e: stack) cout<< e<<endl;
        
        while(!stack.empty()) {
          t = stack.back();
          stack.pop_back();
          
          ans.push_back(t->val);
          for (Node* child: t->children)
            stack.push_back(child);
        }
        
        reverse(ans.begin(), ans.end());
      
        return ans;
    }
};