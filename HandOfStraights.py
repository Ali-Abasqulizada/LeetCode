'''
Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, 
and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, 
return true if she can rearrange the cards, or false otherwise.
'''

class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hand.sort()
        count = len(hand) // groupSize
        card = 0
        while count > 0:
            count -= 1
            check = []
            for i in range(len(hand)):
                if len(check) == groupSize:
                    break
                elif hand[i] == "!":
                    continue
                elif len(check) == 0:
                    check.append(hand[i])
                    hand[i] = "!"
                elif check[-1] + 1 == hand[i]:
                    check.append(hand[i])
                    hand[i] = "!"
            if len(check) == groupSize:
                card += 1
        return True if card * groupSize == len(hand) else False

'''
Example 1:

Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]

Example 2:

Input: hand = [1,2,3,4,5], groupSize = 4
Output: false
Explanation: Alice's hand can not be rearranged into groups of 4.
'''