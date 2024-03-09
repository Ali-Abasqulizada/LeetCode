'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        check = head
        current = head
        count = 0
        while check:
            count += 1
            check = check.next
        count -= n
        if count == 0:
            return head.next
        for i in range(count - 1):
            current = current.next
        if current.next.next:
            current.next = current.next.next
        else:
            current.next = None
        return head
    
#or
    
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow = head
        fast = head
        for i in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head

'''
Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []

Example 3:

Input: head = [1,2], n = 1
Output: [1]
'''