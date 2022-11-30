// return the (n + 1) / 2 + 1 for even list
//            (n + 1) / 2 for odd list
struct ListNode* findMiddle(struct ListNode* head) {
  struct ListNode * slow = head;
  struct ListNode * fast = head;
  
  while(fast && fast->next) {
    slow = slow->next;
    fast = fast->next->next;
    // printf("slow.val: %d\n", slow->val);
  }
  
  return slow;
}


struct ListNode* reverseLinkedList(struct ListNode* head) {
  struct ListNode * prev = NULL;
  struct ListNode * curr = head;
  while (curr->next) {
    // printf("1");
    struct ListNode * nxt = curr->next;
    curr->next = prev;
    prev = curr;
    curr = nxt;
  }
  curr->next = prev;
  return curr;
}


bool isListPalindromic(struct ListNode* left, struct ListNode* right) {
  /**
   * Example: 
   * 1 -> 2 -> 2 <- 1 (even)
   *          /
   *        NULL
   *
   * 1 -> 2 <- 1 (odd)
   *     /
   *   NULL
   */
  while (right) {
    if (left->val != right->val) {
      return false;
    }
    left = left->next;
    right = right->next;
  }
  
  return true;
}

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool isPalindrome(struct ListNode* head){
  struct ListNode * left = head;
  
    // Find the ListNode to starting reverse from
  struct ListNode * slow = findMiddle(left);
  // printf("%d\n", slow->val);
  
  // Reverse the list  
  struct ListNode * right = reverseLinkedList(slow);
  
  return isListPalindromic(left, right);
}