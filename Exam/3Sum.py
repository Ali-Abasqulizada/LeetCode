class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = set()
        pos, neg, zero = [], [], []
        for i in nums:
            if i > 0:
                pos.append(i)
            elif i == 0:
                zero.append(i)
            else:
                neg.append(i)
        P, N = set(pos), set(neg)
        if zero:
            for i in pos:
                if -i in N:
                    ans.add((-i, 0, i))
        if len(zero) >= 3:
            ans.add((0, 0, 0))
        for i in range(len(pos)):
            for j in range(i + 1, len(pos)):
                num = pos[i] + pos[j]
                if -num in N:
                    ans.add(tuple(sorted((-num, pos[i], pos[j]))))
        for i in range(len(neg)):
            for j in range(i + 1, len(neg)):
                num = neg[i] + neg[j]
                if -num in P:
                    ans.add(tuple(sorted((neg[i], neg[j], -num))))
        return ans

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = set()
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    ans.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
        return ans