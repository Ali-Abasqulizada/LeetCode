'''
Given the root of a perfect binary tree, reverse the node values at each odd level of the tree.

For example, suppose the node values at level 3 are [2,1,3,4,7,11,29,18], then it should become [18,29,11,7,4,3,1,2].
Return the root of the reversed tree.

A binary tree is perfect if all parent nodes have two children and all leaves are on the same level.

The level of a node is the number of edges along the path between it and the root node.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def reverseOddLevels(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        def find(lnode, rnode, level):
            if not lnode and not rnode:
                return
            elif lnode and rnode and level % 2 == 0:
                lnode.val, rnode.val = rnode.val, lnode.val
            find(lnode.left, rnode.right, level + 1)
            find(lnode.right, rnode.left, level + 1)
        find(root.left, root.right, 0)
        return root

#or

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def reverseOddLevels(self, root: TreeNode) -> TreeNode:
        stack = [root]
        level = 0
        while stack:
            level += 1
            newStack = []
            for node in stack:
                if node.left:
                    newStack.append(node.left)
                if node.right:
                    newStack.append(node.right)
            if level % 2 != 0:
                for i in range((len(newStack) + 1) // 2):
                    newStack[i].val, newStack[len(newStack) - 1 - i].val = newStack[len(newStack) - 1 - i].val, newStack[i].val
            stack = newStack
        return root

'''
Example 1:

Input: root = [2,3,5,8,13,21,34]
Output: [2,5,3,8,13,21,34]
Explanation: 
The tree has only one odd level.
The nodes at level 1 are 3, 5 respectively, which are reversed and become 5, 3.

Example 2:

Input: root = [7,13,11]
Output: [7,11,13]
Explanation: 
The nodes at level 1 are 13, 11, which are reversed and become 11, 13.

Example 3:

Input: root = [0,1,2,0,0,0,0,1,1,1,1,2,2,2,2]
Output: [0,2,1,0,0,0,0,2,2,2,2,1,1,1,1]
Explanation: 
The odd levels have non-zero values.
The nodes at level 1 were 1, 2, and are 2, 1 after the reversal.
The nodes at level 3 were 1, 1, 1, 1, 2, 2, 2, 2, and are 2, 2, 2, 2, 1, 1, 1, 1 after the reversal.
'''