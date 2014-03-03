# Given numRows, generate the first numRows of Pascal's triangle.

# For example, given numRows = 5,
# Return

# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]



class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        res = []
        
        if numRows >= 1:
            res.append([1])
        if numRows >= 2:
            res.append([1, 1])
        for i in range(3,numRows+1):
            prev = res[-1]
            cur = [1]
            for j in range(0,i-2):
                cur.append(prev[j]+prev[j+1])
            cur.append(1)
            res.append(cur)
        return res
                
               