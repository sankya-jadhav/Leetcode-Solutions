class Solution:
    def mirrorDistance(self, n: int) -> int:
        res = abs(int(str(n)[::-1]))
        return abs(n - res)