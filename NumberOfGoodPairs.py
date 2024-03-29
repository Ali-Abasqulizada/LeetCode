'''
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.
'''

class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    count += 1
        return count

#or

class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        check = {}
        count = 0
        for i in nums:
            if i in check:
                count += check[i]
                check[i] += 1
            else:
                check[i] = 1
        return count

'''
Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.

Example 3:

Input: nums = [1,2,3]
Output: 0
'''