class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        p = {}
        p['('] = ')'
        p['{'] = '}'
        p['['] = ']'
        for i in s:
            if i in p:
                stack.append(i)
            elif i in p.values():
                if not stack:
                    return False
                r = stack.pop()
                if p[r] != i:
                    return False
            else:
                return False
        if stack:
            return False
        return True
                