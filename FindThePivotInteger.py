'''
Given a positive integer n, find the pivot integer x such that:

The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.
Return the pivot integer x. If no such integer exists, return -1. 
It is guaranteed that there will be at most one pivot index for the given input.
'''

class Solution:
    def pivotInteger(self, n: int) -> int:
        left = 0
        right = n
        while left <= right:
            lsum = rsum = 0
            ave = (left + right) // 2
            for i in range(ave):
                lsum += i
            for j in range(ave + 1, n + 1):
                rsum += j
            if lsum == rsum:
                return ave
            elif lsum < rsum:
                left += 1
            else:
                right -= 1
        return -1

#or

class Solution:
    def pivotInteger(self, n: int) -> int:
        ave = n // 2
        lsum = rsum = 0
        for i in range(ave + 1):
            lsum += i
        for j in range(ave, n + 1):
            rsum += j
        while lsum <= rsum:
            if lsum == rsum:
                return ave
            else:
                rsum -= ave
                ave += 1
                lsum += ave
        return -1

'''
Example 1:

Input: n = 8
Output: 6
Explanation: 6 is the pivot integer since: 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21.

Example 2:

Input: n = 1
Output: 1
Explanation: 1 is the pivot integer since: 1 = 1.

Example 3:

Input: n = 4
Output: -1
Explanation: It can be proved that no such integer exist.
'''