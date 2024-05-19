'''
Given the head of a singly linked list and two integers left and right where left <= right, 
reverse the nodes of the list from position left to position right, and return the reversed list.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        ans = ListNode()
        cur = ans
        for _ in range(1, left):
            cur.next = ListNode(head.val)
            cur = cur.next
            head = head.next
        reverse = None
        for _ in range(left, right + 1):
            nextHead = head.next
            head.next = reverse
            reverse = head
            head = nextHead
        while reverse:
            cur.next = ListNode(reverse.val)
            cur = cur.next
            reverse = reverse.next
        cur.next = head
        return ans.next
    
'''
Example 1:

Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]
'''