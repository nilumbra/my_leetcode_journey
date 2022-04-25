/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var swapPairs = function(head) {
    var swap = function swap(ptr) {
        if (ptr.next == null || ptr.next.next == null) {
            return
        }
        
        const first = ptr.next,
              second = ptr.next.next,
              third = ptr.next.next.next;
        ptr.next = second;
        second.next = first;
        first.next = third;
        
        swap(first)
    }
    
    if (head == null || head.next == null) {
        return head
    }
    let placeholder = new ListNode(), 
        new_head = head.next;
    
    placeholder.next = head;
    swap(placeholder);
    
    return new_head
};