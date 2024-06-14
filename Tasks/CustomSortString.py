class Solution:
    def customSortString(self, order: str, s: str) -> str:
        check = [0] * 26
        ans = ""
        for i in s:
            check[ord(i) - ord('a')] += 1
        for i in order:
            ans += i * check[ord(i) - ord('a')]
            check[ord(i) - ord('a')] = 0
        for i in range(len(check)):
            if check[i]:
                ans += chr(ord('a') + i) * check[i]
        return ans