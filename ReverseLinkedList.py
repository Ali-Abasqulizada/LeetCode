'''
Given the head of a singly linked list, reverse the list, and return the reversed list.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        ans = None
        while head:
            next_node = head.next
            head.next = ans
            ans = head
            head = next_node
        return ans
    
'''
Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:

Input: head = [1,2]
Output: [2,1]

Example 3:

Input: head = []
Output: []
'''