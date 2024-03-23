'''
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, 
and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        first = ListNode()
        ans = first
        odd, even = head, head.next
        while odd and odd.next:
            ans.next = ListNode(odd.val)
            ans = ans.next
            odd = odd.next.next
        if odd:
            ans.next = ListNode(odd.val)
            ans = ans.next
        while even and even.next:
            ans.next = ListNode(even.val)
            ans = ans.next
            even = even.next.next
        if even:
            ans.next = ListNode(even.val)
            ans = ans.next
        return first.next
    
#or

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd = ListNode()
        oddC = odd
        even = ListNode()
        evenC = even
        while head and head.next:
            oddC.next = ListNode(head.val)
            oddC = oddC.next
            head = head.next
            evenC.next = ListNode(head.val)
            evenC = evenC.next
            head = head.next
        if head:
            oddC.next = ListNode(head.val)
            oddC = oddC.next
        oddC.next = even.next
        return odd.next

#or

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        odd = head
        even = head.next
        evenH = even
        while even and odd and even.next and odd.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenH
        return head

'''
Example 1:

Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Example 2:

Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
'''