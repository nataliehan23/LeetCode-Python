class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        slist = self.alphanumOnly(s)
        if len(slist) == 0:
            return True
        i = 0
        j = len(slist)-1
        while i<=j:
            if slist[i] != slist[j]:
                return False
            i += 1
            j -= 1
        return True
        
    def alphanumOnly(self, s):
        ss = []
        if s == '':
            return ss
        # build a set
        naset = set()
        for i in range(10):
            naset.add(ord('0') + i)
        alphaset = ()
        for j in range(26):
             naset.add(ord('a') + j)
        
        # check any str in the set or not
        for i in range(len(s)):
            if ord(s[i].lower()) in naset:
                ss.append(s[i].lower())
        return ss
        
            
        