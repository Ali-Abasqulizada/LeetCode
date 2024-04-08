'''
Given a linked list, swap every two adjacent nodes and return its head. 
You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        first = ListNode()
        current = first
        slow, fast = head, head.next
        while fast and fast.next:
            current.next = ListNode(fast.val)
            current = current.next
            fast = fast.next.next
            current.next = ListNode(slow.val)
            current = current.next
            slow = slow.next.next
        if fast:
           current.next = ListNode(fast.val)
           current = current.next
        if slow:
            current.next = ListNode(slow.val)
            current = current.next
        return first.next

'''
Example 1:

Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:

Input: head = []
Output: []

Example 3:

Input: head = [1]
Output: [1]
'''