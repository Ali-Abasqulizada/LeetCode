'''
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a 
height-balanced binary search tree.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        check = []
        while head:
            check.append(head.val)
            head = head.next
        def find(arr):
            if len(arr) == 0:
                return
            l, r = 0, len(arr) - 1
            mid = (l + r) // 2
            root = TreeNode(arr[mid])
            root.left = find(arr[:mid])
            root.right = find(arr[mid + 1:])
            return root
        return find(check)
    
'''
Example 1:

Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.

Example 2:

Input: head = []
Output: []
'''