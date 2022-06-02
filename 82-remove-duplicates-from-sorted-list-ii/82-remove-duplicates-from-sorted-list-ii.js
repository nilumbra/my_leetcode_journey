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
var deleteDuplicates = function(head) {
    var u,
        uh,
        curr;
    
    uh = new ListNode(); // Initialize sentinel head 
    u = uh // The 'unique' linked node list
    
    curr = head; 
    while (curr) {
        
        // Think [uh + 1: u + 1] as contains only unique nodes (eventually returning this range as the answer)
        // Examine (u + 1)-th node and on
        if (curr.next && curr.val === curr.next.val) {
            let dup = curr.val;
            // Terminate when curr is null or 
            // curr.val is no longer equal to dup
            while (curr) {
                curr = curr.next;
                if (!(curr && curr.val === dup)) {
                    break;
                }
            }
            
            // Temporarily set u.next to the first different element
            // after the duplicate (including when u.next is undefined)
            // This covers the edge case of trailing duplicates
            u.next = curr;
        } else { // No duplication, so simply append and update the pointer
            u.next = curr;
            u = u.next;    
            curr = curr.next;
        }
    }
    
    return uh.next;
};