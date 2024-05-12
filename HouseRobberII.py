'''
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. 
That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, 
and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.
'''

class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1: return nums[0]
        def find(house):
            house1, house2 = 0, 0
            for n in house:
                house1, house2 = house2, max(house2, house1 + n)
            return house2
        return max(find(nums[1:]), find(nums[:-1]))

#or

class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 0: return 0
        elif len(nums) <= 2: return max(nums)
        def find(house):
            check = [0] * len(house)
            check[0] = house[0]
            check[1] = max(house[0], house[1])
            for n in range(2, len(house)):
                check[n] = max(check[n - 1], check[n - 2] + house[n])
            return check[-1]
        return max(find(nums[1:]), find(nums[:-1]))

#or

from functools import cache
class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        @cache
        def find1(i):
            if i >= len(nums):
                return 0
            if i == len(nums) - 1:
                return nums[i]
            return max(find1(i + 2) + nums[i], find1(i + 1))
        @cache
        def find2(i):
            if i < 0:
                return 0
            elif i == 0:
                return nums[i]
            return max(find2(i - 2) + nums[i], find2(i - 1))
        return max(find1(1), find2(len(nums) - 2))

'''
Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 3:

Input: nums = [1,2,3]
Output: 3
'''