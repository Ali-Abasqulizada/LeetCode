'''
In English, we have a concept called root, which can be followed by some other word to form another longer word - 
let's call this word derivative. For example, when the root "help" is followed by the word "ful", we can form a derivative "helpful".

Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, 
replace all the derivatives in the sentence with the root forming it. If a derivative can be replaced by more than one root, 
replace it with the root that has the shortest length.

Return the sentence after the replacement.
'''

class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        ans = ""
        check1 = [[] * i for i in range(26)]
        for i in range(len(dictionary)):
            check1[ord(dictionary[i][0]) - ord("a")].append(dictionary[i])
        sentence = sentence.split(" ")
        for i in range(len(sentence)):
            if len(check1[ord(sentence[i][0]) - ord("a")]) == 0:
                ans += sentence[i] + " "
            else:
                check = check1[ord(sentence[i][0]) - ord("a")]
                if len(check) == 1:
                    if sentence[i].startswith(check[0]):
                        ans += check[0] + " "
                    else:
                        ans += sentence[i] + " "
                else:
                    word = ""
                    for a in check:
                        if word == "":
                            if sentence[i].startswith(a):
                                word = a
                        elif sentence[i].startswith(a) and len(a) < len(word):
                            word = a
                    if word != "":
                        ans += word + " "
                    else:
                        ans += sentence[i] + " "
        return ans[:-1]

'''
Example 1:

Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"

Example 2:

Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
Output: "a a b c"
'''