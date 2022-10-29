# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        b = ""
        while True:
            
            print(head.val,end="")
            b += str(head.val)
            if head.next == None :
                break
            else :
                head = head.next
        return int(b,2)