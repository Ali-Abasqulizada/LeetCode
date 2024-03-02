'''
Given the head of a linked list and an integer val, remove all the nodes of the linked list 
that has Node.val == val, and return the new head.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        first = ListNode()
        current = first
        while head:
            if head.val != val:
                current.next = ListNode(head.val)
                current = current.next
            head = head.next
        return first.next

'''
Example 1:

Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Example 2:

Input: head = [], val = 1
Output: []

Example 3:

Input: head = [7,7,7,7], val = 7
Output: []
'''