

res = 0 
l, r = 0, len(height) -1 

while l < r:
# area = width * minimum Height  
  area = (r - l) * min(height[l], height[r])
# update result   
  res = max(res, area) 
  
# Move   
  if height[l] < height[r]: 
    l += 1 
  else: 
    r -=1 
    
return res 









# 8, 2, 3, 4, 6, 8, 7 

# min height would be 7 for maximum area 







