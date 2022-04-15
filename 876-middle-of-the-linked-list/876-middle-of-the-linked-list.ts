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

function middleNode(head: ListNode | null): ListNode | null {
    var count: number = 1, 
        ptr: ListNode = null,
        mid: ListNode = null,
        alt: boolean = true;
    
    ptr = head,
    mid = head;

    while (ptr.next) {
        if (alt) mid = mid.next //((Math.floor(count / 2) + 1) ^ count) & 1
        alt = !alt
        ptr = ptr.next
        count++;
    }
        
    return mid
};