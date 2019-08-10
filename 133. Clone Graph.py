"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node == None:return None
        visited = [node]
        queue = collections.deque()
        queue.append(node)
        node_dic = dict()
        node_dic[node] = Node(node.val,[])
        while queue:
            curr_node = queue.popleft()
            for neighbor in curr_node.neighbors :
                if neighbor not in visited:
                    copy_node = Node(neighbor.val,[])
                    node_dic[neighbor] = copy_node
                    visited.append(neighbor)
                    queue.append(neighbor)
        for dic_key_node in node_dic:
            for neighbor in dic_key_node.neighbors:
                node_dic[dic_key_node].neighbors.append(node_dic[neighbor])
                
        return node_dic[node]
