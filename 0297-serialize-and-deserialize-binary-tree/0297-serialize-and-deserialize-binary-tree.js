/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/**
 * Encodes a tree to a single string.
 *
 * @param {TreeNode} root
 * @return {string}
 */
var serialize = function(root) {
    const SEP = ','
    const NULL = '#'
    const arr = []
    function preorder(root) {
      if (root) {
        arr.push(root.val)
        preorder(root.left)
        preorder(root.right)
      } else {
        arr.push('#')  
      }
    }
    // if root is empty
    if (!root) return ''
  
    preorder(root)
    // console.log(arr.join(','))
    return arr.join(',')
};

/**
 * Decodes your encoded data to tree.
 *
 * @param {string} data
 * @return {TreeNode}
 */
var deserialize = function(data) {
    if (!data) return null
    // console.log(data.split(','))
    const arr = data.split(',')
    let i = 0 // pointer to the node to parse
    function d() {
      // deserialized root
      let root
      if (arr[i] != '#') {
        root = new TreeNode(parseInt(arr[i++]))
        root.left = d()
        root.right = d() 
      } else {
        root = null
        i++
      }
      
      return root 
    } 
  
    return d()
};

/**
 * Your functions will be called as such:
 * deserialize(serialize(root));
 */