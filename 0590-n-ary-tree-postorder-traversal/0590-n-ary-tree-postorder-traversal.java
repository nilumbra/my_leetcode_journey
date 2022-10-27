/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
    public List<Integer> postorder(Node root) {
        traverse(root);
        return res;
    }
  
    List<Integer> res = new LinkedList<>();
    
    void traverse(Node root) {
      if(root == null) return;
      for(Node child: root.children) 
        traverse(child);
      
      res.add(root.val);
    }
}