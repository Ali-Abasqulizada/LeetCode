'''
Given a string s, partition s such that every substring of the partition is a palindrome. 
Return all possible palindrome partitioning of s.
'''

class Solution:
    def partition(self, s: str) -> list[list[str]]:
        ans = []
        def find(i, check):
            if i >= len(s):
                ans.append(check[:])
                return
            for j in range(i + 1, len(s) + 1):
                if s[i:j] == s[i:j][::-1]:
                    find(j, check + [s[i:j]])
        find(0, [])
        return ans
    
'''
Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]
'''