'''
Given the head of a linked list and a value x, partition it such that all nodes 
less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        first = ListNode()
        current = first
        copy = head
        while copy:
            if copy.val < x:
                current.next = ListNode(copy.val)
                current = current.next
            copy = copy.next
        while head:
            if head.val >= x:
                current.next = ListNode(head.val)
                current = current.next
            head = head.next
        return first.next

#or
    
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        less, more = ListNode(), ListNode()
        less_cur, more_cur = less, more
        while head:
            if head.val < x:
                less_cur.next, less_cur = head, head
            else:
                more_cur.next, more_cur = head, head
            head = head.next
        more_cur.next = None
        less_cur.next = more.next
        return less.next

'''
Example 1:

Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Example 2:

Input: head = [2,1], x = 2
Output: [1,2]
'''