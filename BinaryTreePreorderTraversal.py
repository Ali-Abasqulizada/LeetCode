'''
Given the root of a binary tree, return the preorder traversal of its nodes' values.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def find(self, root, stack):
        if not root:
            return
        stack.append(root.val)
        self.find(root.left, stack)
        self.find(root.right, stack)
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        ans = []
        self.find(root, ans)
        return ans

'''
Example 1:

Input: root = [1,null,2,3]
Output: [1,2,3]

Example 2:

Input: root = []
Output: []

Example 3:

Input: root = [1]
Output: [1]
'''