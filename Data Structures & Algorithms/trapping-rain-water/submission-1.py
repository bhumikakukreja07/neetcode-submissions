class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft, maxRight = 0, 0
        left, right = [], []

        for i in range(len(height)):
            if height[i] > maxLeft:
                maxLeft = height[i]
            left.append(maxLeft)
        for j in range(len(height)-1, -1, -1):
            if height[j] > maxRight:
                maxRight = height[j]
            right.append(maxRight)
        right.reverse()
        sum = 0
        for h in range(len(height)):
            x = min(left[h], right[h])
            sum += max(0, x - height[h])
        return sum