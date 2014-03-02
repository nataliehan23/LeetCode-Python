# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# How many possible unique paths are there?

# Dynamic Programming, boundary is important in this case. 

class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        steps = [[0 for x in range(n)] for x in range(m)] 
        for j in range(n):
            steps[0][j] = 1
        for j in range(m):
            steps[j][0] = 1
        for i in range(1,m):
            for j in range(1,n):
                if i-1 < m and j-1 < n:
                    steps[i][j] = steps[i-1][j] + steps[i][j-1]
                elif i-1<m:
                    steps[i][j] = steps[i-1][j]
                elif j-1<n:
                    steps[i][j] = steps[i][j-1]
                    
        return steps[m-1][n-1]
        