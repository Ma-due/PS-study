class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def union(a, b):
            a = find(a)
            b = find(b)

            if a != b:
                parent[b] = a
                return False
            else:
                return True

        def find(x):
            if parent[x] != x:
                return find(parent[x])
            
            return x

        parent = [x for x in range(len(edges) + 1)]

        for a, b in edges:
            if union(a, b):
                return [a, b]
