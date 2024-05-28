class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> list[list[int]]:
        ans = []
        def find(node, total, check):
            if not node:
                return
            elif not node.left and not node.right:
                if node.val + total == targetSum:
                    ans.append(check + [node.val])
            check.append(node.val)
            total += node.val
            find(node.left, total, check)
            find(node.right, total, check)
            check.pop()
            total -= node.val
        find(root, 0, [])
        return ans
    
from collections import deque
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> list[list[int]]:
        ans = []
        check = deque()
        check.append((root, targetSum, []))
        while check:
            node, tSum, hold = check.popleft()
            if not node:
                continue
            elif not node.left and not node.right and node.val == tSum:
                ans.append(hold + [node.val])
            check.append((node.left, tSum - node.val, hold + [node.val]))
            check.append((node.right, tSum - node.val, hold + [node.val]))
        return ans