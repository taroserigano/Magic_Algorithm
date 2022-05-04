from heapq import heappush, heappop, heappushpop
# log n 
class MedianFinder:
    def __init__(self):
        ''' initialize your structure '''
        # two heaps, large, small, minHeap, maxHeap
        # in order to divide to two groups
        # small: [1,2,3] - Large = [4,5,6]
        
        self.small, self.large = [], [] 
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)
        # to make it maxHeap 
        # the less, the greater this way as MAX value
        
        if (self.small and self.large and 
            # the smallest value => the largest 
            # reverse it back
            # if it's less than the smallest of Large array
            # '''make sure every num small is <= every num in large'''
            ( -1 * self.small[0]) > self.large[0]): 
            # restore to the original state and add it to Large 
            val = -1 * heapq.heappop(self.small) 
            heapq.heappush(self.large, val) 
            
        # if either size is larger? 
        if len(self.small) > len(self.large) + 1:
            # reverse it back to original 
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val) 
        if len(self.large) > len(self.small) + 1: 
            val = heapq.heappop(self.large) 
            # because small needs to be MaxHeap
            heapq.heappush(self.small, -1 * val) 
 
    def findMedian(self) -> float:
        # if sizes are not same, return either one
        if len(self.small) > len(self.large): 
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        #if size same, add together and divide
        return ( -1 * self.small[0] + self.large[0]) / 2 
        
            

            # OPTIMIZED:
            
            from heapq import heappush, heappop, heappushpop
# log n 
class MedianFinder:
    def __init__(self):
        ''' initialize your structure '''
        # two heaps, large, small, minHeap, maxHeap
        # in order to divide to two groups
        # small: [1,2,3] - Large = [4,5,6]
        
        self.small, self.large = [], [] 
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)
        # to make it maxHeap 
        # the less, the greater this way as MAX value
        
        if (self.small and self.large and 
            # the smallest value => the largest 
            # reverse it back
            # if it's less than the smallest of Large array
            # '''make sure every num small is <= every num in large'''
            ( -1 * self.small[0]) > self.large[0]): 
            # restore to the original state and add it to Large 
            val = -heapq.heappop(self.small) 
            heapq.heappush(self.large, val) 
            
        # if either size is larger? 
        if len(self.small) > len(self.large) + 1:
            # reverse it back to original 
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val) 
        if len(self.large) > len(self.small) + 1: 
            val = heapq.heappop(self.large) 
            # because small needs to be MaxHeap
            heapq.heappush(self.small, -val) 
 
    def findMedian(self) -> float:
        # if sizes are not same, return either one
        if len(self.small) > len(self.large): 
            return -self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        #if size same, add together and divide
        return ( -self.small[0] + self.large[0]) / 2 
        
            
            
