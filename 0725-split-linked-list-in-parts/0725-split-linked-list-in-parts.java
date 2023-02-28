/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode[] splitListToParts(ListNode head, int k) {
        // Suppose the list length is N, and we have 
        // N % k = r 
        // Then the first r groups will have one more node than the rest of k - r groups
        // We can create partitions by first calculate the number of nodes in `head`, and 
        // iterate the list while assigning the partition to arr in the way discussed above
      
        int n = 0;
        ListNode ptr = head; 
        while (ptr != null) {
          ptr = ptr.next;
          n++;
        }
      
        ListNode[] ans = new ListNode[k];
      
        int r = n % k;
        int i = k;
        while (i > 0) { // from k to 1
          int grpL = n / k + ((r > 0) ? 1 : 0) - 1; // actually size - 1
          // System.out.println(i);
          ListNode gh = head;
          ans[k - i] = gh;
          
          // System.out.printf("%d %d %d\n", grpL+1, r, i);
          while (head != null && grpL > 0) {
            head = head.next; 
            grpL--;
          }
          
          // after forwarded by grpL-1 nodes 
          ListNode curr = head;
          if (head != null) {
            head = head.next;
            curr.next = null;
          }
          
          r--;
          i--;
        }  
      
        
        return ans;
    }
}