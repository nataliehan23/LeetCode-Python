class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        if not a:
            return b
        if not b:
            return a
        astr = [c for c in a]
        bstr = [d for d in b]
        carry = 0
        cstr = []
        while len(astr)!= 0 or len(bstr)!=0:
            if astr and bstr:
                num = int(astr.pop()) + int(bstr.pop()) + carry
            elif bstr:
                num = int(bstr.pop()) + carry
            elif astr:
                num = int(astr.pop()) + carry
            carry = num//2
            cstr.insert(0,str(num%2))
        if carry == 1:
            cstr.insert(0,'1')
            
        return ''.join(cstr)
            
        