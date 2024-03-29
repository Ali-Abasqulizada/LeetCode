'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
'''

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        first = ListNode()
        current = first
        while list1 and list2:
            if list1.val > list2.val:
                current.next = ListNode(list2.val)
                list2 = list2.next
            else:
                current.next = ListNode(list1.val)
                list1 = list1.next
            current = current.next
        current.next = list1 if list1 else list2
        return first.next
    
'''
Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
'''