import heapq

class MedianFinder(object):

    def __init__(self):
        """
        2개의 heap을 유지 maxheap, minheap
        숫자의 절반은 큰 순으로 maxheap에 저장,
        절반은 작은 순으로 minheap에 저장

        median은 maxheap에서 가장 작은 값과 minheap에서 가장 큰 값
        """
        self.maxheap = []
        self.minheap = []
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """

        # maxheap에 추가
        heapq.heappush(self.maxheap, -num)
        # maxheap에서 가장 작은 값을 minheap으로 이동
        heapq.heappush(self.minheap, -self.maxheap[0])
        
        # maxheap의 개수 유지
        heapq.heappop(self.maxheap)

        # minheap은 maxheap의 개수 이하로 유지
        if len(self.maxheap) < len(self.minheap):
            heapq.heappush(self.maxheap, -self.minheap[0])
            heapq.heappop(self.minheap)

    def findMedian(self):
        """
        :rtype: float
        """

        """
        len(maxheap) = len(minheap)
        median = maxheap에서 가장 작은 값 + minheap 가장 큰 값

        len(maxheap) > len(minheap) 홀수 
        median = maxheap에서 가장 작은 값
        """
        
        if len(self.maxheap) > len(self.minheap):
            return -self.maxheap[0]
        else:
            return (self.minheap[0] - self.maxheap[0]) / 2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
