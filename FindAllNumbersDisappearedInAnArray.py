'''
Given an array nums of n integers where nums[i] is in the range [1, n], 
return an array of all the integers in the range [1, n] that do not appear in nums.
'''

class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        length = len(nums)
        check = {}
        ans = []
        for i in nums:
            check[i] = 1
        for i in range(1, length + 1):
            if check.get(i, 0) == 0:
                ans.append(i)
        return ans

#or

class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        length = len(nums)
        check = [0] * (length + 1)
        ans = []
        for i in nums:
            check[i] = 1
        for i in range(1, length + 1):
            if check[i] == 0:
                ans.append(i)
        return ans

'''
Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

Example 2:

Input: nums = [1,1]
Output: [2]
'''