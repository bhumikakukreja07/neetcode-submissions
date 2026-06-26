class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        left, right = 1, 1
        def height(node):
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right))
        if not root:
            return True
        else:
            left = height(root.left)
            right = height(root.right)

            if abs(left - right) > 1:
                return False
            return self.isBalanced(root.left) and self.isBalanced(root.right) and abs(left - right) <= 1