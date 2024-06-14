class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        ans = []
        diff = float("inf")
        arr.sort()
        for i in range(1, len(arr)):
            check = arr[i] - arr[i - 1]
            if check < diff:
                diff = check
                ans = [[arr[i - 1], arr[i]]]
            elif check == diff:
                ans.append([arr[i - 1], arr[i]])
        return ans