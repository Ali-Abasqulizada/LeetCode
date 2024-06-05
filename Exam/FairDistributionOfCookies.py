class Solution:
    def distributeCookies(self, cookies: list[int], k: int) -> int:
        ans = float("inf")
        check = [0] * k
        def find(i):
            nonlocal ans, check
            if i >= len(cookies):
                ans = min(ans, max(check))
                return
            elif ans <= max(check):
                return
            for j in range(k):
                check[j] += cookies[i]
                find(i + 1)
                check[j] -= cookies[i]
        find(0)
        return ans