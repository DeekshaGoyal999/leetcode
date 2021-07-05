# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # prev = None
        # cur = head
        # while(cur):
        #     temp=cur.next
        #     cur.next=prev
        #     prev=cur
        #     cur=temp
        # return prev
        
        
        if not head or not head.next:
            return head;
        p = self.reverseList(head.next);
        head.next.next = head;
        head.next = None
        return p;
​
        
