'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {}
        ans = -1
        for i in s:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1
        for i in seen:
            if seen[i] == 1:
                ans = i
                break
        if ans == -1:
            return ans
        return s.find(ans)

#or
    
class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {}
        for i in s:
            seen[i] = seen.get(i, 0) + 1
        for i in range(len(s)):
            if seen[s[i]] == 1:
                return i
        return -1

'''
Example 1:

Input: s = "leetcode"
Output: 0

Example 2:

Input: s = "loveleetcode"
Output: 2

Example 3:

Input: s = "aabb"
Output: -1
'''