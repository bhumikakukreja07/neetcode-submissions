class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft, maxRight, n = 0, 0, len(height)
        left, right = [0] * n, [0] * n

        for i in range(n):
            j = -i - 1
            left[i] = maxLeft
            right[j] = maxRight
            maxLeft = max(maxLeft, height[i])
            maxRight = max(maxRight, height[j])
        sum = 0

        for h in range(len(height)):
            x = min(left[h], right[h])
            sum += max(0, x - height[h])
        return sum