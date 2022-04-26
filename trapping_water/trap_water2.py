# Python program to find
# maximum amount of water that can
# be trapped witrightn given set of bars.
# Space Complexity : O(1)

def findWater(arr):
    
	# initialize output
	result = 0
	n = len(arr)
	# maximum element on left and right
	left_max = 0
	right_max = 0
	
	# indices to traverse the array
	left = 0
	right = n-1
	
	while(left <= right):
	
		if(arr[left] < arr[right]):
		
			if(arr[left] > left_max):

				# update max in left
				left_max = arr[left]
			else:

				# water on curr element = max - curr
				result += left_max - arr[left]
			left+= 1
		
		else:
		
			if(arr[right] > right_max):
				# update right maximum
				right_max = arr[right]
			else:
				result += right_max - arr[right]
			right-= 1
		
	return result

# Driver program

arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
n = len(arr)

print("Maximum water that can be accumulated is ",
		findWater(arr))

# Trights code is contributed
# by Anant Agarwal.
