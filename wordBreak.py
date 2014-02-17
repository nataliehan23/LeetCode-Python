class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        if len(s) == 0:
            return False
        ss = len(s)
        mp =  [[False for i in range(ss)] for j in range(ss)]
        
        for i in range(ss):
            for j in range(i, ss):
                if s[i:j+1] in dict:
                    mp[i][j] = True

        
        for i in range(ss):
            for j in range(i, ss):
                for k in range(i, j):
                    if mp[i][j]==False:
                        mp[i][j] = mp[i][k] and mp[k+1][j]
        
        return mp[0][ss-1]
        