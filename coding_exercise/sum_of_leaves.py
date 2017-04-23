# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Note, this questions asks for the leaf only
        # always go the left node if possible, if not, go to the right node
        # append val into a list, after verifying that it is a leaf
        # sum(list)
        queue=[root]
        val_ls=[]
        while queue:
            node=queue.pop()
            if node.left:
                queue.append(node.left)
                if not node.left.left and not node.left.right: # verify a leaf
                    val_ls.append(node.val)
            # need to visit right anyway (keep walking)
            if node.right:
                queue.append(node.right)  # next root to go
        return sum(val_ls)


x=Solution()
print x.sumOfLeftLeaves([1,2,3,4,5])
