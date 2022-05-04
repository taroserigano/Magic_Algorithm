class MedianFinder:
    def __init__(self):
        self.array = []
 
    def addNum(self, num: int) -> None:
        self.array.append(num)
 
    def findMedian(self) -> float:
        self.array.sort()
        n = len(self.array)
        if not self.array or n == 1:
            return 0 or self.array[0]
        elif n & 1:
            return self.array[n // 2]
        else:
            return (self.array[n // 2] + self.array[(n // 2) - 1]) / 2
