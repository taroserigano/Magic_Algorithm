import heapq
class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = []
        self.large = []
        
    def addNum(self, num: int) -> None:
        heappush(self.small, -num)
        heappush(self.large, -heappop(self.small))
        
        if len(self.large) > len (self.small):
            heappush(self.small, -heappop(self.large))
        
    def findMedian(self) -> float:
        if len(self.small) != len(self.large):
            return -self.small[0]
        else:
            return (self.large[0]-self.small[0])/2

        
