'''
Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. 
It is guaranteed there is at least one word that is not banned, and that the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in lowercase.
'''

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        check = {}
        for i in "!?',;.":
            paragraph = paragraph.replace(i, " ")
        paragraph = paragraph.lower().split()
        for i in paragraph:
            if i not in banned:
                if i in check:
                    check[i] += 1
                else:
                    check[i] = 1
        ans = ""
        count = 0
        for i in check:
            if count < check[i]:
                count = check[i]
                ans = i
        return ans

'''
Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.

Example 2:

Input: paragraph = "a.", banned = []
Output: "a"
'''