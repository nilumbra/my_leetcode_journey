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
    public List<List<Integer>> levelOrder(Node root) {
        List<List<Integer>> res = new ArrayList<>();
        if (root == null) return res;
        Queue<Node> nextLevel = new LinkedList<>();
        nextLevel.add(root);
      
        while (!nextLevel.isEmpty()) {
          List<Integer> thisLevel = new ArrayList<>();
          int size = nextLevel.size();
          for (int i = 0; i < size; i++) {
            Node node = nextLevel.poll();
            thisLevel.add(node.val);
            nextLevel.addAll(node.children);
          }
          
          res.add(thisLevel);
        }
      
        return res;
    }
}