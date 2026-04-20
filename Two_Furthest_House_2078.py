class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        i = n - 1
        while colors[0] == colors[i]:
            i -= 1
        dis1 = i
        j = 0
        while colors[n-1] == colors[j]:
            j += 1
        dis2 = (n-1) - j
        return max(dis1,dis2)



# Input: colors = [1,1,1,6,1,1,1]
# Output: 3
# Explanation: In the above image, color 1 is blue, and color 6 is red.
# The furthest two houses with different colors are house 0 and house 3.
# House 0 has color 1, and house 3 has color 6. The distance between them is abs(0 - 3) = 3.
# Note that houses 3 and 6 can also produce the optimal answer.