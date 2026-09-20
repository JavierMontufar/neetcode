
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # [0, n-1, 1, n-2, 2, n-3, ...]

        if head.next == None:
            return
        
        node = head
        n = 0
        nodeList = []
        while node:
            nodeList.append(node)
            node = node.next
            n += 1
        
        half = math.ceil(n/2)
        l1 = head
        l2 = nodeList[half]
        nodeList[half-1].next = None # Point the last element of l1 to None

        # Invert the second half of the list
        prev, curr = None, l2
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        l2 = prev
       
        while l1 and l2:
            temp1 = l1.next
            l1.next = l2
            l1 = temp1
            temp2 = l2.next
            l2.next = l1
            l2 = temp2