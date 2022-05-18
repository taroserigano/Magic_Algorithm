# 5
# [[0,1],[0,2],[1,3],[1,4],[3,4]]

# {0: [], 1: [], 2: [], 3: [], 4: []}
# {0: [1, 2], 1: [3, 4], 2: [], 3: [4], 4: []}
# crs 0    pre 1
# crs 1    pre 3
# crs 3    pre 4
# crs 1    pre 4
# crs 0    pre 2

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preMap = { i: [] for i in range(numCourses)}
        print(preMap)
        
        for crs, pre in prerequisites: 
            preMap[crs].append(pre)
        print(preMap)
        
        visitSet = set()
        
        # for pre in preMap[crs]:  ==> pre courses in 0: [1, 2]
        # 0: 1,2 then the pre 1 will dfs, in there, 1 will have pres: [3, 4] so 3 will dfs(crs = 3) again
        # then 3: [4], then dfs(4) then the 4: [] ,
        # empty is passed because   if preMap[crs] == []: # [] empty means it's passed
        #         return True 
        # repeat for every courses like this 
        
        def dfs(crs): 
            if crs in visitSet: # this automatically means Impossible
                return False 
            if preMap[crs] == []: # [] empty means it's passed
                return True 
            
            visitSet.add(crs)
            
            for pre in preMap[crs]:  # ex. preMap[0]: [1, 2] 
                                     #            crs : pre requisite courses * 2
                                     # so it'll run twice for 1 and 2 
                print("crs", crs, " " , " pre", pre, "visit" , visitSet)

                if not dfs(pre): # means, this course cannot be completed 
                    return False 
                
            visitSet.remove(crs) 
            preMap[crs]= [] # check as Done
            return True 
        
        for crs in range(numCourses):
            if not dfs(crs): return False 
        return True     
                
                
        
        
        
        
        
        
        
        
