class Solution:
    def findMinDifference(self, timePoints: list[str]) -> int:
        check = []
        for time in timePoints:
            time = time.split(":")
            h, m = int(time[0]), int(time[1])
            check.append(h * 60 + m)
        check.sort()
        ans = 1440 + check[0] - check[-1]
        for t in range(1, len(check)):
            ans = min(ans, check[t] - check[t - 1])
        return ans