class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
            
    # BFS 
    # Time : O(W^2 * N)
    # Space: O(W * N)
        
        visited = set()
        findWords = set(wordList)
        queue = deque()
        
        # initial setup 
        queue.append((beginWord, 1))
        print(queue)
        visited.add(beginWord)
        
        while queue: # N
            
            
            word, count = queue.popleft()
            
            # if endWord found, the end
            if word == endWord:
                return count
              
            # Shuffle every letter
            for i in range(len(word)): 
                
                for char in ascii_lowercase:
                    
                    # loop through all possible words
                    newWord = word[:i] + char + word[i + 1:] 
                    
                    if newWord in visited or newWord not in findWords:
                        continue
                    
                    # FOUND, next round will start
                    visited.add(newWord)
                    queue.append((newWord, count + 1))
                    
        return 0
