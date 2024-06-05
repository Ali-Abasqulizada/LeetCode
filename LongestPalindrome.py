'''
Given a string s which consists of lowercase or uppercase letters, return the length of the longest 
palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.
'''

class Solution:
    def longestPalindrome(self, s: str) -> int:
        check = {}
        for i in s:
            check[i] = check.get(i, 0) + 1
        ans = 0
        one = False
        for i in check:
            if check[i] % 2 == 0:
                ans += check[i]
            else:
                ans += (check[i] - 1)
                one = True
        return ans + 1 if one else ans

'''
Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
'''