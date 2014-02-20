class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        xstr = str(x)
        i = 0
        j = len(xstr) -1
        while i<=j:
            if xstr[i] !=xstr[j]:
                return False
            i += 1
            j -= 1
        return True
        
        
      