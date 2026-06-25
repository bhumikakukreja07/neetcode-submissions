class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxD = 0

        def height(node):
            if not node:
                return 0
            left = height(node.left)
            right = height(node.right)
            d = left + right

            nonlocal maxD
            maxD = max(maxD, d)
            return 1 + max(left, right)
        height(root)
        return maxD