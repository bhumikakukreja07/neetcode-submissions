class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node):
            if not node:
                return []
            return [node.val] + dfs(node.left) + dfs(node.right)
        ans = dfs(root)
        ans.sort()
        return ans[k - 1]