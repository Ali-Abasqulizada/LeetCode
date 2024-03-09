'''
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. 
The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
'''

class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        for i in range(x + 1):
            if i * i > x:
                return i - 1

#or
            
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        left = 1
        right = x
        while left <= right:
            ave = (left + right) // 2
            if ave == x // ave:
                return ave
            elif ave > x // ave:
                right = ave - 1
            else:
                left = ave + 1
        return right
    
'''
Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
'''