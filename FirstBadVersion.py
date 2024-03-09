'''
You are a product manager and currently leading a team to develop a new product. 
Unfortunately, the latest version of your product fails the quality check. 
Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, 
which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. 
Implement a function to find the first bad version. You should minimize the number of calls to the API.
'''

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

def isBadVersion():
    return "smt"

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n + 1
        for i in range(n + 1):
            ans = (left + right) // 2
            if isBadVersion(ans) == False and isBadVersion(ans + 1) == True:
                return ans + 1
            if isBadVersion(ans) == False:
                left = ans
            else:
                right = ans

#or
                
class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        while left <= right:
            ans = (left + right) // 2
            if isBadVersion(ans) == True:
                right = ans - 1
            else:
                left = ans + 1
        return left
    
'''
Example 1:

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

Example 2:

Input: n = 1, bad = 1
Output: 1
'''