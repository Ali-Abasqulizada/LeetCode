'''
You are given two linked lists: list1 and list2 of sizes n and m respectively.

Remove list1's nodes from the ath node to the bth node, and put list2 in their place.

The blue edges and nodes in the following figure indicate the result:
Build the result list and return its head.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        first = ListNode()
        cur = first
        for _ in range(a):
            cur.next = ListNode(list1.val)
            cur = cur.next
            list1 = list1.next
        while list2:
            cur.next = ListNode(list2.val)
            cur = cur.next
            list2 = list2.next
        for _ in range(b - a + 1):
            list1 = list1.next
        cur.next = list1
        return first.next
    
#or

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        ans = list1
        helper = list1
        for _ in range(a - 1):
            ans = ans.next
            helper = helper.next
        for _ in range(b - a + 2):
            helper = helper.next
        ans.next = list2
        while ans.next:
            ans = ans.next
        ans.next = helper
        return list1

#or

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        ans = list1
        for _ in range(a - 1):
            ans = ans.next
        helper = ans.next
        for _ in range(b - a + 1):
            helper = helper.next
        ans.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = helper
        return list1

'''
Example 1:

Input: list1 = [10,1,13,6,9,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
Output: [10,1,13,1000000,1000001,1000002,5]
Explanation: We remove the nodes 3 and 4 and put the entire list2 in their place. 
The blue edges and nodes in the above figure indicate the result.

Example 2:

Input: list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,1000003,1000004]
Output: [0,1,1000000,1000001,1000002,1000003,1000004,6]
Explanation: The blue edges and nodes in the above figure indicate the result.
'''