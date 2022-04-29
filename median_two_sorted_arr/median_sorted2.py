# Python 3 code for finding median
# of the given two sorted arrays that
# exists in the merged array
# ((n+m) / 2 - 1 position)

# Function to find median of given
# two sorted arrays
def findMedianSortedArrays(a, n, b, m):
	
	min_index = 0
	max_index = n
	
	while (min_index <= max_index):
		
		i = (min_index + max_index) // 2
		j = ((n + m + 1) // 2) - i
		
		print(i)
		print(j)
		print("hey")
	
		# if i = n, it means that Elements
		# from a[] in the second half is
		# an empty set. If j = 0, it means
		# that Elements from b[] in the first
		# half is an empty set. so it is necessary
		# to check that, because we compare elements
		# from these two groups. searching on right
		if (i < n and j > 0 and a[i] < b[j-1]):	
			min_index = i + 1
		
		# if i = 0, it means that Elements from
		# a[] in the first half is an empty set
		# and if j = m, it means that Elements
		# from b[] in the second half is an
		# a[] in the first half is an empty set
		# that, because we compare elements from
		# these two groups. searching on left
		elif (j < m and i > 0 and a[i - 1] > b[j]):	
			max_index = i - 1
		
		# we have found the desired halves.
		else:
			
			# this condition happens when we don't have
			# any elements in the first half from a[] so
			# we returning the last element in b[] from
			# the first half.
			if (i == 0):
				return b[j - 1]		
			
			# and this condition happens when we don't
			# have any elements in the first half from
			# b[] so we returning the last element in
			# a[] from the first half.
			if (j == 0):
				return a[i - 1]		
			else:
				return max(a[i - 1], b[j - 1])
	
	print("ERROR!!! " , "returning\n")
	return 0

 

# Driver code
if __name__ == "__main__":
	b = [1,2,3,4,5]
	a = [0,1,2,3,4]
	n = len(a)
	m = len(b)
	
	# we need to define the smaller array
	# as the first parameter to make sure
	# that the time complexity will be
	# O(log(min(n,m)))
	if (n < m):
		print( "The median is: ",
				findMedianSortedArrays(a, n, b, m))
	else:
		print( "The median is: ",
				findMedianSortedArrays(b, m, a, n))

# This code is contributed
# by ChitraNayal
