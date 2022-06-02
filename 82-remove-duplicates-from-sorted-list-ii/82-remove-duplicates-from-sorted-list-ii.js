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
        curr,
        prev;
    
    uh = new ListNode();
    u = uh 
    
    curr = head;
    prev = head;
    while (curr) {
        // console.log(curr.val)
        if (curr.next && curr.val === curr.next.val) {
            // console.log(`dup`)
            // console.log(curr)
            // console.log('--')
            let dup = curr.val;
            
            // Terminate when curr is null or 
            // curr.val is no longer equal to dup
            while (curr) {
                curr = curr.next;
                if (!(curr && curr.val === dup)) {
                    // console.log()
                    break;
                }
            }
            u.next = curr;
        } else {
            u.next = curr;
            // console.log("non dup")
            // console.log(curr);
            // console.log("--")
            u = u.next;    
            curr = curr.next;
        }
    }
    
    return uh.next;
};