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

function hasCycle(head: ListNode | null): boolean {
    var slow: ListNode = head,
        fast: ListNode = head;

    if (head == null) return false
    
    while (fast.next && fast.next.next) { 
        fast = fast.next.next;
        slow = slow.next;
        if (fast == slow) return true
    }
    
    return false
};