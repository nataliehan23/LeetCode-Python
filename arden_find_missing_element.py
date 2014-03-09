# There is an array of non-negative integers. 
# A second array is formed by shuffling the elements of the first array and deleting a random element. 
# Given these two arrays, find which element is missing in the second array. 

def findMissing(arr1, arr2):
	val = 0
	for num in arr1+arr2:
		val ^= num
	return val
arr1  = [1,2,4,5]
arr2 = [5,4,1]
print findMissing(arr1, arr2)

