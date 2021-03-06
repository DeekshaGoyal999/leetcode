# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # #Method-1
        # arr=[head]
        # while arr[-1].next:
        #     arr.append(arr[-1].next)
        # print(arr)
        # return arr[len(arr)//2]
        #Method-2
        
        fast=slow=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
                    
            
            
            
