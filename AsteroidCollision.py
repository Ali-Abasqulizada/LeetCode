'''
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, 
negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. 
If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.
'''

class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        ans = []
        for i in asteroids:
            if i > 0: 
                ans.append(i)
            elif len(ans) != 0 and ans[-1] > 0:
                while True:
                    if len(ans) == 0 or ans[-1] < 0:
                        ans.append(i)
                        break
                    elif ans[-1] + i == 0:
                        ans.pop()
                        break
                    elif ans[-1] > 0 and ans[-1] + i < 0:
                        ans.pop()
                    else:
                        break
            else:
                ans.append(i)
        return ans

#or

class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        ans = []
        for i in asteroids:
            while ans and ans[-1] > 0 and i < 0:
                if ans[-1] + i < 0:
                    ans.pop()
                elif ans[-1] + i > 0:
                    break
                else:
                    ans.pop()
                    break
            else:
                ans.append(i)
        return ans

'''
Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.

Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
'''