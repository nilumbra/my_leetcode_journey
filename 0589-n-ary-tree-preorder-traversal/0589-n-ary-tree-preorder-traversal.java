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
    public List<Integer> preorder(Node root) {
      List<Integer> ans = new LinkedList<>();
      if(root == null) return ans;
      
      
      Stack<Node> S = new Stack<Node>();
      Node t;
      S.push(root);
      while(!S.isEmpty()) {
         t = S.pop();
        ans.add(t.val);
        for(int i = t.children.size() - 1; i >= 0; --i) {
          S.push(t.children.get(i));
        }
      }
      
      return ans;
    }
}