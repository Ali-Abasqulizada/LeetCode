'''
Given the root of a binary search tree and an integer k, return true 
if there exist two elements in the BST such that their sum is equal to k, or false otherwise.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def find_elements(self, root, arr):
        if not root:
            return 
        self.find_elements(root.left, arr)
        self.find_elements(root.right, arr)
        arr.append(root.val)
    def findTarget(self, root: TreeNode, k: int) -> bool:
        check = {}
        arr = []
        self.find_elements(root, arr)
        for i in arr:
            if k - i in check:
                return True
            check[i] = i
        return False

#or

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        check = {}
        def find(root):
            if not root:
                return False
            if root.val in check:
                return True
            check[k - root.val] = True
            return find(root.left) or find(root.right)
        return find(root)

'''
Example 1:

Input: root = [5,3,6,2,4,null,7], k = 9
Output: true

Example 2:

Input: root = [5,3,6,2,4,null,7], k = 28
Output: false
'''