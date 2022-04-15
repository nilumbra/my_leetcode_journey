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

function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {
    var ptr = head,
        count = 1;
        
    
    while (ptr.next) {
        ptr = ptr.next;
        count++;
    }
    
    if (count == 1) {
        return null
    }
    
    
    const k: number = count - n;
    if (k == 0) {
        return head.next
    }
    count = 1;
    
    ptr = head;
    while (ptr.next) {
        if (count == k) {
            // console.log(count, ptr)
            ptr.next = ptr.next.next
            return head
        }
        ptr = ptr.next
        count++;
    }
};