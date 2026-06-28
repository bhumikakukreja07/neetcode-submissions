class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isBST(node, minn, maxx):
            if not node:
                return True # imp
            if node.val <= minn or node.val >= maxx:
                return False
            return isBST(node.left, minn, node.val) and isBST(node.right, node.val, maxx)
        return isBST(root, float('-inf'), float('inf'))