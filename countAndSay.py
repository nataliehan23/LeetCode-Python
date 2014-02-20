class Solution:
    # @return a string
    def countAndSay(self, n):
        if n == 1:
            return '1'
        ss = self.countAndSay(n-1)
        res = self.say(ss)
        return res
        
    def say(self, ss):
        if ss == '1':
            return '11'
        res = ""
        i = 0
        j = 0
        count = 0
        while j<len(ss):
            print i
            print j
            print "ss now is"
            print ss[i]
            print ss[j] == ss[i]

            while j<len(ss) and ss[i]==ss[j]:
                j = j+1
                count += 1
            res = res + str(count)
            res = res + str(ss[i])
            if j == len(ss):
                break
            count = 0
            i = j
            
        return res
                
t = Solution()
print t.say('1211')             
     