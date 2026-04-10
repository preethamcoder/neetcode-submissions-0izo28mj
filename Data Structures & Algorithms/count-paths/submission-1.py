class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1]*n
        for ind in range(m-1):
            newRow = [1]*n
            for ind2 in range(n-2, -1, -1):
                newRow[ind2] = newRow[ind2+1] + row[ind2]
            row = newRow
        return row[0]