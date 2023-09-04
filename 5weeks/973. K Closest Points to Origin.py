import heapq

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        h = []
        for x, y in points:
            dist = -(x * x + y * y)
            
            if len(h) == k:
                heapq.heappushpop(h, (dist, x, y))
            else:
                heapq.heappush(h, (dist, x, y))

        return [(x, y) for (dist, x, y) in h]
