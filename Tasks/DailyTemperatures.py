class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        ans = [0] * len(temperatures)
        check = []
        for i in range(len(temperatures)):
            while check and check[-1][0] < temperatures[i]:
                temp, index = check.pop()
                ans[index] = i - index
            check.append((temperatures[i], i))
        return ans