/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2){
    // Return list2 if list1 happens to be NULL,
    // and vice versa
    if (list1 == NULL) {
        return list2;
    }
    if (list2 == NULL) {
        return list1;
    }
    
    
    struct ListNode* head;
    head = list1;
    if (list1->val < list2->val) {
        list1 = list1->next;
    } else {
        head = list2;
        list2 = list2->next;
    }
    struct ListNode* ptr = head;
    

    while (list1 && list2 ) {
        if (list1->val < list2->val) {
            ptr->next = list1;
            list1 = list1->next;
        } else {
            ptr->next = list2;
            list2 = list2->next;
        }
        ptr = ptr->next;
    }
    
    if (list1 != NULL) {
        ptr->next = list1;
    } 
    if (list2 != NULL) {
        ptr->next = list2;
    }
    
    return head;
}