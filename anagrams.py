class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        new = set()
        seen = set()
        table = {}
        res = []
        for s in strs:
            ss = ''.join(sorted(s))
            if ss in table:
                table[ss] += [s,] 
            else:
                table[ss] = [s,]
            if ss not in new:
                new.add(ss)
            else:
                seen.add(ss)
                
        for k in seen:
            for tmp in table[k]:
                res.append(tmp)
        
        return res
        
             