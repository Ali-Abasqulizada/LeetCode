'''
Given the head of a linked list, rotate the list to the right by k places.
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        check = head
        count = 1
        while check.next:
            count += 1
            check = check.next
        k = k % count
        check.next = head
        current = head
        for _ in range(count - k - 1):
            current = current.next
        ans = current.next
        current.next = None
        return ans
    
'''
Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:

Input: head = [0,1,2], k = 4
Output: [2,0,1]
'''