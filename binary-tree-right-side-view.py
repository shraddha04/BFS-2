# Time Complexity : O(n) - number of nodes in tree
# Space Complexity : O(n/2) for BFS- n is number of nodes in tree
#                    O(H) - for DFS
# Did this code successfully run on Leetcode : yes
# Any problem you faced while coding this : no

"""

BFS : Do level order traversal and insert the right child first in the queue
And at each level, insert the first element from the queue to the result list

DFS : Maintain level as a parameter of teh recursive function
When level == len(result), add the node.val to the result
And do recursive call on right child first and then left

When we do recursive call on right first, for each new level,
we will add the right hand side node to the result list

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#BFS Solution
from collections import deque
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        if root is None:
            return []

        queue = deque()
        queue.append(root)
        result = []

        while queue:
            size = len(queue)
            for i in range(0, size):
                node = queue.popleft()

                if i == 0:
                    result.append(node.val)

                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)

        return result

#DFS Solution
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        self.result = []
        self.helper(root, 0)
        return self.result

    def helper(self, root, level):

        if root is None:
            return

        if level == len(self.result):
            self.result.append(root.val)
        if root.right:
            self.helper(root.right, level + 1)
        if root.left:
            self.helper(root.left, level + 1)











