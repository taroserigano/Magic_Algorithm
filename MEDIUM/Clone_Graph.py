class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        map = {} 
        
        def dfs(node):
            if node in map:
                # print(map[node])
                return map[node]
            
            copy = Node(node.val) 
            # print(node.val, " " , node.neighbors)
            map[node] = copy   # 1:[ , ]
            
            for nei in node.neighbors: # usually the node has TWO neighbors [2, 4] 
                print(nei.val)
                # add to the copy 
                copy.neighbors.append(dfs(nei))
                # case 1. if node already in map, return this NODE
                # case 2. "for nei in node.neighbors:" releae two neighbors of this NODE, and add to the copy
                
            return copy 
        
        return dfs(node) if node else None  

# seenMap:
#
#     1: [2,4] --->   2: [3,1]
#        ^               ^
#        |               |
#        v               v
#     4: [1,3] --->   3: [2,4]

        
        
