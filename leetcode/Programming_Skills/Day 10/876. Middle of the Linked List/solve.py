# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        head2 = head

        while True:

            arr.append(head.val)
            if head.next == None :
                break
            else :
                head = head.next
        
        for _ in range(len(arr)//2):
            head2 = head2.next
            
        return head2