'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
'''

from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        if not root:
            return []
        queue = deque()
        ans = []
        queue.append(root)
        while queue:
            level = []
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(level)
        return ans
    
#or

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        if not root:
            return []
        ans = []
        def find(root, level):
            if not root:
                return
            elif len(ans) <= level:
                ans.append([])
            ans[level].append(root.val)
            find(root.left, level + 1)
            find(root.right, level + 1)
        find(root, 0)
        return ans

'''
Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:

Input: root = [1]
Output: [[1]]

Example 3:

Input: root = []
Output: []
'''