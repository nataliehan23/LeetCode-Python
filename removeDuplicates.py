# Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

# Do not allocate extra space for another array, you must do this in place with constant memory.

# For example,
# Given input array A = [1,1,2],

# Your function should return length = 2, and A is now [1,2].
class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) < 2:
            return len(A)
        left = 0
        right = 1
        while right < len(A):
            if A[right] == A[left]:
                right += 1
            else:
                left += 1
                A[left] = A[right]
                right += 1

        return left+1
            
            
        
        
        