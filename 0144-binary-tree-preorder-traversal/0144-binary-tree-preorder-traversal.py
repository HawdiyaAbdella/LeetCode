class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def pre(node):
            if not node:
                return
            res.append(node.val)
            pre(node.left)
            pre(node.right)
        pre(root)
        return res