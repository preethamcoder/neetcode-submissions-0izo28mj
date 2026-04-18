class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows = len(text1)
        cols = len(text2)
        matrix = [[0]*(cols+1) for _ in range(rows+1)]
        for x in range(1, rows+1):
            for y in range(1, cols+1):
                if text1[x-1] == text2[y-1]:
                    matrix[x][y] = 1 + matrix[x-1][y-1]
                else:
                    matrix[x][y] = max(matrix[x-1][y], matrix[x][y-1])
        return matrix[-1][-1]