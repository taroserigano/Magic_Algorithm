class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
         #for each start time, mapp them to next endtime using binseach
        maxProfit = 0
        jobs = sorted([(s, e, p) for s, e, p in zip(startTime, endTime, profit)])
        # print(jobs)
        minHeap = []  # (endTime, profit)
        count = 0
        # will use binary search to find the first available startTime
        # for i in range(len(startTime)):
        #     startTime[i] = jobs[i][0]
        
        for s, e, p in jobs:
            # IF starts date >= the FIRST one
            # if minHeap:
                # print("MINHEAP ", minHeap)
                # print("minheap00 " , minHeap[0][0])
            while minHeap and s >= minHeap[0][0]:
                # count+=1
                # print("COUNT" , count)
                # print("minHeap here" , minHeap)
                # print(" s " , s , " min 00 " , minHeap[0][0], " first one is" , minHeap[0])
                # print("whuaaaa", (minHeap)[0] ,"firrst" , (minHeap)[1])
                # extract only the second = profit part
                
                # if profit larger than the currentMAX, change it 
                # minHeap[1] => profit 
                maxProfit = max(maxProfit, heapq.heappop(minHeap)[1])
                # print("what is this" , maxProfit)
                # print("MINHEAP ", minHeap)
            #add ONLY end time and profit and maxprofit
            heapq.heappush(minHeap, (e, p + maxProfit))
            # print(" MUAHHHWAaaa first one is" , minHeap)
        
        # max(p for _, p in minHeap)
        # for p in minHeap:
        #     print(p)
        print(maxProfit, " " ,max(p for _, p in minHeap))
        return max(maxProfit, max(p for _, p in minHeap))
    
# 1. sort Jobs in zip 
# 2. for loop 
# 3. add first job
# 4. if start date ok, pop and compare maxProfit 
# 5. add now with maxProfit 

# 6. return  maxProfit, " " ,max(p for _, p in minHeap)
    
