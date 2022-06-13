# 1572. Matrix Diagonal Sum

'''
Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

Example 1:

Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.

Example 2:

Input: mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
Output: 8

Example 3:

Input: mat = [[5]]
Output: 5

Constraints:

    n == mat.length == mat[i].length
    1 <= n <= 100
    1 <= mat[i][j] <= 100



'''

class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        # check if length of mat is odd or even
        def secondaryDiagonal_sum(mat):
            secondaryDiagonal_sum = 0
            index_row = 0
            index_col = len(mat) - 1
            for i in mat:
                secondaryDiagonal_sum +=mat[index_row][index_col]
                index_row +=1
                index_col -=1
            return secondaryDiagonal_sum
        
        def primaryDiagonal_sum(mat):
            primaryDiagonal_sum = 0
            index_primary = 0
            for i in mat:
                primaryDiagonal_sum += mat[index_primary][index_primary]
                index_primary += 1
            return primaryDiagonal_sum
        
        if len(mat)%2 == 0:
            return primaryDiagonal_sum(mat) + secondaryDiagonal_sum(mat)
        else:
            index_row = len(mat) // 2
            index_col = len(mat) // 2
            return primaryDiagonal_sum(mat) + secondaryDiagonal_sum(mat) - mat[index_row][index_col]


    def diagonalSum2(self, mat: list[list[int]]) -> int:
        diagonal_sum = 0
        for i in range(len(mat)):
            diagonal_sum += mat[i][i]
            diagonal_sum += mat[len(mat)-1-i][i]
        if len(mat)%2 == 0:
            return diagonal_sum
        else:
            return diagonal_sum - mat[len(mat)//2][len(mat)//2]



print(Solution().diagonalSum2([[1,2,3],
              [4,5,6],
              [7,8,9]]))

print(Solution().diagonalSum2([[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]))

print(Solution().diagonalSum2([[5]]))
