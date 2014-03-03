# Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?

# For example,
# Given sorted array A = [1,1,1,2,2,3],

# Your function should return length = 5, and A is now [1,1,2,2,3].


class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) < 3:
            return len(A)
        left = 0
        right = 1
        dup = False
        while right < len(A):
            if A[left] == A[right] and not dup:
                dup = True
                left += 1
                A[left] = A[right]
                right += 1
            elif A[left] != A[right]:
            	left += 1
            	A[left] = A[right]
            	right += 1
            	dup = False
            elif A[left]==A[right] and dup:
            	right += 1
            	continue
               
        return left+1
        
s = Solution()
A = [1,1,1,2]
print A
res = s.removeDuplicates(A)   
print res
print A
print A[:res]         
        
        