'''
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head and not head.next:
            return True
        reverse = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            nextS = slow.next
            slow.next = reverse
            reverse = slow
            slow = nextS
        if fast:
            slow = slow.next
        while slow:
            if slow.val != reverse.val:
                return False
            slow = slow.next
            reverse = reverse.next
        return True

#or

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        check = []
        while head:
            check.append(head.val)
            head = head.next
        return check == check[::-1]

'''
Example 1:

Input: head = [1,2,2,1]
Output: true

Example 2:

Input: head = [1,2]
Output: false
'''