class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        if len(num) == 1:
            return [num]
        res = [prev[:i]+num[0:1]+prev[i:] for prev in self.permute(num[1:]) for i in range(len(prev)+1)]
        return res
        
   