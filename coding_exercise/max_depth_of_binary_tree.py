# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        leng=0
        m_ls=[]
        node=root
        while True:
            if node.left or node.right is not None:
                leng+=1
                node=node.left*(node.left==None) + node.right*(node.right==None)
            else:
                m_ls.append(leng)
                node=root
        return max(m_ls)

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxDepth(self, root):
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


