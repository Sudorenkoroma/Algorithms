from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []  # To store the postorder traversal values

        def preorder(node):
            if node:
                if node is not None:
                    # Обробка поточного вузла перед рекурсивним обходом лівого і правого піддерев
                    result.append(node.val)
                    preorder(node.left)
                    preorder(node.right)

        preorder(root)

        return result


root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

res = Solution()
sol = res.preorderTraversal(root)
print(sol)