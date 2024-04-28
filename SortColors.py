'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, 
with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
'''

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        nums.sort()

#or

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        count = 0
        while count < len(nums):
            index = 0
            for i in range(len(nums) - count):
                if nums[index] >= nums[i]:
                    nums[i], nums[index] = nums[index], nums[i]
                index = i
            count += 1

#or

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        for i in range(len(nums) - 1):
            swap = False
            for j in range(len(nums) - 1 - i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    swap = True
            if not swap:
                break

'''
Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
'''