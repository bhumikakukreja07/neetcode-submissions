class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [[root, 1]]
        maxDepth = 0

        while stack:
            node, depth = stack.pop()
            maxDepth = max(maxDepth, depth)

            if node.left:
                stack.append([node.left, depth + 1])
            if node.right:
                stack.append([node.right, depth + 1])
        return maxDepth