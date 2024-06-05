'''
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). 
You may return the answer in any order.
'''

class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        ans = []
        for i in range(1, len(words)):
            words[i] = list(words[i])
        for i in words[0]:
            seen = 0
            for j in range(1, len(words)):
                for k in range(len(words[j])):
                    if i == words[j][k]:
                        words[j][k] = '!'
                        seen += 1
                        break
            if seen == len(words) - 1:
                ans.append(i)
        return ans

'''
Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]

Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]
'''