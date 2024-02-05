from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        # List to store the inorder traversal
        res = []

        # Helper function to perform recursion
        def traverse(node):
            if not node:
                return
            # Inorder traversal: left, root, right
            traverse(node.left)  # Visit left child
            res.append(node.val)  # Visit node itself
            traverse(node.right)  # Visit right child

        # Start the recursion from the root
        traverse(root)
        return res


root = [1,None,2,3]
sol = Solution()
res = sol.inorderTraversal(root)
print(res)