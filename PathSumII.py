'''
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where 
the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.
'''

from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> list[list[int]]:
        check = deque()
        check.append((root, targetSum))
        ans = []
        def find(node, tSum, ele):
            if not node:
                return
            ele += str(node.val) + " "
            if not node.left and not node.right and node.val == tSum:
                helper = []
                word = ""
                for e in ele:
                    if e != " ":
                        word += e
                    else:
                        helper.append(int(word))
                        word = ""
                ans.append(helper)
                return
            find(node.left, tSum - node.val, ele)
            find(node.right, tSum - node.val, ele)
        find(root, targetSum, "")
        return ans

#or

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> list[list[int]]:
        ans = []
        def find(node, path, ans, tSum):
            if not node:
                return
            path.append(node.val)
            if not node.left and not node.right and node.val == tSum:
                ans.append(path[:])
            find(node.left, path, ans, tSum - node.val)
            find(node.right, path, ans, tSum - node.val)
            path.pop()
        find(root, [], ans, targetSum)
        return ans

#or

from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> list[list[int]]:
        check = deque()
        check.append((root, targetSum, []))
        ans = []
        while check:
            node, tSum, path = check.popleft()
            if not node:
                continue
            if not node.left and not node.right and node.val == tSum:
                ans.append(path + [node.val])
            check.append((node.left, tSum - node.val, path + [node.val]))
            check.append((node.right, tSum - node.val, path + [node.val]))
        return ans

'''
Example 1:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22

Example 2:

Input: root = [1,2,3], targetSum = 5
Output: []

Example 3:

Input: root = [1,2], targetSum = 0
Output: []
'''