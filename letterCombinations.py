class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        res = [""]
        phone = {}
        phone['2'] = ['a','b','c']
        phone['3'] = ['d','e','f']
        phone['4'] = ['g','h','i']
        phone['5'] = ['j','k','l']
        phone['6'] = ['m','n','o']
        phone['7'] = ['p','q','r','s']
        phone['8'] = ['t','u','v']
        phone['9'] = ['w','x','y','z']
        phone['0'] = [' ']
        self.letterCombHelper(digits, res, phone)
        return res
        
    def letterCombHelper(self, digits, res, phone):
        if len(digits) == 0:
            return res
        self.letterCombHelper(digits[:-1], res, phone)
        last = digits[-1]
        letters = phone[last]
        prelen = len(res)
        curlen = len(letters)
        res *= curlen
        for i in range(len(res)):
            ind = i//prelen
            res[i] += letters[ind]
        return res
                
            
            