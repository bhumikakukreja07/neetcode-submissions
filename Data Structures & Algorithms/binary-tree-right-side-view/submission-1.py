class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque([root])
        ans = []
        
        while queue:
            right = None

            for i in range(len(queue)):
                node = queue.popleft()
                
                if node:
                    right = node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(right)
        return ans