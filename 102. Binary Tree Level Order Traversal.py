# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:return root
        res = [[root.val]]
        queue = collections.deque()
        queue.append(root)
        while queue:
            queue_length = len(queue)
            path = []
            for i in range(queue_length):
                curr_node = queue.popleft()
                if curr_node.left:
                    queue.append(curr_node.left)
                    path.append(curr_node.left.val)
                if curr_node.right:
                    queue.append(curr_node.right)
                    path.append(curr_node.right.val)
            if path!=[]:
                res.append(path)
        return res

            
            
            
        
