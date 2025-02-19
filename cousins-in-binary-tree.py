# Time Complexity : O(n) - number of nodes in tree
# Space Complexity : O(n/2) for BFS- n is number of nodes in tree
#                    O(H) - for DFS
# Did this code successfully run on Leetcode : yes
# Any problem you faced while coding this : no

"""

BFS : Do level order traversal, and for each node of each level,
after popping check if it's children(left and right) are x and y, then return False there itself.
As x and y would have the same parent

If not, check if we find x and y both in the same level, if yes - return True else return False


DFS : For each node, check if it's children(left and right) are x and y, then return False there itself.

If not, record the x_level and y_level whenever you find x and y
And then recursively call on left and right with level = level + 1

At the end if x_level == y_level, then return True else return False

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS
from collections import deque
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: Optional[TreeNode]
        :type x: int
        :type y: int
        :rtype: bool
        """

        queue = deque()
        queue.append(root)

        while queue:
            size = len(queue)
            x_found = False
            y_found = False
            for i in range(0 ,size):
                node = queue.popleft()
                if node.left and node.right:
                    if node.left.val == x and node.right.val == y:
                        return False
                    if node.left.val == y and node.right.val == x:
                        return False
                if node.val == x:
                    x_found = True
                if node.val == y:
                    y_found = True

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if x_found and y_found:
                return True
            if x_found or y_found:
                return False
        return False

# DFS
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: Optional[TreeNode]
        :type x: int
        :type y: int
        :rtype: bool
        """

        self.x_level = 0
        self.y_level = 0
        self.flag = True
        self.helper(root, 0, x, y)
        if not self.flag: return False
        return self.x_level == self.y_level

    def helper(self, root, level, x, y):

        if root is None:
            return

        if root.left and root.right:
            if (root.left.val == x and root.right.val == y) or (root.left.val == y and root.right.val == x):
                self.flag = False
                return

        if root.val == x:
            self.x_level = level

        if root.val == y:
            self.y_level = level

        if self.flag:
            self.helper(root.left, level +1, x ,y)
        if self.flag:
            self.helper(root.right, level +1 ,x ,y)






