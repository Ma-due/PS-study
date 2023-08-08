# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parents = {}

        q = deque()
        q.append(root)

        while q:
            for i in range(len(q)):
                parent = q.popleft()

                if parent.left:
                    parents[parent.left.val] = parent
                    q.append(parent.left)

                
                if parent.right:
                    parents[parent.right.val] = parent
                    q.append(parent.right)


        q.append((target, k))
        visited = set()
        visited.add(target.val)
        answer = []

        while q:
            node, count = q.popleft()
            
            if count == 0:
                answer.append(node.val)
                continue

            if node.left and node.left.val not in visited:
                visited.add(node.left.val)
                q.append((node.left, count - 1))

            if node.right and node.right.val not in visited:
                visited.add(node.right.val)
                q.append((node.right, count - 1))

            if node.val in parents and parents[node.val].val not in visited:
                visited.add(parents[node.val].val)
                q.append((parents[node.val], count - 1))

        return answer
