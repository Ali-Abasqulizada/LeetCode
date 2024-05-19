'''
Given the root of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
    
#or

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        ans = 0
        stack = [(root, False)]
        while stack:
            cur, is_Left = stack.pop()
            if not cur:
                continue
            if not cur.left and not cur.right:
                if is_Left:
                    ans += cur.val
            else:
                stack.append((cur.left, True))
                stack.append((cur.right, False))
        return ans

#or

from collections import deque
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        ans = 0
        check = deque()
        check.append((root, False))
        while check:
            node, is_left = check.popleft()
            if not node:
                continue
            if not node.left and not node.right:
                if is_left:
                    ans += node.val
                continue
            check.append((node.left, True))
            check.append((node.right, False))
        return ans

#or

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        ans = 0
        def find(node, is_left):
            nonlocal ans
            if not node:
                return 
            if not node.left and not node.right:
                if is_left:
                    ans += node.val
                return
            find(node.left, True)
            find(node.right, False)
        find(root, False)
        return ans

'''
Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.

Example 2:

Input: root = [1]
Output: 0
'''