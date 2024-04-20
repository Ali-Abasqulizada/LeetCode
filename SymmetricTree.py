'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
            return self.check(root.left, root.right)
    def check(self, leftroot, rightroot):
        if not leftroot and not rightroot:
            return True
        elif not leftroot or not rightroot:
            return False
        elif leftroot.val != rightroot.val:
            return False
        else:
            return self.check(leftroot.left, rightroot.right) and self.check(leftroot.right, rightroot.left)

#or

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack = [(root.left, root.right)]
        while stack:
            left, right = stack.pop()
            if left and right:
                if left.val != right.val:
                    return False
                stack.append((left.left, right.right))
                stack.append((left.right, right.left))
            elif left or right:
                return False
        return True

'''
Example 1:

Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:

Input: root = [1,2,2,null,3,null,3]
Output: false
'''