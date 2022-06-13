#2011. Final Value of Variable After Performing Operations
'''
There is a programming language with only four operations and one variable X:

    ++X and X++ increments the value of the variable X by 1.
    --X and X-- decrements the value of the variable X by 1.

Initially, the value of X is 0.

Given an array of strings operations containing a list of operations, 
return the final value of X after performing all the operations.
'''

# def finalValueAfterOperations(operations) -> int:
#     X = 0
#     for i in operations:
#         if i =="++X" or i == "X++":
#             X = X + 1
#         if i =="--X" or i == "X--":
#             X = X - 1
#     return X


# # operations = ["--X","X++","X++"]
# # operations = ["++X","++X","X++"]
# operations = ["X++","++X","--X","X--"]

# print("Final value of X: ", finalValueAfterOperations(operations))

# from typing import *

class Solution:
    def finalValueAfterOperations(self, operations:list[str]) -> int:
        X = 0
        for i in operations:
            if i =="++X" or i == "X++":
                X = X + 1
            if i =="--X" or i == "X--":
                X = X - 1
        return X

# this creates an instance of the Solution class
# function_call = Solution()
operations = ["--X","X++","X++"]
print(Solution().finalValueAfterOperations(operations))