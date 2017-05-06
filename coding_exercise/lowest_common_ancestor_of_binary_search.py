# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # build a dictionary; for each node, register its child
        #{6: {2,8}), 2:{0,4}, ..}
        queue=[root]
        dic={}
        while queue:
            node=queue.pop()
            dic[node.val]=[]
            if node.left:
                dic[node.val].append(node.left.val)
                queue.append(node.left)
            if node.right:
                dic[node.val].append(node.right.val)
                queue.append(node.right)
        dic={key:set(val) for key, val in dic.items()}
        if set([p, q]) in dic.values():
            return dic.keys()[dic.values().index(set([p, q]))]
        elif p in dic and q in dic[p]:
            return p
        elif q in dic and p in dic[q]:
            return q
