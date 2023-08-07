/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function middleNode(head: ListNode | null): ListNode | null {
    // terminate if L[2n] == null （even）
    //           or L[2n+1] == null (odd)
    let slow = head
    let fast = head
    let prev = null
    
    while (fast && fast.next) {
        prev = slow
        slow = slow.next
        fast = fast.next.next // disconnect left half
    }
    
    if (prev) prev.next = null 
    return slow
};

function sortedListToBST(head: ListNode | null): TreeNode | null {
    // approach 1
    // Find the middle element, and recurse
    if (!head) return null
    
    const mid = middleNode(head) // get the middle ListNode
    const root = new TreeNode(mid.val)
    
    // base case, when the list just contains 1 node
    if (mid === head) return root
    
    root.left = sortedListToBST(head)
    root.right = sortedListToBST(mid.next)
 
    
    return root
};