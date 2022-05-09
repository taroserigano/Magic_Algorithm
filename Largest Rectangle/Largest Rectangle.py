# 1. Stack. If current higher, add and i++. If less, pop and start comparing and maxArea till empty. 

class Solution:
    def largestRectanglemaxArea(self, height: List[int]) -> int:
        stack, maxArea, i = [], 0, 0
        while i <= len(height):
			# if current HIGHER than Last 
			# add current to stack 
            if not stack or (i < len(height) and height[i] > height[stack[-1]]):
            
                stack.append(i)
                i += 1
            else:
				# create Last by popping 
                last = stack.pop()
                if not stack:
                    maxArea = max(maxArea, height[last] * i)
                #           | 3 | 
                #   | 2 | 2 | 2 |
                # 1 | 1 | 1 | 1 |  <= kind of thing 
                else:
                  # first round at 6, 
                  # stack[-1] = stack index is = 2 as stack is [1, 2] # before pop, it was: [1, 2, 3] 
                  # 6 (height[last] = height array[index] )  * (i = 4 - stack[-1] = 2 - 1) = 6 * (4 - 2 - 1) = 6 (maxArea created now)
                  # next round is 5 * 2 = 10 
                    maxArea = max(maxArea, height[last] * (i - stack[-1] - 1 ))
		
		  # i = 4, 
		#           | 3 | 
                #   | 2 | 2 | 2 |
                # 1 | 1 | 1 | 1 |
		#
		# 1 , 2 , 3 , 4 = i 
		# it is made sure that the stack is built by LARGER stack, 
		# so it can count Height * width being ensured
		
        return maxArea
		
		
		
[2,1,5,6,2,3]		
		
  
  
  
  
  
  
  
  
