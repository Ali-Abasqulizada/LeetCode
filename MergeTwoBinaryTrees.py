'''
You are given two binary trees root1 and root2.

Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. 
You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, 
then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

Return the merged tree.

Note: The merging process must start from the root nodes of both trees.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution: 
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2
        elif not root2:
            return root1
        else:
            ans = TreeNode(root1.val + root2.val)
            ans.left = self.mergeTrees(root1.left, root2.left)
            ans.right = self.mergeTrees(root1.right, root2.right)
        return ans

#or

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution: 
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2
        elif not root2:
            return root1
        check = [[root1, root2]]
        while check:
            node1, node2 = check.pop()
            if node1.left and node2.left:
                check.append((node1.left, node2.left))
            elif not node1.left:
                node1.left = node2.left
            if node1.right and node2.right:
                check.append((node1.right, node2.right))
            elif not node1.right:
                node1.right = node2.right
            node1.val += node2.val
        return root1

'''
Example 1:

Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
Output: [3,4,5,5,4,null,7]

Example 2:

Input: root1 = [1], root2 = [1,2]
Output: [2,2]
'''