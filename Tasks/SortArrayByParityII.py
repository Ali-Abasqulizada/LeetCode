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