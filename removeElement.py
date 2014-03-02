# Given an array and a value, remove all instances of that value in place and return the new length.

# The order of elements can be changed. It doesn't matter what you leave beyond the new length.

class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        if len(A) == 1:
            if A[0] == elem:
                return 0
            else:
                return 1
        start = 0
        last = len(A)-1
        result = 0
        while start <= last:
            if A[start] == elem:
                if A[last] == elem:
                    last -= 1
                else:
                    A[start] = A[last]
                    last -= 1
                    start += 1
            else:
                start += 1
        return start
                
        
        
        