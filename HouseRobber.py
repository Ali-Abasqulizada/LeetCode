'''
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of 
them is that adjacent houses have security systems connected and it will automatically contact the police 
if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.
'''

class Solution:
    def rob(self, nums: list[int]) -> int:
        house1, house2 = 0, 0
        for n in nums:
            house1, house2 = house2, max(n + house1, house2)
        return house2

#or

class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 0: return 0
        elif len(nums) <= 2: return max(nums)
        check = [0] * len(nums)
        check[0] = nums[0]
        check[1] = max(nums[0], nums[1])
        for n in range(2, len(nums)):
            check[n] = max(check[n - 1], check[n - 2] + nums[n])
        return check[-1]


#or

class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 0: return 0
        elif len(nums) <= 2: return max(nums)
        house1 = nums[0]
        house2 = max(nums[1], nums[0])
        for n in range(2, len(nums)):
            house1, house2 = house2, max(house2, house1 + nums[n])
        return house2

#or

from functools import cache
class Solution:
    def rob(self, nums: list[int]) -> int:
        @cache
        def find(i):
            if i >= len(nums):
                return 0
            if i == len(nums) - 1:
                return nums[i]
            return max(find(i + 2) + nums[i], find(i + 1))
        return find(0)

#or

from functools import cache
class Solution:
    def rob(self, nums: list[int]) -> int:
        @cache
        def find(i):
            if i < 0:
                return 0
            if i == 0:
                return nums[i]
            return max(find(i - 2) + nums[i], find(i - 1))
        return find(len(nums) - 1)

'''
Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
'''