class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def reverseOddLevels(self, root: TreeNode) -> TreeNode:
        def find(left, right, level):
            if not left and not right:
                return 
            elif level % 2 == 0:
                left.val, right.val = right.val, left.val
            find(left.left, right.right, level + 1)
            find(left.right, right.left, level + 1)
        find(root.left, root.right, 0)
        return root

from collections import deque
class Solution:
    def reverseOddLevels(self, root: TreeNode) -> TreeNode:
        check = deque()
        check.append((root.left, root.right, 0))
        while check:
            left, right, level = check.popleft()
            if not left and not right:
                continue
            elif level % 2 == 0:
                left.val, right.val = right.val, left.val
            check.append((left.left, right.right, level + 1))
            check.append((left.right, right.left, level + 1))
        return root