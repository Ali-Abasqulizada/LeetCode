class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        index = 0
        for i in nums:
            if i != val:
                nums[index] = i
                index += 1
        return index