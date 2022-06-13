# 566. Reshape the Matrix

'''
In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with 
a different size r x c keeping its original data.
You are given an m x n matrix mat and two integers r and c representing the number 
of rows and the number of columns of the wanted reshaped matrix.
The reshaped matrix should be filled with all the elements of the original matrix 
in the same row-traversing order as they were.
If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Example 1:

Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]

Example 2:

Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]

Constraints:

    m == mat.length
    n == mat[i].length
    1 <= m, n <= 100
    -1000 <= mat[i][j] <= 1000
    1 <= r, c <= 300


'''

class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        rows, cols =  len(mat), len(mat[0])
        first_check = r * c
        if rows*cols != first_check: return mat

        output = [[0 for _ in range(c)] for _ in range(r)]
# create a 1d array with elements from 2D in order
        oneD = []
        for i in range(rows):
            for j in range(cols):
                oneD.append(mat[i][j])
        
        count = 0
        for i in range(r):
            for j in range(c):
                output[i][j] = oneD[count]
                count +=1
        return output

    def matrixReshape2(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        rows, cols =  len(mat), len(mat[0])
        l = sum(mat,[])
        print(l)
        first_check = r * c
        if rows*cols != first_check: return mat

        output = [[0 for _ in range(c)] for _ in range(r)]
        k = 0
        for i in range(r):
            for j in range(c):
                # output[k//c][k%c] = mat[i][j]
                output[i][j] = l[k]
                k +=1
        
        return output


print(Solution().matrixReshape2([[1,2],[3,4]], 2, 4))
print(Solution().matrixReshape2([[1,2],[3,4]], 1, 4))
