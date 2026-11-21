class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        from collections import Counter

        count = Counter()

        def dfs(node):
            if not node:
                return
            count[node.val] += 1
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        maximum = max(count.values(), default=0)

        return [num for num, freq in count.items() if freq == maximum]