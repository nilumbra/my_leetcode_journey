/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/


class Solution {
public:
    // original => clone
    unordered_map<int, Node*> mp; // declaring map, to check whwther we have a copy of node or not and also to store copy
    
    Node* cloneGraph(Node* node) {
        if(node == NULL) // if node is null, then simply return null
        {
            return NULL;
        }
        
        // for a node, we will check whether we already creates a copy of this or not. (Note that we can use the node's val as key of the map as they are guarenteed to be unique across the graph)
        // If it is present in map that means we already created a copy of this, so simply return it 
      
        // But if not present in map, we need to first clone the node, then estabish all the edges with its neighbors 
        
        if(mp.find(node->val) == mp.end()) // if not present in map
        {
            mp[node->val] = new Node(node -> val, {}); // make a copy
            
            for(auto adj: node -> neighbors) // travel in adjcant
            {
                mp[node->val] -> neighbors.push_back(cloneGraph(adj)); //add copy
            }
        }
        
        // either node is already cloned  \
        // or it's newly cloned          -- the node is cloned and will be returned to its caller
        return mp[node->val]; 
    }
};