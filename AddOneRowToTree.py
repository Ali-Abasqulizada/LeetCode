'''
Given the root of a binary tree and two integers val and depth, add a row of nodes with value val at the given depth depth.

Note that the root node is at depth 1.

The adding rule is:

Given the integer depth, for each not null tree node cur at the depth depth - 1, create two tree nodes with value val 
as cur's left subtree root and right subtree root.
cur's original left subtree should be the left subtree of the new left subtree root.
cur's original right subtree should be the right subtree of the new right subtree root.
If depth == 1 that means there is no depth depth - 1 at all, then create a tree node with value val as the new root of 
the whole original tree, and the original tree is the new root's left subtree.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        if depth == 1:
            ans = TreeNode(val)
            ans.left = root
            return ans
        def find(node, level):
            if not node:
                return
            elif level == depth - 1:
                leftN = TreeNode(val)
                rightN = TreeNode(val)
                leftN.left = node.left
                rightN.right = node.right
                node.left = leftN
                node.right = rightN
                return
            find(node.left, level + 1)
            find(node.right, level + 1)
        find(root, 1)
        return root
    
'''
Example 1:

Input: root = [4,2,6,3,1,5], val = 1, depth = 2
Output: [4,1,1,2,null,null,6,3,1,5]

Example 2:

Input: root = [4,2,null,3,1], val = 1, depth = 3
Output: [4,2,null,1,1,3,null,null,1]
'''