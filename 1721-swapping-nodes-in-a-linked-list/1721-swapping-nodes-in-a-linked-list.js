/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */
var swapNodes = function(head, k) {
    let toswap, length, swapvalue, toswapvalue;
    var count = 1,
        ptr = head
    
    // First iteration
    // The goal is to get <length> and <swapvalue>
    while (ptr) {
        if(count == k){
           swapvalue = ptr.val;
        };
        
        ptr = ptr.next;
        count++;
    }
    
    length = count - 1;
    
    // Second iteration
    // The goal is to 1. get the (length-(k - 1))-th node's val 
    //                2. set the swapvalue to (length-(k - 1))-th node's val
    toswap = length - (k - 1); 
    ptr = head // Reset ptr to head
    count = 1;
    for (; count < toswap ; count++){
        ptr = ptr.next; // After i-th iteration, ptr points at i+1-th node
    }
    
    // toswap - 1 iteration ends, ptr points at toswap-th node
    toswapvalue = ptr.val;
    ptr.val = swapvalue;
    
    
    // Third iteration
    ptr = head // Reset ptr to head
    count = 1;
    for (; count < k ; count++){
        ptr = ptr.next; // After i-th iteration, ptr points at i+1-th node
    }
    
    ptr.val = toswapvalue
    
    return head
};