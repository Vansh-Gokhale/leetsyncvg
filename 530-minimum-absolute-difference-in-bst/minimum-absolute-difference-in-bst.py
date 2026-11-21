class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev = None
        minimum = float('inf')

        def inorder(node):
            nonlocal prev, minimum

            if not node:
                return

            inorder(node.left)

            if prev is not None:
                minimum = min(minimum, node.val - prev)

            prev = node.val
            inorder(node.right)

        inorder(root)
        return minimum