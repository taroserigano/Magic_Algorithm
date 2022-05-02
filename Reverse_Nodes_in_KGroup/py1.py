# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:\

        def reverse(head, k):
            p = head
            for i in range(k):
                if(p):
                    p = p.next
                else:
                    return head

            pre = head 
            now = head.next
            print("Now " , now)
            pre.next = None
            print("PRE ", pre)
            i = 1
            while(now != None and i < k):
                nex = now.next
                print(" next " , nex)
                now.next = pre
                pre = now 
                now = nex
                i += 1
            print("THE whole pre " , pre)
            print(" head " , head)
            if(now != None):
                head.next = reverse(now, k)

            return pre

        if(head):
            return reverse(head, k)
        else:
            return None
