'''
Given the root of a binary tree, return the inorder traversal of its nodes' values.
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
        self.find(root.left, stack)
        stack.append(root.val)
        self.find(root.right, stack)
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        ans = []
        self.find(root, ans)
        return ans
    
'''
Example 1:

Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:

Input: root = []
Output: []

Example 3:

Input: root = [1]
Output: [1]
'''