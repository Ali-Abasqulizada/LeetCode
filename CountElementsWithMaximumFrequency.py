'''
You are given an array nums consisting of positive integers.

Return the total frequencies of elements in nums such that those elements all have the maximum frequency.

The frequency of an element is the number of occurrences of that element in the array.
'''

class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        ans = {}
        for i in nums:
            if i in ans:
                ans[i] += 1
            else:
                ans[i] = 1
        maxF = max(ans.values())
        check = [num for num, val in ans.items() if val == maxF]
        return maxF * len(check)
    
#or
    
class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        ans = [0] * 101
        count, val = 0, 0
        for i in nums:
            ans[i] += 1
            val = max(val, ans[i])
        for i in ans:
            if val == i:
                count += i
        return count
    
'''
Example 1:

Input: nums = [1,2,2,3,1,4]
Output: 4
Explanation: The elements 1 and 2 have a frequency of 2 which is the maximum frequency in the array.
So the number of elements in the array with maximum frequency is 4.

Example 2:

Input: nums = [1,2,3,4,5]
Output: 5
Explanation: All elements of the array have a frequency of 1 which is the maximum.
So the number of elements in the array with maximum frequency is 5.
'''