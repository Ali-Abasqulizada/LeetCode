'''
You are given two non-empty linked lists representing two non-negative integers. 
The most significant digit comes first and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1, num2 = "", ""
        ans = ListNode()
        cur = ans
        while l1:
            num1 += str(l1.val)
            l1 = l1.next
        while l2:
            num2 += str(l2.val)
            l2 = l2.next
        num1, num2 = num1[::-1], num2[::-1]
        i, j = 0, 0
        helper = 0
        total = ""
        while i < len(num1) or j < len(num2) or helper:
            n1 = int(num1[i]) if i < len(num1) else 0
            n2 = int(num2[j]) if j < len(num2) else 0
            check = n1 + n2 + helper
            total += str(check % 10)
            helper = check // 10
            i += 1
            j += 1
        for i in range(len(total) - 1, -1, -1):
            cur.next = ListNode(int(total[i]))
            cur = cur.next
        return ans.next

'''
Example 1:

Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]

Example 2:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]

Example 3:

Input: l1 = [0], l2 = [0]
Output: [0]
'''