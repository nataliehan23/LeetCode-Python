class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        if x<=0:
            return 0
        if x==1:
            return 1
        left = 0
        right = x
        
        while right-left >1:
            mid = left + (right-left)//2
            if mid*mid <=x:
                left = mid
            else:
                right = mid
        return left
           