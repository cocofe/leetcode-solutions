
// @Title: 移除链表元素 (Remove Linked List Elements)
// @Author: cocofe
// @Date: 2021-06-19 11:09:22
// @Runtime: 1 ms
// @Memory: 39.1 MB

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
    public ListNode removeElements(ListNode head, int val) {
        ListNode dummy = new ListNode();
        dummy.next = head;
        ListNode p = dummy;
        while(p != null && p.next != null){
            if (p.next.val == val){
                p.next = p.next.next;
            }
            else {
                p = p.next;
            }
        }
        return dummy.next;
    }
}
