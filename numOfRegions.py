## given a two Dimension array, find number of connected regions based on 4-coonectivity neighborhood. 
## This is not from LeetCode, but based on a recent phone interview
import numpy as np

def numOfRegions(arr):
	visited = set()
	num = 0
	(row, col)  = arr.shape
	for i in range(row):
		for j in range(col):
			if arr[i,j] == 1 and (i,j) not in visited:
				visited.add((i,j))
				neighbors = []
				if i-1>=0:
					neighbors.append([i-1,j])
				if i+1<col:
					neighbors.append([i+1,j])
				if j-1>=0:
					neighbors.append([i, j-1])
				if j+1<row:
					neighbors.append([i, j+1]) 
				Flag = False
				for n in neighbors:
					if arr[n[0], n[1]] == 1:
						Flag = False
						if (n[0],n[1]) in visited:
							visited.add((i,j))
							break
						else:
							Flag = True
							visited.add((n[0],n[1]))
					else:
						Flag = True
				if Flag:
					num +=1

	return num

## Test case in numpy array
a = np.zeros((4,4))
a[0,0] = 1
a[0,1] = 1
a[0,2] = 1
a[2,2] = 1
a[2,3] = 1
a[3,0] = 1
(row, col) = a.shape
# print row, col
print "The test matrix is: "
print a
print "Connected region number is: "
print numOfRegions(a)





