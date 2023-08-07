class Solution:
    def isSafe(self, s, graph, visited, safeNode):
        if visited[s] == 1:
            return True
        
        if visited[s] == -1:
            return False

        visited[s] = -1
        for it in graph[s]:
            if not self.isSafe(it, graph, visited, safeNode):
                return False

        visited[s] = 1
        return True

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        v = len(graph)

        visited = [0] * v

        safeNode = []

        for i in range(v):
            if self.isSafe(i, graph, visited, safeNode):
                safeNode.append(i)

        return safeNode
