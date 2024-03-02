'''
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.
'''

class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        count = 0
        check = [0] * 26
        for i in chars:
            check[ord(i) - ord("a")] += 1
        for i in words:
            good = True
            copy = check[::]
            for j in i:
                if copy[ord(j) - ord("a")] == 0:
                    good = False
                    break
                copy[ord(j) - ord("a")] -= 1
            if good:
                count += len(i)
        return count
    
'''
Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
'''