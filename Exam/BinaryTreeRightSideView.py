class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        ans = []
        def find(node, level):
            if not node:
                return
            elif len(ans) == level:
                ans.append(node.val)
            find(node.right, level + 1)
            find(node.left, level + 1)
        find(root, 0)
        return ans
    
from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        if not root:
            return []
        ans = []
        check = deque()
        check.append(root)
        while check:
            helper = deque()
            right = 0
            while check:
                node = check.popleft()
                if node.left:
                    helper.append(node.left)
                if node.right:
                    helper.append(node.right)
                right = node
            ans.append(right.val)
            check = helper
        return ans