# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
   
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head=l3=ListNode(0)
        print("Linkedlist(0)",l3)
        carry=0
        while l1 or l2 or carry:
            if l1:
                carry+=l1.val
                l1=l1.next
            if l2:
                carry+=l2.val
                l2=l2.next
            l3.val=carry%10
            carry=carry//10  
            if l1 or l2 or carry:
                l3.next=ListNode(0)
                l3=l3.next
        return head
    
        #reverse 
        # def rev(l):
        #     prev=None
        #     curr=l
        #     while(curr):
        #         temp=curr.next
        #         curr.next=prev
        #         prev=curr
        #         curr=temp
        #     return prev
        # l11=rev(l1)
        # l22=rev(l2)
        # h=l3=ListNode(0)
        # carry=0
        # while l11 or l22 or carry:
        #     if l11:
        #         carry+=l11.val
        #         l11=l11.next
