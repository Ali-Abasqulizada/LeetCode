'''
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, 
leaving only distinct numbers from the original list. Return the linked list sorted as well.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        first = ListNode()
        current = first
        check = {}
        while head:
            check[head.val] = check.get(head.val, 0) + 1
            head = head.next
        for i in check:
            if check[i] == 1:
                current.next = ListNode(i)
                current = current.next
        return first.next

'''
Example 1:

Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:

Input: head = [1,1,1,2,3]
Output: [2,3]
'''