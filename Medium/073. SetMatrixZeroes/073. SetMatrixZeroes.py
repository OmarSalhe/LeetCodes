from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        x = [False] * len(matrix)
        y = [False] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    x[i] = True
                    y[j] = True
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if x[i] or y[j]:
                    matrix[i][j] = 0