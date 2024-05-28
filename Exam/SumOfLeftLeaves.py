class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        ans = 0
        def find(node, left):
            nonlocal ans
            if not node:
                return 
            elif not node.left and not node.right:
                if left:
                    ans += node.val
                return
            find(node.left, True)
            find(node.right, False)
        find(root, False)
        return ans
    
from collections import deque
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        ans = 0
        check = deque()
        check.append((root, False))
        while check:
            node, left = check.popleft()
            if not node:
                continue
            elif not node.right and not node.left:
                if left:
                    ans += node.val
            else:
                check.append((node.left, True))
                check.append((node.right, False))
        return ans