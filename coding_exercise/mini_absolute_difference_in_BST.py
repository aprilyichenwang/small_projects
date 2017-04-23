# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type node: TreeNode
        :rtype: int
        """

        queue=[root]  # initiate queue
        val_ls=[root.val]
        while queue:
            node=queue.pop(0)
            if node.left:  # if not None, or if is a node
                val_ls.append(node.left.val)
                queue.append(node.left)
            if node.right:
                val_ls.append(node.right.val)  # append to the to visit
                queue.append(node.right)
        # once exit out, meaning all nodes have been visited
        val_ls=sorted(val_ls)
        print val_ls
        min_diff=abs(val_ls[0]-val_ls[1])
        for i in range(len(val_ls)-1):
            min_diff=min(min_diff, abs(val_ls[i] - val_ls[i+1]))
        return min_diff



