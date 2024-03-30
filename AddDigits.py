'''
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
'''

class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            check = 0
            while num:
                check += num % 10
                num = num // 10
            num = check
        return num

#or
    
class Solution:
    def addDigits(self, num: int) -> int:
        return num % 9 if num % 9 != 0 or num == 0 else 9\
        
'''
Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.

Example 2:

Input: num = 0
Output: 0
'''