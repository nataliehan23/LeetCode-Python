# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

# For example,
# If n = 4 and k = 2, a solution is:

# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]

class Solution:
    # @return a list of lists of integers
    def combinerecursion(self, n, k):
        if k == 0:
            return ['']
        if k == 1:
            res = [[j] for j in range(1,n+1)]
            return res
        res = []
        for com in self.combine(n, k-1):
            for j in range(com[-1]+1,n+1):
                cc = list(com)
                cc.append(j)
                res.append(cc)
        return res

    def combinedp(self, n, k):
        DP = {}
        DP[0] = []
        DP[1] = [[j] for j in range(1,n+1)]
        
        for kk in range(1,k+1):
            listk = []
            for v in DP[kk]:
                for j in range(v[-1]+1,n+1):
                    cc = list(v)
                    cc.append(j)
                    listk.append(cc)
            DP[kk+1] = listk
        return DP[k]
