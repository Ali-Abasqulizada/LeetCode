'''
Given the root of a binary search tree, and an integer k, 
return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def all_elements(self, root, stack):
        if not root:
            return
        self.all_elements(root.left, stack)
        stack.append(root.val)
        self.all_elements(root.right, stack)
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        self.all_elements(root, stack)
        return stack[k - 1]

'''
Example 1:

Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
'''