# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        arr1 = []
        while l1:
            arr.append(l1.val)  # Add .val here
            l1 = l1.next
        while l2:
            arr1.append(l2.val) # Add .val here
            l2 = l2.next
        arr.reverse()
        arr1.reverse()
        
        res1 = "".join(map(str, arr))
        res2 = "".join(map(str, arr1))

        final = int(res1) + int(res2)
        

        sum_str = str(final)[::-1] 
        
        dummy = ListNode(0)
        current = dummy
        for char in sum_str:
            current.next = ListNode(int(char))
            current = current.next
            
        return dummy.next
            
        