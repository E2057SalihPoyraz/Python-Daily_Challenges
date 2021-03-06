# QUESTION: Level of Interview Question = Easy
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# Example 1:
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

# çözüm:1
from math import factorial
def climbStairs(n):
    count=0
    for i in range(n,1,-2):
        count += factorial(i+(n-i)//2) / factorial(i) / factorial((n-i)//2)
    return int(count)    

#çözüm : 2
class Solution:
    def climbStairs(self, n: int) -> int:
        lst = [1,2]
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 3
        else:
            for i in range(2,n):
                lst.append(lst[-1]+lst[-2])
            return lst[-1]