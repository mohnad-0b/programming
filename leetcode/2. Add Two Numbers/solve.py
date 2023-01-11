# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        self.l3 = ListNode()
        head = self.l3
        c = 0

        while l1 or l2 or c:
          n1 = l1.val if l1 else 0
          n2 = l2.val if l2 else 0
          if (n1 + n2+c)//10 :
              head.next = ListNode((n1 + n2 +c)%10)
              c = 1
          else :
              head.next = ListNode((n1 + n2 +c)%10)
              c = 0

          head = head.next
          l1 = l1.next if l1 else None 
          l2 = l2.next if l2 else None

        return self.l3.next
