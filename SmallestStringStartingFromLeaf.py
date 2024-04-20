'''
You are given the root of a binary tree where each node has a value in the range [0, 25] representing the letters 'a' to 'z'.

Return the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

As a reminder, any shorter prefix of a string is lexicographically smaller.

For example, "ab" is lexicographically smaller than "aba".
A leaf of a node is a node that has no children.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        check = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        ans = []
        def find(node, word):
            if not node:
                return
            word += str(node.val) + " "
            if not node.left and not node.right:
                ans.append(word[:-1])
                return
            find(node.left, word)
            find(node.right, word)
        find(root, "")
        result = ""
        for w in ans:
            word = ""
            wordL = w.split()
            for i in range(len(wordL) - 1, -1, -1):
                word += check[int(wordL[i])]
            if result == "" or result > word:
                result = word
        return result

#or

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        ans = []
        def find(node, word):
            if not node:
                return
            word += str(node.val) + " "
            if not node.left and not node.right:
                ans.append(word[:-1])
                return
            find(node.left, word)
            find(node.right, word)
        find(root, "")
        result = ""
        for w in ans:
            word = ""
            wordL = w.split()
            for i in range(len(wordL) - 1, -1, -1):
                word += chr(97 + int(wordL[i]))
            if result == "" or result > word:
                result = word
        return result

'''
Example 1:

Input: root = [0,1,2,3,4,3,4]
Output: "dba"

Example 2:

Input: root = [25,1,3,1,3,0,2]
Output: "adz"

Example 3:

Input: root = [2,2,1,null,1,0,null,0]
Output: "abc"
'''