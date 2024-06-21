'''
Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. 
(i.e., from left to right, level by level from leaf to root).
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> list[list[int]]:
        ans = []
        def find(node, level):
            if not node:
                return
            elif level == len(ans):
                ans.append([])
            ans[level].append(node.val)
            find(node.left, level + 1)
            find(node.right, level + 1)
        find(root, 0)
        return ans[::-1]
    
'''
Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[15,7],[9,20],[3]]

Example 2:

Input: root = [1]
Output: [[1]]

Example 3:

Input: root = []
Output: []
'''