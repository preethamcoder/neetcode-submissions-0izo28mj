class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        rows = len(word1)
        cols = len(word2)
        matrix = [[0]*(cols+1) for _ in range(rows+1)]
        matrix[0] = [ind for ind in range(cols+1)]
        for ind in range(rows+1):
            matrix[ind][0] = ind
        for x in range(1, rows+1):
            for y in range(1, cols+1):
                if word1[x-1] != word2[y-1]:
                    matrix[x][y] = 1 + min(matrix[x-1][y-1], matrix[x][y-1], matrix[x-1][y])
                else:
                    matrix[x][y] = matrix[x-1][y-1]
        return matrix[-1][-1]