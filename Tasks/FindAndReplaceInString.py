class Solution:
    def findReplaceString(self, s: str, indices: list[int], sources: list[str], targets: list[str]) -> str:
        i = 0
        ans = ""
        check = {}
        for j in range(len(indices)):
            if indices[j] in check:
                check[indices[j]].append([sources[j], targets[j]])
            else:
                check[indices[j]] = [[sources[j], targets[j]]]
        while i < len(s):
            if i not in check:
                ans += s[i]
                i += 1
            elif len(check[i]) == 1:
                k = len(check[i][0][0])
                if s[i : i + k] == check[i][0][0]:
                    ans += check[i][0][1]  
                    i += k
                else:
                    ans += s[i]
                    i += 1
            else:
                seen = False
                for sor, tar in check[i]:
                    if s[i : i + len(sor)] == sor:
                        ans += tar
                        i += len(sor)
                        seen = True
                        break
                if not seen:
                    ans += s[i]
                    i += 1
        return ans