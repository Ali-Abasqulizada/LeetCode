'''
Given an array of integers nums, half of the integers in nums are odd, and the other half are even.

Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.

Return any answer array that satisfies this condition.
'''

class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        ans = []
        even, odd = [], []
        for i in nums:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        i = 0
        while i < len(even):
            ans.append(even[i])
            ans.append(odd[i])
            i += 1
        return ans

#or

class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        ans = [0] * len(nums)
        even, odd = 0, 1
        for num in nums:
            if num % 2 == 0:
                ans[even] = num
                even += 2
            else:
                ans[odd] = num
                odd += 2
        return ans

'''
Example 1:

Input: nums = [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.

Example 2:

Input: nums = [2,3]
Output: [2,3]
'''