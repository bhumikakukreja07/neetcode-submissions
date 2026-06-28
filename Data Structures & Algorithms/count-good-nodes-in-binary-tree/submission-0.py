class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        queue = deque()
        queue.append((root, -float('inf')))

        while queue:
            node, maxVal = queue.popleft()

            if node.val >= maxVal:
                ans += 1
            if node.left:
                queue.append((node.left, max(maxVal, node.val))) # imp
            if node.right:
                queue.append((node.right, max(maxVal, node.val))) # imp
        return ans