# Given an absolute path for a file (Unix-style), simplify it.

# For example,
# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"
# click to show corner cases.

# Corner Cases:
# Did you consider the case where path = "/../"?
# In this case, you should return "/".
# Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
# In this case, you should ignore redundant slashes and return "/home/foo".

class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        s = ['']
        oldpath = path.split('/')
        for p in oldpath:
            if p == "":
                continue
            elif p == ".":
                continue
            elif p == "..":
                if len(s) == 1:
                    continue
                else:
                    s.pop()
            else:
                s.append(p)
        if len(s) == 1:
            newpath = '/'
        else:
            newpath = '/'.join(s)
        return newpath
s = Solution()
path = '/../'
print s.simplifyPath(path)
                    