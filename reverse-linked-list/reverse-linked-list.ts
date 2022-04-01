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

function reverseList(head: ListNode | null): ListNode | null {
    var prev: ListNode = null,
        ptr: ListNode = head,
        oNxt: ListNode = null;
    
        
    while (ptr) {
        oNxt = ptr.next;
        ptr.next = prev;
        
        prev = ptr;
        ptr = oNxt;
    }
    
    return prev
};