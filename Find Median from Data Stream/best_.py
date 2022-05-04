import heapq
class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = []
        self.large = []
        self.size = 0
    def addNum(self, num: int) -> None:
        
        self.size += 1
        if self.size == 1:
            heapq.heappush(self.large, num)
            return
        right_min = self.large[0]
        
        if len(self.large) > len(self.small):
            if num < right_min:

                heapq.heappush(self.small, -num)
            else:
                heapq.heappush(
                    self.small, 
                    -heapq.heappushpop(self.large, num)
                )
        else:
            if num > right_min:
                heapq.heappush(self.large, num)
            else:
                heapq.heappush(
                    self.large, 
                    -heapq.heappushpop(self.small, -num)
                )
        
    def findMedian(self) -> float:
        if self.size % 2 == 0:
            return (-self.small[0]+self.large[0])/2
        else:
            return self.large[0]
