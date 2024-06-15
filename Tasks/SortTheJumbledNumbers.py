class Solution:
    def sortJumbled(self, mapping: list[int], nums: list[int]) -> list[int]:
        def find(i):
            s = str(i)
            n = 0
            for j in s:
                n *= 10
                n += mapping[int(j)]
            return n
        nums.sort(key = find)
        return nums