/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
typedef struct ListNode Node;

struct ListNode* deleteMiddle(struct ListNode* head){
    Node * slow = head, * fast = head, * pre = NULL;
    
    while (fast && fast->next) {
        pre = slow;
        slow = slow->next;
        fast = fast->next->next;
    }
    
    if (pre) {
        pre->next = slow->next;
        slow->next = NULL;
    } else {
        return NULL; // special case for 1-element linked list
    }
     
    return head;
}