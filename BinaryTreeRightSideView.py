'''
Given the root of a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.
'''

from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        if not root:
            return []
        queue = deque()
        ans = []
        queue.append(root)
        while queue:
            check = deque()
            val = 0
            while queue:
                cur = queue.popleft()
                if cur.left:
                    check.append(cur.left)
                if cur.right:
                    check.append(cur.right)
                val = cur
            ans.append(val.val)
            queue = check
        return ans

#or

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        ans = []
        def find(root, level):
            if not root:
                return
            if len(ans) == level:
                ans.append(root.val)
            find(root.right, level + 1)
            find(root.left, level + 1)
        find(root, 0)
        return ans

'''
Example 1:

Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:

Input: root = [1,null,3]
Output: [1,3]

Example 3:

Input: root = []
Output: []
'''