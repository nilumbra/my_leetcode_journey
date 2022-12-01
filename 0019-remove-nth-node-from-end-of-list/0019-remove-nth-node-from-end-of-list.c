
struct ListNode * prev_ptr;
struct ListNode * next_ptr;


/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n){
  // get the number of nodes in list
  
  int cnt = 0;
  struct ListNode* ptr = head;
  for (;ptr;ptr=ptr->next, cnt++)
    ;
  
  int i = cnt - n; // the node to be removed is the i-th node in the list
  

  
  // initialize nodes for traversing
  ptr = head;
  prev_ptr = NULL;
  next_ptr = ptr->next;
  
  if(i == 0) {
    return next_ptr;  
  }
  
  // move (i - 1) times, and do delete
  for (; i > 0; i--) {
    prev_ptr = ptr;
    ptr = next_ptr;
    next_ptr = next_ptr->next;
  }
  
  // if (prev_ptr) {
    prev_ptr->next = next_ptr;
    return head;
  // }
  // else 
  //   return NULL; // 1-element
  
}