

res = 0 
l, r = 0, len(height) -1 

while l < r:
area = (r - l) * min(height[l], height[r]) 
res = max(res, area) 






