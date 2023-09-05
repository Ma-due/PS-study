import heapq

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        
        h = []

        for p in people:
            heapq.heappush(h, (-p[0], p[1]))

        answer = []
        while h:
            p = heapq.heappop(h)
            answer.insert(p[1], (-p[0], p[1]))

        return answer
