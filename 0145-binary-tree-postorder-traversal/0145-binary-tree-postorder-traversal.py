class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result=[]
        stack=[]
        while root or stack:
            while root:
                stack.append(root) 
                root=root.left if root.left else root.right
            root=stack.pop()
            result.append(root.val) 
            if stack and stack[len(stack)-1].left==root: 
                root=stack[len(stack)-1].right
            else:
                root=None 
        return(result)