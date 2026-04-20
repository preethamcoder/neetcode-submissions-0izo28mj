class Solution:
    def countBits(self, n: int) -> List[int]:
        return [bin(ind).count('1') for ind in range(n+1)]