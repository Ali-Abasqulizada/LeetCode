'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
'''

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        check = {}
        ans = []
        for i in nums:
            check[i] = check.get(i, 0) + 1
        while k > 0:
            k -= 1
            maxim = 0
            ele = 0
            for i in check:
                if check[i] == "!":
                    continue
                elif maxim < check[i]:
                    maxim = check[i]
                    ele = i
            ans.append(ele)
            check[ele] = "!"
        return ans

'''
Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]
'''